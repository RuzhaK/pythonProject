key=input()
line=input()
while line!="Generate":
    command, *tokens=line.split(">>>")
    if command=="Contains":
        substring=tokens[0]
        if substring in key:
            print(f"{key} contains {substring}")
        else:
            print("Substring not found!")
    elif command=="Flip":
        case=tokens[0]
        start_index=int(tokens[1])
        end_index=int(tokens[2])
        if case=="Upper":
            substring=key[start_index:end_index].upper()
            key=key[:start_index]+substring+key[end_index:]

        else:
            substring = key[start_index:end_index].lower()
            key = key[:start_index] + substring + key[end_index:]
        print(key)

    elif command=="Slice":
        start_index = int(tokens[0])
        end_index = int(tokens[1])
        key = key[:start_index] +  key[end_index:]
        print(key)
    line=input()
print(f"Your activation key is: {key}")
