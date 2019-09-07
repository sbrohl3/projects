## Week 8 - While Loops Assignment
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN

## Declaring list to store entries
entries = []

## Delcaring count variable to control program while loop
program = 0

## A while loop to stop the program after 5 entries
while program < 5:
    ## Declaring a Flag to control a while loop
    employee_id_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_id_ok:
        ## Asking for an ID (int) and checking if int not > 7
        employee_id = input("\nPlease enter your Employee ID number: ")
        if employee_id.isdigit():
            if len(employee_id) <= 7:
                employee_id_ok = True
            else:
                employee_id_ok = False
        else:
            employee_id_ok = False

    ## Declaring a Flag to control a while loop
    employee_name_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_name_ok:
        ## Declaring a list of characters that are not allowed in employee address
        bad_chars = ["!", "\"", "@","#", "$", "%", "^", "&", "*","(",")" "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        ## Asking for a name and checking if it has any defined bad characters
        employee_name = input("Please enter your name: ")
        if employee_name:
            ## Checking employee name for bad characters
            for char in employee_name:
                ## If bad characters are found, exit the program
                if char in bad_chars or char.isdigit():
                    employee_name_ok = False
                    break
                else:
                    employee_name_ok = True
        ## if no input is provided exit the program
        else:
            employee_name_ok = False


    ## Declaring a Flag to control a while loop
    employee_email_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_email_ok:
        ## Declaring a list of characters that are not allowed in employee email address
        bad_chars = ["!", "\"", "#", "$", "%", "^", "&", "*","(", ")", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        employee_email_address = input("Please enter your email address: ")
        if employee_email_address:
            ## Checking employee email address for bad characters
            for char in employee_email_address:
                ## If bad characters are found, exit the program
                if char in bad_chars:
                    employee_email_ok = False
                else:
                    employee_email_ok = True
        ## if no input is provided exit the program
        else:
            employee_email_ok = False


    ## Declaring a Flag to control a while loop
    employee_address_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_address_ok:
        ## Declaring a list of characters that are not allowed in employee address
        bad_chars = ["!", "\"", "@", "$", "%", "^", "&", "*", "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        employee_address = input("Please enter your address: ")
        if employee_address:
            ## Checking employee address for bad characters
            for char in employee_address:
                ## If bad characters are found, exit the program
                if char in bad_chars:
                    employee_address_ok = False
                ## Else, add the address to a new employee_address variable
                else:
                    address = "Your address is " + employee_address + "."
                    employee_address_ok = True
                    break
        ## If no input is provided
        else:
            address = "You did not provide an address."
            employee_address_ok = True

    ## Printing out my results
    print("Hello, " + employee_name.title() + ". Your Employee ID is " + employee_id + ", and your Email address is " + employee_email_address + ". " + address)     
    ## Appending each entry to a list
    entries.append({"number": employee_id, "name": employee_name, "email": employee_email_address, "address": employee_address})
    ## Incrementing my count variable each loop by 1
    program += 1         

## Print the list of entries
print("\nList of Employees:\n", entries)
