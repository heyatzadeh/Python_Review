# Iterate a given list and count the occurrence of each element and create a dictionary to show the count of each element

sample_list = [11, 45, 8, 11, 23, 45, 23, 45, 89]

result = dict()

for i in sample_list:
    result[i] = result.get(i, 0) + 1

print(result)
