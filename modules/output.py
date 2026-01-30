from rich.console import Console

console = Console()

COL_DOMAIN = 36
COL_STATUS = 10
COL_LEFT = 36
COL_DNS = 8

def subdomain_findings(subs):
    for s in subs:
        if s["alive"]:
            console.print(
                f"[bold cyan][SUB][/bold cyan] "
                f"{s['subdomain']:<{COL_DOMAIN}} "
                f"{'alive':<{COL_STATUS}} "
                f"{s['ip']}"
            )

def dns_findings(dns):
    for rtype, values in dns.items():
        for v in values:
            console.print(
                f"[bold blue][DNS][/bold blue] "
                f"{rtype:<{COL_DNS}} "
                f"{v}"
            )

def asn_findings(asn_map):
    for ip, info in asn_map.items():
        org = info.get("org", "Unknown")
        console.print(
            f"[bold green][ASN][/bold green] "
            f"{ip:<{COL_LEFT}} "
            f"{org}"
        )

def header_findings(headers):
    interesting = ["Server", "X-Powered-By", "platform", "panel", "Content-Security-Policy"]
    for k in interesting:
        if k in headers:
            console.print(
                f"[bold magenta][HDR][/bold magenta] "
                f"{k:<{COL_LEFT}} "
                f"{headers[k]}"
            )

def tech_findings(tech):
    for t in tech:
        console.print(f"[bold cyan][TEC][/bold cyan] {t}")

def scope_findings(hints):
    for h in hints:
        console.print(f"[bold yellow][SCOPE][/bold yellow] {h}")

def risk_findings(whois):
    if whois.get("dnssec") != "signed":
        console.print("[bold red][RISK][/bold red] DNSSEC disabled")

    if whois.get("creation_date"):
        console.print("[bold yellow][INFO][/bold yellow] Domain recently registered")
