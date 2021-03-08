def has_winning_symbol(first_part, second_part):
    if first_part.count("$") >= 6 and second_part.count("$") >= 6:
        return "$"


    elif first_part.count("@") >= 6 and second_part.count("@") >= 6:
        return "@"


    elif first_part.count("^") >= 6 and second_part.count("^") >= 6:
        return "^"


    elif first_part.count("#") >= 6 and second_part.count("#") >= 6:
        return "#"
    else:
        return "a"



line = input().split(", ")
for i in range(len(line)):
    if len(line[i]) != 20:
        print("invalid ticket")
        continue
    first_part = line[i][:10]
    second_part = line[i][10:]




    winning_symbol = has_winning_symbol(first_part, second_part)
    if winning_symbol == "a":
        print(f"ticket \"{line[i]}\" - no match")
    else:
        count = min(first_part.count(winning_symbol), second_part.count(winning_symbol))

        if count == 10:
            print(f"ticket \"{line[i]}\" - {count}{winning_symbol} Jackpot!")
        else:
            print(f"ticket \"{line[i]}\" - {count}{winning_symbol}")
            #todo v judge na 0lev text mi dava greshka koiato tuk ia niama


    #
    # winning_one=6*"$"
    # winning_two=6*"#"
    # winning_three=6*"@"
    # winning_four=6*"^"

    # if winning_one in first_part and winning_one in second_part:
