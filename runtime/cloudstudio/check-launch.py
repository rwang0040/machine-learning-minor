"""Check the course Jupyter server on a spare loopback port; retain authentication."""
from pathlib import Path
import os
import socket
import subprocess
import tempfile
import time
import urllib.error
import urllib.request

scripts = Path(__file__).resolve().parent
with socket.socket() as probe:
    probe.bind(('127.0.0.1', 0))
    port = probe.getsockname()[1]
environment = dict(os.environ, ML_JUPYTER_IP='127.0.0.1', ML_JUPYTER_PORT=str(port))
with tempfile.TemporaryFile(mode='w+') as log:
    process = subprocess.Popen(['bash', str(scripts / 'start-lab.sh')], cwd=scripts,
                               env=environment, stdout=log, stderr=subprocess.STDOUT)
    try:
        for _ in range(45):
            if process.poll() is not None:
                raise RuntimeError('Course Jupyter exited before the HTTP check')
            try:
                with urllib.request.urlopen(f'http://127.0.0.1:{port}/lab', timeout=1) as response:
                    assert response.status == 200
                    assert process.poll() is None
                    print('Jupyter HTTP launch check passed (loopback; authentication retained).')
                    break
            except (OSError, urllib.error.URLError):
                time.sleep(1)
        else:
            raise TimeoutError('Jupyter did not start within 45 seconds')
    finally:
        process.terminate()
        try:
            process.wait(timeout=15)
        except subprocess.TimeoutExpired:
            process.kill()
            process.wait()
# Temporary server logs may contain credentials and are never retained.
