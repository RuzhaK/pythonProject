companions = int(input())
days = int(input())
total_coins = 0
for day_number in range(1, days + 1):
    if day_number % 10 == 0:
        companions -= 2
    if day_number % 15== 0:
        companions += 5
    total_coins += ( 50 - 2 * companions)
    if day_number % 3 == 0:
        total_coins -= companions * 3
    if day_number % 5 == 0:
        total_coins += companions * 20
        if day_number % 3 == 0:
            total_coins -= companions * 2

print(f"{companions} companions received {int(total_coins / companions)} coins each.")
