capacity_A=int(input())
capacity_B=int(input())
capacity_C=int(input())
students=int(input())
total_capacity_per_hour=capacity_C+capacity_B+capacity_A
count =0
while students>0:
    count += 1
    if count%4==0:
        continue
    students-=total_capacity_per_hour

print(f"Time needed: {count}h.")

