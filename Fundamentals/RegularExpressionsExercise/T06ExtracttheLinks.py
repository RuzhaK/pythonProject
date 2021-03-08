import re
text=input()
while True:
    pattern=r'(www\.[a-zA-Z0-9-]+(\.[a-z-]+)+)'
    matches=re.finditer(pattern,text)
    if matches is None:
        continue
    for match in matches:
        print(match[0])
    text = input()
    if not text:
        break