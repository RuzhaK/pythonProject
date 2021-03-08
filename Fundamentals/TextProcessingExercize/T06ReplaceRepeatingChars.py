line = input()
for i in range(len(line)):
    ch = line[i]

    if i + 1 == len(line):
        print(ch, end="")
        break
    if ch != line[i + 1]:
        print(ch, end="")
