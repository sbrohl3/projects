## Final Project
## IT412
## 08/18/2019
## BROHL, STEVEN

from classes.database import Database

## Instantiating the database class to a variable for later use
database = Database()

## Setting my program to run as True 
program_run = True

## A loop to run the enirety of my program
while program_run == True:
    ## Printing an option menu to screen
    print("\nPlease select an option below to continue: ")
    print("==============================================")
    print("\t1. Import a new data file \n\t2. Show data currently in a database \n\t3. Add a record to the databases \n\t4. Edit a record \n\t5. Exit program\n")
    ## User input to choose an option
    selection = input("Enter the corresponding number next to the option you wish to select: ")

    ## An option to import a new data file 
    if selection == '1':
        None ## Temporary placeholder to keep program from breaking during initial testing


    ## An option to show the current data in a chosen database
    elif selection == '2':
    
        show_data = True
        while show_data:
            choice = input("\nEnter the number next to the corresponding database you would like to display the cotents of: \n============================================================================================ \n\n\t - 1. CRM \n\t - 2. Mailings \n\nChoice: ") 
            if choice == "1":
                db_choice = "CRM"
                database.showContents(db_choice)
                show_data = False

            elif choice == "2":
                db_choice = "Mailings"
                database.showContents(db_choice)
                show_data = False

            elif choice.lower() == "q":
                print("Returning to the main menu...")
                show_data = False

            else:
                print("You have entered an invalid choice. Please choose from one of the options above, or enter \"q\" to return to the main menu.")

    ## An option to add a record to a database
    elif selection == '3':

        first_name_check = False
        while not first_name_check: 
            ## Validating and adding a new first name
            database.first_name = input("Please enter a first name: ")
            option = "first name"
            first_name_check = database.validate_NamePart(option, database.first_name)
            
        last_name_check = False
        while not last_name_check: 
            ## Validating and adding a new last name
            database.last_name = input("Please enter a last name: ")
            option = "last name"
            last_name_check = database.validate_NamePart(option, database.last_name)
       
        address_check = False
        while not address_check: 
            ## Validating and adding a new address
            database.address = input("Please enter an address: ")
            address_check = database.validate_address()

        city_check = False
        while not city_check: 
            ## Validating and adding a new city
            database.city = input("Please enter a city: ")
            option = "city"
            city_check = database.validate_cityInfo(option, database.city)

        county_check = False
        while not county_check: 
            ## Validating and adding a new county
            database.county = input("Please enter a county: ")
            county_check = database.validate_cityInfo(option, database.county)

        state_check = False
        while not state_check: 
            ## Validating and adding a new state
            database.state_code = input("Please enter an abbreviated state code (example: MI): ")
            state_check = database.validate_State()

        zip_code_check = False
        while not zip_code_check: 
            ## Validating and adding a new zip code
            database.zip_code = input("Please enter a 4 or 5 digit Zip Code: ")
            zip_code_check = database.validate_zipCode()

        company_name_check = False
        while not company_name_check: 
            ## Validating and adding a new zip code
            database.company_name = input("Please enter a company name: ")
            ## ADD LOGIC TO VALIDATOR SO # CAN BE BLANK!
            company_name_check = database.validate_companyName()

        primary_phone_check = False
        while not primary_phone_check: 
            ## Validating and adding a new zip code
            database.phone_number = input("Please enter a phone number: ")
            option = "primary"
            primary_phone_check = database.validate_phoneNumber(option, database.phone_number)

        secondary_phone_check = False
        while not secondary_phone_check: 
            ## Validating and adding a new zip code
            database.phone_number_2 = input("Please enter a secondary phone number: ")
            option = "secondary"
            secondary_phone_check = database.validate_phoneNumber(option, database.phone_number_2)

        email_check = False
        while not email_check: 
            ## Validating and adding a new zip code
            database.email_address = input("Please enter an email address: ")
            email_check = database.validate_emailAddress()

        ## Displaying the users current changes to screen    
        database.displayInput()
        ## Prompting the user if they wish to save their changes
        save_add = False
        while not save_add:
            save_add = input("\nDo you wish to save your addition to the database? Y/N: ")
            if save_add.lower() == "y":
                database.addRecord()
                save_add = True
            
            elif save_add.lower() == "n":
                print("Discarding changes and returning to main menu...")
                save_add = True

            else:
                print("You have entered an invalid response. Please answer (Y)es or (N)o.")
                save_add = False

    ## An option to edit or delete a record in a chosen database
    elif selection == '4':

        choose_database = True
        while choose_database:
            choice = input("\nEnter the number next to the corresponding database you would like to make edits to: \n============================================================================================ \n\n\t - 1. CRM \n\t - 2. Mailings \n\nChoice: ") 
            if choice == "1":
                db_choice = "CRM"
                database.showContents(db_choice)
                choose_database = False
                editing = True

            elif choice == "2":
                db_choice = "Mailings"
                database.showContents(db_choice)
                choose_database = False
                editing = True
                

            elif choice.lower() == "q":
                print("Returning to the main menu...")
                choose_database = False

            else:
                print("You have entered an invalid choice. Please choose from one of the options above, or enter \"q\" to return to the main menu.")


        while editing:
            record = input("\nPlease enter the record number you wish to edit: ")
            if record.lower() == "q":
                print("Returning to the main menu...")
                editing = False
            
            else:
                try:
                    record = int(record)

                except ValueError:
                    print("\nYou have entered an invalid record. Please choose a record from the " + selected_database + " database, or enter \"q\" to return to the main menu.")
            
                else:
                    selected_database = db_choice
                    database.editRecord(record, selected_database)

    ## An option to end the program
    elif selection == '5':
        print("Terminating Program...")
        program_run = False
    
    ## An error in case a user enters an invalid option in the main menu
    else:
        print("You have chosen an invalid option or entered an incorrect value. Please try again.")
        program_run = True
