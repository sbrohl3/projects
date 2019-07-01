## Week01 - Modularization Assingment
## 06/30/2019
## Brohl, Steven

## Week 9 - Functions Assignment
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




## Week 10 - Classes Assignment (Modified)
## IT 410 - Walsh College
## 07/01/2019
## BROHL, STEVEN

class Validator():
    """A class for input validation"""
        
    def __init__(self, IDnum=0, name='', email='', program_of_study='', last_institution='', highest_degree=''):
        self.IDnum = IDnum
        self.name = name
        self.email = email
        self.program_of_study = program_of_study
        self.last_institution = last_institution
        self.highest_degree = highest_degree


    def validateEmail(self):
        ## Declaring a Flag to control a while loop
        email_addresses_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not email_addresses_ok:
            ## Declaring a list of characters that are not allowed in employee email address
            bad_chars = ["!", "\"", "#", "$", "%", "^", "&", "*","(", ")", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
            if self.email:
                ## Checking employee email address for bad characters
                for char in self.email:
                    ## If bad characters are found, exit the program
                    if char in bad_chars or char.isspace():
                        self.email = input("What is your email: ")
                        email_addresses_ok = False 
                        
                    else:
                        email_addresses_ok = True
            ## if no input is provided re-prompt
            else:
                self.email = input("What is your email: ")
                

    def validateHighestDegree(self):
        ## Declaring a Flag to control a while loop
        degree_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not degree_check_ok:
            ## Asking for an ID (int) and checking if int not > 5
            if self.highest_degree.isalpha():
                degree_check_ok = True

            else:
                self.highest_degree = input("What is the highest degree you earned:  ")
                

    def validateInstructorID(self):
        ## Declaring a Flag to control a while loop
        instructor_id_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not instructor_id_ok:
            ## Asking for an ID (int) and checking if int not > 7
            if self.IDnum.isdigit():
                if len(self.IDnum) <= 5:
                    instructor_id_ok = True
                else:
                    self.IDnum = input("What is your Instructor ID: ")
                    
            else:
                self.IDnum = input("What is your Instructor ID: ")
                

    def validateInstitution(self):
        ## Declaring a Flag to control a while loop
        institution_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not institution_check_ok:
            ## Asking for an ID (int) and checking if int not > 5
            if self.last_institution.isalpha():
                institution_check_ok = True
    
            else:
                self.last_institution = input("What is the last institution you graduated from: ")
                
   
    def validateName(self):
        ## Declaring a Flag to control a while loop
        name_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not name_ok:
            ## Declaring a list of characters that are not allowed in employee address
            bad_chars = ["!", "\"", "@","#", "$", "%", "^", "&", "*","(",")" "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
            ## Asking for a name and checking if it has any defined bad characters
            if self.name:
                ## Checking employee name for bad characters
                for char in self.name:
                    ## If bad characters are found, exit the program
                    if char in bad_chars or char.isdigit() or self.name.isspace():
                        self.name = input("What is your name: ")
                        name_ok = False
                        
                    else:
                        name_ok = True
            ## if no input is provided re-prompt
            else:
                self.name = input("What is your name: ")
                
                

    def validateProgram(self):
        ## Declaring a Flag to control a while loop
        program_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not program_check_ok:
            ## Asking for an ID (int) and checking if int not > 5
            if self.program_of_study.isalpha():
                program_check_ok = True
    
            else:
                self.program_of_study = input("What is your program of study: ")
                

    def validateStudentID(self):
        ## Declaring a Flag to control a while loop
        student_id_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not student_id_ok:
            ## Asking for an ID (int) and checking if int not > 7
            if self.IDnum.isdigit():
                if len(self.IDnum) <= 7:
                    student_id_ok = True
                else:
                    self.IDnum = input("What is your Student ID: ")
                    
            else:
                self.IDnum = input("What is your Student ID: ")
                

class Person(Validator):
  """A simple person class"""

  def __init__(self, name, email):
      super().__init__(IDnum, name, email)
      self.name = name
      self.email = email


class Student(Person):
    """A simple Student class"""

    def __init__(self, IDnum=0, name='', email='', program_of_study='', college_records=[]):
        self.college_records = college_records
        self.IDnum = IDnum
        self.name = name
        self.email = email
        self.program_of_study = program_of_study

    def displayInformation(self):
        print("\nStudent Information: ")
        print("Student ID: " + self.IDnum)
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("Program of Study: " + self.program_of_study)
        self.college_records.append([self.IDnum, self.name, self.email, self.program_of_study])


class Instructor(Person):
    """A simple Instructor class"""

    def __init__(self, IDnum=0, name='', email='', last_institution='', highest_degree='', college_records=[]):
        self.college_records = college_records
        self.IDnum = IDnum
        self.name = name
        self.email = email
        self.last_institution = last_institution
        self.highest_degree = highest_degree

    def displayInformation(self):
        print("\nInstructor Information: ")
        print("Instructor ID: " , self.IDnum)
        print("Name:" + self.name)
        print("Email: " + self.email)
        print("Last Institution Attended: " + self.last_institution)
        print("Highest degree obtained: " + self.highest_degree)
        self.college_records.append([self.IDnum, self.name, self.email, self.last_institution, self.highest_degree])
        



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
        student.IDnum = input("What is your Student ID: ")
        student.validateStudentID()
        student.name = input("What is your name: ")
        student.validateName()
        student.email = input("What is your email: ")
        student.validateEmail()
        student.program_of_study = input("What is your program of study: ")
        student.validateProgram()
        student.displayInformation()
   
          

    ## If the user is an Instructor the Instructor class will be called to ask for their information   
    elif person_type.upper() == "I":
        instructor = Instructor() 
        instructor.IDnum = input("What is your Instructor ID: ")
        instructor.validateInstructorID()
        instructor.email = input("What is your email: ")
        instructor.validateEmail()
        instructor.last_institution = input("What is the last institution you graduated from: ")
        instructor.validateInstitution()
        instructor.highest_degree = input("What is the highest degree you earned: ")
        instructor.validateHighestDegree()
        instructor.displayInformation()
       

    ## If the user enters Q, then the program will exit   
    elif person_type.upper() == "Q":
        program = False

    else:
        exit_program = input("Incorrect Input provided! Do you want to quit? Y/N: ")
        if exit_program.upper() == "Y":
            program = False

print("COLLEGE RECORDS: ")
print(student.college_records)
print(instructor.college_records)