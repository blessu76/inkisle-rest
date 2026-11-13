#!/bin/bash
# Daily publish (one post a day, in a random afternoon slot picked by ops/slot_gate.sh): pull -> push leftovers -> publish_post --daily -> green gate -> commit -> push -> live check -> IndexNow.
# Install notes: ops/README.md. Needs: python3, git (non-interactive push access to origin), network for IndexNow.
#
# Safety rules
#   - Runs only in a dedicated publish clone (INKISLE_PUBLISH_DIR, default ~/Developer/inkisle-rest) that is checked out on `main` with a clean tree;
#     otherwise it does nothing and exits 0 (see the log). Never point it at a clone where feature branches / work in progress live.
#   - Local commits not yet on origin/main (a previous push failed) are pushed first, even when there is nothing new to publish.
#   - Publishing is all-or-nothing: if anything before the commit fails (publish_post, the green gate, the path check, git add/commit, SIGTERM), the tree is reset to the commit it started from.
#   - One run at a time: .git/publish.lock (stale after its process is gone or 3 h).
#   - Only the paths a publish creates are staged (never `git add -A`).
#   - The private ipe_web_kit in vendor/ (gitignored) must match vendor/ipe_web_kit.lock. After the rebase the lock may have moved (11-08: lock v0.2.3, vendor v0.1.1 ->
#     ImportError, no post that day), so the run first re-syncs vendor from the local kit clone (INKISLE_KIT_DIR, default ~/Developer/ipe_web_kit) and,
#     if it still does not match, fails loudly (KIT_MISMATCH in the log + a macOS notification) before touching any content.
# Test hooks: INKISLE_CHECK_CMD (default "bash scripts/check.sh"), INKISLE_SKIP_NET=1 (no sleep / live check / IndexNow / notification),
#             INKISLE_KIT_CHECK_CMD (default "python3 scripts/kit_lock.py check"), INKISLE_KIT_SYNC_CMD (default "python3 scripts/kit_lock.py sync --kit <INKISLE_KIT_DIR>").
set -euo pipefail
export TZ=Asia/Seoul
export GIT_TERMINAL_PROMPT=0     # under launchd nobody can type a password: fail instead of hanging
log() { echo "[$(date '+%Y-%m-%d %H:%M:%S') KST] publish_daily: $*"; }
skip() { log "SKIP — $*"; exit 0; }

REPO="${INKISLE_PUBLISH_DIR:-$HOME/Developer/inkisle-rest}"
CHECK_CMD="${INKISLE_CHECK_CMD:-bash scripts/check.sh}"
KIT_DIR="${INKISLE_KIT_DIR:-$HOME/Developer/ipe_web_kit}"
KIT_CHECK_CMD="${INKISLE_KIT_CHECK_CMD:-python3 scripts/kit_lock.py check}"
KIT_SYNC_CMD="${INKISLE_KIT_SYNC_CMD:-python3 scripts/kit_lock.py sync --kit \"$KIT_DIR\"}"
# Everything publish_post.py + build_site.py may create or change. Anything else in the tree after a publish means abort.
# The language dirs must be exactly the non-English languages of build_site.LANGS (en lives at the root) — tests/test_publish_daily.py fails when they drift.
PUBLISH_PATHS="content/journal content/queue index.html 404.html sitemap.xml llms.txt robots.txt journal ko ja zh-Hant es fr de pt-BR id th vi tr"

[ -d "$REPO/.git" ] || skip "$REPO is not a git clone"
cd "$REPO"

# One run at a time (a manual run or `launchctl kickstart` can overlap a scheduled tick). mkdir is atomic; a lock whose process is gone, or that is older
# than 3 hours, is stale and is taken over.
lock="$REPO/.git/publish.lock"
if ! mkdir "$lock" 2>/dev/null; then
  holder="$(cat "$lock/pid" 2>/dev/null || true)"
  if { [ -n "$holder" ] && ! kill -0 "$holder" 2>/dev/null; } || [ -n "$(find "$lock" -maxdepth 0 -mmin +180 2>/dev/null)" ]; then
    log "stale lock (pid ${holder:-?}) — taking over"; rm -rf "$lock"; mkdir "$lock" || skip "could not take the lock"
  else
    skip "another publish run is in progress (pid ${holder:-?})"
  fi
