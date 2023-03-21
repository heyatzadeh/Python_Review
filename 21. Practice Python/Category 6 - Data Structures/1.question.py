# Given two lists create a third list by picking odd-index elements from the first list and even-index elements from the second.

list_one = [3, 6, 9, 12, 15, 18, 21]
list_two = [4, 8, 12, 16, 20, 24, 28]

result = [x for x in list_one if x % 2 != 0] + [x for x in list_two if x & 2 == 0]

print(result)
