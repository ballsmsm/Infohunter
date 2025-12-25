#!/usr/bin/env python3

# ===== Colors =====
GREEN = "\033[92m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
RESET = "\033[0m"

# ===== Imports =====
from modules import system
from modules import ip_osint
from modules import domain_osint
from modules import password_check
from modules import roblox_osint
from modules import port_scanner
from modules import hash_identifier
from modules import username_osint
from modules import discord_menu

def banner():
    print(f"""{GREEN}
██████╗ ██╗ ██████╗ ██╗  ██╗██╗   ██╗
██╔══██╗██║██╔═══██╗██║ ██╔╝██║   ██║
██████╔╝██║██║   ██║█████╔╝ ██║   ██║
██╔═══╝ ██║██║   ██║██╔═██╗ ██║   ██║
██║     ██║╚██████╔╝██║  ██╗╚██████╔╝
╚═╝     ╚═╝ ╚═════╝ ╚═╝  ╚═╝ ╚═════╝
{CYAN}      INF0HUNTER  — Pocket OSINT Toolkit{RESET}
""")


def menu():
    print("""
[1] System Info
[2] IP OSINT
[3] Domain OSINT
[4] Password Strength Checker
[5] Roblox OSINT
[6] Port Scanner
[7] Hash Identifier
[8] Username OSINT
[9] Discord OSINT
[0] Exit
""")

# Show banner once
banner()

# Main menu loop
while True:
    menu()
    choice = input("ispeaks-kali > ")

    if choice == "1":
        system.run()
    elif choice == "2":
        ip_osint.run()
    elif choice == "3":
        domain_osint.run()
    elif choice == "4":
        password_checkrun()
    elif choice == "5":
        roblox_osint.run()
    elif choice == "6":
        port_scanner.run()
    elif choice == "7":
        hash_identifier.run()
    elif choice == "8":
        username_osint.run()
    elif choice == "9":
        discord_menu.run()
    elif choice == "0":
        print("Exiting Ispeak's Kali")
        break
    else:
        print("Invalid option")
