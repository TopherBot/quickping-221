# quickping

A **single‑file** Python CLI that sends an ICMP echo request (ping) to a host and prints the latency.

```bash
$ python -m quickping example.com
PING example.com (93.184.216.34): 23.4 ms
```

* Works on Windows, macOS & Linux (requires Python 3.8+).
* No external libraries – only the standard library.
* Tiny GitHub Actions CI that builds, tests and publishes a binary via `pipx`.

## Installation

```bash
# From source
git clone https://github.com/your‑user/quickping.git
cd quickping
python -m pip install --user .
```

Or install directly from the repo with `pipx` (creates an isolated entry‑point):

```bash
pipx install git+https://github.com/your‑user/quickping.git
```

## Usage

```bash
quickping <host>
```

## Development

```bash
# Create a virtual‑env for hacking
python -m venv .venv && source .venv/bin/activate
pip install -e .[dev]
pytest -q
```

## CI / CD

The repository ships a **GitHub Actions** workflow (`.github/workflows/ci.yml`) that:

1. **Checks out** the code using a pinned action SHA.
2. Sets up **Python 3.12** (cache‑pinning the version).
3. Caches the `~/.cache/pip` directory for faster installs.
4. Runs **unit tests** with `pytest`.
5. Builds a **wheel** and uploads it as an artifact (no secret needed, read‑only token).

All actions are **pinned to full commit SHAs** and the default `GITHUB_TOKEN` permissions are set to `read‑only`.

---

*Happy hacking!*