import json

def load_config():
    try:
        with open("text_files/config_override.json") as config_override:
            config_data = json.load(config_override)
            return config_data

    except FileNotFoundError:
        with open("text_files/basic_config.json") as config:
            config_data = json.load(config)
            return config_data
