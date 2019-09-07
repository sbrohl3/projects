## Week 8 - User Input Assignment
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN

## Asking for an ID (int) and checking if int not > 7
employee_id = input("Please enter your Employee ID number: ")
if employee_id.isdigit():
    ## If employee ID passes all checks its value is carried to the final output
    try:
        if len(employee_id) > 7:
            exit()
    except:
        exit()
else:
    exit()

## Declaring a list of characters that are not allowed in employee address
bad_chars = ["!", "\"", "@","#", "$", "%", "^", "&", "*","(",")" "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
## Asking for a name and checking if it has any defined bad characters
employee_name = input("Please enter your name: ")
if employee_name:
    ## Checking employee name for bad characters
    for char in employee_name:
        ## If bad characters are found, exit the program
        if char in bad_chars or char.isdigit():
            exit()
## if no input is provided exit the program
else:
    exit()

## Declaring a list of characters that are not allowed in employee email address
bad_chars = ["!", "\"", "#", "$", "%", "^", "&", "*","(", ")", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
employee_email_address = input("Please enter your email address: ")
if employee_email_address:
    ## Checking employee email address for bad characters
    for char in employee_email_address:
        ## If bad characters are found, exit the program
        if char in bad_chars:
            exit()
## if no input is provided exit the program
else:
    exit()

## Declaring a list of characters that are not allowed in employee address
bad_chars = ["!", "\"", "@", "$", "%", "^", "&", "*", "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
employee_address = input("Please enter your address: ")
if employee_address:
    ## Checking employee address for bad characters
    for char in employee_address:
        ## If bad characters are found, exit the program
        if char in bad_chars:
            exit()
        ## Else, add the address to a new employee_address variable
        else:
            employee_address = "Your address is " + employee_address + "."
            break
## If no input is provided
else:
    employee_address = "You did not provide an address."

## Printing out my results
print("Hello, " + employee_name.title() + ". Your Employee ID is " + employee_id + ", and your Email address is " + employee_email_address + ". " + employee_address)     
               
