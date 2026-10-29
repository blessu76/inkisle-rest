# Daily publish automation (not installed by this repo)

Policy: **one post a day at 19:00 KST** while the app is unreleased (2026-10-29). The publish time recorded in each post is the real time
the script ran (HH:MM KST); a future time is refused.

| File | Role |
|---|---|
| `publish_daily.sh` | safety checks → push leftovers → `publish_post.py --daily` → green gate → commit → push → live check → IndexNow |
| `rest.ipe.inkisle-publish.plist.template` | launchd job template (`__HOME__` placeholder; launchd does not expand `~`), 19:00 every day, log `~/Library/Logs/inkisle-publish.log` |
| `install_launchd.sh` | renders the template for the current user, `plutil -lint`, writes `~/Library/LaunchAgents/…plist` — does **not** load it |

## Safety rules (tests: `tests/test_publish_daily.py`)

- Runs in a **dedicated publish clone**: `INKISLE_PUBLISH_DIR` (default `~/Developer/inkisle-rest`). That clone must stay on `main` with a clean tree and
  must not be a place where anyone (or any agent) works on feature branches. On any other branch, or with uncommitted changes, the run logs `SKIP` and exits 0.
- A previous failed push is retried first (`origin/main..HEAD`), even when nothing new is due.
- Publishing is atomic: if `publish_post.py` (build + sitemap check), the green gate or the path check fails, the tree is reset to where it started
  (`ROLLBACK` in the log), so no stamp for today is left behind and the next run can retry.
- Only the publish set is staged (`content/journal`, `content/queue`, generated pages); anything else in the tree aborts the run. Never `git add -A`.
- IndexNow gets the new post in every published language plus `/` and `/journal/`.

## Install (by the maintainer, once; the repo never does this itself)

1. Make the publish clone: `git clone https://github.com/blessu76/inkisle-rest.git ~/Developer/inkisle-rest` (must be on `main`; `git push` must work non-interactively).
2. The Mac's time zone must be KST (launchd's 19:00 is local time).
3. Install and load:

```
bash ops/install_launchd.sh                                      # renders + lints; loads nothing
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/rest.ipe.inkisle-publish.plist
launchctl kickstart -k gui/$(id -u)/rest.ipe.inkisle-publish     # run once now (only if you want a post now)
```

Uninstall: `launchctl bootout gui/$(id -u)/rest.ipe.inkisle-publish && rm ~/Library/LaunchAgents/rest.ipe.inkisle-publish.plist`.
Log: `tail -f ~/Library/Logs/inkisle-publish.log` (lines: `SKIP`, `FAIL`, `ROLLBACK`, `committed`, `pushed`).

Before relying on it: the queue (`content/queue/`) has posts and their translations exist (docs/TRANSLATION.md). When the queue is empty the job does
nothing and exits 0 — write new posts into `content/queue/NN-slug/` (NN keeps the order).
