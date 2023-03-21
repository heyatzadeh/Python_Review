# Given a list, remove the element at index 4 and add it to the 2nd position and at the end of the list

list = [34, 54, 67, 89, 11, 43, 94]

temp = list.pop(4)
list.insert(-1, temp)
print(list)
