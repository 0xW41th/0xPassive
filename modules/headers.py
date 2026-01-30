import requests

def get_headers(domain):
    try:
        r = requests.get(f"http://{domain}", timeout=10)
        return dict(r.headers)
    except:
        return {}