fi
echo $$ > "$lock/pid"
trap 'rm -rf "$lock"' EXIT

branch="$(git symbolic-ref --short -q HEAD || echo '(detached)')"
[ "$branch" = "main" ] || skip "branch is '$branch', not main"
[ -z "$(git status --porcelain)" ] || skip "working tree is not clean"

git fetch -q origin main || { log "FAIL — git fetch"; exit 1; }

# Local commits not on origin/main (a failed push, or someone committing in this clone) are judged BEFORE the rebase: if they touch anything outside the
# publish set they must never ride along to the public main, and rebasing them onto a moved origin/main can conflict (10-31: a release-notes commit made
# here collided with the same files on origin and the run failed). Skipping leaves the clone untouched for a human.
if [ "$(git rev-list --count origin/main..HEAD)" -gt 0 ]; then
  stray=""
  while IFS= read -r f; do
    ok=0
    for p in $PUBLISH_PATHS; do case "$f" in "$p"|"$p"/*) ok=1;; esac; done
    [ "$ok" = 1 ] || stray="$stray $f"
  done < <(git diff --name-only origin/main...HEAD)
  [ -z "$stray" ] || skip "unpushed commits touch paths outside the publish set:${stray:0:200} — not pushing (move them to a feature branch: git branch backup/x; git reset --hard origin/main)"
fi

git rebase -q origin/main || {
  conflicts="$(git diff --name-only --diff-filter=U | head -5 | tr '\n' ' ')"
  git rebase --abort 2>/dev/null || true
  log "FAIL — cannot rebase onto origin/main (local unpushed: $(git log --oneline origin/main..HEAD | head -3 | tr '\n' ';') conflicts: ${conflicts:-?}) — clone left as it was"
  exit 1
}

if [ "$(git rev-list --count origin/main..HEAD)" -gt 0 ]; then
  log "pushing $(git rev-list --count origin/main..HEAD) unpushed commit(s)"
  git push -q origin HEAD:main || { log "FAIL — push of unpushed commits"; exit 1; }
fi

# vendor/ipe_web_kit must be the locked kit version (vendor/ is gitignored, so a pull that moves the lock does not move it). Re-sync from the local kit clone;
# a failure here changes nothing in the tree, so there is nothing to roll back.
if ! bash -c "$KIT_CHECK_CMD" >/dev/null 2>&1; then
  log "kit does not match vendor/ipe_web_kit.lock — syncing from $KIT_DIR"
  git -C "$KIT_DIR" fetch -q --tags origin 2>/dev/null || true       # the lock may name a tag newer than the clone knows; best effort
  if ! sync_out="$(bash -c "$KIT_SYNC_CMD" 2>&1)" || ! kit_out="$(bash -c "$KIT_CHECK_CMD" 2>&1)"; then
    log "FAIL — KIT_MISMATCH: vendor/ipe_web_kit does not match vendor/ipe_web_kit.lock and the sync from $KIT_DIR failed: ${sync_out:-${kit_out:-?}}"
    log "fix by hand: cd $REPO && python3 scripts/kit_lock.py sync --kit <ipe_web_kit clone with the locked tag>"
    if [ "${INKISLE_SKIP_NET:-0}" != "1" ] && command -v osascript >/dev/null 2>&1; then
      osascript -e 'display notification "ipe_web_kit lock mismatch — daily publish did not run (see inkisle-publish.log)" with title "inkisle publish FAILED"' >/dev/null 2>&1 || true
    fi
    exit 1
  fi
  log "kit re-synced: $sync_out"
fi

# An empty queue ends the daily post series silently, so make it loud in the log (still exit 0: it is not an error).
if [ -z "$(find content/queue -mindepth 1 -maxdepth 1 -type d 2>/dev/null)" ]; then
  log "QUEUE_EMPTY — no post left in content/queue/; add content/queue/NN-slug/{en,ko}.md (+ translations) or the daily publishing stops"
  exit 0
fi

queued="$(find content/queue -mindepth 1 -maxdepth 1 -type d | wc -l | tr -d ' ')"
[ "$queued" -gt 3 ] || log "QUEUE_LOW $queued — only $queued post(s) queued in content/queue/ (counted before today's publish); write more soon"

# From here until the commit exists, ANY non-zero exit (a failed step, git add/commit error, SIGINT/SIGTERM) restores the tree, which was clean when
# we started — otherwise a half-published dirty tree would make every later run SKIP silently.
base="$(git rev-parse HEAD)"
stage=prepublish
# A failing rollback must neither stop the script (set -e) nor keep the lock: it is logged loudly and the tree stays dirty for a human (later runs SKIP).
rollback() {
  local ok=1
  git reset -q --hard "$base" || ok=0
  git clean -fdq || ok=0
  stage=rolledback
  if [ "$ok" = 1 ]; then log "ROLLBACK — tree restored to ${base:0:7}"
  else log "ROLLBACK FAILED — the working tree in $REPO is NOT clean; fix by hand (git status; git reset --hard ${base:0:7}; git clean -fd) or every later run SKIPs"; fi
}
on_exit() { local rc=$?; rm -rf "$lock"; if [ "$rc" -ne 0 ] && [ "$stage" = prepublish ]; then rollback; fi; }
trap on_exit EXIT
trap 'log "signal received"; exit 143' INT TERM

if ! out="$(python3 scripts/publish_post.py --daily 2>&1)"; then
  echo "$out"; rollback; log "FAIL — publish_post"; exit 1
fi
echo "$out"
if [ -z "$(git status --porcelain)" ]; then log "nothing to publish"; exit 0; fi
slug="$(echo "$out" | sed -n 's/^publish_post: \([^ ]*\) at .*/\1/p' | head -1)"
[ -n "$slug" ] || { rollback; log "FAIL — changes without a published slug"; exit 1; }

