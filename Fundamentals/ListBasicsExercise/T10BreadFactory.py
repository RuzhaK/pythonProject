line=input().split("|")
initial_energy=100
energy=initial_energy
initial_coins=100
coins=initial_coins
day_completed=True
for word in line:
    ingredient, number=word.split("-")
    number=int(number)
    if ingredient=="rest":
        energy_gained = min(initial_energy-energy, number)
        energy=min(initial_energy, energy+number)

        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {energy}.")
    elif ingredient=="order":

        if energy<30:
            energy+=50
            print(f"You had to rest!")
            continue
        else:
            energy -= 30
            coins+=number
            print(f"You earned {number} coins.")
    else:
        coins-=number
        if coins>0:
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            day_completed=False
            break

if day_completed:
    print(f"Day completed!\nCoins: {coins}\nEnergy: {energy}")