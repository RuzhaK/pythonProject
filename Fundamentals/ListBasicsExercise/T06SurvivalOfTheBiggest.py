numbers=[int(n) for n in input().split()]
n=int(input())
for i in range(n):
    minimal=min(numbers)
    numbers.remove(minimal)
print(numbers)