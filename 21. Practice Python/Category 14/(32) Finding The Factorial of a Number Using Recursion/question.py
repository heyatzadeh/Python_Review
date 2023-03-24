# ----------------- Program Task Description
# Write a program that takes a number from the user and displays the factorial of that number using recursion

def factorial(n):
    if n <= 1:
        return n
    return n * factorial(n - 1)


print(factorial(3))
