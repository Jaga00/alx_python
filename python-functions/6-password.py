# function called validate_password that takes a password as input and performs checks

def validate_password(password):
    # Check the length of the password
    if len(password) < 8:
        return False

    # Check if the password has at least one uppercase letter, one lowercase letter, and one digit
    has_uppercase = False
    has_lowercase = False
    has_digit = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True

    if not (has_uppercase and has_lowercase and has_digit):
        return False

    # Check if the password has spaces
    if " " in password:
        return False

    return True
