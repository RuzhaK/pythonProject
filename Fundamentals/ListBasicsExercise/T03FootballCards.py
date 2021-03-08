line=input().split(" ")
team_A={1,2,3,4,5,6,7,8,9,10,11}
team_B={1,2,3,4,5,6,7,8,9,10,11}
# todo boolean
is_more_than_seven=True
#A-1 A-5 A-10 B-2
for el in line:
    team,player=el.split("-")
    player = int(player)
    if team=="A" and player in team_A:
            team_A.remove(player)
    if team=="B" and player in team_B:
            team_B.remove(player)
    if len(team_A)<7 or len(team_B)<7:
        is_more_than_seven=False
        break

print(f"Team A - {len(team_A)}; Team B - {len(team_B)}")

if not is_more_than_seven:
    print(f"Game was terminated")

