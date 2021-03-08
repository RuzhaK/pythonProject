data=input()
companies={}
while data!="End":
    line=data.split(" -> ")
    company_name=line[0]
    employee=line[1]
    if company_name not in companies:
        companies[company_name]=[]
    if employee not in companies[company_name]:
        companies[company_name].append(employee)
    data = input()
for key, value in sorted(companies.items()):
    print(f"{key}")
    for x in value:
        print(f"-- {x}")
