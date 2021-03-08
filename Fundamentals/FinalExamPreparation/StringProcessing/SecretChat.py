message=input()
line=input()
while not line=="Reveal":
    command,*value=line.split(":|:")
    if command=="InsertSpace":
        message=message[:int(value[0])]+" "+message[int(value[0]):]
        print(message)
    elif command=="Reverse":
        substring=value[0]
        if substring in message:
            message=message.split(substring,1)
            substring=substring[::-1]
            message=message[0]+message[1]+substring
            print(message)
        else:
            print("error")
            
    elif command=="ChangeAll":
        substring=value[0]
        replacement=value[1]
        if substring in message:
            message=message.replace(substring,replacement)
            print(message)

    line =input()
print(f"You have a new text message: {message}")