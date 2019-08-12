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
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
        for row in my_query_result:
            if self.isbn == row.isbn:
                print("You are attempting to add a duplicate entry! Discarding changes and returning to the main menu.")
                break
            else:    
                print("Saving book to the database...")
                db_connection.executeQuery("INSERT INTO dbo.library_catalogue (book_author, book_title, isbn, num_copies_purchased, num_copies_checked, retail_price) VALUES ('" + self.book_author.title() + "', '" + self.book_title.replace("\'", "\'\'").title() + "', '" + self.isbn + "', '" + str(self.num_copies_purchased) + "', '" + str(self.num_copies_checked) + "', '" + str(self.retail_price) + "'); COMMIT")
                break 

    def currentList(self):
        print("\n\tCurrent library: ")
        print("\t=====================")
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
        count = 1
        for row in my_query_result:
            print(str(count) + ". " + "\tTitle: " + row.book_title + "\n\tAuthor: " + row.book_author + "\n\tISBN #:" + row.isbn + "\n\t# Copies Purchased: " + str(row.num_copies_purchased) + "\n\t# Copies Checked Out: " + str(row.num_copies_checked) + "\n\tRetail Price: " + str(row.retail_price))
            count += 1
            print("\n")
    
    def commitChanges(self):
        print("Committing changes to the database...")
        db_connection.executeQuery("COMMIT")

    def displayInput(self):
        print("\nTitle: " + self.book_title.title(),"\nAuthor: " + self.book_author.title(), "\nISBN: " + str(self.isbn), "\nCopies Purchased: " + str(self.num_copies_purchased), "\nCopies Checked Out: " + str(self.num_copies_checked), "\nRetail Price: " + str(self.retail_price))
        

    def editBook(self):
        my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
        edit_book = False
        while not edit_book:
            if self.number:
                try:
                    self.number = int(self.number)

                except ValueError:
                    print("You entered an invalid character. Please enter a number that corresponds to a value listed above.")
                    return False

                else:      
                    count = 1
                    for row in my_query_result:
                        if self.number == count:
                            print("\nWhat would you like to edit for " + row.book_title + "?\n\n" + "\t1. Title: " + row.book_title + "\n\t2. Author: " + row.book_author + "\n\t3. ISBN #:" + row.isbn + "\n\t4. # Copies Purchased: " + str(row.num_copies_purchased) + "\n\t5. # Copies Checked Out: " + str(row.num_copies_checked) + "\n\t6. Retail Price: " + str(row.retail_price))
                            edit_book = True
                            return False
                        
                        elif self.number > len(row) + 1:
                            print(len(row))
                            print("You did not enter a number that corresponds to a value listed above. Please try again.")
                            return True

                        else:
                            count += 1
                             
            else:
                print("You entered an invalid value. Please try again.")
                return True
                    

    def removeBook(self):
        delete_book_ok = False
        while not delete_book_ok:
            if self.number:
                my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
                count = 1
                for row in my_query_result:
                    if self.number == str(count):
                        confirmation = input("Are you sure you want to delete " + "\"" + str(row.book_title) + "\"" + " from the library catalogue? Y/N: ")
                        if confirmation.lower() == "y":
                            db_connection.executeQuery("DELETE FROM dbo.library_catalogue  WHERE isbn='" + row.isbn + "'; COMMIT")
                            print("\nDeleting " + "\"" + row.book_title.title() + "\"" + " from the catalogue and returning to the main menu...")
                            delete_book_ok = True
                            return True

                        elif confirmation.lower() == "n":
                            print("\nDiscarding changes and returning to main menu...")
                            delete_book_ok = True
                            return True

                        else:
                            print("Please enter Y or N to confirm your selection.")
                            delete_book_ok = False

                    elif self.number.lower() == "q":
                        print("Returning to the main menu...")
                        delete_book_ok = True
                        return True  

                    else:
                        count += 1
                               
            else:
                print("You have either not entered a number or entered an invalid number. Please try again or enter \"q\" to return to the main menu..")
                return False      

    def updateContents(self, option, passed_value):
        updatecontents = False
        while not updatecontents:
            my_query_result = db_connection.executeSelectQuery("SELECT * FROM dbo.library_catalogue")
            count = 1
            for row in my_query_result:
                if self.number == count:
                    db_connection.executeQuery("UPDATE dbo.library_catalogue SET " + option +"='" + str(passed_value) + "' WHERE book_title='" + row.book_title.replace("\'", "\'\'") + "'")
                    updatecontents = True
                    break

                else:
                    count += 1


    def validateAuthorName(self):
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
                        print("\nYour ISBN is not properly formatted. Please ensure you have placed your \"-\"'s correctly and try again")
                        isbn_ok = False
                        return False
            ## if no input is provided re-prompt
            else:
                print("\nYou have not entered an ISBN. Please try again.")
                return False

    def validateNumCopies(self):
        ## Declaring a Flag to control a while loop
        num_copies_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not num_copies_ok:
            if self.num_copies_purchased:
                try:
                    self.num_copies_purchased = int(self.num_copies_purchased)
                
                except ValueError:
                    print("\nYou have entered an invalid number. Please try again.")
                    return False

                else:
                    print("The inputted number of copies purchased is: " + str(self.num_copies_purchased))
                    num_copies_ok = True
                    return True
                                
            ## if no input is provided re-prompt
            else:
                print("\nYou have not provided a number of copies purchased. Please try again.")
                return False
                    
    def validateNumCopiesChecked(self):
        ## Declaring a Flag to control a while loop
        num_copies_checked_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not num_copies_checked_ok:
            if self.num_copies_checked:
                try:
                    self.num_copies_checked = int(self.num_copies_checked)
                    
                except ValueError:
                    print("\nYou have entered an invalid character. Please enter a valid integer value.")
                    return False

                else:
                    if int(self.num_copies_checked) <= int(self.num_copies_purchased):
                        print("The inputted number of copies checked out is: " + str(self.num_copies_checked))
                        num_copies_checked_ok = True
                        return True

                    else:
                        print("\nThe amount of books checked out is greater than the amount of purchased books on-hand. Please re-enter the amount of books checked out.")
                        return False
                    
            ## if no input is provided re-prompt
            else:
                print("\nYou have provided an invalid number. Please try again.")
                return False

    def validateRetailPrice(self):
        ## Declaring a Flag to control a while loop
        retail_price_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not retail_price_check_ok:
            if self.retail_price:
                try:
                    self.retail_price = float(self.retail_price)
                
                except ValueError:
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

 