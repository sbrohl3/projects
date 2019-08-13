## SQL Database Assignment
## IT412
## 08/10/2019
## BROHL, STEVEN
from classes.library import library

## Instantiating the library class to a variable for later use
library = library()

## Setting my program to run as True 
program_run = True

## A loop to run the enirety of my program
while program_run == True:
    ## Printing an option menu to screen
    print("\nPlease select an option below to continue: ")
    print("==============================================")
    print("\t1. Show all books \n\t2. Add a book \n\t3. Edit a book \n\t4. Remove a book \n\t5. Exit program\n")
    ## User input to choose an option
    selection = input("Enter the corresponding number next to the option you wish to select: ")

    ## An option to print all current books to screen
    if selection == '1':
     library.currentList()

    ## An option to add new books to the Database
    elif selection == '2':
        title_check = False
        while title_check == False: 
            ## Validating and adding a new book title
            library.book_title = input("Please enter the title of the book you wish to add: ")
            title_check = library.validateBookTitle()
            
        author_check = False
        while author_check == False:
            ## Validating and adding a new book author 
            library.book_author = input("Please enter the name of the of the Author for the book you wish to add: ")
            author_check = library.validateAuthorName()
        
        isbn_check = False
        while isbn_check == False:
            ## Validating and adding a new book ISBN 
            library.isbn = input("Please enter the ISBN for the book you wish to add: ")
            isbn_check = library.validateISBN()
    
        copies_check = False
        while copies_check == False:
            ## Validating and adding a number of books purchased 
            library.num_copies_purchased = input("Please enter the number of copies purchased for the book you wish to add: ")
            copies_check = library.validateNumCopies()
        
        copies_checked_check = False
        while copies_checked_check == False:
            ## Validating and adding a number of books checked out 
            library.num_copies_checked = input("Please enter the number of copies checked out for the book you wish to add: ")
            copies_checked_check = library.validateNumCopiesChecked()

        retail_price_check = False
        while retail_price_check == False:
            ## Validating and adding a retail price for the new book 
            library.retail_price = input("Please enter the retail price for the book you wish to add or leave this field empty and press enter: ")
            retail_price_check = library.validateRetailPrice()
       
        ## Displaying the users current changes to screen    
        library.displayInput()
        ## Prompting the user if they wish to save their changes
        save_add = input("Do you wish to save your addition to the database? Y/N: ")
        if save_add.lower() == "y":
            library.addContents()
        
        elif save_add.lower() == "n":
            print("Discarding changes and returning to main menu...")
            program_run = True

    ## An option to edit books in the current library
    elif selection == '3':
        ## Printing the current list of books to screen
        library.currentList()
        ## Prompting the user to select the book they wish to edit
        library.number = input("Please enter the number next to the book you wish to edit: ")
        return_values = library.editBook()
        editing = return_values[0]
    
        editing = True
        while editing:
            ## Asking the user to select a book value they wish to edit          
            edit_selection = input("\nPlease enter a number that corresponds to a value you wish to edit: ")
            if edit_selection == "1":
                title_check = False
                while title_check == False:
                    ## A prompt to validate and edit the selected book's title 
                    library.book_title = input("\nWhat would you like to change the title to?: ")
                    title_check = library.validateBookTitle()
                    option = "book_title"
                    library.updateContents(option, library.book_title)

            elif edit_selection == "2":
                author_check = False
                while author_check == False:
                    ## A prompt to validate and edit the selected book's author name 
                    library.book_author = input("What would you like to change the Author's name to?: ")
                    author_check = library.validateAuthorName()
                    option = "book_author"
                    library.updateContents(option, library.book_author)

            elif edit_selection == "3":
                isbn_check = False
                while isbn_check == False:
                    ## A prompt to validate and edit the selected book's ISBN 
                    library.isbn = input("What would you like to change the ISBN to?: ")
                    isbn_check = library.validateISBN()
                    option = "isbn"
                    library.updateContents(option, library.isbn)

            elif edit_selection == "4":   
                copies_check = False
                while copies_check == False:
                    ## A prompt to validate and edit the selected book's # of purchased copies 
                    library.num_copies_purchased = input("What would you like to change the number of purchased copies to?: ")
                    copies_check = library.validateNumCopies()
                    option = "num_copies_purchased"
                    library.updateContents(option, library.num_copies_purchased)

            elif edit_selection == "5":   
                copies_checked_check = False
                while copies_checked_check == False:
                    ## A prompt to validate and edit the selected book's # of copies checked out 
                    library.num_copies_checked = input("What would you like to change the number of checked out copies to?: ")
                    num_copies_purchased_temp = return_values[1]
                    ## The temporary value of books purchased is passed through to the validation class exclusively made for editing the number of checked out books
                    copies_checked_check = library.validateNumCopiesChecked2(num_copies_purchased_temp)
                    option = "num_copies_checked"
                    library.updateContents(option, library.num_copies_checked)

            elif edit_selection == "6": 
                retail_price_check = False
                while retail_price_check == False: 
                    ## A prompt to validate and edit the selected book's retail price
                    library.retail_price = input("What would you like to change the retail price to?: ")
                    retail_price_check = library.validateRetailPrice()
                    option = "retail_price"
                    library.updateContents(option, library.retail_price)

            ## A prompt asking whether the user wishes to continue editing their selected book
            continue_prompt = input("Do you wish to continue making changes to this book: Y/N ")
            if continue_prompt.lower() == "y":
                editing = True

            elif continue_prompt.lower() == "n":
                editing = False
                ## A prompt asking the user if they wish to save their updated edits to the database
                save_add = False
                while save_add == False:
                    save_add = input("Do you wish to save your updates to the database? Y/N: ")
                    if save_add.lower() == "y":
                        editing = False
                        save_add = True
                        library.commitChanges()
                        
                    ## A prompt to discard changes if a user chooses not to save their updates
                    elif save_add.lower() == "n":
                        print("Discarding changes and returning to main menu...")
                        editing = False
                        save_add = True
                        program_run = True
                    
                    else:
                        ## An error message if a user enters an invalid response
                        print("You have entered an invalid response. Please answer (Y)es or (N)o.")
                        
            else:
                ## An error message if a user enters an invalid response
                print("You have entered an invalid response. Please answer (Y)es or (N)o.")
    
    ## An option to delete library entries
    elif selection == '4':
        delete_book_check = False
        while delete_book_check == False:
            ## Display current library list
            library.currentList()
            ## A prompt to delete a selected book in the library
            library.number = input("Please enter the number next to the book you wish to remove: ")
            delete_book_check = library.removeBook()
            program_run = True

    ## An option to end the program
    elif selection == '5':
        print("Terminating Program...")
        program_run = False
    
    ## An error in case a user enters an invalid option in the main menu
    else:
        print("You have chosen an invalid option or entered an incorrect value. Please try again.")
        program_run = True