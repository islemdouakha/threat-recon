import whois

def whois_lookup(domain: str):
    results = []
    try:
        data = whois.whois(domain)
        if data.domain_name:
            results.append({"type": "whois_domain", "value": str(data.domain_name)})
        if data.emails:
            results.append({"type": "whois_email", "value": str(data.emails)})
        if data.registrar:
            results.append({"type": "whois_registrar", "value": str(data.registrar)})
    except Exception:
        pass

    return results
