groceries=input().split("!")
line=input()
def if_exists(item, list):
    if item in list:
        return True
while line!="Go Shopping!":
    command, *token=line.split()
    item=token[0]
    if command=="Urgent":

        if if_exists(item, groceries):
            line=input()
            continue
        else:
            groceries.insert(0,item)
    elif command=="Unnecessary":
        if if_exists(item, groceries):
            groceries.remove(item)
    #         todo moje da triabwa cikal!
    elif command=="Correct":

        if if_exists(item,groceries):
            groceries=[token[1] if x==item else x for x in groceries]
    elif command=="Rearrange":
        if if_exists(item,groceries):
            groceries.remove(item)
            groceries.append(item)
    # todo
    line = input()

print(*groceries, sep = ", ")