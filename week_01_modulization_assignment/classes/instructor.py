from classes.person import Person

class Instructor(Person):
    """A simple Instructor class"""
    
    def __init__(self):
        self.IDnum = input("What is your Instructor ID: ")
        self.validateInstructorID()
        
        self.validateName()
        self.email = input("What is your email: ")
        self.validateEmail()
        self.last_institution = input("What is the last institution you graduated from: ")
        self.validateInstitution()
        self.highest_degree = input("What is the highest degree you earned: ")
        self.validateHighestDegree()
        college_records.append({self.IDnum, self.name, self.email, self.last_institution, self.highest_degree})
        self.displayInformation()

    def displayInformation(self):
        print("\nInstructor Information: ")
        print("Instructor ID: " + self.IDnum)
        print("Name:" + self.name)
        print("Email: " + self.email)
        print("Last Institution Attended: " + self.last_institution)
        print("Highest degree obtained: " + self.highest_degree)
