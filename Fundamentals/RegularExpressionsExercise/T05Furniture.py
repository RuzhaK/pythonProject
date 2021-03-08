import re
text=input()

pattern=r'>>([a-zA-Z]+)<<(\d+(\.\d+)*)!([0-9]+)'
print("Bought furniture:")
total_money=0
while text!="Purchase":
    matches=re.fullmatch(pattern,text)
    if matches is None:
        text=input()
        continue
    print(matches[1])
    price=float(matches[2])
    quantity=int(matches[4])
    total_money+=quantity*price

    text = input()
print(f"Total money spend: {total_money:.2f}")