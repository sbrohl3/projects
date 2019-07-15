import json

def save_config(config_data):
    save_config = config_data
    with open("text_files/config_override.json", "w") as overwrite_config:
        json.dump(save_config, overwrite_config)

