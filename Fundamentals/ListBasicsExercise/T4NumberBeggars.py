numbers = [int(n) for n in input().split(", ")]
beggars = int(input())
start = 0
taken = []
for i in range(1, beggars + 1):
    sum_per_beggar = 0

    for k in range(start, len(numbers), beggars):

        sum_per_beggar += numbers[k]
       
    taken.append(sum_per_beggar)

    start += 1
print(taken)
