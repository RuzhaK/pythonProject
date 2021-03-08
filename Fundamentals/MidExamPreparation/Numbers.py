line=[int(x) for x in input().split()]
average=sum(line)/len(line)
greater=[x for x in line if x>average]
if len(greater)==0:
    print("No")


else:
    greater = sorted(greater)
    greater.reverse()
    boundary=min(5, len(greater))
    final=greater[:boundary]
    print(" ".join(map(str,final)))



