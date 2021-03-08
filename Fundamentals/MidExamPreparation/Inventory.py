items=input().split(", ")
tokens=input().split(" - ")
while tokens[0]!="Craft!":

    if tokens[0]=="Collect":
        if tokens[1] in items:
            tokens = input().split(" - ")
            continue

        items.append(tokens[1])
    elif tokens[0]=="Drop":
        if tokens[1] in items:
            items.remove(tokens[1])
    elif tokens[0]=="Combine Items":
        items_to_combine=tokens[1].split(":")
        if items_to_combine[0] in items:
            index=items.index(items_to_combine[0])
            items.insert(index+1,items_to_combine[1])
    elif tokens[0]=="Renew":
        if tokens[1] in items:
            items.remove(tokens[1])
            items.append(tokens[1])
    tokens = input().split(" - ")
print(', '.join(items))



