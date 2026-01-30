import requests

def from_crtsh(domain):
    subs = set()
    try:
        r = requests.get(f"https://crt.sh/?q=%25.{domain}&output=json", timeout=15)
        for e in r.json():
            for s in e["name_value"].split("\n"):
                subs.add(s.strip())
    except:
        pass
    return subs

def from_threatcrowd(domain):
    subs = set()
    try:
        r = requests.get(f"https://www.threatcrowd.org/searchApi/v2/domain/report/?domain={domain}", timeout=15)
        for s in r.json().get("subdomains", []):
            subs.add(s)
    except:
        pass
    return subs

def from_hackertarget(domain):
    subs = set()
    try:
        r = requests.get(f"https://api.hackertarget.com/hostsearch/?q={domain}", timeout=15)
        for line in r.text.splitlines():
            subs.add(line.split(",")[0])
    except:
        pass
    return subs

def get_all_subdomains(domain):
    subs = set()
    subs |= from_crtsh(domain)
    subs |= from_threatcrowd(domain)
    subs |= from_hackertarget(domain)
    return sorted(subs)
