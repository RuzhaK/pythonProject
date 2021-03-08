water_tank_capacity=255
n=int(input())
current_litres=0
for i in range(n):
    litres=int(input())
    if litres>water_tank_capacity-current_litres:
        print("Insufficient capacity!")
    else:
        current_litres+=litres
print(current_litres)