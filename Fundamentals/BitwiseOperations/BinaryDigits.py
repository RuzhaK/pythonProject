number=int(input())
element=int(input())
count=0
while not number==0:
    reminder=number%2
    if reminder==element:
        count+=1
    number/=2
print(count)