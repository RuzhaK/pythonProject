n=int(input())
synonyms={}
for i in range(n):
    word=input()
    syn=input()
    if word not in synonyms:
        synonyms[word]=[]
    synonyms[word].append(syn)
for word in synonyms:
    print(f"{word} - {', '.join(synonyms[word])}")