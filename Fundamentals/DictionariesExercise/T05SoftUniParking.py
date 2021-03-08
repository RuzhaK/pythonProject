n=int(input())
parking={}
for i in range(n):
    data=input().split()
    command=data[0]
    name=data[1]
    if command=="register":
        car=data[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {car}")
            continue
        parking[name]=car
        print(f"{name} registered {car} successfully")

    if command=="unregister":
        if name not in parking:
            print(f"ERROR: user {name} not found")
            continue
        parking.pop(name)
        print(f"{name} unregistered successfully")


for key,value in parking.items():
    print(f"{key} => {value}")

