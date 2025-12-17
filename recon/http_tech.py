import requests

def fingerprint_http(domain: str) -> dict:
    """
    Performs a simple HTTP GET request and extracts technology indicators
    from response headers. Passive and legal.
    """
    url = f"http://{domain}"
    result = {
        "url": url,
        "status": None,
        "headers": {},
        "tech": []
    }

    try:
        res = requests.get(url, timeout=5)
        result["status"] = res.status_code
        result["headers"] = dict(res.headers)

        server = res.headers.get("Server")
        powered = res.headers.get("X-Powered-By")

        if server:
            result["tech"].append(f"Server: {server}")
        if powered:
            result["tech"].append(f"Powered-By: {powered}")

        # heuristic-based clues
        text = res.text.lower()
        if "wp-content" in text:
            result["tech"].append("WordPress detected")
        if "drupal" in text:
            result["tech"].append("Drupal detected")
        if "laravel" in text:
            result["tech"].append("Laravel detected")
        if "cloudflare" in (server or "").lower():
            result["tech"].append("Cloudflare proxy")

    except Exception as e:
        result["error"] = str(e)

    return result
