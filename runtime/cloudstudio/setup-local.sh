#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
# Only this entry uses the machine's uv index to install the shared locked set.
export ML_LOCAL_MIRROR_SYNC=1
exec bash "$script_dir/setup-remote.sh"
