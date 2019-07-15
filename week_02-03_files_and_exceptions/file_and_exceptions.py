## Week 2 and 3: Files and Exceptions Assignment
## 07/012/2019
## Brohl, Steven

## Importing json
import json


## Opening the basic_config json file and printing it's contents
with open("text_files/basic_config.json") as config:
    count = 1
    config_data = json.load(config)
    print("===========================================================")
    for key, value in config_data.items():
        print(str(count) + ". " + str(key) + " - " + str(value))
        count += 1
print("=========================================================== \n")


program_run = True
while program_run == True:
    modify_input = input("Would you like to modify any of the values above: Y/N ")
    if modify_input.capitalize() == "Y":
        value_check = True
        while value_check == True:
            value_input = input("Please enter the value you wish you modify: ")
            for key, value in config_data.items():
                if value_input.title() == key:
                    print("\nThe current value is: " + key + " - " + value )
                    value_modify = input("How would you like to modify " + key + ": ")
                    print("\n The new value is: " + key + " - " + value )
                    value_check = False

    elif modify_input.capitalize() == "N":
        program_run = False

    else:
        print("You have entered the wrong value, please enter (Y) or (N).")
        program_run = True
