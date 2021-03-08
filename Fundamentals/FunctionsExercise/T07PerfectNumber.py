number=int(input())

def is_perfect_number(n):
    sum = 0
    for i in range (1,n):
        if n%i==0:
            sum+=i
    if sum==n:
        return True

if is_perfect_number(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")