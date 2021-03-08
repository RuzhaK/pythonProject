year=int(input())+1


while True:
    is_happy = True
    year_as_string=str(year)
    for index_1 in range(len(year_as_string)):
        for index_2 in range(len(year_as_string)):
            if index_2==index_1:
                continue
            if year_as_string[index_2]==year_as_string[index_1]:
                is_happy=False
    if is_happy==True:
        print(year_as_string)
        break
    else:
        year+=1

