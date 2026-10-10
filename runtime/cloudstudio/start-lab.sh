#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir/../.."
export PATH="$PWD/.venv/bin:$script_dir/tools:$PATH"
export OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 MKL_NUM_THREADS=1
exec .venv/bin/python -m jupyterlab --allow-root --ip="${ML_JUPYTER_IP:-127.0.0.1}" --port="${ML_JUPYTER_PORT:-8888}" --no-browser --ServerApp.port_retries=0
