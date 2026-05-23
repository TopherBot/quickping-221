import subprocess
import sys
from pathlib import Path

def test_cli_returns_zero_exit_code(tmp_path: Path):
    # Use a well‑known host that should always resolve.
    result = subprocess.run(
        [sys.executable, "-m", "quickping", "example.com"],
        capture_output=True,
        text=True,
    )
    # The CLI must exit with code 0 on success.
    assert result.returncode == 0
    # The output should contain the word PING and a latency value.
    assert "PING" in result.stdout
    # Basic sanity check on the latency format.
    assert "ms" in result.stdout
