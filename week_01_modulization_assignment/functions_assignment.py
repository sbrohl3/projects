## Week 9 - Modularization Assingment - Functions 
## IT 410 - Walsh College
## 06/30/2019
## BROHL, STEVEN

##Importing the validation functions
from functions.validation import *

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
