# Daily publish automation (not installed by this repo)

Policy: **one post a day in a random afternoon slot (12:00–17:59 KST, never the same hour as the day before)** while the app is unreleased (2026-10-29; was a fixed 19:00 until 2026-11-13). The publish time recorded in each post is the real time
the script ran (HH:MM KST); a future time is refused.

| File | Role |
|---|---|
| `slot_gate.sh` / `slot_gate.py` | launchd entry, every 15 min 12:00–18:45 KST: draws today's slot (`~/.ipe/queue/inkisle/slot.json`, override `INKISLE_SLOT_FILE`). Runs `publish_daily.sh` at eligible ticks before 18:00. Only a successful run that logs `pushed <slug>`, `nothing to publish`, or `Pages verified` completes the slot. Tests: `tests/test_slot_gate.py` |
| `publish_daily.sh` | safety checks → push leftovers → `publish_post.py --daily` → green gate → commit → push → live check → IndexNow |
| `rest.ipe.inkisle-publish.plist.template` | launchd job template (`__HOME__` placeholder; launchd does not expand `~`), every 15 min 12:00–18:45 → `slot_gate.sh`, log `~/Library/Logs/inkisle-publish.log` |
| `install_launchd.sh` | renders the template for the current user, `plutil -lint`, writes `~/Library/LaunchAgents/…plist` — does **not** load it |

## Safety rules (tests: `tests/test_publish_daily.py`)

- Runs in a **dedicated publish clone**: `INKISLE_PUBLISH_DIR` (default `~/Developer/inkisle-rest`). That clone must stay on `main` with a clean tree and
  must not be a place where anyone (or any agent) works on feature branches. On any other branch, or with uncommitted changes, the run logs `SKIP` and exits 0.
- A previous failed push is retried first (`origin/main..HEAD`), even when nothing new is due — but only if those commits touch nothing outside the publish set; otherwise they are kept on a `backup/stray-<time>` branch, the clone is reset to origin/main and the day's post still publishes (a local work-in-progress commit never rides along to main; 11-19 the old `SKIP` blocked every tick).
- A `vendor/ipe_web_kit` that does not match `vendor/ipe_web_kit.lock` (`vendor/` is gitignored, so a pull that moves the lock does not move it) is re-synced from `INKISLE_KIT_DIR` (default `~/Developer/ipe_web_kit`) before publishing; if that fails the run logs `KIT_MISMATCH`, shows a macOS notification and exits 1 without touching the tree.
- An empty queue logs `QUEUE_EMPTY` and checks any pending Pages URLs. Check the log for `SKIP`/`FAIL`/`QUEUE_EMPTY` regularly.
- Publishing is atomic: if `publish_post.py` (build + sitemap check), the green gate or the path check fails, the tree is reset to where it started
  (`ROLLBACK` in the log), so no stamp for today is left behind and the next run can retry.
- One run at a time (`.git/publish.lock`; a lock from a dead process or older than 3 h is taken over). A second run logs `SKIP — another publish run is in progress`.
- Only the publish set is staged (`content/journal`, `content/queue`, generated pages); anything else in the tree aborts the run. Never `git add -A`.
- push 직전 새 글의 언어별 URL을 발행 클론의 `.git/publish-pages.pending`에 저장한다. 새 글을 push한 뒤와 각 배포 재요청 뒤 120초를 기다리고, 새 `?v=` 쿼리로 HTTP 200 응답을 30초 간격으로 최대 7회 확인한다. 이 구간에 페이지가 열리지 않으면 `gh workflow run 'Deploy to GitHub Pages' --ref main`으로 배포를 최대 두 번 새로 요청한다.
- 모든 대기 URL이 200이면 쿼리 없는 원본 URL과 `/`, `/journal/`을 IndexNow에 제출한다. 성공하면 대기 파일을 지운다. `PAGES_NOT_LIVE` 또는 `INDEXNOW_PENDING`이면 발행 커밋은 main에 남고 대기 파일을 유지한다. 다음 발행 가능 틱에는 새 글이 없거나 큐가 비어 있어도 저장된 URL을 한 차례 확인하고, 모두 열리면 IndexNow를 다시 제출한다. 추가 배포 요청은 새 글을 push한 실행에만 허용한다.

## Install (by the maintainer, once; the repo never does this itself)

1. Make the publish clone: `git clone https://github.com/blessu76/inkisle-rest.git ~/Developer/inkisle-rest` (must be on `main`; `git push` must work non-interactively).
2. The Mac's time zone must be KST (launchd's schedule is local time).
3. Check that pushing works the way launchd will do it (no terminal, no prompt):

```
git -C ~/Developer/inkisle-rest push --dry-run origin HEAD:main     # must succeed without asking for anything (osxkeychain / ssh key / gh credential helper)
```

   [Whether the keychain is reachable from the LaunchAgent session itself is only proven by the first real run — watch the log that day.]
   Pages 재시도에는 LaunchAgent의 PATH에 있는 `gh`, 프롬프트 없이 읽을 수 있는 로그인, 저장소의 Actions 워크플로 실행 권한이 필요하다.
4. Install and load:

```
launchctl bootout gui/$(id -u)/rest.ipe.inkisle-publish 2>/dev/null   # only if an older version is already loaded; ignore the error otherwise
bash ops/install_launchd.sh                                      # renders + lints; loads nothing
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/rest.ipe.inkisle-publish.plist
launchctl kickstart gui/$(id -u)/rest.ipe.inkisle-publish        # run once now (only if you want a post now); never with -k: that kills a run in progress
```

Uninstall: `launchctl bootout gui/$(id -u)/rest.ipe.inkisle-publish && rm ~/Library/LaunchAgents/rest.ipe.inkisle-publish.plist`.
Log: `tail -f ~/Library/Logs/inkisle-publish.log` (lines: `SKIP`, `FAIL`, `ROLLBACK` / `ROLLBACK FAILED`, `QUEUE_LOW n` (3 or fewer queued), `QUEUE_EMPTY`, `committed`, `pushed`).

Before relying on it: the queue (`content/queue/`) has posts and their translations exist (docs/TRANSLATION.md). When the queue is empty the job does
nothing and exits 0 — write new posts into `content/queue/NN-slug/` (NN keeps the order).
