# ----------------- Program Task Description
# Write a program that takes a number from the user and displays the sum of all natural number upto that number using recursion

def sum_rec(n):
    if n <= 1:
        return n
    return n + sum_rec(n - 1)


print(sum_rec(10))
