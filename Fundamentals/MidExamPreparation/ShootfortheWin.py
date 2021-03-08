targets = [int(x) for x in input().split()]
line = input()
count = 0
while line != "End":
    index = int(line)
    if 0 <= index < len(targets):
        if targets[index] > -1:
            value = targets[index]
            for i in range(len(targets)):
                if targets[i] > value:
                    targets[i] -= value
                elif targets[i]==-1:
                    continue
                elif targets[i] <= value:
                    targets[i] += value

            targets[index] = -1
            count += 1

    line = input()
print(f"Shot targets: {count} -> {' '.join(map(str,targets))}")
