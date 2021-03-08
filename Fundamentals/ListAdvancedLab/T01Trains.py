number=int(input())
wagon=[0]*number


tokens=input()
while tokens!="End":
    line=tokens.split()
    if line[0]=="add":
        wagon[-1]+=int(line[1])
    if line[0]=="insert":
        wagon[int(line[1])]+=int(line[2])
    if line[0]=="leave":
        wagon[int(line[1])]-=int(line[2])
    tokens = input()
print(wagon)