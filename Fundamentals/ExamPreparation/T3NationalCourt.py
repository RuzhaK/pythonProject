import math

first_employee_capacity=int(input())
second_employee_capacity=int(input())
third_employee_capacity=int(input())
customers=int(input())

time_needed=0

total_efficiency_per_hour=first_employee_capacity+second_employee_capacity+third_employee_capacity
time_needed+=math.ceil(customers/total_efficiency_per_hour)
if time_needed>3:
    for i in range(3,time_needed,+3):
        time_needed+=1

print(f"Time needed: {time_needed}h.")