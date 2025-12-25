import socket

COMMON_PORTS = [
    21, 22, 23, 25, 53,
    80, 110, 139, 143,
    443, 445, 8080
]

def run():
    target = input("Target IP or domain: ")

    print("\n[ PORT SCAN RESULTS ]")

    for port in COMMON_PORTS:
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((target, port))
            sock.close()

            if result == 0:
                print(f"[+] Port {port}: OPEN")
            else:
                print(f"[-] Port {port}: CLOSED")

        except:
            print(f"[!] Port {port}: ERROR")
