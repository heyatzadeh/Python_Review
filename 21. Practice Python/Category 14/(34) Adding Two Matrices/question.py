# ----------------- Program Task Description
# Write a program that adds two matrices in two different ways.
# 1- Nested Loop
# 2- Using Nested List Comprehension

# 3x3 matrix
x = [[1, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# 3x3 matrix
y = [[1, 9, 1],
     [6, 7, 3],
     [4, 5, 9]]

result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for row in range(len(x)):
    for col in range(len(x[0])):
        result[row][col] = x[row][col] + y[row][col]
print(result)

matrix_sum = [[x[row][col] + y[row][col] for col in range(len(x))] for row in range(len(x[0]))]

print(matrix_sum)
