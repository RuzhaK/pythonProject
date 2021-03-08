line=input()
for i in range(len(line)):
    if ord(line[i])==58 and i<len(line)-1 and ord(line[i+1])!=32:
        print(f"{line[i]}{line[i+1]}")
