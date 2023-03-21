# Swap the following two tuples

tuple_one = (11, 22)
tuple_two = (99, 88)

temp = tuple_two
tuple_two = tuple_one
tuple_one = temp

# OR
# tuple_one, tuple_two = tuple_two, tuple_one

print(tuple_one, tuple_two)
