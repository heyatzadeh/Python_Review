# ----------------- Program Task Description
# Write a program that takes the number of terms to be displayed in the fibonacci sequence from the user and returns the modified sequence using recursion

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


for i in range(20):
    print(fibonacci(i))
