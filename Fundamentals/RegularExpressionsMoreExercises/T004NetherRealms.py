import re

line=[x.strip()for x in input().split(",")]
line=sorted(line)
for i in range(len(line)):
    text=line[i]
    pattern_health=r"[^\d\.\*\/\-\+]"
    health=0
    damage=0

    matches=re.findall(pattern_health,text)
    for match in matches:
        health+=ord(match)
    pattern_damage=r"([+-]*\d+(\.\d+)*)"
    matches_d=re.findall(pattern_damage,text)
    for match_d in matches_d:
        damage+=float(match_d[0])
    pattern_operations=r"[\*\/]"
    matches_op=re.findall(pattern_operations,text)
    for match_op in matches_op:
        if match_op=="*":
            damage*=2
        else:
            damage/=2
    print(f"{text} - {health} health, {damage:.2f} damage")





