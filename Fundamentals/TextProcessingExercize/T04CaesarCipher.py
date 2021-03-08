line=input()
new_line=""
for ch in line:
    if ch.isdigit():
        ch=int(ch)+3
        ch=str(ch)
    else:
        ch=ord(ch)+3
        ch=chr(ch)
    new_line+=ch
print(new_line)