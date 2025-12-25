import platform
import os

def run():
    print("\n[ SYSTEM INFORMATION ]")
    print("OS:", platform.system())
    print("Release:", platform.release())
    print("Architecture:", platform.machine())
    print("User:", os.getenv("USER"))
