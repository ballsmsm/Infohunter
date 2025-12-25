import os

def run():
    print("\n[ SQL Injection Scanner ]")
    target = input("Target URL (with parameter): ").strip()

    if "?" not in target or "=" not in target:
        print("URL must contain parameters (example: ?id=1)")
        return

    os.system(f"python $HOME/sqlmap/sqlmap.py -u \"{target}\" --batch")
