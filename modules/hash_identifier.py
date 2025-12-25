def run():
    hash_value = input("Enter hash: ").strip()

    length = len(hash_value)

    print("\n[ HASH IDENTIFICATION ]")

    if length == 32:
        print("Possible type: MD5 / NTLM")
    elif length == 40:
        print("Possible type: SHA1")
    elif length == 64:
        print("Possible type: SHA256")
    elif length == 128:
        print("Possible type: SHA512")
    else:
        print("Unknown or unsupported hash type")
