password = input()

is_it_valid = True


def validate_password(password):
    global is_it_valid
    counter = 0
    if not (10 >= len(password) >= 6):
        is_it_valid = False
        print("Password must be between 6 and 10 characters")

    for el in password:
        if not el.isdigit() and not el.isalpha():
            is_it_valid = False
            print("Password must consist only of letters and digits")
            break
    for el in password:
        if el.isdigit():
            counter += 1
    if counter < 2:
        is_it_valid = False
        print("Password must have at least 2 digits")

    return is_it_valid


if validate_password(password):
    print("Password is valid")
