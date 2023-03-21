# Given two list of equal size create a Python set such that it shows the element from both lists in the pair

list_one = [2, 3, 4, 5, 6, 7, 8]
list_two = [4, 9, 16, 25, 36, 49, 64]

result = set()

for i in range(len(list_one)):
    result.add((list_one[i], list_two[i]))

print(result)
