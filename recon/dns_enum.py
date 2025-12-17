import dns.resolver

def enumerate_dns(domain: str):
    results = []
    resolver = dns.resolver.Resolver()

    record_types = ["A", "AAAA", "MX", "NS", "TXT"]

    for rtype in record_types:
        try:
            answers = resolver.resolve(domain, rtype)
            for rdata in answers:
                results.append({
                    "type": f"dns_{rtype.lower()}",
                    "value": str(rdata)
                })
        except Exception:
            pass

    return results
