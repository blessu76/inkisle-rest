#!/bin/bash
# Daily publish — DRAFT, not installed. Publishes the next queued post (one per day, 19:00 KST), builds, checks, commits, pushes, pings IndexNow.
# Install notes: ops/README.md. Needs: python3, git (push access to origin), network for IndexNow.
set -euo pipefail
REPO="${INKISLE_REPO:-$HOME/Developer/inkisle-rest}"
cd "$REPO"
export TZ=Asia/Seoul
git pull --rebase --autostash origin main
python3 scripts/publish_post.py --daily                  # no-op (exit 0) if today already has a post or the queue is empty
if [ -z "$(git status --porcelain)" ]; then echo "nothing to publish"; exit 0; fi
bash scripts/check.sh                                    # green gate: refuse to push a red build
slug="$(git status --porcelain content/journal | sed -n 's#.*content/journal/\([^/]*\)/.*#\1#p' | sort -u | head -1)"
git add -A
git diff --cached --stat | tail -1
git diff --cached --name-only --diff-filter=D | grep -v '^content/queue/' && { echo "unexpected deleted files — abort"; exit 1; } || true
git commit -q -m "journal: publish ${slug} ($(date '+%Y-%m-%d %H:%M') KST)"
git push origin HEAD:main
# IndexNow only after the deploy is live: wait for Pages, then submit the new URLs.
sleep 120
python3 scripts/check_sitemap.py --live || echo "live check failed — retry later: python3 scripts/check_sitemap.py --live"
python3 scripts/indexnow.py "https://inkisle.ipe.rest/journal/${slug}/" "https://inkisle.ipe.rest/ko/journal/${slug}/" "https://inkisle.ipe.rest/journal/" || true
