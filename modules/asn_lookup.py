import requests

def lookup_asn(ip):
    try:
        r = requests.get(f"https://ipinfo.io/{ip}/json", timeout=8)
        data = r.json()
        return {
            "asn": data.get("org", "Unknown"),
            "country": data.get("country", "Unknown"),
            "org": data.get("org", "Unknown")
        }
    except:
        return {}
