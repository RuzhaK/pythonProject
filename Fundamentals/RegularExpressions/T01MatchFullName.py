import re
names=input()
pattern=r'\b([A-Z][a-z]+ [A-Z][a-z]+)\b'
matches:list=re.findall(pattern,names)
print(' '.join(matches))