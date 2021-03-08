import math
import re
text=input()
calories_needed_per_day=2000
total_calories=0
pattern=r"([#|\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,5})\1"
matches=re.finditer(pattern,text)

for match in matches:

    total_calories+=int(match[4])
days=math.floor(total_calories/calories_needed_per_day)

print(f"You have food to last you for: {days} days!")

matches=re.finditer(pattern,text)
for match in matches:
    item=match[2]
    print(f"Item: {match[2]}, Best before: {match[3]}, Nutrition: {match[4]}")
