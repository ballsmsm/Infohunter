import requests
import re

HEADERS = {"User-Agent": "Mozilla/5.0"}

def check_discord(email):
    results = []
    # Discord public username lookup patterns
    # Note: Discord API does not allow direct email lookup
    # We'll use known URL patterns for user discovery (public servers / invites)
    # This is the max realistic correlation without root or private APIs

    # Example 1: check if email appears in Discord-related search
    search_urls = [
        f"https://discord.com/search?q={email}",
        f"https://discordlookup.me/search?query={email}"
    ]

    for url in search_urls:
        try:
            r = requests.get(url, headers=HEADERS, timeout=10)
            if r.status_code == 200 and email in r.text:
                results.append(url)
        except:
            continue

    return results

def run():
    email = input("Email > ").strip()

    print("\n--- EMAIL → DISCORD CORRELATION ---")

    results = check_discord(email)

    if results:
        for r in results:
            print(f"Possible Discord correlation found: {r}")
    else:
        print("No public Discord correlation detected.")
