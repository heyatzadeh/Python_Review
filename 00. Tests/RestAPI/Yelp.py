import requests
import config

client_id = "zpxAkVdfLeZCxfWu5jQhZw"

header = {
    "Authorization": f"Bearer {config.yelp_api_key}",
    "accept": "application/json"
}

param = {
    "limit": 10,
    "location": "New_York",
    "term": "game"
}

response = requests.get("https://api.yelp.com/v3/businesses/search", headers=header, params=param)

businesses = response.json()["businesses"]

names = [business["name"] for business in businesses if business["rating"] > 4]

print(names)
