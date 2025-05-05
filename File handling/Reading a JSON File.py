import json

# Reading a JSON file
with open('data.json', mode='r') as file:
    data = json.load(file)
    print(data)
