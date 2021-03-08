import math

students=int(input())
lectures=int(input())
bonus=int(input())
max_total_bonus=0
attendances=0
for i in range(students):
    attendance=int(input())
    total_bonus = attendance/lectures*(5 + bonus)
    if total_bonus>max_total_bonus and lectures>0:
        max_total_bonus=total_bonus
        attendances=attendance
print(f"Max Bonus: {math.ceil(max_total_bonus)}.")
print(f"The student has attended {attendances} lectures.")

