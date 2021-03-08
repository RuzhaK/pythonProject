line = input()
products = {}

while line != "buy":
    data = line.split()
    product = data[0]
    price = float(data[1])
    quantity = float(data[2])
    if product not in products:
        products[product] = {'quantity': 0, 'price': 0, 'total_price':0}
    products[product]['quantity'] += quantity
    products[product]['price'] = price
    products[product]['total_price'] = price*products[product]['quantity']

    line = input()
for product, parameters in products.items():
    print(f"{product} -> {parameters['total_price']:.2f}")

