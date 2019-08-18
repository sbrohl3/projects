class Validator():
    """A class representing a validator"""

    def __init__(self, book_author=" ", book_title=" ", isbn=0, num_copies_purchased=0, num_copies_checked=0, retail_price=0.0, number=0):
        """A constructor for the validator Class"""
        self.book_author = book_author
        self.book_title = book_title
        self.isbn = isbn
        self.num_copies_purchased = num_copies_purchased 
        self.num_copies_checked = num_copies_checked
        self.retail_price = retail_price
        self.num_copies_purchased_temp = 0
        self.number = number


    def validateAuthorName(self):
            """A class for validating the author's name"""
            ## Declaring a Flag to control a while loop
            author_name_ok = False
            ## While loop to have user retry their input if they enter incorrectly
            while not author_name_ok:
                ## Declaring a list of characters that are not allowed in book_author
                bad_chars = ["!", "\"", "@", "#", "$", "%", "^", "&", "*","(", ")", "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9" ]
                if self.book_author:
                    ## Checking book_author for bad characters
                    for char in self.book_author:
                        ## If bad characters are found, exit the program
                        if char not in bad_chars:
                            invalid_char = False
                            
                                
                        else:
                            print("\nThe Author's name you provided contains invalid characters. Please try again.")
                            author_name_ok = False
                            return False

                    if invalid_char == False:
                        print("The inputted Author name is: " + self.book_author.title())
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
                print("The inputted title is: " + self.book_title.title())
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
                    if char in good_chars:
                        if len(self.isbn) == 14 or len(self.isbn) == 13 or len(self.isbn) == 11 or len(self.isbn) == 10:
                            invalid_char = False

                        else:
                            print("\nYour ISBN is not properly formatted. Please ensure you have placed your \"-\"'s correctly and try again")
                            return False
                            
                    else:
                       ## If the ISBN does not meet formatting standards an error is thrown
                       print("Your ISBN contains an invalid character. Please try again.")
                       return False
                
                if invalid_char == False:
                    print("The inputted ISBN name is: " + self.isbn)
                    isbn_ok = True
                    return True

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
    
    def validateNumCopiesChecked2(self):
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
                    if int(self.num_copies_checked) <= int(self.num_copies_purchased_temp):
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

    