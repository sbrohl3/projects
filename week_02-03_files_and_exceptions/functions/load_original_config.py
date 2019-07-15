import json

def load_original_config():
    with open("text_files/basic_config.json") as orig_config:
        original_config = json.load(orig_config)
        return (original_config)
