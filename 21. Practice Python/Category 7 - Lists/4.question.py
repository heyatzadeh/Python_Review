# Concatenate two lists in the following order


list1 = ["Hello ", "Hi "]
list2 = ["Dear", "Sir"]

['Hello Dear', 'Hello Sir', 'Hi Dear', 'Hi Sir']

result = [x + y for x, y in zip(list1, list2)] + [x + y for x, y in zip(list1, list(list2[::-1]))]
result = [x + y for x in list1 for y in list2]
print(result)
