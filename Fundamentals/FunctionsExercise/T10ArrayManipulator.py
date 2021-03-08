def exchange(numbers_list,index):
    if 0<=index<len(numbers_list):
        first_part=numbers_list[:index+1]
        second_part=numbers_list[index+1:]
        exchanged_list=first_part+second_part
        return exchanged_list
    else:
        print("Invalid index")
        return numbers_list
def get_max_odd(nums_list):
    filter_only_odds=[]
    for el in nums_list:
        if el%2==1:
            filter_only_odds.append(el)

    max_odd=max(filter_only_odds)
    for index in range(len(nums_list,-1,-1)):
        if nums_list[index]==max_odd:
            print(index)
            break

numbers_as_string=input().split()
numbers=list(map(int,numbers_as_string))
command=input()


def get_max_even(nums_list):
    filter_only_evens = []
    for el in nums_list:
        if el % 2 == 0:
            filter_only_evens.append(el)

    max_even = max(filter_only_evens)
    for index in range(len(nums_list, -1, -1)):
        if nums_list[index] == max_even:
            print(index)
            break

   #todo finish


while command=="End":
    action=command.split()[0]
    if action=="exchange":
        index=int(command.split()[1])
        numbers=exchange(numbers,index)
    elif action == "max":
        if command.split()[1]=="odd":
            get_max_odd()
        elif command.split()[1]=="even":
            get_max_even()


    command = input()