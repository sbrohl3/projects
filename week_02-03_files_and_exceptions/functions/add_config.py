from functions.load_config import load_config
from functions.save_config import save_config

def add_config():
    config_data = load_config()
    input_check = False
    while input_check == False:
        try:
            key_input = input("Enter the name of a configuration key you wish to add: ")
            value_input = input("Enter a value for your configuration: ")
            input_check = True
            
        except:
            print("Your key and value inputs are invalid!")
            input_check = False
        
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