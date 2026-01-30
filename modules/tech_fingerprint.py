def fingerprint(headers):
    tech = []

    server = headers.get("Server", "").lower()
    powered = headers.get("X-Powered-By", "").lower()

    if "litespeed" in server:
        tech.append("LiteSpeed")
    if "apache" in server:
        tech.append("Apache")
    if "nginx" in server:
        tech.append("Nginx")

    if "php" in powered:
        tech.append(powered.upper())

    if "wp-json" in headers.get("Link", ""):
        tech.append("WordPress")

    if "cloudflare" in server:
        tech.append("Cloudflare")

    return list(set(tech))
