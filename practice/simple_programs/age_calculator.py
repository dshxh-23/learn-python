import re
import sys
import inflect
from datetime import date


def main():
    print(calc_age(input("What's your DoB (yyyy-mm-dd): ")))


def calc_age(ip):

    if not validate_ip(ip):
        sys.exit("Incorrect or missing DoB")

    cd = date.today()
    dob = get_dob(ip)
    age = cd - dob
    minutes = round(int(age.total_seconds())/60)

    p = inflect.engine()
    return f"{(p.number_to_words(minutes)).capitalize().replace(' and ', ' ')} minutes"


def validate_ip(dob):
    return True if re.fullmatch(r"\d\d\d\d-\d\d-\d\d", dob) else False

def get_dob(ip):
    year, month, day = ip.split("-")
    return date(int(year), int(month), int(day))


if __name__ == "__main__":
    main()
