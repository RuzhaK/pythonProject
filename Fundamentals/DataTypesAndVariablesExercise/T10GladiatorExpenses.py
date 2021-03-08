lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
expenses = 0
count_of_shields_broken = 0

for fight_num in range(1, lost_fights + 1):
    if fight_num % 2 == 0:
        expenses += helmet_price

    if fight_num % 3 == 0:
        expenses += sword_price
    if fight_num % 3 == 0 and fight_num % 2 == 0:
        expenses += shield_price
        count_of_shields_broken += 1
        if count_of_shields_broken % 2==0:
            expenses += armour_price

print(f"Gladiator expenses: {expenses:.2f} aureus")
