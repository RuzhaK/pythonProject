energy=int(input())
line=input()
won_battles=0
battle_won=True
while line!="End of battle" :

    distance=int(line)
    if distance>energy:
        print(f"Not enough energy! Game ends with {won_battles}"
              f" won battles and {energy} energy")
        battle_won=False
        break
    else:
        energy-=distance
        won_battles+=1

    if won_battles%3==0:
        energy+=won_battles
    line = input()
if battle_won:
    print(f"Won battles: {won_battles}. Energy left: {energy}" )

