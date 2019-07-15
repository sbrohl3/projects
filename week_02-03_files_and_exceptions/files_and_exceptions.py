import json
from functions.load_config import load_config
from functions.add_config import add_config
from functions.mod_config import mod_config

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