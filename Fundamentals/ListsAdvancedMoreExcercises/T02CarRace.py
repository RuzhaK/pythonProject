numbers=input().split()
time_a=0
time_b=0

for i in range(int(len(numbers)/2)):
    if int(numbers[i])==0:
        time_a=0.8*time_a
    else:
        time_a+=int(numbers[i])
for i in range(len(numbers)-1,int(len(numbers)/2),-1):
    if int(numbers[i])==0:
        time_b=0.8*time_b
    else:
        time_b+=int(numbers[i])

if time_a<time_b:
    winner="left"
else:
    winner="right"
print(f"The winner is {winner} with total time: {min(time_b,time_a):.1f}")