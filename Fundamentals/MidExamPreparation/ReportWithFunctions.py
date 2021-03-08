friends = input().split(", ")
line = input()
lost = 0
blacklisted = 0


def index_in_range(index, friends):
    if 0 <= index < len(friends):
        return True


def name_not(index, friends):
    if friends[index] != "Lost" and friends[index] != "Blacklisted":
        return True


def name_in(name, friends):
    if name in friends:
        return True


while line != "Report":
    command, *value = line.split()
    if command == "Blacklist":
        name = value[0]
        if name_in(name, friends):
            friends = [x if x != name else "Blacklisted" for x in friends]

            blacklisted += 1
            print(f"{name} was blacklisted.")
        else:
            print(f"{name} was not found.")
    if command == "Error":
        index = int(value[0])
        name=friends[index]
        if index_in_range(index, friends) and name_not(index, friends):
            lost += 1
            friends = [x if x != friends[index] else "Lost" for x in friends]
            print(f"{name} was lost due to an error.")
    if command == "Change":
        index = int(value[0])
        name_change = value[1]
        name_tochange=friends[index]
        if index_in_range(index, friends) and name_not(index,friends):
            friends[index] = name_change
            print(f"{name_tochange} changed his username to {name_change}.")

    line = input()
print(f"Blacklisted names: {blacklisted} ")
print(f"Lost names: {lost}")
print(" ".join(friends))
