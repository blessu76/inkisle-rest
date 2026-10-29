#!/bin/bash
# Render ops/rest.ipe.inkisle-publish.plist.template for this user (__HOME__ -> $HOME), lint it, and write it to ~/Library/LaunchAgents.
# It does NOT load the job — that is a separate, deliberate step (see ops/README.md).
#   bash ops/install_launchd.sh            # writes ~/Library/LaunchAgents/rest.ipe.inkisle-publish.plist
# Test hooks: INKISLE_LAUNCH_AGENTS_DIR (target dir), INKISLE_HOME (value for __HOME__, default $HOME).
set -euo pipefail
here="$(cd "$(dirname "$0")" && pwd)"
home="${INKISLE_HOME:-$HOME}"
dest_dir="${INKISLE_LAUNCH_AGENTS_DIR:-$HOME/Library/LaunchAgents}"
dest="$dest_dir/rest.ipe.inkisle-publish.plist"
case "$home" in *'#'*|*'&'*|*'|'*) echo "install_launchd: unsupported character in HOME path" >&2; exit 1;; esac
mkdir -p "$dest_dir" "$home/Library/Logs"
sed "s#__HOME__#$home#g" "$here/rest.ipe.inkisle-publish.plist.template" > "$dest.tmp"
if command -v plutil >/dev/null 2>&1 && ! plutil -lint "$dest.tmp" >/dev/null; then
  rm -f "$dest.tmp"; echo "install_launchd: rendered plist failed plutil -lint" >&2; exit 1
fi
if grep -q '__HOME__' "$dest.tmp"; then rm -f "$dest.tmp"; echo "install_launchd: unreplaced placeholder" >&2; exit 1; fi
mv "$dest.tmp" "$dest"
echo "wrote $dest"
