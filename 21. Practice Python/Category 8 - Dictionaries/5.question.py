# Create a new dictionary by extracting the following keys from a below dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}

# Keys to extract

keys = ["name", "salary"]

result = dict()
for i in sampleDict.keys():
    if i in keys:
        result[i] = sampleDict[i]

print(result)