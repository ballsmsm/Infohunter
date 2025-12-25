import datetime

DISCORD_EPOCH = 1420070400000

def run():
    user_id = input("Discord User ID: ").strip()

    if not user_id.isdigit():
        print("Invalid ID")
        return

    timestamp = (int(user_id) >> 22) + DISCORD_EPOCH
    created = datetime.datetime.utcfromtimestamp(timestamp / 1000)

    print("\n[ Discord User ID Info ]")
    print("User ID:", user_id)
    print("Created:", created, "UTC")
