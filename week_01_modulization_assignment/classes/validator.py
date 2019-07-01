class Validator():
    """A class for input validation"""

    def __init__(self):
        self.IDnum = IDnum
        self.name = name
        self.email = email
        self.highest_degree = highest_degree
        self.last_institution = last_institution
        self.program_of_study = program_of_study

    def validateEmail():
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