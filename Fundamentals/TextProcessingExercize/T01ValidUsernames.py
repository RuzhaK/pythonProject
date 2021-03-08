def is_right_length(word):
    if len(word) <= 16 and len(word) >= 3:
        return True
    else:
        return False


def contains_right_symbols(word):
    for ch in word:
        if ch.isalnum() or ch == chr(95) or ch == chr(45):
            continue
        else:
            return False
    return True



line = input().split(", ")
for i in range(len(line)):
    word = line[i]
    if is_right_length(word) and contains_right_symbols(word):
        print(word)
