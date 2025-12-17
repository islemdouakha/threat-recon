MITRE_MAP = {
    "dns_a": "T1590 - Gather Victim Network Information",
    "dns_mx": "T1590 - Gather Victim Network Information",
    "dns_txt": "T1590 - Gather Victim Network Information",
    "dns_ns": "T1590 - Gather Victim Network Information",
    "whois_email": "T1589 - Gather Victim Identity Information",
    "whois_registrar": "T1589 - People Identify Information",
    "whois_domain": "T1584 - Acquire Infrastructure"
}

def map_finding_to_mitre(finding_type: str) -> str:
    return MITRE_MAP.get(finding_type, "Unknown")
