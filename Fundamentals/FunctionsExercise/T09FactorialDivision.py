n = int(input())
m = int(input())


def calc_factorial(n):
    result = 1
    for num in range(1, n + 1):
        result *= num
    return result


factorial_n = calc_factorial(n)
factorial_m = calc_factorial(m)
print(f"{factorial_n / factorial_m:.2f}")
