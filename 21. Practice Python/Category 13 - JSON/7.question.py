# Parse the following JSON to get all the values of a key ‘name’ within an array
import json

example = \
    """
      [
        {
            "id": 1,
            "name": "name1",
            "color": [
                "red",
                "green"
            ]
        },
        {
            "id": 2,
            "name": "name2",
            "color": [
                "pink",
                "yellow"
            ]
        }
    ]
    """

result = json.loads(example)
print([x.get("name") for x in result])
