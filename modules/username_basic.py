import requests

HEADERS = {"User-Agent": "Mozilla/5.0"}

def check(platform, url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        if r.status_code == 200:
            print(f"[+] {platform}: FOUND")
        else:
            print(f"[-] {platform}: Not found")
    except:
        print(f"[!] {platform}: Error")

def run():
    username = input("Target username: ")

    print("\n[ BASIC USERNAME OSINT ]")

    check("GitHub", f"https://github.com/{username}")
    check("Reddit", f"https://www.reddit.com/user/{username}")
    check("Twitter/X", f"https://twitter.com/{username}")
    check("Instagram", f"https://www.instagram.com/{username}")
    check("YouTube", f"https://www.youtube.com/@{username}")
    check("Facebook", f"https://www.facebook.com/{username}")
