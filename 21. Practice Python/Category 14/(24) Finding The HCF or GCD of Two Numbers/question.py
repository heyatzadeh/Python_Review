# ----------------- Program Task Description
# Write a program that takes two numbers from the user and returns the highest common factor (H.C.F) or greatest common divisor (G.C.D) of the numbers.


# The highest common factor (H.C.F) or greatest common divisor (G.C.D) of two numbers is the largest positive integer that perfectly divides the two given numbers. For example, the H.C.F of 12 and 14 is 2.

first = 9
second = 6

result = 1
for i in range(1, max(first, second)):
    if first % i == 0 and second % i == 0:
        result = i

result = filter(lambda x: first % x == 0 and second % x == 0, range(1, max(first, second)))

print(max(list(result)))
