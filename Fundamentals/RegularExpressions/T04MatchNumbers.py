import re
text=input()
pattern=r'((^|(?<=\s))(-*)(\d+)((\.\d+)*)($|(?=\s)))'
matches=re.findall(pattern,text)

for match in matches:
    number,*others=match
    print(number,end=' ')