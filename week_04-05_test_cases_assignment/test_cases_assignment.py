## Test Cases Assignment
## IT412
## 07/25/2019
## BROHL, STEVEN

## Importing Modules
from classes.phonebook import Phonebook

program_run = True

while program_run == True:
    ## A variable to call the Phonebook class
    phone_book = Phonebook()

    ## This loop only allows for a valid first name (only letters) to be input by a user
    first_name_check = False
    while first_name_check == False: 
        phone_book.first_name = input("What is your First Name: ")
        first_name_check = phone_book.validateNamePart(phone_book.first_name)

    ## This loop only allows for a valid last name (only letters) to be input by a user
    last_name_check = False
    while last_name_check == False: 
        phone_book.last_name = input("What is your Last Name: ")
        last_name_check = phone_book.validateNamePart(phone_book.last_name)

    ## This loop only allows for a valid phone number (only digits; length equal to 10) to be input by a user
    phone_number_check = False
    while phone_number_check == False: 
        phone_book.phone_number = input("What is your Phone Number: ")
        phone_number_check = phone_book.validatePhoneNumber()

    ## This loop only allows a valid phone number type (home, office, cell) to be input by a user
    phone_number_type_check = False
    while phone_number_type_check == False: 
        phone_book.phone_number_type = input("What is your Phone Number Type: \"home\", \"office\", \"cell\": ")
        phone_number_type_check = phone_book.validatePhoneNumberType()

    ## Append contact info to a list
    phone_book.format_data()
    

    exit_program_check = False
    while exit_program_check == False:
        exit_program = input("Do you want to add more contacts Y/N: ")
        if exit_program.lower() == "y":
            program_run = True
            exit_program_check = True

        elif exit_program.lower() == "n":
            program_run = False
            exit_program_check = True

        else:
            print("Incorrect Input. Please Try again.")
            exit_program_check = False

## Prints contact info appended to the list
print(phone_book.contact_list)