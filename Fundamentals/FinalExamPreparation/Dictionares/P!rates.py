line=input()
cities={}
while line!="Sail":
    city, population, gold=line.split("||")
    if city in cities:

        cities[city]['population']+=int(population)
        cities[city]['gold']+=int(gold)
    else:
        cities[city]={'population':int(population),'gold':int(gold)}
    line=input()
text=input()
while text!="End":
    command, city,*tokens=text.split("=>")
    if command=="Plunder":
        people=int(tokens[0])
        gold=int(tokens[1])
        gold_stolen=min(gold, cities[city]['gold'])
        people_killed=min(people, cities[city]['population'])
        cities[city]['population'] -= people
        cities[city]['gold'] -= gold
        print(f"{city} plundered! {gold_stolen} gold stolen, {people_killed} citizens killed.")
        if cities[city]['population']<=0 or cities[city]['gold']<=0:
            cities.pop(city)
            print(f"{city} has been wiped off the map!")
    if command=="Prosper":
        gold=int(tokens[0])
        if gold<0:
            print("Gold added cannot be a negative number!" )
            text = input()
            continue
        else:
            cities[city]['gold'] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['gold']} gold.")


    text=input()
if len(cities)==0:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    sorted_cities=sorted(cities.items(),key=lambda x:(-x[1]['gold'],x[0]))
    for k,v in sorted_cities:
        print(f"{k} -> Population: {v['population']} citizens, Gold: {v['gold']} kg")
