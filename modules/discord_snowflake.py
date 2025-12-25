import datetime

DISCORD_EPOCH = 1420070400000

def run():
    snowflake = input("Snowflake ID: ").strip()

    if not snowflake.isdigit():
        print("Invalid snowflake")
        return

    timestamp = (int(snowflake) >> 22) + DISCORD_EPOCH
    created = datetime.datetime.utcfromtimestamp(timestamp / 1000)

    print("\n[ Discord Snowflake Decoder ]")
    print("Snowflake:", snowflake)
    print("Created:", created, "UTC")
