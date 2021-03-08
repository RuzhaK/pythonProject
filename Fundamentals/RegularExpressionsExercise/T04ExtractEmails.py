import re
user_patterm=r'( |^)[a-zA-Z0-9]+((\.|\-|_)[a-zA-Z0-9]+)*'
host_patterm=r'[a-zA-Z]+(-[a-zA-Z]+)*(\.[a-zA-Z]+(-[a-zA-Z]+)*)+'
pattern=rf'{user_patterm}@{host_patterm}'
text=input()
emails=re.finditer(pattern, text)
for email in emails:
    print(email[0])
