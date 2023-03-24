# ----------------- Program Task Description
# Write a program that transposes a matrix in two different ways.
# 1- Nested Loop
# 2- Using Nested List Comprehension

# 3x2 matrix
matrix = [[1, 7],
          [4, 5],
          [7, 8]]

result = [[0, 0, 0],
          [0, 0, 0]]

for j in range(len(matrix)):
    for i in range(len(matrix[0])):
        result[i][j] = matrix[j][i]

transpose = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

print(result)
