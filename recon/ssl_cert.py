import ssl
import socket
from datetime import datetime

def get_ssl_info(domain: str, port: int = 443) -> dict:
    """
    Connects to the domain and retrieves SSL certificate info.
    Returns issuer, subject, expiration date, and SANs.
    """
    result = {}
    try:
        context = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=5) as sock:
            with context.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()

        # Extract relevant fields
        result["issuer"] = dict(x[0] for x in cert.get("issuer", []))
        result["subject"] = dict(x[0] for x in cert.get("subject", []))
        result["notBefore"] = cert.get("notBefore")
        result["notAfter"] = cert.get("notAfter")
        result["san"] = cert.get("subjectAltName", [])

    except Exception as e:
        result["error"] = str(e)

    return result
