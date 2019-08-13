from classes.database_access import DB_Connect
db_connection = DB_Connect("it412_sbrohl2", "Pr0grammingRul3s!", "it412_sbrohl2")

class library():
    """A class representing a library catalogue"""

    def __init__(self, book_author=" ", book_title=" ", isbn=0, num_copies_purchased=0, num_copies_checked=0, retail_price=0.0, number=0):
        """A constructor for the validator Class"""
        self.book_author = book_author
        self.book_title = book_title
        self.isbn = isbn
        self.num_copies_purchased = num_copies_purchased 
        self.num_copies_checked = num_copies_checked
        self.retail_price = retail_price
        self.number = number

    def addContents(self):
        """A class for adding new book content to the database"""
        ## A query that selects all records in the library table
        my_query_result = db_connection.executeSelectQuery("SELECT isbn FROM dbo.library_catalogue")
        ## Looping through all of the records in the library table
        for row in my_query_result:
            ## Checking to ensure a duplicate book is not added based on ISBN
            if self.isbn == row.isbn:
                print("You are attempting to add a duplicate entry! Discarding changes and returning to the main menu.")
                break
            ## If a duplicate is not detected then the book is saved and committed to the database
            else:    
                print("Saving book to the database...")
                db_connection.executeQuery("INSERT INTO dbo.library_catalogue (book_author, book_title, isbn, num_copies_purchased, num_copies_checked, retail_price) VALUES ('" + self.book_author.title() + "', '" + self.book_title.replace("\'", "\'\'").title() + "', '" + self.isbn + "', '" + str(self.num_copies_purchased) + "', '" + str(self.num_copies_checked) + "', '" + str(self.retail_price) + "'); COMMIT")
                break 

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
                            num_copies_purchased_temp = row.num_copies_purchased
                            ## The temporary value of books purchased is passed through to the validation class exclusively made for editing the number of checked out books
                            validateNumCopiesChecked(num_copies_purchased_temp)
                            edit_book = True
                            return False
                        
                        elif self.number > len(row) + 1:
                            ## If the user inputs a number that does not correspond with a value that can be changed an error is thrown and they are re-prompted
                            print("You did not enter a number that corresponds to a value listed above. Please try again.")
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


    def validateAuthorName(self):
        """A class for validating the author's name"""
        ## Declaring a Flag to control a while loop
        author_name_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not author_name_ok:
            ## Declaring a list of characters that are not allowed in book_author
            bad_chars = ["!", "\"", "@", "#", "$", "%", "^", "&", "*","(", ")", "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
            if self.book_author:
                ## Checking book_author for bad characters
                for char in self.book_author:
                    ## If bad characters are found, exit the program
                    if char in bad_chars or char.isspace():
                        print("\nThe Author's name you provided contains invalid characters. Please try again.")
                        author_name_ok = False
                        return False
                            
                    else:
                        print("The inputted Author name is: " + self.book_author)
                        author_name_ok = True
                        return True
            ## if no input is provided re-prompt
            else:
                print("\nYou have not entered an Author's name. Please try again.")
                return False
                
    def validateBookTitle(self):
        """A class for validating the book title"""
        ## Declaring a Flag to control a while loop
        book_title_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not book_title_ok:
            if self.book_title:
                print("The inputted title is: " + self.book_title)
                book_title_ok = True
                return True

            ## if no input is provided re-prompt
            else:
                print("\nYou have not entered a book title. Please Try again.")
                return False

    def validateISBN(self):
        """A class for validating the book's ISBN #"""
        ## Declaring a Flag to control a while loop
        isbn_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not isbn_ok:
            ## Declaring a list of characters that are allowed in the ISBN
            good_chars = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-"]
            if self.isbn:
                ## Checking ISBN for bad characters
                for char in self.isbn:
                    ## If characters match digits or contains -, then proceed with the program
                    if char in good_chars and len(self.isbn) == 14 or len(self.isbn) == 13 or len(self.isbn) == 11 or len(self.isbn) == 10:
                        print("The inputted ISBN name is: " + self.isbn)
                        isbn_ok = True
                        return True
                            
                    else:
                        ## If the ISBN does not meet formatting standards an error is thrown
                        print("\nYour ISBN is not properly formatted. Please ensure you have placed your \"-\"'s correctly and try again")
                        isbn_ok = False
                        return False
            ## if no input is provided re-prompt
            else:
                print("\nYou have not entered an ISBN. Please try again.")
                return False

    def validateNumCopies(self):
        """A class for validating the number of purchased books on-hand"""
        ## Declaring a Flag to control a while loop
        num_copies_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not num_copies_ok:
            if self.num_copies_purchased:
                try:
                    ## Attempting to cast the number of books purchased as an int
                    self.num_copies_purchased = int(self.num_copies_purchased)
                
                except ValueError:
                    ## If a user inputs a value that is not an int an exception is thrown
                    print("\nYou have entered an invalid number. Please try again.")
                    num_copies_ok = False
                    return False

                else:
                    ## If the number of books can be cast as an int and is less then amount of purchased books on-hand validation is passed
                    print("The inputted number of copies purchased is: " + str(self.num_copies_purchased))
                    num_copies_ok = True
                    return True
                                
            ## if no input is provided re-prompt
            else:
                print("\nYou have not provided a number of copies purchased. Please try again.")
                num_copies_ok = False
                return False

    def validateNumCopiesChecked(self):
        """A class for validating the number for books checked out"""
        ## Declaring a Flag to control a while loop
        num_copies_checked_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not num_copies_checked_ok:
            if self.num_copies_checked:
                try:
                    ## Attempting to cast the number of books checked out as an int
                    self.num_copies_checked = int(self.num_copies_checked)
                    
                except ValueError:
                    ## If a user inputs a value that is not an int an exception is thrown
                    print("\nYou have entered an invalid character. Please enter a valid integer value.")
                    return False

                else:

                    if int(self.num_copies_checked) <= int(self.num_copies_purchased):
                        print("The inputted number of copies checked out is: " + str(self.num_copies_checked))
                        num_copies_checked_ok = True
                        return True

                    else:
                        ## If the number of books checked out exceeds the number of books on-hand an error will be thrown asking for a re-prompt for a lesser/equal value
                        print("\nThe amount of books checked out is greater than the amount of purchased books on-hand. Please re-enter the amount of books checked out.")
                        return False
                    
            ## if no input is provided re-prompt
            else:
                print("\nYou have provided an invalid number. Please try again.")
                return False
       
    def validateNumCopiesChecked2(self, passed_value):
        """Another class for validating the number of books checked out; This class is exclusively used by the editBook class"""
        ## Declaring a Flag to control a while loop
        num_copies_checked_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not num_copies_checked_ok:
            if self.num_copies_checked:
                try:
                    ## Attempting to cast the number of books checked out as an int
                    self.num_copies_checked = int(self.num_copies_checked)
                    
                except ValueError:
                    ## If a user inputs a value that is not an int an exception is thrown
                    print("\nYou have entered an invalid character. Please enter a valid integer value.")
                    return False

                else:
                    ## If the number of books can be cast as an int and is less then amount of purchased books on-hand validation is passed
                    if int(self.num_copies_checked) <= int(passed_value):
                        print("The inputted number of copies checked out is: " + str(self.num_copies_checked))
                        num_copies_checked_ok = True
                        return True

                    else:
                        ## If the number of books checked out exceeds the number of books on-hand an error will be thrown asking for a re-prompt for a lesser/equal value
                        print("\nThe amount of books checked out is greater than the amount of purchased books on-hand. Please re-enter the amount of books checked out.")
                        return False
                    
            ## if no input is provided re-prompt
            else:
                print("\nYou have provided an invalid number. Please try again.")
                return False

    def validateRetailPrice(self):
        """A class for validating the retail price of books"""
        ## Declaring a Flag to control a while loop
        retail_price_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not retail_price_check_ok:
            if self.retail_price:
                try:
                    ## Attempting to cast the number of books checked out as an float
                    self.retail_price = float(self.retail_price)
                
                except ValueError:
                    ## If a user inputs a value that is not an float an exception is thrown
                    print("\nYou have entered an invalid value. Please try again.")
                    return False

                else:
                    print("The inputted retail price is: " + str(self.retail_price))
                    retail_price_check_ok = True
                    return True

            ## if no input is provided re-prompt
            else:
                print("\nNo Retail Price provided...")
                return True

 