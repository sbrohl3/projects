## Week 10 - Modularization Assingment - Classes
## IT 410 - Walsh College
## 07/01/2019
## BROHL, STEVEN

## Import the Student and Instructor classes from the Student and Instructor Module
from classes.student import Student
from classes.instructor import Instructor

## Declaring the empty list for storage of college records
college_records = []

## Declaring a variable to loop the program to keep it running 
program = True

## Loop for the main program
while program:
    ##Determining if the user is a student or instructor
    person_type = input("\nAre you a Student or an Instructor? Enter S or I, or Q to quit: ")
    ## If the user is a Student the Student class will be called to ask for their information 
    if person_type.upper() == "S":
        
        student = Student()
        
        ## A loop that takes only valid user input for the Student's ID and then appends it to a list
        id_check = False
        while id_check == False: 
            student.IDnum = input("What is your Student ID: ")
            id_check = student.validateStudentID()
        
        ## A loop that takes only valid user input for the Student's name and then appends it to a list
        name_check = False
        while name_check == False: 
            student.name = input("What is your name: ")
            name_check = student.validateName()

        ## A loop that takes only valid user input for the Student's email and then appends it to a list
        email_check = False
        while email_check == False: 
            student.email = input("What is your email: ")
            email_check = student.validateEmail()
        
        ## A loop that takes only valid user input for the Student's program of study and then appends it to a list
        program_check = False
        while program_check == False: 
            student.program_of_study = input("What is your program of study: ")
            program_check = student.validateProgram()
        
        ## Display Student Information
        student.displayInformation()
        college_records.append(student)
   
          

    ## If the user is an Instructor the Instructor class will be called to ask for their information   
    elif person_type.upper() == "I":

        ## The instructor class is assigned to a variable and is used to feed in and validate user input below
        instructor = Instructor() 

        ## A loop that takes only valid user input for the Instructor's ID and then appends it to a list
        id_check = False
        while id_check == False: 
            instructor.IDnum = input("What is your Instructor ID: ")
            id_check = instructor.validateInstructorID()
        
        ## A loop that takes only valid user input for the Instructor's name and then appends it to a list
        name_check = False
        while name_check == False: 
            instructor.name = input("What is your name: ")
            name_check = instructor.validateName()

        ## A loop that takes only valid user input for the Instructor's email and then appends it to a list
        email_check = False
        while email_check == False: 
            instructor.email = input("What is your email: ")
            email_check = instructor.validateEmail()

        ## A loop that takes only valid user input for the Instructor's last institution graduated and then appends it to a list
        institution_check = False
        while institution_check == False: 
            instructor.last_institution = input("What is the last institution you graduated from: ")
            institution_check = instructor.validateInstitution()
        
        ## A loop that takes only valid user input for the Instructor's highest degree earned and then appends it to a list
        degree_check = False
        while degree_check == False: 
            instructor.highest_degree = input("What is the highest degree you earned: ")
            degree_check = instructor.validateHighestDegree()
        
        ## Display Instructor Information
        instructor.displayInformation()
        college_records.append(instructor)

    ## If the user enters Q, then the program will exit   
    elif person_type.upper() == "Q":
        program = False

    ## If any other incorrect input is inserted, the user will be prompted asking if they wish to exit the program
    else:
        exit_program = input("Incorrect Input provided! Do you want to quit? Y/N: ")
        if exit_program.upper() == "Y":
            program = False

## At the end of the program all college records will be printed
print("COLLEGE RECORDS: ")
print(college_records)