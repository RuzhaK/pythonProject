import re
n=int(input())
for i in range(n):
    sequence=input()

    pattern=r"(@)(#{1,})[A-Z][A-Za-z\d]{4,}[A-Z]\1(#{1,})"
    matches=re.fullmatch(pattern,sequence)
    if matches is None:

        print("Invalid barcode")
    else:
        has_product_group=False
        product_group = "00"
        sum=""
        barcode=matches[0]
        for i in range(len(barcode)):
            if barcode[i].isdigit():
                has_product_group=True
                sum+=barcode[i]
        if has_product_group:
            print(f"Product group: {sum}")
        else:
            print(f"Product group: {product_group}")