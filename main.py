import string
import secrets


def make_secure_pass(length=16, include_uppercase=True, include_numbers=True, include_symbols=True):
    # base password
    chars = string.ascii_lowercase

    if include_uppercase:
        chars += string.ascii_uppercase
    if include_numbers:
        chars += string.digits
    if include_symbols:
        chars += string.punctuation


    password = ''.join(secrets.choice(chars) for _ in range(length))


    # ensure password meets criteria
    while True:
        conditions = []
        conditions.append(any(c.islower() for c in password))

        if include_uppercase:
            conditions.append(any(c.isupper() for c in password))

        if include_numbers:
            conditions.append(any(c.isdigit() for c in password))

        if include_symbols:
            conditions.append(any(c in string.punctuation for c in password))

        if all(conditions):
            break

        password = ''.join(secrets.choice(chars) for _ in range(length))

    return password


if __name__ == '__main__':
    print('Password examples:')
    print(f'Default password (16): {make_secure_pass()}')
    print(f'Easy password (12, non-numbers): {make_secure_pass(length=8, include_numbers=False)}')
    print(f'Symbols and Letters: {make_secure_pass(length=32, include_numbers=False)}')