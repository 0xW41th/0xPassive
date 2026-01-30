import argparse
from urllib.parse import urlparse

from modules.logger import info, step, done, banner
from modules.subdomain_sources import get_all_subdomains
from modules.subdomain_resolver import resolve_subdomains
from modules.dns_enum import get_dns_records
from modules.whois_lookup import get_whois
from modules.headers import get_headers

from modules.asn_lookup import lookup_asn
from modules.tech_fingerprint import fingerprint
from modules.scope_hints import scope_hints

from modules.logger import info, step, done
from modules.output import (
    subdomain_findings,
    dns_findings,
    header_findings,
    asn_findings,
    tech_findings,
    scope_findings,
    risk_findings
)


def normalize_domain(target):
    if target.startswith("http"):
        return urlparse(target).netloc
    return target.strip("/")


def main():
    parser = argparse.ArgumentParser(description="Passive domain intelligence & recon framework (0xW41th)")
    parser.add_argument("-d", "--domain", required=True)
    args = parser.parse_args()

    domain = normalize_domain(args.domain)

    banner()

    info("0xPassive v1.1")
    info(f"Target: {domain}\n")


    step("SUB", "Discovering subdomains...")
    subs = get_all_subdomains(domain)
    done(f"({len(subs)})")

    step("SUB", "Resolving subdomains...")
    resolved = resolve_subdomains(subs)
    alive = len([s for s in resolved if s["alive"]])
    done(f"({alive} alive)")

    step("DNS", "Fetching DNS records...")
    dns = get_dns_records(domain)
    done()

    step("WHO", "Fetching WHOIS...")
    whois = get_whois(domain)
    done()

    step("HDR", "Fetching headers...")
    headers = get_headers(domain)
    done("\n")

    asn_map = {}
    for s in resolved:
        if s["ip"] and s["ip"] not in asn_map:
            asn_map[s["ip"]] = lookup_asn(s["ip"])

    tech = fingerprint(headers)
    hints = scope_hints(headers, list(asn_map.values())[0] if asn_map else {})

    subdomain_findings(resolved)
    dns_findings(dns)
    asn_findings(asn_map)
    header_findings(headers)
    tech_findings(tech)
    scope_findings(hints)
    risk_findings(whois)


if __name__ == "__main__":
    main()
