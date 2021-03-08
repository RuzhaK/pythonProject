initial_health = 100
health = initial_health
bitcoins = 0
dungeon_rooms = input().split("|")
is_alive=True
for i in range(0, len(dungeon_rooms)):
    command, number = dungeon_rooms[i].split()
    amount = int(number)
    if command == "potion":
        if amount+health>initial_health:
            amount=initial_health-health
            health=initial_health
        else:
            health=health+amount
        #health = min(health+amount, initial_health)
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += amount
        print(f"You found {amount} bitcoins.")

    else:
        health -= amount
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {i+1}")
            is_alive=False
            break
if is_alive==True:
    print(f"You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")

