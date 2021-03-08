import re
line=input()

pattern_emojis=r"(\*{2}|:{2})([A-Z][a-z]{2,})\1"
pattern_digits="\d"
matches_emojis=re.finditer(pattern_emojis,line)
matches=re.findall(pattern_digits,line)
threshold = 1
for m in matches:
    threshold*=int(m)


all_emojis=[m for m in matches_emojis]
print(f"Cool threshold: {threshold}")
print(f"{len(all_emojis)} emojis found in the text. The cool ones are:")

for emoji in all_emojis:
    sum=0
    a=emoji[2]
    for i in range(len(emoji[2])):
        if emoji[2][i].isalpha():
            sum+=ord(emoji[2][i])
    if sum>threshold:
        print(emoji[0])
