import re
import dns.resolver
import requests
import hashlib

HEADERS = {"User-Agent": "Mozilla/5.0"}

def valid_email(email):
    return re.match(r"^[^@]+@[^@]+\.[^@]+$", email)

def mx_lookup(domain):
    try:
        records = dns.resolver.resolve(domain, "MX")
        return [str(r.exchange) for r in records]
    except:
        return []

def spf_check(domain):
    try:
        records = dns.resolver.resolve(domain, "TXT")
        for r in records:
            if "v=spf1" in str(r):
                return True
        return False
    except:
        return False

def dmarc_check(domain):
    try:
        dns.resolver.resolve(f"_dmarc.{domain}", "TXT")
        return True
    except:
        return False

def gravatar_check(email):
    h = hashlib.md5(email.lower().encode()).hexdigest()
    url = f"https://www.gravatar.com/avatar/{h}?d=404"
    r = requests.get(url, headers=HEADERS)
    return r.status_code == 200

def account_check(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=10)
        return r.status_code == 200
    except:
        return False

def run():
    email = input("Email > ").strip()

    if not valid_email(email):
        print("Invalid email format")
        return

    user, domain = email.split("@")

    print("\n--- Email OSINT ---")

    print(f"Email format           : Valid")
    print(f"Domain                 : {domain}")

    mx = mx_lookup(domain)
    print(f"MX Records             : {'Yes' if mx else 'No'}")

    print(f"SPF Present            : {'Yes' if spf_check(domain) else 'No'}")
    print(f"DMARC Present          : {'Yes' if dmarc_check(domain) else 'No'}")

    print(f"Gravatar Profile       : {'Yes' if gravatar_check(email) else 'No'}")

    # Correlations
    print("\n--- Account Correlation ---")
    print(f"YouTube                : {'Likely' if account_check(f'https://www.youtube.com/@{user}') else 'No'}")
    print(f"Twitter/X              : {'Likely' if account_check(f'https://twitter.com/{user}') else 'No'}")
    print(f"GitHub                 : {'Likely' if account_check(f'https://github.com/{user}') else 'No'}")

    print("\nNote:")
    print("- Email existence cannot be fully confirmed")
    print("- Results are correlation-based, not guaranteed")
