# Delete set of keys from a dictionary

sampleDict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"

}
keysToRemove = ["name", "salary"]

# for i in keysToRemove:
#     if i in sampleDict.keys():
#         sampleDict.pop(i)
print({x: sampleDict.pop(x) for x in keysToRemove})
print(sampleDict)
