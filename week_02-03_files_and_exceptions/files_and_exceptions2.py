import json

def add_config():
    config_data = load_config()
    input_check = False
    while input_check == False:
        key_input = input("Enter the name of a configuration key you wish to add: ")
        value_input = input("Enter a value for your configuration: ")
        if key_input.isalnum() and value_input.isalnum():
            input_check = True
    
    config_data[key_input.title()] = value_input
    print("\nThe configuration key you want to add is " + str(key_input.upper()) + " with a value of " + str(value_input.upper() + "."))
    save_check = False
    while save_check == False:
        save_input = input("Do you want to (s)ave or (d)iscard these changes: ")
        if save_input.upper() == "S":
            save_config(config_data)
            input_check = True
            save_check = True
        elif save_input.upper() == "D":
            print("Discarding changes...")
            input_check = True
            save_check = True
        else:
            print("Incorrect Input. Try again.")
            save_check = False

def load_config():
    try:
        with open("text_files/config_override.json") as config_override:
            config_data = json.load(config_override)
            return config_data

    except FileNotFoundError:
        with open("text_files/basic_config.json") as config:
            config_data = json.load(config)
            return config_data

def mod_config():
    config_data = load_config()
    input_check = False
    while input_check == False:
        value_input = input("Enter the name of a value you wish to modify: ")
        if value_input.upper() == "Q":
            break

        for key, value in config_data.items():
            if value_input.title() == key:
                print("\nThe current value is: " + key + " - " + str("\"" + value + "\""))
                value_modify = input("How would you like to modify " + key + ": ")
                config_data[key] = value_modify
                print("\nThe new value is: " + key + " - " + str("\"" + value_modify + "\""))
                save_check = False
                while save_check == False:
                    save_input = input("Do you want to (s)ave or (d)iscard these changes: ")
                    if save_input.upper() == "S":
                        save_config(config_data)
                        input_check = True
                        save_check = True
                    elif save_input.upper() == "D":
                        print("Discarding changes...")
                        input_check = True
                        save_check = True
                    else:
                        print("Incorrect Input. Try again.")
                        save_check = False
                        input_check = False

def save_config(config_data):
    save_config = config_data
    with open("text_files/config_override.json", "w") as overwrite_config:
        json.dump(save_config, overwrite_config)








program_run = True
while program_run == True:
    count = 1
    config_data = load_config()
    print("\nCurrent Configuration: ")
    print("===========================================================")
    for key, value in config_data.items():
        print(str(count) + ". " + str(key) + " - " + str("\"" + value + "\""))
        count += 1
    print("=========================================================== \n")
    print("Enter \"q\" to quit the program.")
    load_config()
    user_select = input("Do you want to (a)dd to or (m)odify the configuration file: ")
    if user_select.upper() == "A":
        add_config()

    elif user_select.upper() == "M":
        mod_config()

    elif user_select.upper() == "Q":
        program_run = False
    
    else:
        print("Incorrect input. Try Again!")