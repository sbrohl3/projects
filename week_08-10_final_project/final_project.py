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
        
        select = True
        while select:
            print("\nWARNING: You are about to overwrite the existing contents of both the CRM and Mailings database!")
            choice = input("\nAre you sure you wish to import a new data file (Y)es or (N)o: ")
            if choice.lower() == "y":
                database.importFile()
                select = False

            elif choice.lower() == "n":
                print("\nAborting action and returning to the main menu...")
                select = False

            else:
                print("\nInvalid entry. Please enter (Y)es or (N)o to continue.")
                select = True

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
                print("\nReturning to the main menu...")
                show_data = False

            else:
                print("\nYou have entered an invalid choice. Please choose from one of the options above, or enter \"q\" to return to the main menu.")

    ## An option to add a record to a database
    elif selection == '3':

        first_name_check = False
        while not first_name_check: 
            ## Validating and adding a new first name
            database.first_name = input("\nPlease enter a first name: ")
            option = "first name"
            first_name_check = database.validate_NamePart(option, database.first_name)
            
        last_name_check = False
        while not last_name_check: 
            ## Validating and adding a new last name
            database.last_name = input("\nPlease enter a last name: ")
            option = "last name"
            last_name_check = database.validate_NamePart(option, database.last_name)

        company_name_check = False
        while not company_name_check: 
            ## Validating and adding a new company name
            database.company_name = input("\nPlease enter a company name or enter \"N/A\" if no company name: ").rstrip()
            company_name_check = database.validate_companyName()
       
        address_check = False
        while not address_check: 
            ## Validating and adding a new address
            database.address = input("\nPlease enter an address: ")
            address_check = database.validate_address()

        city_check = False
        while not city_check: 
            ## Validating and adding a new city
            database.city = input("\nPlease enter a city: ")
            option = "city"
            city_check = database.validate_cityInfo(option, database.city)

        county_check = False
        while not county_check: 
            ## Validating and adding a new county
            database.county = input("\nPlease enter a county: ")
            option = "county"
            county_check = database.validate_cityInfo(option, database.county)

        state_check = False
        while not state_check: 
            ## Validating and adding a new state
            database.state_code = input("\nPlease enter an abbreviated state code (example: MI): ")
            state_check = database.validate_State()

        zip_code_check = False
        while not zip_code_check: 
            ## Validating and adding a new zip code
            database.zip_code = input("\nPlease enter a 4 or 5 digit Zip Code: ")
            zip_code_check = database.validate_zipCode()

        primary_phone_check = False
        while not primary_phone_check: 
            ## Validating and adding a new phone number
            database.phone_number = input("\nPlease enter a phone number: ")
            option = "primary"
            primary_phone_check = database.validate_phoneNumber(option, database.phone_number)

        secondary_phone_check = False
        while not secondary_phone_check: 
            ## Validating and adding a new secondary phone number
            database.phone_number_2 = input("\nPlease enter a secondary phone number: ")
            option = "secondary"
            secondary_phone_check = database.validate_phoneNumber(option, database.phone_number_2)

        email_check = False
        while not email_check: 
            ## Validating and adding a new email address
            database.email_address = input("\nPlease enter an email address: ")
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
                choose_record = True

            elif choice == "2":
                db_choice = "Mailings"
                database.showContents(db_choice)
                choose_database = False
                choose_record = True
                
            elif choice.lower() == "q":
                print("\nReturning to the main menu...")
                choose_database = False
                choose_record = False

            else:
                print("You have entered an invalid choice. Please choose from one of the options above, or enter \"q\" to return to the main menu.")


            while choose_record:
                record = input("\nPlease enter the record number you wish to edit, or enter \"q\" to return to the main menu: ")
                
                if record.lower() == "q":
                    print("\nReturning to the main menu...")
                    choose_record = False
                    edit_choice = False
                    delete_record = False
                
                else:
                    try:
                        record = int(record)

                    except ValueError:
                        print("\nYou have entered an invalid value. Please choose a record from the " + db_choice + " database, or enter \"q\" to return to the main menu.")
                        edit_choice = False

                    else:
                        selected_database = db_choice
                        print("\nSelected Record to Edit\n=======================")
                        choose_record = database.editRecord(record, selected_database)
                        edit_choice = True

                while edit_choice:
                    choice = input("\nDo you want to (E)dit or (D)elete this record: ")
                    if choice.upper() == "E":
                        edit_choice = False
                        editing = True
                        delete_record = False

                    elif choice.upper() == "D":
                        edit_choice = False
                        editing = False
                        delete_record = True

                    elif choice.upper() == "Q":
                        print("\nReturning to the main menu...")
                        edit_choice = False
                        editing = False
                        delete_record = False

                    else:
                        print("\nInvalid selection. Please enter \"E\" to Edit, \"D\" to Delete, or \"Q\" to return to the main menu.")

                    while delete_record:
                        ## Display current library list
                        print("\nSelected Record to Delete\n=========================")
                        database.editRecord(record, selected_database)
                        ## A prompt to delete a selected book in the library
                        delete_record = database.removeRecord(record, selected_database)
                        
                    while editing:
                        if db_choice == "CRM":
                            field_choice = input("\nWhat field would you like to edit (Example: First Name): ")

                            if field_choice.lower() == "first name":
                                first_name_check = False
                                while not first_name_check: 
                                    ## Validating and adding a new first name
                                    database.first_name = input("\nPlease enter a first name: ")
                                    option = "first name"
                                    making_changes = True
                                    field_option = "f_name"
                                    database.updateContents(record, field_option, db_choice, database.first_name)
                                    first_name_check = database.validate_NamePart(option, database.first_name)
                                 
                            elif field_choice.lower() == "last name":    
                                last_name_check = False
                                while not last_name_check: 
                                    ## Validating and adding a new last name
                                    database.last_name = input("\nPlease enter a last name: ")
                                    option = "last name"
                                    making_changes = True
                                    field_option = "l_name"
                                    database.updateContents(record, field_option, db_choice, database.first_name)
                                    last_name_check = database.validate_NamePart(option, database.last_name)
                                    
                            elif field_choice.lower() == "company":
                                company_name_check = False
                                while not company_name_check: 
                                    ## Validating and adding a new company name
                                    database.company_name = input("\nPlease enter a company name or enter \"N/A\" if no company name: ")
                                    making_changes = True
                                    field_option = "company"
                                    database.updateContents(record, field_option, db_choice, database.crm_company_name)
                                    company_name_check = database.validate_companyName()
                  
                            elif field_choice.lower() == "address":
                                address_check = False
                                while not address_check: 
                                    ## Validating and adding a new address
                                    database.address = input("\nPlease enter an address: ")
                                    making_changes = True
                                    field_option = "address"
                                    database.updateContents(record, field_option, db_choice, database.address)
                                    address_check = database.validate_address()
                                
                            elif field_choice.lower() == "city":
                                city_check = False
                                while not city_check: 
                                    ## Validating and adding a new city
                                    database.city = input("\nPlease enter a city: ")
                                    option = "city"
                                    making_changes = True
                                    field_option = "city"
                                    database.updateContents(record, field_option, db_choice, database.city)
                                    city_check = database.validate_cityInfo(option, database.city)
                                    
                            elif field_choice.lower() == "county":
                                county_check = False
                                while not county_check: 
                                    ## Validating and adding a new county
                                    database.county = input("\nPlease enter a county: ")
                                    making_changes = True
                                    field_option = "county"
                                    database.updateContents(record, field_option, db_choice, database.county)
                                    county_check = database.validate_cityInfo(option, database.county)

                            elif field_choice.lower() == "state":
                                state_check = False
                                while not state_check: 
                                    ## Validating and adding a new state
                                    database.state_code = input("\nPlease enter an abbreviated state code (example: MI): ")
                                    making_changes = True
                                    field_option = "state"
                                    database.updateContents(record, field_option, db_choice, database.state_code)
                                    state_check = database.validate_State()

                            elif field_choice.lower() == "zip":
                                zip_code_check = False
                                while not zip_code_check: 
                                    ## Validating and adding a new zip code
                                    database.zip_code = input("\nPlease enter a 4 or 5 digit Zip Code: ")
                                    making_changes = True
                                    field_option = "zip"
                                    database.updateContents(record, field_option, db_choice, database.zip)
                                    zip_code_check = database.validate_zipCode()

                            elif field_choice.lower() == "primary phone":
                                primary_phone_check = False
                                while not primary_phone_check: 
                                    ## Validating and adding a new phone number
                                    database.phone_number = input("\nPlease enter a phone number: ")
                                    option = "primary"
                                    making_changes = True
                                    field_option = "primary_phone"
                                    database.updateContents(record, field_option, db_choice, database.phone_number)
                                    primary_phone_check = database.validate_phoneNumber(option, database.phone_number)
                            
                            elif field_choice.lower() == "secondary phone":
                                secondary_phone_check = False
                                while not secondary_phone_check: 
                                    ## Validating and adding a new secondary phone number
                                    database.phone_number_2 = input("\nPlease enter a secondary phone number: ")
                                    option = "secondary"
                                    making_changes = True
                                    field_option = "secondary_phone"
                                    database.updateContents(record, field_option, db_choice, database.phone_number_2)
                                    secondary_phone_check = database.validate_phoneNumber(option, database.phone_number_2)

                            elif field_choice.lower() == "email":
                                email_check = False
                                while not email_check: 
                                    ## Validating and adding a new email address
                                    database.email_address = input("\nPlease enter an email address: ")
                                    making_changes = True
                                    field_option = "email_address"
                                    database.updateContents(record, field_option, db_choice, database.email_address)
                                    email_check = database.validate_emailAddress()

                            else:
                                print("You have entered an incorrect value. Please try again.")
                                            
                        elif db_choice == "Mailings":
                            field_choice = input("\nWhat field would you like to edit (Example: Name): ")

                            if field_choice.lower() == "name":
                                first_name_check = False
                                while not first_name_check: 
                                    ## Validating and adding a new first name
                                    database.first_name = input("\nPlease enter a first name: ")
                                    option = "first name"
                                    first_name_check = database.validate_NamePart(option, database.first_name)
                                    
                                last_name_check = False
                                while not last_name_check: 
                                    ## Validating and adding a new last name
                                    database.last_name = input("\nPlease enter a last name: ")
                                    option = "last name"
                                    last_name_check = database.validate_NamePart(option, database.last_name)

                                field_option = "name"
                                making_changes = True
                                concat_name = database.first_name + " " + database.last_name
                                database.updateContents(record, field_option, db_choice, concat_name)
                            
                            elif field_choice.lower() == "company":
                                company_name_check = False
                                while not company_name_check: 
                                    ## Validating and adding a new company name
                                    database.company_name = input("\nPlease enter a company name or enter \"N/A\" if no company name: ")
                                    making_changes = True
                                    company_name_check = database.validate_companyName()
                                    field_option = "company"
                                    database.updateContents(record, field_option, db_choice, database.company_name)
                        
                            elif field_choice.lower() == "address":
                                address_check = False
                                while not address_check: 
                                    ## Validating and adding a new address
                                    database.address = input("\nPlease enter an address: ")
                                    making_changes = True
                                    address_check = database.validate_address()

                                city_check = False
                                while not city_check: 
                                    ## Validating and adding a new city
                                    database.city = input("\nPlease enter a city: ")
                                    option = "city"
                                    making_changes = True
                                    city_check = database.validate_cityInfo(option, database.city)

                                county_check = False
                                while not county_check: 
                                    ## Validating and adding a new county
                                    database.county = input("\nPlease enter a county: ")
                                    making_changes = True
                                    county_check = database.validate_cityInfo(option, database.county)

                                state_check = False
                                while not state_check: 
                                    ## Validating and adding a new state
                                    database.state_code = input("\nPlease enter an abbreviated state code (example: MI): ")
                                    making_changes = True
                                    state_check = database.validate_State()

                                zip_code_check = False
                                while not zip_code_check: 
                                    ## Validating and adding a new zip code
                                    database.zip_code = input("\nPlease enter a 4 or 5 digit Zip Code: ")
                                    making_changes = True
                                    zip_code_check = database.validate_zipCode()

                                field_option = "address"
                                making_changes = True
                                concat_address = database.address + " " + database.city + " " + database.county + " " + database.state_code + " " + database.zip_code
                                database.updateContents(record, field_option, db_choice, concat_address)

                            else:
                                print("You have entered an incorrect value. Please try again.")
                                making_changes = False
                    

                                    
                        while making_changes == True:
                            continue_prompt = input("\nDo you wish to continue making changes to this book: Y/N ")
                            
                            if continue_prompt.lower() == "y":
                                editing = False
                                making_changes = False

                            elif continue_prompt.lower() == "n":
                                making_changes = False
                                editing = True
                                ## A prompt asking the user if they wish to save their updated edits to the database
                                save_add = False   
                                
                                ## Prompting the user if they wish to save their changes
                                while not save_add:
                                    save_add = input("\nDo you wish to update your changes to the " + selected_database + " database? Y/N: ")
                                    if save_add.lower() == "y":
                                        database.commitChanges()
                                        save_add = True
                                        editing = False
                                    
                                    elif save_add.lower() == "n":
                                        print("\nDiscarding changes and returning to main menu...")
                                        save_add = True
                                        editing = False

                                    else:
                                        print("\nYou have entered an invalid response. Please answer (Y)es or (N)o.")
                                        save_add = False
                                        editing = False

                    
    ## An option to end the program
    elif selection == '5':
        print("\nTerminating Program...")
        program_run = False
    
    ## An error in case a user enters an invalid option in the main menu
    else:
        print("\nYou have chosen an invalid option or entered an incorrect value. Please try again.")
        program_run = True
