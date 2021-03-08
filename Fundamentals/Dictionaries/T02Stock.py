line=input().split()
products={}
for i in range(0,len(line),2):
    key=line[i]
    value=int(line[i+1])
    products[key]=value
searching_for=input().split()
for  product in searching_for:
    if product in products:
        print(f"We have {products[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

