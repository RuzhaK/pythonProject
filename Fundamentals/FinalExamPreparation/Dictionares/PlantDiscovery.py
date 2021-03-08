n = int(input())
plants = {}
for _ in range(n):
    plant, rarity = input().split("<->")
    plants[plant] = {'rarity': int(rarity), 'ratings': []}
data = input()
while not data == "Exhibition":
    command, value = data.split(': ')
    try:
        if command == 'Rate':
            plant, rating = value.split(" - ")
            plants[plant]['ratings'].append(int(rating))
        elif command == "Update":
            plant, rarity = value.split(" - ")
            plants[plant]['rarity'] = int(rarity)
        elif command == "Reset":
            plant = value
            plants[plant]['ratings'].clear()
    except:
        print("error")

    data = input()
for plant, plant_data in plants.items():
    if plants[plant]['ratings']:
        plants[plant]['avg'] = sum(plants[plant]['ratings']) / len(plants[plant]['ratings'])
    else:
        plants[plant]['avg'] = 0
sorted_plants = sorted(plants.items(), key=lambda x: (x[1]['rarity'], x[1]['avg']), reverse=True)
print("Plants for the exhibition:")
for plant, value in sorted_plants:
    print(f"- {plant}; Rarity: {value['rarity']}; Rating: {value['avg']:.2f}")

# todo try except example, sorting po dva elementa, sazdavane na novo property na dictionary za sortirovka, reverse=True
