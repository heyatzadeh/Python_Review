# Given two sets, Checks if One Set is a subset or superset of another Set. if the subset is found delete all elements from that set

first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}

if first_set.issubset(second_set):
    second_set -= first_set
elif first_set.issuperset(second_set):
    pass

print(first_set, second_set, sep="\n")