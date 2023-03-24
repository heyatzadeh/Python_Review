# ----------------- Program Task Description
# Write a program that takes the number of terms in the fibonacci sequence from the user and displays the sequence.

def fibonacci(n):
    result = [1, 1]
    for i in range(0, n - 2):
        result.append(result[len(result) - 1] + result[len(result) - 2])
    return result


def fibonacci_rec(n):
    if n <= 2:
        return 1
    return fibonacci_rec(n - 1) + fibonacci_rec(n - 2)


# {1, 1, 2, 3, 5, 8}
print(fibonacci(6))
