import requests
import socket

GREEN = "\033[92m"
CYAN = "\033[96m"
RESET = "\033[0m"

def row(label, value):
    print(f"{label:<20}: {CYAN}{value}{RESET}")

def run():
    ip = input("Enter IP target: ").strip()

    try:
        r = requests.get(f"https://ipwho.is/{ip}", timeout=10)
        data = r.json()

        if not data.get("success", True):
            print("Invalid IP or lookup failed.")
            return

        print("\n========== IP INFORMATION ==========\n")

        row("IP Address", data.get("ip"))
        row("Type", "IPv4" if "." in ip else "IPv6")

        print("\n--- GEOLOCATION ---")
        row("Country", data.get("country"))
        row("Country Code", data.get("country_code"))
        row("Region", data.get("region"))
        row("City", data.get("city"))
        row("Postal", data.get("postal"))
        row("Latitude", data.get("latitude"))
        row("Longitude", data.get("longitude"))
        row("Timezone", data.get("timezone", {}).get("id"))
        row("UTC Offset", data.get("timezone", {}).get("utc"))

        if data.get("latitude") and data.get("longitude"):
            row(
                "Google Maps",
                f"https://www.google.com/maps/@{data['latitude']},{data['longitude']},8z"
            )

        print("\n--- NETWORK ---")
        row("ASN", data.get("connection", {}).get("asn"))
        row("ISP", data.get("connection", {}).get("isp"))
        row("Organization", data.get("connection", {}).get("org"))
        row("Domain", data.get("connection", {}).get("domain"))

        print("\n--- SECURITY / TYPE ---")
        row("Hosting", data.get("connection", {}).get("type"))
        row("VPN / Proxy", data.get("security", {}).get("vpn"))
        row("Tor Exit", data.get("security", {}).get("tor"))
        row("Proxy", data.get("security", {}).get("proxy"))
        row("Bogon IP", data.get("bogon"))

        print("\n--- REVERSE DNS ---")
        try:
            hostname = socket.gethostbyaddr(ip)[0]
            row("Hostname", hostname)
        except:
            row("Hostname", "None")

        print("\n--- ABUSE CONTACT ---")
        abuse = data.get("abuse", {})
        row("Abuse Email", abuse.get("email"))
        row("Abuse Phone", abuse.get("phone"))

    except Exception as e:
        print("Error:", e)

    input("\n[ + ] Press Enter to continue...")
