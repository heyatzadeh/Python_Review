# ----------------- Program Task Description
# Write a program that takes a number from the user and displays if that number is an armstrong number.


"""
A positive integer is called an Armstrong number of order n if
abcd... = an + bn + cn + dn + ...

In case of an Armstrong number of 3 digits, the sum of cubes of each digit is equal to the number itself. For example:

153 = 1*1*1 + 5*5*5 + 3*3*3                        ------>>>>> Armstrong Number
9474 = 9*9*9*9 + 4*4*4*4 + 7*7*7*7 + 4*4*4*4       ------>>>>> Armstrong Number
"""

number = 153
temp_number = number
calculated_number = 0
list_numbers = []
while number > 0:
    list_numbers.append(number % 10)
    number //= 10

for i in list_numbers:
    calculated_number += pow(i, len(list_numbers))

if calculated_number == temp_number:
    print("Its perfect number")
else:
    print("Its Not")
