# Access the value of key2 from the following JSON

import json

sample_json = """{"key1": "value1", "key2": "value2"}"""

print(json.loads(sample_json)["key2"])
