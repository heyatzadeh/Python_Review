# ----------------- Program Task Description
# Write a program that takes a number from the user and returns the factorials of that number.

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


def factorial_rec(n):
    if n <= 1:
        return 1
    return n * factorial_rec(n - 1)


print(factorial_rec(12))
print(factorial_rec(3))
print(factorial_rec(4))
print(factorial_rec(5))
