# HTTP/2 Support Scanner (`check_h2.py`)

Lightweight Python script that reads a list of domains from a text file, tests each domain over port `443` using TLS Application-Layer Protocol Negotiation (ALPN), and reports whether the server supports HTTP/2 (`h2`).

## Prerequisites

- **Python 3.6+** (Uses standard libraries `ssl`, `socket`, and `sys`
- No third-party packages required)

## Setup

1. Ensure the Python script (`check_h2.py`) is saved in your working directory.
2. Create a file named `domains.txt` in the same directory and add the target domains you want to scan, one per line:

```text
domain1.com
domain2.com
# Comments and blank lines are ignored
example.org
```

## Usage

Run the script from your terminal:

```bash
python3 check_h2.py
```

## Example Output

```text
Scanning 3 domains for HTTP/2 support...

domain1.com                    -> Supporting HTTP2 - potentially vulnerable
domain2.com                    -> Not supporting HTTP2
example.org                    -> Connection Error / Unreachable
```

### Status Legend
- **Red (`Supporting HTTP2 - potentially vulnerable`)**: The server negotiated the `h2` ALPN protocol.
- **Green (`Not supporting HTTP2`)**: The server completed the TLS handshake without negotiating `h2`.
- **Yellow (`Connection Error / Unreachable`)**: The connection timed out, DNS failed to resolve, or the TLS handshake encountered an error. (Maybe give it another try later)

## Disclaimer
Use at your own risk and do it responsibly, please!