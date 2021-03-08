numbers=list(map(int,input().split(", ")))

max_element=max(numbers)
limit=10
result = []
while limit<max_element+10:

    result=[x for x in numbers if x<=limit]
    numbers=[x for x in numbers if x>limit]


    print(f"Group of {limit}'s: {result}")

    limit +=10
    result=[]
