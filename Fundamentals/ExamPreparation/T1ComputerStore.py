line=input()
price_without_tax=0

while not (line=="regular" or  line=="special"):
    price=float(line)
    if price<0:
        print("Invalid price!")
        line = input()
        continue

    price_without_tax+=price


    line = input()
taxes=price_without_tax*0.2
total_price=price_without_tax*1.2
if line=="special":
    total_price=total_price*0.9
if total_price==0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer!")
    print(f"Price without taxes: {price_without_tax:.2f}$")
    print(f"Taxes: {taxes:.2f}$")
    print(f"-----------")
    print(f"Total price: {total_price:.2f}$")

