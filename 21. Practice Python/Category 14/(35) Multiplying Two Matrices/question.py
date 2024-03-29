# ----------------- Program Task Description
# Write a program that multiplies two matrices in two different ways.
# 1- Nested Loop
# 2- Using Nested List Comprehension


x = [[9, 5, 2],
     [4, 8, 6],
     [7, 3, 1]]

y = [[1, 9, 1, 11],
     [2, 6, 5, 7],
     [3, 4, 1, 5]]

result = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

for row in range(len(x)):
    for col in range(len(y[0])):
        result[row][col] = x[row][col] * y[row][col]

print(result)
