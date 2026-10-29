# Daily publish automation (draft — nothing here is installed)

Policy: **one post a day at 19:00 KST** while the app is unreleased (Davy, 2026-10-29). The publish time recorded in each post is the real time
the script ran (HH:MM KST); a future time is refused.

| File | Role |
|---|---|
| `publish_daily.sh` | pull → `publish_post.py --daily` → green gate → commit → push → live check → IndexNow |
| `rest.ipe.inkisle-publish.plist.draft` | launchd job, 19:00 every day |

Install (by the room lead, after the GitHub remote and Pages exist):

```
mkdir -p ~/.ipe/logs
cp ops/rest.ipe.inkisle-publish.plist.draft ~/Library/LaunchAgents/rest.ipe.inkisle-publish.plist
launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/rest.ipe.inkisle-publish.plist
launchctl kickstart -k gui/$(id -u)/rest.ipe.inkisle-publish     # run once now (only if you want a post now)
```

Before relying on it: confirm the queue (`content/queue/`) has posts, translations are added for queued posts (docs/TRANSLATION.md), and
`git push` works non-interactively from that account. When the queue is empty the job does nothing and exits 0 — write new posts into
`content/queue/NN-slug/` (NN keeps the order).
