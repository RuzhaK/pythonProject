numbers = input().split()

guess_line = input()
moves = 0
didnt_win=True
while not guess_line == "end":

    index1, index2 = guess_line.split()
    index1 = int(index1)
    index2 = int(index2)
    moves += 1
    if index1 == index2 or len(numbers) <= index1 or index1 < 0 or len(numbers) <= index2 or index2 < 0:
        print("Invalid input! Adding additional elements to the board")
        new_index = len(numbers) // 2
        new_element = "-"+str(moves)+"a"


        numbers.insert(new_index, new_element)
        numbers.insert(new_index + 1, new_element)
        guess_line = input()
        continue
    if numbers[index1] == numbers[index2]:
        matching_element = numbers[index2]
        numbers.pop(max(index1, index2))
        numbers.pop(min(index1, index2))
        print(f"Congrats! You have found matching elements - {matching_element}!")
    else:
        print("Try again!")
    if len(numbers) == 0:
            print(f"You have won in {moves} turns!")
            didnt_win=False
            break
    guess_line = input()
if didnt_win:
    print(f"Sorry you lose :(")
    #todo printing int list without commas and brackets
    print(' '.join(map(str, numbers)))

