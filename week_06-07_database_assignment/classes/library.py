from classes.database_access import DB_Connect
from classes.validator import Validator
db_connection = DB_Connect("it412_sbrohl2", "Pr0grammingRul3s!", "it412_sbrohl2")

class library(Validator):
    """A class representing a library catalogue"""

    def __init__(self, book_author=" ", book_title=" ", isbn=0, num_copies_purchased=0, num_copies_checked=0, retail_price=0.0, number=0):
        """A constructor for the library Class"""
        self.book_author = book_author
        self.book_title = book_title
        self.isbn = isbn
        self.num_copies_purchased = num_copies_purchased 
        self.num_copies_checked = num_copies_checked
        self.retail_price = retail_price
        self.num_copies_purchased_temp = 0
        self.number = number

    def addContents(self):
        """A class for adding new book content to the database"""
        ## A query that selects all records in the library table
        my_query_result = db_connection.executeSelectQuery("SELECT isbn FROM dbo.library_catalogue")
        ## Looping through all of the records in the library table
        for row in my_query_result:
            ## Checking to ensure a duplicate book is not added based on ISBN
            if self.isbn in row.isbn:
                print("You are attempting to add a duplicate entry! Discarding changes and returning to the main menu.")
                duplicates = True
                break

            else:
                duplicates = False
        
        if duplicates == False:
                print("Saving book to the database...")
                db_connection.executeQuery("INSERT INTO dbo.library_catalogue (book_author, book_title, isbn, num_copies_purchased, num_copies_checked, retail_price) VALUES ('" + self.book_author.title() + "', '" + self.book_title.replace("\'", "\'\'").title() + "', '" + self.isbn + "', '" + str(self.num_copies_purchased) + "', '" + str(self.num_copies_checked) + "', '" + str(self.retail_price) + "'); COMMIT")
                

    def currentList(self):
        """A class that displays the current list of books in the database"""
        print("\n\tCurrent library: ")
        print("\t=====================")
        ## A query selecting all records in the library
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
        count = 1
        ## Looping through current records and printing them to screen
        for row in my_query_result:
            print(str(count) + ". " + "\tTitle: " + row.book_title + "\n\tAuthor: " + row.book_author + "\n\tISBN #:" + row.isbn + "\n\t# Copies Purchased: " + str(row.num_copies_purchased) + "\n\t# Copies Checked Out: " + str(row.num_copies_checked) + "\n\tRetail Price: " + str(row.retail_price))
            count += 1
            print("\n")
    
    def commitChanges(self):
        """A class that commits all update changes to the database"""
        ## User is prompted that changes are being committed
        print("Committing changes to the database...")
        db_connection.executeQuery("COMMIT")

    def displayInput(self):
        """A class that displays changes a user has made to book values before they commit them to the database"""
        ## Before changes are committed the user can see all changes made
        print("\nTitle: " + self.book_title.title(),"\nAuthor: " + self.book_author.title(), "\nISBN: " + str(self.isbn), "\nCopies Purchased: " + str(self.num_copies_purchased), "\nCopies Checked Out: " + str(self.num_copies_checked), "\nRetail Price: " + str(self.retail_price))
        
    def editBook(self):
        """A class for editing a book"""
        ## A query selecting all records from the library table
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
        edit_book = False
        ## A loop to edit book values
        while not edit_book:
            if self.number:
                try:
                    ## Ensuring the user has input a value equal to an int
                    self.number = int(self.number)

                except ValueError:
                    ## If a user inputs a value that is not an int an exception is thrown
                    print("You entered an invalid character. Please enter a number that corresponds to a value listed above.")
                    return False

                else:      
                    count = 1
                    for row in my_query_result:
                        ## If the selected option number input by the user equals the count variable then the corresponding record to that number is displayed on screen for editing 
                        if self.number == count:
                            print("\nWhat would you like to edit for " + row.book_title + "?\n\n" + "\t1. Title: " + row.book_title + "\n\t2. Author: " + row.book_author + "\n\t3. ISBN #:" + row.isbn + "\n\t4. # Copies Purchased: " + str(row.num_copies_purchased) + "\n\t5. # Copies Checked Out: " + str(row.num_copies_checked) + "\n\t6. Retail Price: " + str(row.retail_price))
                            ## The number of books purchased is temporarily stored for a later validation check against the number of books checked out 
                            self.num_copies_purchased_temp = row.num_copies_purchased
                            edit_book = True
                            return False
                        
                        elif self.number > len(my_query_result) + 1:
                            ## If the user inputs a number that does not correspond with a value that can be changed an error is thrown and they are re-prompted
                            print("You did not enter a number that corresponds to a value listed above. Please try again.")
                            edit_book = False
                            return True

                        else:
                            ## Increment a count variable to loop through the list of queried results
                            count += 1
                             
            else:
                ## If an invalid number option is input the user is thrown an error and reprompted to try again
                print("You entered an invalid value. Please try again.")
                return True
                    

    def removeBook(self):
        """A class for removing a book"""
        delete_book_ok = False
        while not delete_book_ok:
            if self.number:
                ## A query selecting all of the library table
                my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
                count = 1
                ## Looping throughht the library table to select a value that matches the number input by the user
                for row in my_query_result:
                    if self.number == str(count):
                        confirmation = input("Are you sure you want to delete " + "\"" + str(row.book_title) + "\"" + " from the library catalogue? Y/N: ")
                        if confirmation.lower() == "y":
                            ## Deleting the user's selection and committing the change to the database
                            db_connection.executeQuery("DELETE FROM dbo.library_catalogue  WHERE isbn='" + row.isbn + "'; COMMIT")
                            ## The user is prompted with a message confirming deletion then they are returned to the main menu
                            print("\nDeleting " + "\"" + row.book_title.title() + "\"" + " from the catalogue and returning to the main menu...")
                            delete_book_ok = True
                            return True

                        elif confirmation.lower() == "n":
                            ## If a user enter N for no then deletion of their chosen record is aborted
                            print("\nDiscarding changes and returning to main menu...")
                            delete_book_ok = True
                            return True

                        else:
                            ## This error is thrown if a user does not enter Yes or No for their deletion selection
                            print("Please enter Y or N to confirm your selection.")
                            delete_book_ok = False

                    elif self.number.lower() == "q":
                        ## This option allows a user to quit a deletion operation and return to the main menu
                        print("Returning to the main menu...")
                        delete_book_ok = True
                        return True  

                    else:
                        ## Incrementing a counter variable to loop through queried results
                        count += 1
                               
            else:
                ## If an invalid selection is made an error message is thrown and the user is given a re-prompt
                print("You have either not entered a number or entered an invalid number. Please try again or enter \"q\" to return to the main menu..")
                return False      

    def updateContents(self, option, passed_value):
        """A class for updating the contents of a book; does not commit changes until approved by the user with the commit class"""
        updatecontents = False
        while not updatecontents:
            ## A query to select all contents from the library table
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
            count = 1
            for row in my_query_result:
                if self.number == count:
                    ## Update selected row with new values; Does not commit changes!
                    db_connection.executeQuery("UPDATE dbo.library_catalogue SET " + option +"='" + str(passed_value) + "' WHERE book_title='" + row.book_title.replace("\'", "\'\'") + "'")
                    updatecontents = True
                    break

                else:
                    count += 1


   