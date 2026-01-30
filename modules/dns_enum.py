import dns.resolver

def get_dns_records(domain):
    results = {}
    for record in ["A", "AAAA", "MX", "NS", "TXT"]:
        try:
            answers = dns.resolver.resolve(domain, record)
            results[record] = [str(a) for a in answers]
        except:
            results[record] = []
    return results
