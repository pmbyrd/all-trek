import json

with("config.json") as config_file:
    config = json.load(config_file)
