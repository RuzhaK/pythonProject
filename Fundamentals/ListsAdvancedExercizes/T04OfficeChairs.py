n=int(input())
room=0
free_chairs=0
enough_chairs=True
for i in range(n):
    room+=1
    data=input().split()
    chairs=len(data[0])
    people=int(data[1])
    if chairs<people:
        print(f"{people-chairs} more chairs needed in room {room}")
        enough_chairs=False
    else:
        free_chairs+=chairs-people
if enough_chairs:
    print(f"Game On, {free_chairs} free chairs left")
