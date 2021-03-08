fire_data = input().split("#")
water_amount = int(input())
RANGE_HIGH = range(81, 126)
RANGE_MEDIUM = range(51, 81)
RANGE_LOW = range(1, 51)
effort = 0
put_out_cells = []

for fire in fire_data:
    type_of_fire, value = fire.split(" = ")
    value = int(value)

    if type_of_fire == "High" and value not in RANGE_HIGH:
        continue
    if type_of_fire == "Medium" and value not in RANGE_MEDIUM:
        continue
    if type_of_fire == "Low" and value not in RANGE_LOW:
        continue

    if water_amount >= value:
        effort += 0.25 * value
        water_amount -= value
        put_out_cells.append(value)


print("Cells:")
for cells in put_out_cells:
    print(f"- {cells}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {sum(put_out_cells)}")