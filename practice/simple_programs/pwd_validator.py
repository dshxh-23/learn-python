def main():
    ip = input("Password: ")
    if chk_pwd(ip):
        print("Valid")
    else:
        print("Invalid")


def chk_pwd(pwd):
    if chk_chrs(pwd) and chk_digits(pwd) and chk_spchrs(pwd) and chk_upper(pwd):
        return True
    else:
        return False


def chk_chrs(pwd):
    return True if len(pwd) >=8 else False

def chk_upper(pwd):
    for c in pwd:
        if c.isupper():
            return True
    return False

def chk_digits(pwd):
    for c in pwd:
        if c.isdigit():
            return True
    return False

def chk_spchrs(pwd):
    for c in pwd:
        if c.isalnum():
            return True
    return False



if __name__ == "__main__":
    main()