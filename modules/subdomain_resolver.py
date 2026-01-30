import socket
import requests
import warnings
from urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter("ignore", InsecureRequestWarning)

def resolve_subdomains(subdomains):
    results = []

    for sub in subdomains:
        entry = {"subdomain": sub, "ip": None, "alive": False}

        try:
            ip = socket.gethostbyname(sub)
            entry["ip"] = ip
        except:
            results.append(entry)
            continue

        try:
            r = requests.get(f"http://{sub}", timeout=5)
            entry["alive"] = True
        except:
            try:
                r = requests.get(f"https://{sub}", timeout=5, verify=False)
                entry["alive"] = True
            except:
                pass

        results.append(entry)

    return results
