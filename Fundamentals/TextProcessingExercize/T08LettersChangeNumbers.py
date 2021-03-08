def get_letter_position(letter):
    position=ord(letter)-96
    if letter.isupper():
        position=ord(letter)-64
    return position
def calculate_item_result(item):
    first_letter = item[0]
    second_letter = item[-1]
    number = int(item[1:-1])
    first_letter_position = get_letter_position(first_letter)
    second_letter_position = get_letter_position(second_letter)
    result = 0
    if first_letter.isupper():
        result = number / first_letter_position
    else:
        result = number * first_letter_position

    if second_letter.isupper():
        result = result -second_letter_position
    else:
        result = result +second_letter_position
    return result

line=input().split()
total_sum=0
for item in line:
    result=calculate_item_result(item)
    total_sum+=result

print(f"{total_sum:.2f}")
