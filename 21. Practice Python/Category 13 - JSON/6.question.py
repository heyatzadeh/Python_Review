# Convert the following JSON into Vehicle Object
import json

example = {"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}


class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price


def vehicle_decoder(obj: json) -> Vehicle:
    return Vehicle(obj["name"], obj["engine"], obj["price"])


vehicle = json.loads('{"name": "Toyota Rav4", "engine": "2.5L", "price": 32000}', object_hook=vehicle_decoder)
print(vehicle.name, vehicle.engine, vehicle.price)
