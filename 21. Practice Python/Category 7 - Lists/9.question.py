# find value 20 in the list, and if it is present, replace it with 200. Only update the first occurrence of a value

list = [5, 20, 10, 15, 20, 25, 50, 20]

for index, item in enumerate(list):
    if item == 20:
        list.pop(index)
        list.insert(index, 200)
        break
print(list)
