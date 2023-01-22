import json

with open('config.json', 'r') as f:
    config = json.load(f)
api_key = config['api_key']

