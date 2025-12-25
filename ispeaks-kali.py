#!/usr/bin/env python3

# ===== Colors =====
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# ===== Imports =====

import os
from modules import system
from modules import ip_osint
from modules import domain_osint
from modules import password_check
from modules import roblox_osint
from modules import port_scanner
from modules import hash_identifier
from modules import username_osint
from modules import discord_menu
from modules import email_osint
from modules import email_discord_correlation
from modules import phone_osint
from modules import sqlmap_tool

# ===== Clear screen function =====
def clear():
    os.system("cls" if os.name == "nt" else "clear")


# ===== Banner =====
def banner():
    print(f"""{GREEN}
===============================
          INFOHUNTER
{CYAN}     Pocket OSINT Toolkit{RESET}
===============================
""")

# ===== Area Menus =====

def osint_menu():
    while True:
        clear()
        print("""
[1] IP OSINT
[2] Domain OSINT
[3] Username OSINT
[4] Email OSINT
[5] Email → Discord Correlation
[6] Phone OSINT
[0] Back
""")

        choice = input("osint > ")

        if choice == "1":
            ip_osint.run()
            input("\nPress Enter to return…")

        elif choice == "2":
            domain_osint.run()
            input("\nPress Enter to return…")

        elif choice == "3":
            username_osint.run()
            input("\nPress Enter to return…")

        elif choice == "4":
            email_osint.run()
            input("\nPress Enter to return…")

        elif choice == "5":
            email_discord_correlation.run()
            input("\nPress Enter to return…")

        elif choice == "6":
            phone_osint.run()
            input("\nPress Enter to return…")

        elif choice == "0":
            break

        else:
            print("Invalid option")
            input("\nPress Enter to continue…")

def network_menu():
    while True:
        print("""
[ Network & Scanning ]
[1] Port Scanner
[2] SQL Injection Scanner
[0] Back
""")

        choice = input("network > ").strip()

        if choice == "1":
            port_scanner.run()
            input("\nPress Enter to return...")
        elif choice == "2":
            sqlmap_tool.run()
            input("\nPress Enter to return...")
        elif choice == "0":
            break
        else:
            print("Invalid option")




def credentials_menu():
    while True:
        clear()
        print("""
[1] Password Strength Checker
[2] Hash Identifier
[0] Back
""")
        choice = input("creds > ")

        if choice == "1":
            password_check.run()
            input("\nPress Enter to return…")
        elif choice == "2":
            hash_identifier.run()
            input("\nPress Enter to return…")
        elif choice == "0":
            break
        else:
            print("Invalid option")


def platform_menu():
    while True:
        clear()
        print("""
[1] Roblox OSINT
[2] Discord OSINT
[0] Back
""")
        choice = input("platforms > ")

        if choice == "1":
            roblox_osint.run()
            input("\nPress Enter to return…")
        elif choice == "2":
            discord_menu.run()
            input("\nPress Enter to return…")
        elif choice == "0":
            break
        else:
            print("Invalid option")


# ===== Main Menu =====
def main_menu():
    print("""
[1] OSINT & Recon
[2] Network & Scanning
[3] Credentials & Hashes
[4] Platform OSINT
[0] Exit
""")

# ===== Main Loop =====
while True:
    clear()        # <- clears screen
    banner()
    main_menu()
    choice = input("infohunt > ")

    if choice == "1":
        osint_menu()
    elif choice == "2":
        network_menu()
    elif choice == "3":
        credentials_menu()
    elif choice == "4":
        platform_menu()
    elif choice == "0":
        print("Exiting Infohunt")
        break
    else:
        print("Invalid option")
