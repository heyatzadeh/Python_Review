# ----------------- Program Task Description
# Write a program that inputs a number and displays the successive powers of 2 upto that number

number = int(input("enter a number: "))

result = map(lambda x: pow(2, x), range(number))
print(list(result))
