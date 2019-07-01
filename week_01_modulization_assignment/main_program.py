## Week01 - Modularization Assingment
## 06/30/2019
## Brohl, Steven

## Week 9 - Functions Assignment
## IT 410 - Walsh College
## 06/03/2019
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


















## Week 10 - Classes Assignment 
## IT 410 - Walsh College
## 06/11/2019
## BROHL, STEVEN


            




from classes.student import Student


## Declaring the empty list for storage of college records
college_records = []

## Declaring a variable to loop the program to keep it running 
program = True

## Loop for the main program
while program:
    student = Student()
    ##Determining if the user is a student or instructor
    person_type = input("\nAre you a Student or an Instructor? Enter S or I, or Q to quit: ")
    ## If the user is a Student the Student class will be called to ask for their information 
    if person_type.upper() == "S":
        student.IDnum = input("What is your Student ID: ")
        student.name = input("What is your name: ")
        student.email = input("What is your email: ")
        student.program_of_study = input("What is your program of study: ")

    ## If the user is an Instructor the Instructor class will be called to ask for their information   
    elif person_type.upper() == "I":
        Instructor()

    ## If the user enters Q, then the program will exit   
    elif person_type.upper() == "Q":
        program = False

    else:
        exit_program = input("Incorrect Input provided! Do you want to quit? Y/N: ")
        if exit_program.upper() == "Y":
            program = False

print("COLLEGE RECORDS: ")
print(college_records)
