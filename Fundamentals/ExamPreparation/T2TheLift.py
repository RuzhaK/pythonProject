people = int(input())
lifts_line = input().split()
lifts = list(map(int, lifts_line))
sum_of_people_in_lifts = sum(lifts)
max_people = len(lifts) * 4
single_capacity=4
for i in range(len(lifts)):

    free_spaces=single_capacity-lifts[i]
    people_entering=min(people,free_spaces)
    lifts[i]+=people_entering
    people-=people_entering
    sum_of_people_in_lifts+=people_entering
    if people==0:
        break

if people>0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(' '.join(map(str,lifts)))
elif people==0 and sum_of_people_in_lifts<max_people:
    print("The lift has empty spots!")
    print(' '.join(map(str,lifts)))
elif people==0 and sum_of_people_in_lifts==max_people:
    print(' '.join(map(str,lifts)))

