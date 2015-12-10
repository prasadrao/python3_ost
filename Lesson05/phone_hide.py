import re

def phone_hide(text):

    #Don't forget to use a raw string constant!
    return re.subn(r"\d{3}-\d{4}", "XXX-XXXX", text)

if __name__ == "__main__":
    print(phone_hide("""While I was at the store I tried to call 555-123-4567 on my mobile
but accidentally called 555-754-4321. The person on the line redirected me to
999-999-9999 which I don't think is a real number. Neither is 000-000-0000 or 55
5-555-0000.
Well, I will try (555)-123-4567 again now."""))
