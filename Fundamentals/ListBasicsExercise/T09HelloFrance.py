initial_data=input().split("|")
budget=float(input())
#RANGE_CLOTHES=range(0,51,0.01)
#RANGE_SHOES=range(0,36)
#RANGE_ACCESSORIES=range(0,20.51)
profit=0;
new_prices=[]

for data in initial_data:
    price_difference=0
    product, price=data.split("->")
    price=float(price)
    if product=="Clothes" and price>50:
        continue
    elif product == "Shoes" and price > 35:
        continue
    elif product == "Accessories" and price > 20.51:
        continue
    if budget>=price:
        budget-=price
        price_difference =1.4*price-price
        price=1.4*price
        new_prices.append(price)
        profit+=price_difference


budget+=sum(new_prices)
# for prices in new_prices:
#     budget+=prices
for prices in new_prices:
    print(f"{prices:.2f} ",end="")
print()
print(f"Profit: {profit:.2f}")
if budget>=150:
    print("Hello, France!")
else:
    print("Time to go.")



