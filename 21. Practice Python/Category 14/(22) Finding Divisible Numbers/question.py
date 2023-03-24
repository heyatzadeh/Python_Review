# ----------------- Program Task Description
# Write a program that takes a divisor, a dividend lower limit and a dividend upper limit from the user and returns the numbers divisible by the divisor in the dividend range.

divisor = 12

dividend_lower = 1
dividend_upper = 100

result = filter(lambda x: x % divisor == 0, range(dividend_lower, dividend_upper))

print(list(result))
