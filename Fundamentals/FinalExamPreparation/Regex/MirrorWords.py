text=input()
import re
pattern=r"(@|#)([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
mirror_words= []
matches=re.findall(pattern,text)
for match in matches:
    reversed_word=match[2][::-1]
    word=match[1]
    if match[1]==reversed_word:
        mirror_words.append(match[1]+" <=> "+ match[2])

if len(matches)==0:
    print(f"No word pairs found!")
else:
    print(f"{len(matches)} word pairs found!")


if len(mirror_words)==0:
    print(f"No mirror words!")
else:
    print("The mirror words are:")
    print(", ".join(mirror_words))




