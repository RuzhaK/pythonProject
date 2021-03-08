n=int(input())
cars={}
for i in range(n):
    car,mileage, fuel = input().split("|")
    cars[car]={"mileage":int(mileage),"fuel":int(fuel)}

line=input()
while line!="Stop":
    command, car, *tokens=line.split(" : ")
    if command=="Drive":
        distance=int(tokens[0])
        fuel=int(tokens[1])
        if cars[car]["fuel"]<fuel:
            print("Not enough fuel to make that ride")
        else:
            cars[car]["fuel"] -=fuel
            cars[car]["mileage"]+=distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if cars[car]["mileage"]>=100000:
                cars.pop(car)
                print(f"Time to sell the {car}!")
    elif command=="Refuel":
        fuel = int(tokens[0])
        max=75
        to_fill=min(fuel,max-cars[car]["fuel"])
        cars[car]["fuel"] += to_fill
        print(f"{car} refueled with {to_fill} liters")

    elif command=="Revert":
        kilometers = int(tokens[0])
        cars[car]["mileage"] -= kilometers
        if cars[car]["mileage"]<10000:
            cars[car]["mileage"] =10000
        else:

            print(f"{car} mileage decreased by {kilometers} kilometers")
    line=input()
sorted_cars=sorted(cars.items(),key=lambda x:(-x[1]["mileage"],x[0]))
for k,v in sorted_cars:
    print(f"{k} -> Mileage: {v['mileage']} kms, Fuel in the tank: {v['fuel']} lt.")