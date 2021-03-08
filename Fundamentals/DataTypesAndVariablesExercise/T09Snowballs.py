snowballs=int(input())

highest_value=None
highest_snow=None
highest_time=None
highest_quality=-99999999999999999999999999999999999999999999999999999999999999999999999999999999999999999

for i in range(1,snowballs+1):
    snow = int(input())
    time = int(input())
    quality = int(input())

    value=(snow / time) **quality
    if value>highest_value:
        highest_value=value
        highest_time=time
        highest_snow=snow
        highest_quality=quality

print(f"{highest_snow} : {highest_time} = {highest_value:.0f} ({highest_quality})")


