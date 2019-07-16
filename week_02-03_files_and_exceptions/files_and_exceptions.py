
from functions.functions import *


## A loop to run the main program
program_run = True
while program_run == True:
    
    count = 1
    ## Current configuration data is loaded
    config_data = load_config()

    ## Current configuration data is printed to screen
    print("\nCurrent Configuration: ")
    print("===========================================================")
    for key, value in config_data.items():
        print(str(count) + ". " + str(key) + " - " + str("\"" + value + "\""))
        count += 1
    print("=========================================================== \n")
    print("Enter \"q\" to quit the program.")
    
    ## The user is prompted with a choice to add to the current config or modify current values
    user_select = input("Do you want to (a)dd to or (m)odify the configuration file: ")
    
    ## If the user enters "A" then the add_config function will be called for them to add configuration data
    if user_select.upper() == "A":
        add_config()

    ## If the user enters "M" then the mod_config function will be called for them to add configuration data
    elif user_select.upper() == "M":
        mod_config()

    ## If the user enters "Q" then the program will quit
    elif user_select.upper() == "Q":
        program_run = False
    
    ## If the user enters invalid input they will be prompted to try again.
    else:
        print("\n Incorrect input. Try Again!")