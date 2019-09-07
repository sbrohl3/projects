## Week 10 - Classes Assignment 
## IT 410 - Walsh College
## 06/11/2019
## BROHL, STEVEN

class Validator():
    """A class for input validation"""

    ## Using default constructor created by Python 

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
                email_addresses_ok = False

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
                degree_check_ok = False

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
                    instructor_id_ok = False
            else:
                self.IDnum = input("What is your Instructor ID: ")
                instructor_id_ok = False

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
                institution_check_ok = False
   
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
                name_ok = False

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
                program_check_ok = False

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
                    student_id_ok = False
            else:
                self.IDnum = input("What is your Student ID: ")
                student_id_ok = False
            
class Instructor(Validator):
    """A simple Instructor class"""
    
    def __init__(self):
        self.IDnum = input("What is your Instructor ID: ")
        self.validateInstructorID()
        self.name = input("What is your name: ")
        self.validateName()
        self.email = input("What is your email: ")
        self.validateEmail()
        self.last_institution = input("What is the last institution you graduated from: ")
        self.validateInstitution()
        self.highest_degree = input("What is the highest degree you earned: ")
        self.validateHighestDegree()
        college_records.append({"instructorID": self.IDnum, "name": self.name,"email": self.email, "last_institution": self.last_institution, "highest_degree": self.highest_degree})
        self.displayInformation()

    def displayInformation(self):
        print("\nInstructor Information: ")
        print("Instructor ID: " + self.IDnum)
        print("Name:" + self.name)
        print("Email: " + self.email)
        print("Last Institution Attended: " + self.last_institution)
        print("Highest degree obtained: " + self.highest_degree)


class Student(Validator):
    """A simple Student class"""

    def __init__(self):
        self.IDnum = input("What is your Student ID: ")
        self.validateStudentID()
        self.name = input("What is your name: ")
        self.validateName()
        self.email = input("What is your email: ")
        self.validateEmail()
        self.program_of_study = input("What is your program of study: ")
        self.validateProgram()
        college_records.append({"studentID": self.IDnum, "name": self.name,"email": self.email, "program_of_study": self.program_of_study})
        self.displayInformation()

    def displayInformation(self):
        print("\nStudent Information: ")
        print("Student ID: " + self.IDnum)
        print("Name: " + self.name)
        print("Email: " + self.email)
        print("Program of Study: " + self.program_of_study)

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
        Student()

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
