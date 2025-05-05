import json

# Writing to a JSON file
data = {
    'name': 'prince',
    'age': 20,
    'city': 'Surat'
}

with open('output.json', mode='w') as file:
    json.dump(data, file, indent=4)
