n=int(input())
total_price=0
for i in range(n):
    price=float(input())
    days=int(input())
    count=int(input())
    order_price=days*count*price
    total_price+=order_price
    print(f"The price for the coffee is: ${order_price:.2f}")
print(f"Total: ${total_price:.2f}")