from modules import discord_userid
from modules import discord_server
from modules import discord_snowflake

def run():
    while True:
        print("""
==============================
      DISCORD OSINT TOOLS
==============================
[1] Discord User ID Info
[2] Discord Server Invite OSINT
[3] Discord Snowflake Decoder
[0] Back
""")

        choice = input("discord > ")

        if choice == "1":
            discord_userid.run()
        elif choice == "2":
            discord_server.run()
        elif choice == "3":
            discord_snowflake.run()
        elif choice == "0":
            break
        else:
            print("Invalid option")
