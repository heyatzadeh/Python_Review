# remove all occurrence of 20 from the list

list = [5, 20, 15, 20, 25, 50, 20]

list = [x for x in list if x != 20]

print(list)
