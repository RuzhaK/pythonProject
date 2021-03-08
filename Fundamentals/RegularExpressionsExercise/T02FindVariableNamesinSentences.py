import re
text=input()
pattern=r'\b_([a-zA-Z0-9]+)\b'
matches=re.finditer(pattern,text)
all_variable_names=[m[1]for m in matches]
print(",".join(all_variable_names))

