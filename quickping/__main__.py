import sys
import socket
import subprocess
import platform
from typing import Tuple

def _resolve(host: str) -> str:
    """Return the IPv4 address for *host* using the system resolver.
    Raises a friendly error if resolution fails.
    """
    try:
        return socket.gethostbyname(host)
    except socket.gaierror as exc:
        sys.exit(f"ERROR: Unable to resolve '{host}': {exc}")

def _ping(host: str) -> Tuple[bool, float]:
    """Perform a single ping.
    Returns ``(success, latency_ms)``.
    Uses the platform‑appropriate command and parses the first latency.
    """
    system = platform.system().lower()
    if system == "windows":
        cmd = ["ping", "-n", "1", host]
    else:
        # macOS and Linux both understand ``-c 1``
        cmd = ["ping", "-c", "1", host]

    try:
        result = subprocess.run(
            cmd,
            capture_output=True,
            text=True,
            timeout=5,
        )
    except subprocess.TimeoutExpired:
        return False, 0.0

    if result.returncode != 0:
        return False, 0.0

    # Extract the latency from the output (cross‑platform rough parse)
    import re
    # typical pattern: time=23.4 ms  or  time<1ms
    m = re.search(r"time[=<]\s*([0-9.]+)\s*ms", result.stdout)
    if not m:
        # fallback for Windows: "Average = 23ms"
        m = re.search(r"Average =\s*([0-9]+)ms", result.stdout)
    if m:
        try:
            latency = float(m.group(1))
            return True, latency
        except ValueError:
            pass
    return False, 0.0

def main() -> None:
    if len(sys.argv) != 2:
        sys.exit("Usage: quickping <host>")
    host = sys.argv[1]
    ip = _resolve(host)
    success, latency = _ping(ip)
    if success:
        print(f"PING {host} ({ip}): {latency:.1f} ms")
    else:
        print(f"PING {host} ({ip}): request timed out")

if __name__ == "__main__":
    main()
