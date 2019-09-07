## Week 9 - Functions Assignment
## IT 410 - Walsh College
## 06/03/2019
## BROHL, STEVEN


def emp_id(employee_id):
    ## Declaring a Flag to control a while loop
    employee_id_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_id_ok:
        ## Asking for an ID (int) and checking if int not > 7
        if employee_id.isdigit():
            if len(employee_id) <= 7:
                employee_id_ok = True
            else:
                employee_id_ok = False
                return True
        else:
            employee_id_ok = False
            return False
    return employee_id 


def emp_name(employee_name):
    ## Declaring a Flag to control a while loop
    employee_name_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_name_ok:
        ## Declaring a list of characters that are not allowed in employee address
        bad_chars = ["!", "\"", "@","#", "$", "%", "^", "&", "*","(",")" "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        ## Asking for a name and checking if it has any defined bad characters
        if employee_name:
            ## Checking employee name for bad characters
            for char in employee_name:
                ## If bad characters are found, exit the program
                if char in bad_chars or char.isdigit() or employee_name.isspace():
                    employee_name_ok = False
                    return False
                else:
                    employee_name_ok = True
        ## if no input is provided exit the program
        else:
            employee_name_ok = False
            return False
    return employee_name


def emp_email(employee_email_address):
    ## Declaring a Flag to control a while loop
    employee_email_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_email_ok:
        ## Declaring a list of characters that are not allowed in employee email address
        bad_chars = ["!", "\"", "#", "$", "%", "^", "&", "*","(", ")", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        if employee_email_address:
            ## Checking employee email address for bad characters
            for char in employee_email_address:
                ## If bad characters are found, exit the program
                if char in bad_chars or char.isspace():
                    employee_email_ok = False
                    return False

                else:
                    employee_email_ok = True
        ## if no input is provided exit the program
        else:
            employee_email_ok = False
            return False
    return employee_email_address
    


def emp_address(employee_address):
    ## Declaring a Flag to control a while loop
    employee_address_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_address_ok:
        ## Declaring a list of characters that are not allowed in employee address
        bad_chars = ["!", "\"", "@", "$", "%", "^", "&", "*", "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        if employee_address:
            ## Checking employee address for bad characters
            for char in employee_address:
                ## If bad characters are found, exit the program
                if char in bad_chars:
                    employee_address_ok = False
                    break
                ## Else, add the address to a new employee_address variable
                else:
                    address = "Your address is " + employee_address + "."
                    employee_address_ok = True
        ## If no input is provided
        else:
            address = "You did not provide an address."
            employee_address_ok = True
    return(address, employee_address)


## Declaring an empty list to fill up with employee information from my functions
entries = []
program = 0
while program < 5:
    ## Storing the results of each function in a variable
    id_check = False
    while id_check == False: 
        id_check = emp_id(employee_id = input("\nPlease enter your Employee ID number: "))
    
    name_check = False
    while name_check == False:
        name_check = emp_name(employee_name = input("Please enter your name: "))
    
    email_check = False
    while email_check == False:
        email_check = emp_email(employee_email_address = input("Please enter your email address: "))
    
    address_check = False
    while address_check == False:
        ## This variable holds a tuple with two different values
        address_check = emp_address(employee_address = input("Please enter your address: "))
    
    ## Appending each entry to a list
    entries.append({"number": id_check, "name": name_check, "email": email_check, "address": address_check[1]})
    ## Printing out my results using the variables created above
    print("Hello, " + name_check.title() + ". Your Employee ID is " + id_check + ", and your Email address is " + email_check + ". " + address_check[0])     

    ## Incrementing my count variable each loop by 1
    program += 1


## printing my entries list after the main function loop ends
print("\n Employee Entries List:",entries)