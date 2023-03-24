# ----------------- Program Task Description
# Write a program that takes a number input from the user and returns the factors of that number.

given_number = 99
print(list(filter(lambda x: given_number % x == 0, range(1, given_number))))
