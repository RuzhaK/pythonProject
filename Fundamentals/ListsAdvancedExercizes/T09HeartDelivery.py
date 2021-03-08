neighbourhood_as_string=input().split("@")
neighbourhood = list(map(int,neighbourhood_as_string))
command=input()
last_position=0

while not command=="Love!":
    jump_length=int(command.split()[1])
    starting_index=0
    house_index= last_position+ jump_length

    if house_index>=len(neighbourhood):
        house_index=0
    last_position = house_index
    if 0<=house_index<=len(neighbourhood):
        if neighbourhood[house_index]>2:
            neighbourhood[house_index]-=2
        elif neighbourhood[house_index]==2:
            neighbourhood[house_index]-=2

            print(f"Place {house_index} has Valentine's day.")
        else:
            neighbourhood[house_index] =0
            print(f"Place {house_index} already had Valentine's day.")




    command = input()

print(f"Cupid's last position was {last_position}.")
houses_failed=0
for house in neighbourhood:
    if house>0:
        houses_failed+=1

if houses_failed==0:
    print(f"Mission was successful.")
else:
    print(f"Cupid has failed {houses_failed} places.")


