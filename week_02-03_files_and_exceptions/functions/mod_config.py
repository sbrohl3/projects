from functions.load_config import load_config
from functions.save_config import save_config
from functions.load_original_config import load_original_config

def mod_config():
    config_data = load_config()
    input_check = False
    save_check = True
    while input_check == False:
        print("Enter \"q\" to exit modifying the configuration")
        value_input = input("Enter the name of a value you wish to modify: ")
        if value_input.upper() == "Q":
            break

        for key, value in list(config_data.items()):
            if value_input.title() == key:
                
                print("\nThe current value is: " + key + " - " + str("\"" + value + "\""))
                modify = input("Enter .")
                value_modify = input("What would you like to change " + key + " to: ")
                config_data[key] = value_modify
                if value_modify.upper() == "X":
                    confirm_del = False
                    while confirm_del == False:
                        confirm = input("Are you sure you want to delete " + str(key) + ": Y/N ")
                        if confirm.upper() == "Y":
                            original_config = load_original_config()

                            if key in original_config.keys():
                                print("You cannot delete original configuration entries!")
                            
                            elif key not in original_config.keys():
                                del config_data[key]
                                confirm_del = True
                                save_check = True
                                input_check = True
                                save_config(config_data)

                        elif confirm.upper() == "N":
                            confirm_del = True
                            save_check = False
                            input_check = True

                    else:
                        confirm_del = False

                while save_check == False:
                    print("\nThe new value is: " + key + " - " + str("\"" + value_modify + "\""))
                    
                    save_input = input("Do you want to (s)ave or (d)iscard these changes or to delete this value entirely enter (x): ")
                    
                    if save_input.upper() == "S":
                        save_config(config_data)
                        input_check = True
                        save_check = True

                    elif save_input.upper() == "D":
                        print("Discarding changes...")
                        input_check = True
                        save_check = True
                

                    elif save_input.upper() == "X":
                        confirm = input("Are you sure you want to delete " + str(key) + ": Y/N ")
                        if confirm.upper() == "Y":
                            confirm_del = False
                    while confirm_del == False:
                        confirm = input("Are you sure you want to delete " + str(key) + ": Y/N ")
                        if confirm.upper() == "Y":
                            original_config = load_original_config()

                            if key in original_config.keys():
                                print("You cannot delete original configuration entries!")
                            
                            elif key not in original_config.keys():
                                del config_data[key]
                                confirm_del = True
                                save_check = True
                                input_check = True
                                save_config(config_data)

                        elif confirm.upper() == "N":
                            confirm_del = True
                            save_check = False
                            input_check = True

                        else:
                            confirm_del = False


                    else:
                        print("Incorrect Input. Try again.")
                        save_check = False
                        input_check = False