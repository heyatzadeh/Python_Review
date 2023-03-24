# ----------------- Program Task Description
# Write a program that takes two numbers from the user and returns least common multiple (L.C.M.) of two numbers.


# The least common multiple (L.C.M.) of two numbers is the smallest positive integer that is perfectly divisible by the two given numbers.

# For example, the L.C.M. of 12 and 14 is 84.

first = 12
second = 14

hcf = max(filter(lambda x: first % x == 0 and second % x == 0, range(1, max(first, second))))
lcm = first * second // hcf
print(lcm)
