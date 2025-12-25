import phonenumbers
from phonenumbers import geocoder, carrier, timezone, number_type
import requests
import re

HEADERS = {"User-Agent": "Mozilla/5.0"}

def check_url(url):
    try:
        r = requests.get(url, headers=HEADERS, timeout=8)
        return r.status_code == 200
    except:
        return False

def run():
    number = input("Phone number (+countrycode) > ").strip()

    try:
        parsed = phonenumbers.parse(number, None)
    except:
        print("Invalid format")
        return

    if not phonenumbers.is_valid_number(parsed):
        print("Invalid phone number")
        return

    clean = re.sub(r"\D", "", number)

    print("\n--- PHONE OSINT ---")
    print(f"International Format : {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.INTERNATIONAL)}")
    print(f"E164 Format          : {phonenumbers.format_number(parsed, phonenumbers.PhoneNumberFormat.E164)}")
    print(f"Country              : {geocoder.description_for_number(parsed, 'en')}")
    print(f"Country Code         : +{parsed.country_code}")
    print(f"National Number      : {parsed.national_number}")
    print(f"Carrier              : {carrier.name_for_number(parsed, 'en') or 'Unknown'}")

    tz = timezone.time_zones_for_number(parsed)
    print(f"Timezone(s)          : {', '.join(tz) if tz else 'Unknown'}")

    ntype = number_type(parsed)
    if ntype == phonenumbers.PhoneNumberType.MOBILE:
        ltype = "Mobile"
    elif ntype == phonenumbers.PhoneNumberType.FIXED_LINE:
        ltype = "Landline"
    elif ntype == phonenumbers.PhoneNumberType.VOIP:
        ltype = "VoIP"
    else:
        ltype = "Other"

    print(f"Line Type            : {ltype}")

    print("\n--- PLATFORM CORRELATION ---")
    print(f"WhatsApp             : {'Possible' if check_url(f'https://wa.me/{clean}') else 'Not detected'}")
    print(f"Telegram             : {'Possible' if check_url(f'https://t.me/{clean}') else 'Not detected'}")
    print(f"Viber                : {'Possible' if check_url(f'https://invite.viber.com/?number={clean}') else 'Not detected'}")
    print(f"Truecaller Page      : {'Exists' if check_url(f'https://www.truecaller.com/search/{parsed.country_code}/{clean}') else 'Not detected'}")

    print("\n--- SEARCH FOOTPRINT ---")
    print(f"Google Search URL    : https://www.google.com/search?q={clean}")
    print(f"Facebook Search URL  : https://www.facebook.com/search/top?q={clean}")
    print(f"Twitter/X Search URL : https://twitter.com/search?q={clean}")
