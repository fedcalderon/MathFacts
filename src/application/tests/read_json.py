import json

with open("users.json", "registration") as rf:
    decoded_data = json.load(rf)

print(decoded_data)
# Check is the json object was loaded correctly
try:
    print(decoded_data["name"])
except KeyError:
    print("JSON Data not loaded correctly.")

{'name': 'Micah', 'type': 'website', 'language': 'Python'}