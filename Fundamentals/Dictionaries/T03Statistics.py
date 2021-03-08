line=input()
products={}
while line!="statistics":
    product=line.split(": ")
    key = product[0]
    value = product[1]
    if key not in products:
        products[key]=0
    products[key]+=int(value)

    line = input()
print("Products in stock:")
for product,quantities in products.items():

    print(f"- {product}: {quantities}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")