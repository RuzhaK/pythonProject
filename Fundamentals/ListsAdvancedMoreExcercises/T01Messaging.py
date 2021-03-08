numbers=input().split()
line=input()
output=""
for i in range(len(numbers)):
    number_as_string=numbers[i]
    sum=0
    for k in range(0,len(number_as_string)):
        number=int(number_as_string[k])
        sum+=number
    length=len(line)
    index=sum%length
    output+=line[index]
    line=line[:index]+line[index+1:]
print(output)




