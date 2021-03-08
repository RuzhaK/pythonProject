n=int(input())
word=input()
elements=[]
filtered=[]
for i in range(n):
    element=input()
    elements.append(element)
print(elements)
for i in range(n):
    if word in elements[i]:
        filtered.append(elements[i])
print(filtered)


