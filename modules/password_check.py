import re

def run():
    password = input("Enter password to check: ")

    score = 0

    if len(password) >= 8:
        score += 1
    if re.search(r"[A-Z]", password):
        score += 1
    if re.search(r"[a-z]", password):
        score += 1
    if re.search(r"[0-9]", password):
        score += 1
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1

    print("\n[ PASSWORD ANALYSIS ]")

    if score <= 2:
        print("Strength: VERY WEAK ❌")
    elif score == 3:
        print("Strength: WEAK ⚠️")
    elif score == 4:
        print("Strength: STRONG ✅")
    elif score == 5:
        print("Strength: VERY STRONG 🔥")
