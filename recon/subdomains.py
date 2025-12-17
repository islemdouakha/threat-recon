import requests
import json

def get_subdomains(domain: str) -> dict:
    """
    Passive subdomain enumeration using crt.sh certificate transparency logs.
    Returns a dict with list of discovered subdomains.
    """
    url = f"https://crt.sh/?q=%25.{domain}&output=json"
    try:
        res = requests.get(url, timeout=10)
        if res.status_code != 200:
            return {"subdomains": [], "error": f"crt.sh status {res.status_code}"}

        data = json.loads(res.text)
        found = set()

        for entry in data:
            name = entry.get("name_value", "")
            # some entries include multiple domains separated by \n
            for item in name.split("\n"):
                if item.endswith(domain):
                    found.add(item.strip())

        return {"subdomains": sorted(found)}
    except Exception as e:
        return {"subdomains": [], "error": str(e)}
