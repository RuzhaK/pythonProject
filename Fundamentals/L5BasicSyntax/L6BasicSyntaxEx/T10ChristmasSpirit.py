quantity = int(input())
days = int(input())
christmasSpirit = 0
totalCost = 0
ORNAMENT_SET = 2
TREE_SKIRT = 5
TREE_GARLANDS = 3
TREE_LIGHTS = 15

for day_number in range(1, days + 1):
    if day_number % 11 == 0:
        quantity += 2

    if day_number % 2 == 0:
        totalCost += ORNAMENT_SET * quantity
        christmasSpirit += 5
    if day_number % 3 == 0:
        totalCost += TREE_SKIRT * quantity + TREE_GARLANDS * quantity
        christmasSpirit += 13
    if day_number % 5 == 0:
        totalCost += TREE_LIGHTS * quantity
        christmasSpirit += 17
        if day_number % 3 == 0:
            christmasSpirit += 30

    if day_number % 10 == 0:
        totalCost += TREE_SKIRT + TREE_LIGHTS + TREE_GARLANDS
        christmasSpirit -= 20


    if day_number % 10 == 0 and days==day_number:
        christmasSpirit -= 30


print(f"Total cost: {totalCost}")
print(f"Total spirit: {christmasSpirit}")
