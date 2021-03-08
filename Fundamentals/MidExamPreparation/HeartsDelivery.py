neighborhood=[int(x) for x in input().split("a")]
commands=input()
position=0
while commands!="Love":
    jump,length=commands.split()
    length=int(length)
    position=position+length
    if position>=len(neighborhood):
        position=0
    if neighborhood[position]==0:
        print(f"")
    else:
        neighborhood-=2




    commands = input()