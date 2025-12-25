import requests

def run():
    invite = input("Invite code (abc123): ").strip()
    url = f"https://discord.com/api/v9/invites/{invite}?with_counts=true"

    r = requests.get(url)

    if r.status_code != 200:
        print("Invalid or expired invite")
        return

    data = r.json()

    print("\n[ Discord Server OSINT ]")
    print("Server:", data["guild"]["name"])
    print("Server ID:", data["guild"]["id"])
    print("Members:", data.get("approximate_member_count"))
    print("Online:", data.get("approximate_presence_count"))
    print("Verification Level:", data["guild"]["verification_level"])
