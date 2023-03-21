# Initialize dictionary with default values

employees = ['Kelly', 'Emma', 'John']
defaults = {"designation": 'Application Developer', "salary": 8000}

result = dict()

for person in employees:
    result[person] = defaults

print(result)
