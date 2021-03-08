password=input()
tokens=input()


def take_odd(password):
    result=""
    for i in range(1, len(password),2):

        result+=password[i]
    print(result)
    return result


def cut(raw_pass,i, length):
    sub_string=raw_pass[i:i+length]
    result=raw_pass[:i]+raw_pass[i+length:]
    print(result)
    return result


def substitute(password, sub_str, replacement):
    result=password.replace(sub_str,replacement)
    if result==password:
        print("Nothing to replace!")
    else:
        print(result)
    return result




while tokens!="Done":
    data=tokens.split(' ')
    command=data[0]
    if command=="TakeOdd":
        password=take_odd(password)
    elif command=="Cut":
        index,length=[int(el)for el in data[1:]]
        password=cut(password,index, length)
    elif command=="Substitute":
        sub_str, replacement=data[1:]
        password=substitute(password,sub_str,replacement)

    tokens = input()
print(f"Your password is: {password}")