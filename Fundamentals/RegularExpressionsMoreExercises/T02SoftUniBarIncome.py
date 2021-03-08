import re
text=input()
total_income=0.0
while text!="end of shift":
    pattern=r'%([A-Z][a-z]+)%([^\||\$|\%|\.])*<(\w+)>([^\||\$|\%|\.])*\|([\d]+)\|([^\||\$|\%|\.0-9])*([0-9]+(\.[0-9]+)*)\$'
    #pattern=r'%([A-Z][a-z]+)%([^\||\$|\%|\.])*<([A-Z][a-z]+)>([^\||\$|\%|\.])*\|([\d]+)\|([^\||\$|\%|\.0-9])*([0-9]+(\.[0-9]+)*)\$'
    matches=re.finditer(pattern,text)
    for match in matches:
        name=match[1]
        product=match[3]
        quantity=int(match[5])
        price=float(match[7])

        total_income+=price*quantity
        print(f"{name}: {product} - {price*quantity:.2f}")
    text = input()

print(f"Total income: {total_income:.2f}")