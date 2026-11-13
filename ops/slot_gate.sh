#!/bin/bash
# launchd entry (every 15 min, 12:00-18:45 KST): random afternoon slot gate -> ops/publish_daily.sh. Logic + state file docs: ops/slot_gate.py.
set -uo pipefail
export TZ=Asia/Seoul
exec python3 "$(cd "$(dirname "$0")" && pwd)/slot_gate.py"
