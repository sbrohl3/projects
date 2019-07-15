from functions.load_original_config import load_original_config
from functions.load_config import load_config
from functions.save_config import save_config


config_data = load_config()


for key, value in list(config_data.items()):
    if key.title() == key:
        
        print("\nThe current value is: " + key + " - " + str("\"" + value + "\""))
        print("Enter \"x\" to delete a value.")
        value_modify = input("How would you like to modify " + key + ": ")
        config_data[key] = value_modify
        if value_modify.upper() == "X":
            original_config = load_original_config()

            if key in original_config.keys():
                print("Cannot delete original values!")
                
            elif key != original_config.keys():

                try:
                    del config_data[key]

                except KeyError:
                    pass
                
                else:
                    save_check = False
                    input_check = True
                    save_config(config_data)

            elif confirm.upper() == "N":
                input_check = True
                save_check = False

        else:
            save_check = False

