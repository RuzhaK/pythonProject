devisor=int(input())
bound=int(input())
n=0
for num in range(bound,0,-1):
    if num%devisor==0:
        n=num
        break
print(n)