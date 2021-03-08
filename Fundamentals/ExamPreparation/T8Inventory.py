health = 100
bitcoins = 0
rooms = input().split("|")
is_alive=True
for i in range(len(rooms)):
    room=rooms[i]
    args=room.split()
    command=args[0]
    number = int(args[1])
    if command == "potion":
        temp=health
        health+=number
        healed=number

        if health>100:
            health=100
            healed=100-temp
        else:
            health=health+number

        print(f"You healed for {healed} hp")
        print(f"Current health: {health} hp.")

    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")

    else:
        health -= number
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

#todo 50/100 1:14 https://softuni.bg/trainings/resources/video/51221/video-01-july-2020-slavi-kapsalov-python-fundamentals-may-2020/2833
