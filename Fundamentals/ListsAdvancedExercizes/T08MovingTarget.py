targets_as_strings=input().split()
targets=[int(targets) for targets in targets_as_strings]
#todo list comprehension example
#targets=list(map(int,targets_as_strings))
commands_list=input()



def shoot_index_power(index,targets_list,power):
    if 0<=index<len(targets_list):
        if targets_list[index]>power:
            targets_list[index] -= power
        else:targets_list.pop(index)
    return targets_list


def add_index_value(index, targets_list, value):
    if 0 <= index < len(targets_list):
        targets_list.insert(index,value)
    else:
        print("Invalid placement!")

    return targets_list


def strike_index_radius(index, targets_list, radius):
    if 0 <= index < len(targets_list):
        left_index=index-radius
        right_index=index+radius
        if left_index>=0 and right_index<len(targets_list):

            for i in range(right_index, left_index-1,-1):
                targets_list.pop(i)
        else:
            print("Strike missed!")

    return targets_list


while not commands_list=="End":
    command, index, data=commands_list.split()
    index=int(index)
    power=int(data)
    if command=="Shoot":
        shoot_index_power(index, targets, power)

    elif command=="Add":
        add_index_value(index, targets, power)


    elif command=="Strike":

        strike_index_radius(index, targets, power)



    commands_list = input()
print('|'.join([str(el) for el in targets]))
