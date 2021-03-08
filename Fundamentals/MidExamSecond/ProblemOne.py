cost = float(input())
months = int(input())
budget = 0
for i in range(months):

    if (i + 1) % 2 != 0 and i + 1 > 1:
        budget -= 0.16 * budget
    elif (i + 1) % 4 == 0:
        budget = budget * 1.25

    budget += 0.25 * cost
if cost <= budget:
    print(f"Bravo! You can go to Disneyland and you will have {budget - cost:.2f}lv. for souvenirs.")
else:
    print(f"Sorry. You need {cost - budget:.2f}lv. more.")
