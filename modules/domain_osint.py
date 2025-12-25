import subprocess
import socket
import requests

CYAN = "\033[96m"
RESET = "\033[0m"

def row(label, value):
    print(f"{label:<22}: {CYAN}{value}{RESET}")

def run():
    domain = input("Enter domain target: ").strip()

    print("\n========== DOMAIN INFORMATION ==========\n")

    # WHOIS
    print("--- WHOIS ---")
    try:
        whois = subprocess.check_output(
            ["whois", domain], stderr=subprocess.DEVNULL, text=True
        )

        for line in whois.splitlines():
            keywords = [
                "Registrar:",
                "Creation Date:",
                "Updated Date:",
                "Registry Expiry Date:",
                "Domain Status:",
                "Registrant Organization:",
                "Registrar Abuse Contact Email",
            ]
            if any(k in line for k in keywords):
                print(line)

    except:
        print("WHOIS lookup failed.")

    # DNS
    print("\n--- DNS RECORDS ---")

    def dig(record):
        try:
            return subprocess.check_output(
                ["dig", domain, record, "+short"],
                stderr=subprocess.DEVNULL,
                text=True
            ).strip() or "None"
        except:
            return "None"

    row("A Records", dig("A"))
    row("AAAA Records", dig("AAAA"))
    row("NS Records", dig("NS"))
    row("MX Records", dig("MX"))
    row("TXT Records", dig("TXT"))
    row("CNAME", dig("CNAME"))

    # IP & Hosting
    print("\n--- HOSTING / NETWORK ---")
    try:
        ip = socket.gethostbyname(domain)
        row("Resolved IP", ip)

        ipinfo = requests.get(f"https://ipwho.is/{ip}", timeout=10).json()

        row("Country", ipinfo.get("country"))
        row("Region", ipinfo.get("region"))
        row("City", ipinfo.get("city"))
        row("ISP", ipinfo.get("connection", {}).get("isp"))
        row("ASN", ipinfo.get("connection", {}).get("asn"))
        row("ORG", ipinfo.get("connection", {}).get("org"))

    except:
        row("Resolved IP", "Failed")

    # HTTPS
    print("\n--- SECURITY ---")
    try:
        r = requests.get(f"https://{domain}", timeout=5)
        row("HTTPS", "Enabled")
        row("Status Code", r.status_code)
    except:
        row("HTTPS", "Not supported")

    # EMAIL SECURITY
    print("\n--- EMAIL SECURITY ---")
    txt = dig("TXT")
    row("SPF Present", "Yes" if "spf" in txt.lower() else "No")
    row("DMARC Present", "Yes" if "dmarc" in txt.lower() else "No")

    input("\n[ + ] Press Enter to continue...")
