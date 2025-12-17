import argparse
import json
import sys


from recon.dns_enum import enumerate_dns
from recon.whois_lookup import whois_lookup
from mitre.mapping import map_finding_to_mitre
from mitre.mapping import techniques
from recon import get_subdomains
from recon.ssl_cert import get_ssl_info


def validate_domain(domain: str) -> bool:
    if "." not in domain:
        return False
    return True


def main():
    parser = argparse.ArgumentParser(
        description="Threat Intelligence Recon Tool – Passive OSINT + MITRE Mapping"
    )
    parser.add_argument(
        "--domain", required=True,
        help="Target domain for reconnaissance (e.g., example.com)"
    )
    parser.add_argument(
        "--output",
        help="Optional output file to save JSON results"
    )

    args = parser.parse_args()
    domain = args.domain.strip()

    if not validate_domain(domain):
        print("[-] Invalid domain format.")
        sys.exit(1)

    results = {
        "domain": domain,
        "findings": []
    }

    print(f"[+] Starting recon on: {domain}")

    # DNS Enumeration Module
    dns_results = enumerate_dns(domain)
    for item in dns_results:
        results["findings"].append({
            "type": item["type"],
            "value": item["value"],
            "mitre": map_finding_to_mitre(item["type"])
        })

    # WHOIS Lookup
    whois_results = whois_lookup(domain)
    for item in whois_results:
        results["findings"].append({
            "type": item["type"],
            "value": item["value"],
            "mitre": map_finding_to_mitre(item["type"])
        })

    ssl_info = get_ssl_info(args.domain)
    results["ssl_certificate"] = ssl_info
    results["ssl_certificate"]["mitre"] = techniques.get("SSL_certificate_analysis", "Unknown")
    results["subdomains"] = get_subdomains(args.domain)
    results["subdomains"]["mitre"] = techniques.get("subdomain_enum", "Unknown")
    # Output JSON to file or stdout
    output_data = json.dumps(results, indent=4)
    if args.output:
        with open(args.output, "w") as f:
            f.write(output_data)
        print(f"[+] Results saved to {args.output}")
    else:
        print(output_data)


if __name__ == "__main__":
    main()
