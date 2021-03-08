line_1=input()
line_2=input()
result=""
previous_string=line_1


n=len(line_2)
for i in range(n):
    for j in range(i+1):
        result += line_2[j]
    for j in range(i+1,n):
        result +=line_1[j]

    if not result==previous_string:
        print(result)
    previous_string=result
    result=""

