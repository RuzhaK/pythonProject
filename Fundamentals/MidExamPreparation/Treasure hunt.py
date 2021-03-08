loot=input().split()
commands=input().split()
items=commands[1:]
[loot.insert(0,x) for x in items if x not in loot]


index=int(commands[1])
# mahame elementa ot tozi index i go zalepiame nakraia, pop maha no i vrashta
loot.append(loot.pop(index))

# mahame poslednite count indexa
count=int(commands[1])
stolen=loot[-count:]


averageGain=sum([len(x) for x in loot])/len(loot)