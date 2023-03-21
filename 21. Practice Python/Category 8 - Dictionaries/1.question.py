# Convert the below lists into a dictionary

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = {x: y for x in keys for y in values}
print(result)
