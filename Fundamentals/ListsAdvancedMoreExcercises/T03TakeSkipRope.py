line=input()
numbers_list=[]
non_numbers_list=[]
result=[]
for ch in line:
    if ch.isdigit():
        numbers_list.append(ch)
    else:
        non_numbers_list.append(ch)
take_list=[]
skip_list=[]
for i in range(len(numbers_list)):
    if i%2==0:
        take_list.append(numbers_list[i])
    else:
        skip_list.append(numbers_list[i])
position=0
for i in range (len(take_list)):
    boundary=position+int(take_list[i])
    result+=non_numbers_list[position:boundary]
    non_numbers_list=non_numbers_list[:position]+non_numbers_list[boundary:]


    position+=int(skip_list[i])


print(''.join(result))