import requests

HEADERS = {"User-Agent": "Mozilla/5.0"}

def run():
    username = input("Roblox username: ")

    print("\n[ ROBLOX OSINT ]")

    try:
        payload = {
            "usernames": [username],
            "excludeBannedUsers": False
        }

        r = requests.post(
            "https://users.roblox.com/v1/usernames/users",
            json=payload,
            headers=HEADERS
        )

        data = r.json().get("data")

        if not data:
            print("[-] Roblox user not found")
            return

        user_id = data[0]["id"]

        r2 = requests.get(
            f"https://users.roblox.com/v1/users/{user_id}",
            headers=HEADERS
        )

        info = r2.json()

        print("[+] Roblox: FOUND")
        print("User ID:", info["id"])
        print("Display Name:", info["displayName"])
        print("Created:", info["created"])
        print("Banned:", info["isBanned"])

    except:
        print("[!] Roblox OSINT failed")
