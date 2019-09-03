## Importing validation as well as database connection classes
from classes.database_access import DB_Connect
from classes.validator import Validator

## Importing built-in modules
import csv
import os.path
import json
import shutil
import time

## Database connection information instatiated to a variable
db_connection = DB_Connect("it412_sbrohl2", "Pr0grammingRul3s!", "it412_sbrohl2")

class Database(Validator):
    """A class for performing database functions"""

    def __init__(self, first_name=" ", last_name=" ", company_name=" ", address=" ", city=" ", county=" ", state_code=" ", zip_code=0, phone_number=" ", phone_number_2=" ", email_address=" "):
        """A constructor for the Database Class"""
        
        self.first_name = first_name
        self.last_name = last_name
        self.crm_company_name = ""
        self.company_name = company_name
        self.address = address
        self.city = city
        self.county = county
        self.state_code = state_code
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.phone_number_2 = phone_number_2
        self.email_address = email_address

    def addRecord(self):
        """A method for adding a record to all databases"""

        ## Saving recorded entries to the CRM and Mailings Database
        print("Saving entries to the CRM and Mailings database...")
        db_connection.executeQuery("INSERT INTO dbo.CRM (f_name, l_name, company, address, city, county, state, zip, primary_phone, secondary_phone, email_address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + "', '" + self.last_name.replace("\'", "\'\'").title() + "', '" + self.crm_company_name.replace("\'", "\'\'").title() + "', '" + self.address.title() + "', '" + self.city.replace("\'", "\'\'").title() + "', '" + self.county.replace("\'", "\'\'").title() + "', '" + self.state_code.upper() + "', '" + str(self.zip_code) + "', '" + self.phone_number + "', '" + self.phone_number_2 + "' , '" + self.email_address + "'); COMMIT")
        db_connection.executeQuery("INSERT INTO dbo.Mailings (name, company, address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + " " + self.last_name.replace("\'", "\'\'").title() + "', '" + self.company_name.replace("\'", "\'\'").title() + "','" + self.address + " " + self.city.title() + " " + self.county.title() + " " + self.state_code.upper() + " " + str(self.zip_code) + "'); COMMIT")        

    def commitChanges(self):
        """A method that commits all update changes to the database"""
        
        ## User is prompted that changes are being committed
        print("Committing changes to the CRM and Mailings database...")
        db_connection.executeQuery("COMMIT;")

    def displayInput(self):
        """A method that displays compiled user input before committing to the database"""

        ## Before changes are committed the user can see all changes made
        print("\nCurrent Record:\n===============\nName: " + self.first_name.title() + " " + self.last_name.title() + "\nCompany: " + self.company_name.title() + "\nAddress: " + self.address.title() + "\nCity: " + self.city.title() + "\nState: " + self.state_code.upper() + "\nZip Code: " + str(self.zip_code) + "\nPrimary Phone: " + self.phone_number  + "\nSecondary Phone: " + self.phone_number_2 + "\nEmail: " + self.email_address)
        
    def editRecord(self, record, selected_database):
        """A method for editing a record in a chosen database"""

        ## Initiating a "False" flag to prevent errors in case the database is empty
        invalid_record = False
        ## A query selecting all records from the database table
        if selected_database == "CRM":
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database + "; ")
            ## A loop to select the row that matches the provided record 
            for row in my_query_result:
                if record == row.crm_id:
                    print("\n" + str(row.crm_id) + ". First Name: " + str(row.f_name) + " | Last Name: " + str(row.l_name) + " | Company: " + str(row.company) + " | Address: " + str(row.address) + " | City: " + str(row.city) + " | County: " + str(row.county) + " | State: " + str(row.state) + " | Zip: " + str(row.zip) + " | Primary Phone: " + str(row.primary_phone) + " | Secondary Phone: " + str(row.secondary_phone) + " | Email: " + str(row.email_address))
                    return False

                else:
                    invalid_record = True

            if invalid_record == True:
                print("\nA record matching that number does not exist. Please try again.")
                return True
            
            ## If the database is empty an error will return that the given record is invalid and to check the database
            else:
                print("\nThe record number you provided does not exist. Please check that the database is not empty and try again!")
                return True

        elif selected_database == "Mailings":
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database + "; ")
            ## A loop to select the row that matches the provided record 
            for row in my_query_result:
                if record == row.mail_id:
                    print("\n" + str(row.mail_id) + ". Name: " + str(row.name) + " | Company: " + str(row.company) + " | Address: " + str(row.address))
                    return False

                else:
                    invalid_record = True

            if invalid_record == True:
                print("\nA record matching that number does not exist. Please try again.")
                return True

            ## If the database is empty an error will return that the given record is invalid and to check the database
            else:
                print("\nThe record number you provided does not exist. Please check that the database is not empty and try again!")
                return True

    def importFile(self):
        """A method for importing in a data file"""

        ## Backing up old CSV and JSON files before beginning import operations
        if os.path.isfile("text_files/customers.csv") and os.path.isfile("text_files/customers.json"):
            print("\nCreating a backup of the existing customer .csv and .json files before overwriting")
            shutil.copy2("text_files/customers.csv", "text_files/customers.csv.backup" + str(time.time()))
            shutil.copy2("text_files/customers.json", "text_files/customers.json.backup" + str(time.time()))

        ## Importing the text file for cleaning then converting to CSV
        input_file = open("text_files/customer_export.txt", "r")
        output_file = open("text_files/customers.csv", "w")

        ## A loop to clean and write the customer_export txt file to a CSV
        for line in input_file:
            clean_text = ""
            check_line = line.replace("#", "").replace(",,","").split("|")
            for line in check_line:
                if line != check_line[10]:
                    clean_text += line + ","
                elif line == check_line[10]:
                    clean_text += line + "\n"
                    output_file.write(clean_text)

        ## Closing TXT file and CSV file after formatting
        input_file.close()
        output_file.close()

        ## Opening the cleaned CSV file for conversion to Json
        with open('text_files/customers.csv') as clean_csv:
            ## Converting CSV file to Json
            converted = csv.DictReader(clean_csv)
            rows = list(converted)

        ## Writing converted CSV to Json file
        with open('text_files/customers.json', 'w') as convert:
            json.dump(rows, convert)

        ## Deleting all data currently in database before importing new file
        db_connection.executeQuery("DELETE FROM CRM;DBCC CHECKIDENT ('CRM', RESEED, 0)  DELETE FROM Mailings; DBCC CHECKIDENT ('Mailings', RESEED, 0)  COMMIT")  

        ## Loading the newly created Json file
        with open("text_files/customers.json") as customers_json:
            customers = json.load(customers_json)

        ## A loop to add the contents of the Json file to the database         
        print("Writing imported file to database please wait...")
        for key in customers:
            db_connection.executeQuery("INSERT INTO dbo.CRM (f_name, l_name, company, address, city, county, state, zip, primary_phone, secondary_phone, email_address) VALUES ('" + key["first_name"].replace("\'", "\'\'") + "', '" + key["last_name"].replace("\'", "\'\'") + "', '" + key["company_name"].replace("\'", "\'\'") + "', '" + key["address"] + "', '" + key["city"].replace("\'", "\'\'") + "', '" + key["county"].replace("\'", "\'\'") + "', '" + key["state"] + "', '" + str(key["zip"]) + "', '" + key["phone1"] + "', '" + key["phone2"] + "' , '" + key["email"] + "'); COMMIT")
            db_connection.executeQuery("INSERT INTO dbo.Mailings (name, company, address) VALUES ('" + key["first_name"].replace("\'", "\'\'") + " " + key["last_name"].replace("\'", "\'\'") + "', '" + key["company_name"].replace("\'", "\'\'") + "','" + key["address"] + " " + key["city"] + " " + key["county"] + " " + key["state"] + " " + str(key["zip"]) + "'); COMMIT")        

        print("\nFinished writing to file. Returning to main menu...")

    def removeRecord(self, record, selected_database):
        """A method for removing a record from all databases"""
        
        ## A query selecting all of the selected database table
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database)
        for row in my_query_result:
            if record == row[0]:
                confirm_delete = True
                while confirm_delete:
                    confirmation = input("\nAre you sure you want to delete Record #" + str(record) + " from the database? Y/N: ")
                    if confirmation.lower() == "y":
                        ## Deleting the user's selection and committing the change to the database
                        db_connection.executeQuery("DELETE FROM dbo.CRM WHERE crm_id='" + str(row[0]) + "'; COMMIT")
                        db_connection.executeQuery("DELETE FROM dbo.Mailings WHERE mail_id='" + str(row[0]) + "'; COMMIT")
                        ## The user is prompted with a message confirming deletion then they are returned to the main menu
                        print("\nDeleting Record #: " + str(record) + " from the CRM and Mailings database. \n\nNow returning to the main menu...")
                        return False


                    elif confirmation.lower() == "n":
                        ## If a user enter N for no then deletion of their chosen record is aborted
                        print("\nDiscarding changes and returning to main menu...")
                        return False

                    else:
                        ## This error is thrown if a user does not enter Yes or No for their deletion selection
                        print("Please enter Y or N to confirm your selection.")
                        confirm_delete = True

            else:
                ## In case the program hits an error it will pass over the error message instead of halting the program
               pass

    def showContents(self, db_choice):
        """A method for showing all of the contents of a chosen database"""

        ## Query records from the selected database
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + db_choice)

        print("\nDisplaying contents of the " + db_choice + " database\n=============================================")
        
        ## Contents are displayed based on chosen DB
        if db_choice == "CRM":
            for row in my_query_result:     
                print(str(row.crm_id) + ". First Name: " + str(row.f_name) + " | Last Name: " + str(row.l_name) + " | Company: " + str(row.company) + " | Address: " + str(row.address) + " | City: " + str(row.city) + " | County: " + str(row.county) + " | State: " + str(row.state) + " | Zip: " + str(row.zip) + " | Primary Phone: " + str(row.primary_phone) + " | Secondary Phone: " + str(row.secondary_phone) + " | Email: " + str(row.email_address) + "\n")

        else:
            for row in my_query_result:     
                print(str(row.mail_id) + ". Name: " + str(row.name) + " | Company: " + str(row.company) + " | Address: " + str(row.address) + "\n")

    def updateContents(self, record, option, selected_database, passed_value):
        """A class for updating the contents of both databases; does not commit changes until approved by the user with the commit class"""

        ## A query to select all contents from the selected database
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database)
        
        ## If the selected databae is the CRM database, update all values to the CRM and concatenate selected values to update the Mailings DB
        if selected_database == "CRM":
            for row in my_query_result:
                if record == row.crm_id:
                    ## Update selected row with new values; Does not commit changes!
                    if option == "f_name":
                        ## Updating CRM DB
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.first_name.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                        
                        ## Updating Mailings DB
                        option = "name"
                        concat_name = self.first_name + " " + row.l_name
                        db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(concat_name.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")          
                    
                    elif option == "l_name":
                        ## Updating CRM DB
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.last_name.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                        
                        ## Updating Mailings DB
                        option = "name"
                        concat_name = row.f_name + " " + self.last_name
                        db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(concat_name.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")          
                   
                    elif option == "address":
                       ## Updating CRM DB
                       db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.address.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                       
                       ## Updating Mailings DB
                       option = "address"
                       concat_address = self.address.title() + " " + row.city + " " + row.county + " " + row.state + " " + str(row.zip)
                       db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(concat_address.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")          
                   
                    elif option == "city":
                       ## Updating CRM DB
                       db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.city.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                       
                       ## Updating Mailings DB
                       option = "address"
                       concat_address = row.address + " " + self.city.title() + " " + row.county + " " + row.state + " " + str(row.zip)
                       db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(concat_address.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")          
                   
                    elif option == "county":
                       ## Updating CRM DB
                       db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.county.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                       
                       ## Updating Mailings DB
                       option = "address"
                       concat_address = row.address + " " + row.county + " " + self.county + " " + row.state + " " + str(row.zip)
                       db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(concat_address.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")          
                   
                    elif option == "state":
                       ## Updating CRM DB
                       db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(passed_value.upper()) + "' WHERE crm_id='" + str(record) + "'")
                       
                       ## Updating Mailings DB
                       option = "address"
                       concat_address = row.address + " " + row.city + " " + row.county + " " + self.state_code.upper() + " " + str(row.zip)
                       db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(concat_address) + "' WHERE mail_id='" + str(record) + "'")          
                   
                    elif option == "zip":
                        ## Updating CRM DB
                       db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(passed_value.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                       
                       ## Updating Mailings DB
                       option = "address"
                       concat_address = row.address + " " + row.city + " " + row.county + " " + row.state + " " + str(self.zip_code)
                       db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(concat_address.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")          
                    
                    elif option.lower() == "company":                                                
                        ## Updating CRM DB
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.crm_company_name.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")

                        ## Updating Mailings DB
                        db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(passed_value.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")

                    elif option.lower() == "primary_phone":
                        ## Updating CRM DB
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(passed_value) + "' WHERE crm_id='" + str(record) + "'")

                    elif option.lower() == "secondary_phone":
                        ## Updating CRM DB
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(passed_value) + "' WHERE crm_id='" + str(record) + "'")

                    elif option.lower() == "email_address":
                        ## Updating CRM DB
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(passed_value) + "' WHERE crm_id='" + str(record) + "'")

        
        ## If the selected databae is the Mailings database concatenate selected values and update them to the DB, then add un-concatenated values to the CRM
        else:
            for row in my_query_result:
                if record == row.mail_id:
                    ## Update selected row with new values; Does not commit changes!
                    if option == "name":
                        ## Updating Mailings DB
                        db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(passed_value.replace("\'", "\'\'")) + "' WHERE mail_id='" + str(record) + "'")
                    
                        ## Updating CRM DB                    
                        option = "f_name"
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.first_name.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                        
                        ## Updating CRM DB
                        option = "l_name"
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.last_name.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")

                    elif option.lower() == "company":
                        ## Updating Mailings DB
                        db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(passed_value.replace("\'", "\'\'").title()) + "' WHERE mail_id='" + str(record) + "'")
                        
                        ## Updating CRM DB
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.crm_company_name.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")

                    elif option == "address":
                        ## Updating Mailings DB
                        db_connection.executeQuery("UPDATE dbo.Mailings SET " + option +"='" + str(passed_value.replace("\'", "\'\'")) + "' WHERE mail_id='" + str(record) + "'")
                    
                        ## Updating CRM DB
                        option = "address"
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.address.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                        
                        ## Updating CRM DB
                        option = "city"
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.city.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                        
                        ## Updating CRM DB
                        option = "county"
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.county.replace("\'", "\'\'").title()) + "' WHERE crm_id='" + str(record) + "'")
                        
                        ## Updating CRM DB
                        option = "state"
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.state_code.upper()) + "' WHERE crm_id='" + str(record) + "'")
                        
                        ## Updating CRM DB
                        option = "zip"
                        db_connection.executeQuery("UPDATE dbo.CRM SET " + option +"='" + str(self.zip_code) + "' WHERE crm_id='" + str(record) + "'")
                        
