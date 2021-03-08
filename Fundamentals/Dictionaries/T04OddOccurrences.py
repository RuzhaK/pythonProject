line=input().split()

occurrences={}

for item in line:
    item_lower_case=item.lower()
    if item_lower_case not in occurrences:
        occurrences[item_lower_case]=0
    occurrences[item_lower_case]+=1
for key,times in occurrences.items():
    if times%2!=0:
        print(key,end=" ")
