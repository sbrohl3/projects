class Phonebook():
    """"A class representing a phonebook"""

    def __init__(self, first_name=" ", last_name=" ", phone_number=0, phone_number_type=" "):
        """A constructor for the Phonebook Class"""
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.phone_number_type = phone_number_type
        self.valid_phone_number_types = ["home", "office", "cell"]
        self.contact_list = []

    def validateNamePart(self, passed_name):
        """Validates the first and last name"""
        ## Declaring a Flag to control a while loop
        name_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not name_ok:
            if passed_name.isalpha():
                name_ok = True

            else:
                print("You have entered an invalid character. Please try again.")
                return False

    def validatePhoneNumber(self):
        """Validates that the phone number is 10 digits"""
        ## Declaring a Flag to control a while loop
        phone_number_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not phone_number_ok:
            ## Asking for a phone number and checkig to see if it is 10 digits
            if self.phone_number.isdigit():
                if len(self.phone_number) == 10:
                    phone_number_ok = True
                    return True
                else:
                    print("Please Enter a 10 digit phone number.")
                    return False
                               
            else:
                print("You have enetered an invalid phone number. Please try again.")
                return False

    def validatePhoneNumberType(self):
        """Validates the phone number type as home, office, or cell"""
        ## Declaring a Flag to control a while loop
        phone_number_type_ok = False
        ## While loop to have user retry their input if they enter incorrectly
        while not phone_number_type_ok:
            if self.phone_number_type.lower() in self.valid_phone_number_types:
                phone_number_type_ok = True
                return True

            else:
                return False

    def format_data(self):
        """Appends all of the values after they have been validated"""
        self.contact_list.append({"Name": self.first_name + " " + self.last_name, "Phone Number": self.phone_number, "Phone Number Type": self.phone_number_type})

