n=int(input())
heroes={}
max_HP=100
max_MP=200
for i in range(n):
    hero, HP,MP=input().split()
    heroes[hero]={"HP":int(HP),"MP":int(MP)}
line=input()
while line!="End":
    command,name,*tokens=line.split(" - ")
    if command=="CastSpell":
        MP_needed=int(tokens[0])
        spell_name=tokens[1]
        if MP_needed<=heroes[name]["MP"]:
            heroes[name]["MP"]-=MP_needed
            print(f"{name} has successfully cast {spell_name} and now has {heroes[name]['MP']} MP!")
        else:
            print(f"{name} does not have enough MP to cast {spell_name}!")

    elif command=="TakeDamage":
        damage = int(tokens[0])
        attacker = tokens[1]
        heroes[name]["HP"]-=damage
        if heroes[name]["HP"] >0:
            print(f"{name} was hit for {damage} HP by {attacker} and now has {heroes[name]['HP']} HP left!")
        else:
            heroes.pop(name)
            print(f"{name} has been killed by {attacker}!")

    elif command=="Recharge":
        amount = int(tokens[0])
        amount_recovered=min(max_MP-heroes[name]["MP"], amount)
        heroes[name]["MP"]+=amount_recovered
        print(f"{name} recharged for {amount_recovered} MP!")
    elif command=="Heal":
        amount = int(tokens[0])
        amount_recovered = min(max_HP - heroes[name]["HP"], amount)
        heroes[name]["HP"] += amount_recovered
        print(f"{name} healed for {amount_recovered} HP!")
    line=input()
sorted_heroes=sorted(heroes.items(), key=lambda x:(-x[1]['HP'],x[0]))
for k,v in sorted_heroes:
    print(k)
    print(f"  HP: {v['HP']}")
    print(f"  MP: {v['MP']}")