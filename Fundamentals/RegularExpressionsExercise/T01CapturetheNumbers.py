import re
pattern="\d+"

while True:
    text = input()
    if not text:
        break

    matches=re.findall(pattern,text)
    for match in matches:
        print(match,end=" ")
