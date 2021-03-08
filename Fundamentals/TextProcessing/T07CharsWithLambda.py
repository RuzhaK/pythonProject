text = input()


def all_digits(text):
    return get_all_chars_meeting_criteria(text, lambda char: char.isdigit())


def all_letters(text):
    return get_all_chars_meeting_criteria(text, lambda char: char.isalpha())


def all_signs(text):
    return get_all_chars_meeting_criteria(text, lambda char: not char.isalpha() and not char.isdigit())


def get_all_chars_meeting_criteria(text, fn):
    result = ''
    for char in text:
        if fn(char):
            result += char
    return result


print(all_digits(text))
print(all_letters(text))
print(all_signs(text))
