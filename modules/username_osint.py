import requests
import sys
import time

TIMEOUT = 6
HEADERS = {
    "User-Agent": "Mozilla/5.0"
}

PLATFORMS = {
    "GitHub": "https://github.com/{}",
    "GitLab": "https://gitlab.com/{}",
    "Twitter / X": "https://x.com/{}",
    "Instagram": "https://www.instagram.com/{}/",
    "Reddit": "https://www.reddit.com/user/{}/",
    "TikTok": "https://www.tiktok.com/@{}",
    "YouTube": "https://www.youtube.com/@{}",
    "Pinterest": "https://www.pinterest.com/{}/",
    "SoundCloud": "https://soundcloud.com/{}",
    "Twitch": "https://www.twitch.tv/{}",
    "Steam": "https://steamcommunity.com/id/{}",
    "Medium": "https://medium.com/@{}",
    "Dev.to": "https://dev.to/{}",
    "Keybase": "https://keybase.io/{}",
    "Pastebin": "https://pastebin.com/u/{}",
    "Roblox": "https://www.roblox.com/user.aspx?username={}",
    "Telegram": "https://t.me/{}",
    "Snapchat": "https://www.snapchat.com/add/{}"
}

def check_username(platform, url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=TIMEOUT)

        if r.status_code == 200:
            # basic false-positive filtering
            if "not found" in r.text.lower():
                return False
            if "doesn't exist" in r.text.lower():
                return False
            if "page not found" in r.text.lower():
                return False
            return True

        return False

    except requests.RequestException:
        return None


def run():
    username = input("Username > ").strip()

    if not username:
        print("No username provided")
        return

    print(f"\nResults for: {username}\n")

    found = 0

    for platform, base_url in PLATFORMS.items():
        url = base_url.format(username)
        result = check_username(platform, url)

        if result is True:
            print(f"[FOUND] {platform:<18} → {url}")
            found += 1
        elif result is False:
            print(f"[NOT FOUND] {platform}")
        else:
            print(f"[ERROR] {platform}")

        time.sleep(0.5)

    print(f"\nDone. Found on {found} platform(s).\n")
