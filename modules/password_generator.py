from random import choice

ALPHABET            = list('abcdefghijklmnopqrstuvwxyz')
UPPERCASE_ALPHABET  = [letter.upper() for letter in ALPHABET]
NUMBERS             = list('0123456789')
SPECIAL_CHARACTERS  = list("!@#$%^&*()_-+={[}]\:;<,>.?/")


def create_password(include_special_characters=True, password_length=16):
    new_password = ''
    
    for i in range(password_length):
        if include_special_characters:
            new_password += choice(choice([ALPHABET, UPPERCASE_ALPHABET, NUMBERS, SPECIAL_CHARACTERS]))
        else:
            new_password += choice(choice([ALPHABET, UPPERCASE_ALPHABET, NUMBERS]))
    
    return new_password