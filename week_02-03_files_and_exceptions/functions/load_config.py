import json

def load_config():
    with open("text_files/basic_config.json") as config:
        count = 1
        config_data = json.load(config)
        print("===========================================================")
        for key, value in config_data.items():
            print(str(count) + ". " + str(key) + " - " + str(value))
            count += 1
    print("=========================================================== \n")

