import json
import shutil
import os.path

def add_config():
    """Allows the user to add in additional config options overriding the basic config
    Arguments:
    save_input [user input] -- Save, or discard additions to the current configuration
    Returns:
    New configuration output to main program
    """
    config_data = load_config()

    key_input = False
    while not key_input:
        key_input = input("Enter the name of a configuration key you wish to add or \"q\" to quit without saving: ")
        save_check = False
        value_input = False
        if key_input.upper() == "Q":
            value_input = True
            key_input = True
            save_check = True

    while not value_input:
        value_input = input("Enter a value for your configuration or \"q\" to quit without saving: ")
        save_check = False
        if value_input.upper() == "Q":
            value_input = True
            save_check = True

 
    while save_check == False:
        config_data[key_input.title()] = value_input
        print("\nThe configuration key you want to add is " + str(key_input.upper()) + " with a value of " + str(value_input.upper() + "."))
        
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

def add_config_alternative():
    """Adds in additional configuration options overriding the basic config
    Arguments:
    save_input [user input] -- Save, or discard additions to the current configuration
    Returns:
    New configuration output to main program
    """
    ## Loading in the config_data pulled from either basic_config or override config
    config_data = load_config()
    ## Adding required configuration options into the override config file
    config_data["Allow File Uploads"] = "Yes"
    config_data["Use Caching"] = "Yes"
    config_data["Cache File"] = "cache/filecache.cache"
    config_data["Mail Host"] = "mail.apphost.com"

    ## Loop to save changes to config file or discard them
    save_check = False
    while save_check == False:
        
        ## Displaying Temporary config before saving
        print("\nTemporary Configuration: ")      
        
        count = 1
        print("===========================================================")
        for key, value in config_data.items():
            print(str(count) + ". " + str(key) + " - " + str("\"" + value + "\""))
            count += 1
        print("=========================================================== \n")
        
        ## Prompting the user with an option save additions to the config or discard them
        save_input = input("Do you want to (s)ave or (d)iscard these changes: ")
        if save_input.upper() == "S":
            ## Saved changes are passed over to the save_config function for saving
            save_config(config_data)
            input_check = True
            save_check = True

        elif save_input.upper() == "D":
            ## Discarding changes returns a user to the main menu
            print("Discarding changes...")
            input_check = True
            save_check = True

        else:
            ## Entering incorrect input re-prompts users to save or discard changes
            print("Incorrect Input. Try again.")
            save_check = False
    

## A function to load the override_configuration file if found or basic_config if not
def load_config():
    """Loads in either the basic or override configuration file
    Arguments:
    If override config exists use it, else use basic_config
    Returns:
    config_data to the main program
    """
    try:
        with open("text_files/config_override.json") as config_override:
            config_data = json.load(config_override)
            return config_data

    except FileNotFoundError:
        with open("text_files/basic_config.json") as config:
            config_data = json.load(config)
            return config_data

## A function to load the basic_config file for value comparisons
def load_original_config():
    """Loads in the basic config file for comparison purposes
    Arguments:
    If key in override config matches a key in basic config it cannot be deleted
    Returns:
    original_config to mod_config
    """
    with open("text_files/basic_config.json") as orig_config:
        original_config = json.load(orig_config)
        return (original_config)


def mod_config():
    """Allows the use to modify config values
    Arguments:
    value_input [user input] - User enters a key to modify
    value_modify [user input] - User enters a value to modiy
    save_input [user input] - User can save, discard, or delete selected entries
    Returns:
    config_data to the main program
    """
    ## Loading in configuration data from either basic_config or override_config
    config_data = load_config()
    
    ## A loop to modify values in the configuration file
    input_check = False
    while input_check == False:
        print("\nEnter \"q\" to exit modifying the configuration")
        ## Prompting user for a Key to modify
        value_input = input("Enter the name of a value you wish to modify: ")
        if value_input.upper() == "Q":
            break

        ## Looping through the values from the configuration file
        for key, value in list(config_data.items()):
            
            ## If the user's input matches a key in the configuration they will be asked to enter a new value
            if value_input.title() == key: 
                print("\nThe current value is: " + key + " - " + str("\"" + value + "\""))
                value_modify = False
                while not value_modify:
                    value_modify = input("Enter a new value for " + key + " or press enter to leave entry as-is: ")
                    
                    ## The user's input is combined with their supplied key to change a configuration value
                    if value_modify:
                        config_data[key] = value_modify
                        input_check = True
                        save_check = False


                    else:
                        ## If the user leaves the new value option blank the previous value will be used in-place
                        print("The original value has not been changed.")
                        value_modify = value
                        config_data[key] = value_modify
                        save_check = False
                        input_check = True
                        break
                    

                while save_check == False:
                    ## The user is shown their new value after entry
                    print("\nThe new value is: " + key + " - " + str("\"" + str(value_modify) + "\""))
                    
                    ## The user is asked if they want to save, discard or delete their entry to the configuration
                    save_input = input("\nDo you want to (s)ave or (d)iscard these changes or to delete this value entirely enter (x): ")
            
                    ## If a user enters "S" their changes are saved to the override config file
                    if save_input.upper() == "S":
                        ## The user's new config_data is passed into the save_config function to write to file
                        save_config(config_data)
                        input_check = True
                        save_check = True

                    ## If a user discards changes they will be returned to the program's main menu
                    elif save_input.upper() == "D":
                        print("Discarding changes...")
                        input_check = True
                        save_check = True
                
                    ## If a user enters "X" the key and value being modifed will be deleted from the override config file
                    elif save_input.upper() == "X":
                        confirm_del = False
                        while confirm_del == False:
                            confirm = input("\nAre you sure you want to delete " + str(key) + ": Y/N ")
                            if confirm.upper() == "Y":
                                ## The basic config file is loaded for comparison
                                original_config = load_original_config()

                                ## If the key being deleted matches one in the basic_config file the user recieves an error
                                if key in original_config.keys():
                                    print("\nYou cannot delete original configuration entries!")
                                    confirm_del = True
                                    ## The user is re-prompted on whether they wish to now discard or save their changes
                                    save_check = False
                                
                                ## If the key being deleted doesn't match a key in basic_config it will be deleted
                                elif key not in original_config.keys():
                                    del config_data[key]
                                    confirm_del = True
                                    save_check = True
                                    input_check = True
                                    ## After the key is deleted the updated config is saved using the save_config function
                                    save_config(config_data)

                            ## If a user enters "N" they are re-mprompted to confirm their choice
                            elif confirm.upper() == "N":
                                confirm_del = True
                                save_check = False
                                input_check = True
                            
                            ## If bad input is supplied the user is re-prompted to choose the appropriate response
                            else:
                                confirm_del = False

                    ## If bad input is detected the user is re-prompted to try again.
                    else:
                        print("Incorrect Input. Try again.")
                        save_check = False
                        input_check = False



## This function saves the current configuration to the override config file
def save_config(config_data):
    """Allows the user to save configuration data
    Arguments:
    If config_override already exists a backup is created
    Returns:
    nothing
    """
    save_config = config_data
    with open("text_files/config_override.json", "w") as overwrite_config:
        json.dump(save_config, overwrite_config)
        
    ## This statement creates a backup of the current config    
    if os.path.isfile("text_files/config_override.json"):
        shutil.copy2("text_files/config_override.json", "text_files/config_override.json.backup")

