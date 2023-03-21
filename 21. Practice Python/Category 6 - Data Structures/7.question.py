# Iterate a given list and Check if a given element already exists in a dictionary as a key’s value if not delete it from the list

roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'John': 47, 'Emma': 69, 'Kelly': 76, 'Jason': 97}

# Error
# for i in roll_number:
#     if i not in sample_dict.values():
#         roll_number.remove(i)

# roll_number[:] = [x for x in roll_number if x in sample_dict.values()]
print(set(roll_number).intersection(set(sample_dict.values())))
