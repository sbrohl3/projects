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

        print("Saving entries to the CRM database...")
        db_connection.executeQuery("INSERT INTO dbo.CRM (f_name, l_name, company, address, city, county, state, zip, primary_phone, secondary_phone, email_address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + "', '" + self.last_name.replace("\'", "\'\'").title() + "', '" + self.crm_company_name.replace("\'", "\'\'") + "', '" + self.address + "', '" + self.city.replace("\'", "\'\'") + "', '" + self.county.replace("\'", "\'\'") + "', '" + self.state_code.upper() + "', '" + str(self.zip_code) + "', '" + self.phone_number + "', '" + self.phone_number_2 + "' , '" + self.email_address + "'); COMMIT")
        
        print("\nSaving entries to the Mailings database...")
        db_connection.executeQuery("INSERT INTO dbo.Mailings (name, company, address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + " " + self.last_name.replace("\'", "\'\'").title() + "', '" + self.company_name.replace("\'", "\'\'") + "','" + self.address + " " + self.city + " " + self.county + " " + self.state_code + " " + str(self.zip_code) + "'); COMMIT")        

    def displayInput(self):
        """A class that displays compiled user input before committing to the database"""

        ## Before changes are committed the user can see all changes made
        print("\nCurrent Record:\n===============\nName: " + self.first_name.title() + self.last_name.title(), + "\nCompany Name: " + self.company_name.title() +"\nAddress: " + self.address.title(), "\nCity: " + self.city + "\nState: " + self.state_code.upper() + "\nZip Code: " + self.zip_code + "\nPrimary Phone: " + self.phone_number  + "\nSecondary Phone: " + self.phone_number_2 + "\nEmail Address: " + self.email_address)
        
    def editRecord(self, record, selected_database):
        """A method for editing a record in a chosen database"""

        ## A query selecting all records from the database table
        if selected_database == "CRM":
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database + "; ")
            for row in my_query_result:
                if record == row.crm_id:
                    print("\n" + str(row.crm_id) + ". First Name: " + str(row.f_name) + " | Last Name: " + str(row.l_name) + " | Address: " + str(row.address) + " | City: " + str(row.city) + " | County: " + str(row.county) + " | State: " + str(row.state) + " | Zip Code: " + str(row.zip) + " | Company Name: " + str(row.company) + " | Primary Phone#: " + str(row.primary_phone) + " | Secondary Phone#: " + str(row.secondary_phone) + " | Email Address: " + str(row.email_address))
                    return False

                else:
                    invalid_record = True

            if invalid_record == True:
                print("\nA record matching that number does not exist. Please try again.")
                return True


        elif selected_database == "Mailings":
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database + "; ")
            for row in my_query_result:
                if record == row.mail_id:
                    print("\n" + str(row.mail_id) + ". Name: " + str(row.name) + " | Company name: " + str(row.company) + " | Address: " + str(row.address))
                    return False

                else:
                    invalid_record = True

            if invalid_record == True:
                print("\nA record matching that number does not exist. Please try again.")
                return True


    def importFile(self):
        """A method for importing in a data file"""

        ## Backing up old CSV file before beginning import operations
        if os.path.isfile("text_files/customers.csv"):
            shutil.copy2("text_files/customers.csv", "text_files/customers.csv.backup" + str(time.time()))
        
        ## Backing up old JSON file before beginning import operations
        if os.path.isfile("text_files/customers.json"):
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
            convert = csv.DictReader(clean_csv)
            rows = list(convert)

        ## Writing converted CSV to Json file
        with open('text_files/customers.json', 'w') as convert:
            json.dump(rows, convert)

        ## Deleting all data currently in database before importing new file
        db_connection.executeQuery("DELETE FROM CRM; DELETE FROM Mailings; COMMIT")  

        ## Addings contents to the database
        with open("text_files/customers.json") as customers_json:
            customers = json.load(customers_json)
                
        print("Writing imported file to database please wait...")
        for key in customers:
            self.first_name = str(key["first_name"])
            self.last_name = str(key["last_name"])
            self.crm_company_name = str(key["company_name"])
            self.company_name = str(key["company_name"])
            self.address = str(key["address"])
            self.city = str(key["city"])
            self.county = str(key["county"])
            self.state_code = str(key["state"])
            self.zip_code = str(key["zip"])
            self.phone_number = str(key["phone1"])
            self.phone_number_2 = str(key["phone2"])
            self.email_address = str(key["email"])
            db_connection.executeQuery("INSERT INTO dbo.CRM (f_name, l_name, company, address, city, county, state, zip, primary_phone, secondary_phone, email_address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + "', '" + self.last_name.replace("\'", "\'\'").title() + "', '" + str(self.crm_company_name.replace("\'", "\'\'")) + "', '" + self.address + "', '" + self.city.replace("\'", "\'\'") + "', '" + self.county.replace("\'", "\'\'") + "', '" + self.state_code.upper() + "', '" + str(self.zip_code) + "', '" + self.phone_number + "', '" + str(self.phone_number_2) + "' , '" + self.email_address + "'); COMMIT")
            db_connection.executeQuery("INSERT INTO dbo.Mailings (name, company, address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + " " + self.last_name.replace("\'", "\'\'").title() + "', '" + self.company_name.replace("\'", "\'\'") + "','" + self.address + " " + self.city + " " + self.county + " " + self.state_code + " " + self.zip_code + "'); COMMIT")        

        print("Finished writing to file. Returning to main menu...")


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
                        if selected_database == "CRM":
                            db_id = "crm"

                        else:
                            db_id = "mail"
                            
                            
                        db_connection.executeQuery("DELETE FROM dbo." + selected_database + " WHERE " + db_id + "_id='" + str(row[0]) + "'; COMMIT")
                        ## The user is prompted with a message confirming deletion then they are returned to the main menu
                        print("\nDeleting Record #: " + str(record) + " from the " + selected_database + " database and returning to the main menu...")
                        return False


                    elif confirmation.lower() == "n":
                        ## If a user enter N for no then deletion of their chosen record is aborted
                        print("\nDiscarding changes and returning to main menu...")
                        return False

                    else:
                        ## This error is thrown if a user does not enter Yes or No for their deletion selection
                        print("Please enter Y or N to confirm your selection.")
                        confirm_delete = True
    
    def showContents(self, db_choice):
        """A method for showing all of the contents of a chosen database"""

        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + db_choice)

        print("\nDisplaying contents of the " + db_choice + " database\n=============================================")
        
        if db_choice == "CRM":
            for row in my_query_result:     
                print(str(row.crm_id) + ". First Name: " + str(row.f_name) + " | Last Name: " + str(row.l_name) + " | Address: " + str(row.address) + " | City: " + str(row.city) + " | County: " + str(row.county) + " | State: " + str(row.state) + " | Zip Code: " + str(row.zip) + " | Company Name: " + str(row.company) + " | Primary Phone#: " + str(row.primary_phone) + " | Secondary Phone#: " + str(row.secondary_phone) + " | Email Address: " + str(row.email_address) + "\n")

        else:
            for row in my_query_result:     
                print(str(row.mail_id) + ". Name: " + str(row.name) + " | Company Name: " + str(row.company) + " | Address: " + str(row.address) + "\n")

    def updateContents(self):
        None