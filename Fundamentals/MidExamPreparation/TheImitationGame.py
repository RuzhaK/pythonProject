message=input()
instructions =input()
while instructions !="Decode" :
    commands=instructions.split("|")
    if commands[0]=="Move":
       first=message[:int(commands[1])]
       second=message[int(commands[1]):]
       message=second+first

    elif commands[0]=="ChangeAll":
        substring = commands[1]
        replacement = commands[2]
        new_message=message.split(substring)
        message=f"{replacement.join(new_message)}"
    elif commands[0]=="Insert":

        first = message[:int(commands[1])]
        second = message[int(commands[1]):]
        substring = commands[2]
        message = first + substring + second


    instructions = input()
print(f"The decrypted message is: {message}")


