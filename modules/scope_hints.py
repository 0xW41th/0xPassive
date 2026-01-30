def scope_hints(headers, asn_info):
    hints = []

    if "cloudflare" in headers.get("Server", "").lower():
        hints.append("CDN detected (Cloudflare)")

    if "hostinger" in headers.get("platform", "").lower():
        hints.append("Shared hosting (Hostinger)")

    if "aws" in asn_info.get("org", "").lower():
        hints.append("AWS infrastructure")

    if "google" in asn_info.get("org", "").lower():
        hints.append("GCP infrastructure")

    return hints
