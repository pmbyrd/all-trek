import json

# read the formatted_file.json
with open('data/animal.json') as json_file:
    data = json.load(json_file)

print(data[90]["name"])





