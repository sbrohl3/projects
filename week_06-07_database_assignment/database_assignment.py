## SQL Database Assignment
## IT412
## 08/10/2019
## BROHL, STEVEN
from classes.library import library

library = library()
program_run = True

while program_run == True:
    print("\nPlease select an option below to continue: ")
    print("==============================================")
    print("\t1. Show all books \n\t2. Add a book \n\t3. Edit a book \n\t4. Remove a book \n\t5. Exit program\n")
    selection = input("Enter the corresponding number next to the option you wish to select: ")

    if selection == '1':
     library.currentList()

    elif selection == '2':
        title_check = False
        while title_check == False: 
            library.book_title = input("Please enter the title of the book you wish to add: ")
            title_check = library.validateBookTitle()
        
        author_check = False
        while author_check == False: 
            library.book_author = input("Please enter the name of the of the Author for the book you wish to add: ")
            author_check = library.validateAuthorName()
        
        isbn_check = False
        while isbn_check == False: 
            library.isbn = input("Please enter the ISBN for the book you wish to add: ")
            isbn_check = library.validateISBN()
    
        copies_check = False
        while copies_check == False: 
            library.num_copies_purchased = input("Please enter the number of copies purchased for the book you wish to add: ")
            copies_check = library.validateNumCopies()
        
        copies_checked_check = False
        while copies_checked_check == False: 
            library.num_copies_checked = input("Please enter the number of copies checked out for the book you wish to add: ")
            copies_checked_check = library.validateNumCopiesChecked()

        retail_price_check = False
        while retail_price_check == False: 
            library.retail_price = input("Please enter the retail price for the book you wish to add or leave this field empty and press enter: ")
            retail_price_check = library.validateRetailPrice()
       
        library.displayInput()
        save_add = input("Do you wish to save your addition to the database? Y/N: ")
        if save_add.lower() == "y":
            library.addContents()
        
        elif save_add.lower() == "n":
            print("Discarding changes and returning to main menu...")
            program_run = True

    elif selection == '3':
        
        library.currentList()
        library.number = input("Please enter the number next to the book you wish to edit: ")
        editing = library.editBook()
        
        editing = True
        while editing:          
            edit_selection = input("\nPlease enter a number that corresponds to a value you wish to edit: ")
            if edit_selection == "1":
                title_check = False
                while title_check == False: 
                    library.book_title = input("\nWhat would you like to change the title to?: ")
                    title_check = library.validateBookTitle()
                    option = "book_title"
                    library.updateContents(option, library.book_title)

            elif edit_selection == "2":
                author_check = False
                while author_check == False: 
                    library.book_author = input("What would you like to change the Author's name to?: ")
                    author_check = library.validateAuthorName()
                    option = "book_author"
                    library.updateContents(option, library.book_author)

            elif edit_selection == "3":
                isbn_check = False
                while isbn_check == False: 
                    library.isbn = input("What would you like to change the ISBN to?: ")
                    isbn_check = library.validateISBN()
                    option = "isbn"
                    library.updateContents(option, library.isbn)

            elif edit_selection == "4":   
                copies_check = False
                while copies_check == False: 
                    library.num_copies_purchased = input("What would you like to change the number of purchased copies to?: ")
                    copies_check = library.validateNumCopies()
                    option = "num_copies_purchased"
                    library.updateContents(option, library.num_copies_purchased)

            elif edit_selection == "5":   
                copies_checked_check = False
                while copies_checked_check == False: 
                    library.num_copies_checked = input("What would you like to change the number of checked out copies to?: ")
                    copies_checked_check = library.validateNumCopiesChecked2()
                    option = "num_copies_checked"
                    library.updateContents(option, library.num_copies_checked)

            elif edit_selection == "6": 
                retail_price_check = False
                while retail_price_check == False: 
                    library.retail_price = input("What would you like to change the retail price to?: ")
                    retail_price_check = library.validateRetailPrice()
                    option = "retail_price"
                    library.updateContents(option, library.retail_price)

            continue_prompt = input("Do you wish to continue making changes to this book: Y/N ")
            if continue_prompt.lower() == "y":
                editing = True

            elif continue_prompt.lower() == "n":
                editing = False
                save_add = input("Do you wish to save your updates to the database? Y/N: ")
                if save_add.lower() == "y":
                    editing = False
                    library.commitChanges()
                    
                elif save_add.lower() == "n":
                    print("Discarding changes and returning to main menu...")
                    editing = False
                    program_run = True
                
                else:
                    print("You have entered an invalid response. Please answer (Y)es or (N)o.")
                
            else:
                print("You have entered an invalid response. Please answer (Y)es or (N)o.")
    
    elif selection == '4':
        delete_book_check = False
        while delete_book_check == False:
            library.currentList()
            library.number = input("Please enter the number next to the book you wish to remove: ")
            delete_book_check = library.removeBook()
            program_run = True

    elif selection == '5':
        print("Terminating Program...")
        program_run = False
    
    else:
        print("You have chosen an invalid option or entered an incorrect value. Please try again.")
        program_run = True