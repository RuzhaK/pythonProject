def reverse(string):
    return string[::-1]
    #todo tova e obryshtane na string. Syshto moje:
    #return ''.join(reversed(string))
    #ili
    # s = ""
    #for char in reversed(string)
         # s+=char
         #return s
words=[]
while True:
    command=input()
    if command=="end":
        break
    words.append(command)
for word in words:
    print(f"{word} = {reverse(word)}")


