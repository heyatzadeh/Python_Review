# Convert the following Vehicle Object into JSON

import json


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

    # def to_json(self):
    #     return json.dumps(dict({"name": self.name, "engine": self.engine, "price": self.price}))


class VehicleEncoder(json.JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)
print(json.dumps(vehicle, indent=4, cls=VehicleEncoder))
