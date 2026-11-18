import ssl
import socket
import sys

# ANSI color codes
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"

def check_http2(domain, port=443, timeout=5):
    """Checks if a domain supports HTTP/2 via TLS ALPN."""
    context = ssl.create_default_context()
    # Request h2 and fallback protocols
    context.set_alpn_protocols(['h2', 'http/1.1'])
    
    try:
        with socket.create_connection((domain, port), timeout=timeout) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                return ssock.selected_alpn_protocol() == 'h2'
    except Exception:
        # Catch connection timeouts, DNS resolution errors, or SSL handshakes
        return None

def main():
    input_file = "domains.txt"
    
    try:
        with open(input_file, "r") as f:
            domains = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' was not found.")
        sys.exit(1)

    print(f"Scanning {len(domains)} domains for HTTP/2 support...\n")
    
    for domain in domains:
        result = check_http2(domain)
        
        if result is True:
            print(f"{domain:<30} -> {RED}Supporting HTTP2 - potentially vulnerable{RESET}")
        elif result is False:
            print(f"{domain:<30} -> {GREEN}Not supporting HTTP2{RESET}")
        else:
            print(f"{domain:<30} -> {YELLOW}Connection Error / Unreachable{RESET}")

if __name__ == "__main__":
    main()