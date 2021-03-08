friends=input().split(", ")
line=input()
blacklisted=0
lost=0
while not line=="Report":
    command, *value=line.split()
    if command=="Blacklist":
        name=value[0]

        if name in friends:
            if name != "Blacklisted" and name != "Lost":
                for i in range(len(friends)):
                    if friends[i]==name:
                        blacklisted += 1
                friends = ["Blacklisted" if x == name else x for x in friends]
            #     index=friends.index(name)
            #     friends.pop(index)
            #     friends.insert(index,"Blacklisted")
                print(f"{name} was blacklisted.")
                

        else:
            print(f"{name} was not found")
    elif command=="Error":
        index=int(value[0])
        if 0 <= index < len(friends):
            if friends[index]!="Blacklisted" and friends[index]!="Lost" and friends[index]!=' ' and friends[index]!="":
                name=friends.pop(index)
                friends.insert(index,"Lost")
                print(f"{name} was lost due to an error.")
                lost+=1
    elif command=="Change":
        index = int(value[0])
        new_name=value[1]

        if 0<=index<len(friends):
            if friends[index] != "Blacklisted" and friends[index] != "Lost":
                old_name=friends.pop(index)
                friends.insert(index, new_name)
                print(f"{old_name} changed his username to {new_name}. ")
    line = input()
print(f"Blacklisted names: {blacklisted}")
print(f"Lost names: {lost} ")
print(" ".join(friends))
