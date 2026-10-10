#!/usr/bin/env bash
set -euo pipefail
script_dir="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
cd "$script_dir/../.."
export UV_PYTHON_INSTALL_DIR="$PWD/.python"
export UV_CACHE_DIR="$PWD/.uv-cache"
export UV_PYTHON_DOWNLOADS=automatic
if test -L .venv; then
  export UV_PROJECT_ENVIRONMENT="$(readlink -f .venv)"
fi
if command -v uv >/dev/null 2>&1; then
  uv_bin="$(command -v uv)"
else
  uv_bin="$script_dir/tools/uv"
  if ! test -x "$uv_bin"; then
    mkdir -p "$script_dir/tools"
    installer="$(mktemp)"
    trap 'rm -f "$installer"' EXIT
    curl --fail --location --retry 2 --connect-timeout 20 --max-time 180 https://astral.sh/uv/0.12.22/install.sh -o "$installer"
    UV_INSTALL_DIR="$script_dir/tools" UV_NO_MODIFY_PATH=1 bash "$installer"
  fi
fi
"$uv_bin" --version
python_version="$(tr -d '\r\n' < .python-version)"
"$uv_bin" python install --no-bin "$python_version"
if test "${ML_LOCAL_MIRROR_SYNC:-0}" = 1; then
  # Export fixed versions/hashes without replacing the shared lock's registry.
  "$uv_bin" venv --allow-existing --python "$python_version" "${UV_PROJECT_ENVIRONMENT:-$PWD/.venv}"
  requirements="$(mktemp)"
  trap 'rm -f "$requirements" "${installer:-}"' EXIT
  "$uv_bin" export --frozen --group verification --no-emit-project --format requirements.txt --output-file "$requirements" >/dev/null
  "$uv_bin" pip sync --python "$PWD/.venv/bin/python" --require-hashes "$requirements"
else
  "$uv_bin" sync --locked --group verification
fi
export PATH="$PWD/.venv/bin:$script_dir/tools:$PATH"
kernel_version="$(.venv/bin/python -c 'import sys; print(f"{sys.version_info.major}.{sys.version_info.minor}")')"
.venv/bin/python -m ipykernel install --prefix "$PWD/.venv" --name ml-course --display-name "机器学习 · Python $kernel_version"
.venv/bin/python -c 'import sys,numpy,pandas,sklearn; print(sys.executable); print(sys.version); print(numpy.__version__,pandas.__version__,sklearn.__version__)'
