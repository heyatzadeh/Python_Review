# Sort JSON keys in and write them into a file
import json

sample_json = {"id": 1, "name": "value2", "age": 29}

with open("sample_json.json", "w") as file:
    json.dump(sample_json, file, sort_keys=True, indent=4)
