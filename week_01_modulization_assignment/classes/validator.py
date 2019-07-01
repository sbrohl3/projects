class Validator():
    """A class for input validation"""
        
    def __init__(self, IDnum=0, name='', email='', program_of_study='', last_institution='', highest_degree=''):
        ## A constructor for instantiating variables to be used in the validator class
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
                        email_addresses_ok = False
                        return False
                         
                        
                    else:
                        email_addresses_ok = True
            ## if no input is provided re-prompt
            else:
                return False
                

    def validateHighestDegree(self):
        ## Declaring a Flag to control a while loop
        degree_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not degree_check_ok:
            ## Asking for an ID (int) and checking if int not > 5
            if self.highest_degree.isalpha():
                degree_check_ok = True

            else:
                return False
            
                

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
                    return False
                    
            else:
                return False
                

    def validateInstitution(self):
        ## Declaring a Flag to control a while loop
        institution_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not institution_check_ok:
            ## Asking for an ID (int) and checking if int not > 5
            if self.last_institution.isalpha():
                institution_check_ok = True
    
            else:
                return False
                
   
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
                        name_ok = False
                        return False
                        
                        
                    else:
                        name_ok = True
            ## if no input is provided re-prompt
            else:
                return False
                
                

    def validateProgram(self):
        ## Declaring a Flag to control a while loop
        program_check_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not program_check_ok:
            ## Asking for an ID (int) and checking if int not > 5
            if self.program_of_study.isalpha():
                program_check_ok = True
    
            else:
                return False
                

    def validateStudentID(self):
        ## Declaring a Flag to control a while loop
        student_id_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not student_id_ok:
            ## Asking for an ID (int) and checking if int not > 7
            if self.IDnum.isdigit():
                if len(self.IDnum) <= 7:
                    student_id_ok = True
                    return True
                else:
                    student_id_ok = False
                    return False
                    
            else:
                return False