if ! bash -c "$CHECK_CMD"; then rollback; log "FAIL — green gate"; exit 1; fi

add=""
for p in $PUBLISH_PATHS; do [ -e "$p" ] && add="$add $p"; done   # a path that does not exist (e.g. a language dir in a small test site) is not an error
# shellcheck disable=SC2086
git add -A -- $add                                              # -A is limited to these paths so that queue deletions are staged
if [ -n "$(git status --porcelain | grep -v '^[MADR] ')" ]; then
  git status --short; rollback; log "FAIL — unexpected paths outside the publish set"; exit 1
fi
if git diff --cached --name-only --diff-filter=D | grep -qv '^content/queue/'; then
  rollback; log "FAIL — unexpected deleted files"; exit 1
fi
git diff --cached --stat | tail -1
git commit -q -m "journal: publish ${slug} ($(date '+%Y-%m-%d %H:%M') KST)"
stage=committed                                                  # from now on a failure keeps the commit; the next run pushes it first
log "committed ${slug}"
git push -q origin HEAD:main || { log "FAIL — push (commit kept locally; the next run pushes it first)"; exit 1; }
log "pushed ${slug}"

[ "${INKISLE_SKIP_NET:-0}" = "1" ] && exit 0
# IndexNow only after the deploy is live: wait for Pages, then submit the new post in every language plus the home and journal pages.
sleep 120
python3 scripts/check_sitemap.py --live || log "live check failed — retry later: python3 scripts/check_sitemap.py --live"
urls="$(echo "$out" | sed -n 's/^  \(https:\/\/[^ ]*\)$/\1/p') https://inkisle.ipe.rest/ https://inkisle.ipe.rest/journal/"
# shellcheck disable=SC2086
python3 scripts/indexnow.py $urls || log "IndexNow failed (not critical)"
