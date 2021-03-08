import re
n=int(input())
attacked=[]
destroyed=[]
for i in range(n):
    text=input()
    pattern=r's|t|a|r'
    matches=re.findall(pattern,text,re.IGNORECASE)
    deduction=(len(matches))
    decrypted=""
    for ch in text:
        ch=ord(ch)-deduction
        decrypted+=chr(ch)
    pattern_word=r"@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->\d+"
    matches=re.finditer(pattern_word,decrypted)

    for match_word in matches:
        type=match_word[3]
        if match_word[3]=="A":
            attacked.append(match_word[1])
        else:
            destroyed.append(match_word[1])

destroyed=sorted(destroyed)
attacked=sorted(attacked)
print(f"Attacked planets: {len(attacked)}")
for i in range(len(attacked)):
    print(f"-> "+"".join(attacked[i]))
print(f"Destroyed planets: {len(destroyed)}")
for i in range(len(destroyed)):
    print(f"-> "+"".join(destroyed[i]))