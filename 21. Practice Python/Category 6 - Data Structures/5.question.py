# Given the following two sets find the intersection and remove those elements from the first set

set1 = {65, 42, 78, 83, 23, 57, 29}
set2 = {67, 73, 43, 48, 83, 57, 29}

intersection = set()
for i in set1:
    if i in set2:
        intersection.add(i)

print(set1 - intersection)

# OR
print(set1.difference(set2))
