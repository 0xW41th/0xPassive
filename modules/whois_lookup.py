import whois
import contextlib
import io

def get_whois(domain):
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            w = whois.whois(domain)
        return dict(w)
    except:
        return {}
