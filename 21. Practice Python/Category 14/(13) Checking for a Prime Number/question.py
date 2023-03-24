# ----------------- Program Task Description
# Write a program that takes a number as an input from the user and displays to the user if the entered number is a prime number.

def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            print(f"not {n}")
            return False
    print(f"is {n}")
    return True


def is_prime_rec(n, div=2):
    if n < 2:
        return False
    if n == 2 or n == 3:
        return True
    elif div >= n:
        return True
    elif n % div == 0:
        return False

    else:
        return is_prime_rec(n, div + 1)


print(is_prime_rec(14))
print(is_prime_rec(13))
print(is_prime_rec(15))
print(is_prime_rec(12))
