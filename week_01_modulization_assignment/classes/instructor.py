from classes.person import Person

class Instructor(Person):
    """A simple Instructor class"""

    def __init__(self, IDnum=0, name='', email='', last_institution='', highest_degree=''):
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
        
   