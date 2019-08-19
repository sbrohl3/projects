## Importing validation as well as database connection classes
from classes.database_access import DB_Connect
from classes.validator import Validator

## Importing built-in Json module
import json

## Database connection information instatiated to a variable
db_connection = DB_Connect("it412_sbrohl2", "Pr0grammingRul3s!", "it412_sbrohl2")

class Database(Validator):
    """A class for performing database functions"""

    def __init__(self, first_name=" ", last_name=" ", company_name=" ", address=" ", city=" ", county=" ", state_code=" ", zip_code=0, phone_number=" ", phone_number_2=" ", email_address=" "):
        """A constructor for the Database Class"""
        self.first_name = first_name
        self.last_name = last_name
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
        db_connection.executeQuery("INSERT INTO dbo.CRM (f_name, l_name, address, city, county, state, zip, company, primary_phone, secondary_phone, email_address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + "', '" + self.last_name.replace("\'", "\'\'").title() + "', '" + self.address + "', '" + self.city.replace("\'", "\'\'") + "', '" + self.county.replace("\'", "\'\'") + "', '" + self.state_code.upper() + "', '" + self.zip_code + "', '" + self.company_name.replace("\'", "\'\'") + "', '" + self.phone_number + "', '" + self.phone_number_2 + "' , '" + self.email_address + "'); COMMIT")
        
        print("\nSaving entries to the Mailings database...")
        db_connection.executeQuery("INSERT INTO dbo.Mailings (name, company, address) VALUES ('" + self.first_name.replace("\'", "\'\'").title() + " " + self.last_name.replace("\'", "\'\'").title() + "', '" + self.company_name.replace("\'", "\'\'") + "', '" + self.address + "'); COMMIT")        

    def displayInput(self):
        """A class that displays compiled user input before committing to the database"""

        ## Before changes are committed the user can see all changes made
        print("\nCurrent Record: \n=============== \nName: " + self.first_name.title() + self.last_name.title(),"\nAddress: " + self.address.title(), "\nCity: " + self.city + "\nState: " + self.state_code.upper() + "\nZip Code: " + self.zip_code + "\nCompany Name: " + self.company_name + "\nPrimary Phone: " + self.phone_number  + "\nSecondary Phone: " + self.phone_number_2 + "\nEmail Address: " + self.email_address)
        
    def editRecord(self, record, selected_database):
        """A method for editing a record in a chosen database"""

        ## A query selecting all records from the database table
        if selected_database == "CRM":
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database + " Where crm_id= '" + str(record) + "'; ")
            for row in my_query_result:
                if record == row.crm_id:
                    print("Record Number: " + str(row.crm_id) + " | First Name: " + str(row.f_name) + " | Last Name: " + str(row.l_name) + " | Address: " + str(row.address) + " | City: " + str(row.city) + " | County: " + str(row.county) + " | State: " + str(row.state) + " | Zip Code: " + str(row.zip) + " | Company Name: " + str(row.company) + " | Primary Phone#: " + str(row.primary_phone) + " | Secondary Phone#: " + str(row.secondary_phone) + " | Email Address: " + str(row.email_address))
                    edit_field = input("\nWhat field would you like to edit in this record: ")


        elif selected_database == "Mailings":
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + selected_database + " Where mail_id=" + str(record))



    def importFile(self):
        """A method for importing in a data file"""

        None ## Temporary placeholder to keep program from breaking during initial testing
    
    def loadDatabase(self):
        """A method for loading the contents of a selected database"""

        None ## Temporary placeholder to keep program from breaking during initial testing

    def removeRecord(self):
        """A method for removing a record from all databases"""

        None ## Temporary placeholder to keep program from breaking during initial testing
    
    def showContents(self, db_choice):
        """A method for showing all of the contents of a chosen database"""

        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo." + db_choice)

        print("\n Displaying contents of the " + db_choice + " database. \n=============================================")
        
        if db_choice == "CRM":
            count = 1
            for row in my_query_result:     
                print(str(count) + ". Record Number: " + str(row.crm_id) + " | First Name: " + str(row.f_name) + " | Last Name: " + str(row.l_name) + " | Address: " + str(row.address) + " | City: " + str(row.city) + " | County: " + str(row.county) + " | State: " + str(row.state) + " | Zip Code: " + str(row.zip) + " | Company Name: " + str(row.company) + " | Primary Phone#: " + str(row.primary_phone) + " | Secondary Phone#: " + str(row.secondary_phone) + " | Email Address: " + str(row.email_address))
                count += 1

        else:
            count = 1
            for row in my_query_result:     
                print(str(count) + ". Record Number: " + str(row.mail_id) + " | Name: " + str(row.name) + " | Company Name: " + str(row.company) + " | Address: " + str(row.address))
                count += 1