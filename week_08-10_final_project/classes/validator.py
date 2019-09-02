
class Validator():
    """A class representing a validator"""

    def __init__(self, first_name=" ", last_name=" ", company_name=" ", address=" ", city=" ", county=" ", state_code=" ", zip_code=0, phone_number=" ", phone_number_2=" ", email_address=" "):
        """A constructor for the validator Class"""
        self.first_name = first_name
        self.last_name = last_name
        self.company_name = company_name
        self.crm_company_name = ""
        self.address = address
        self.city = city
        self.county = county
        self.state_code = state_code
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.phone_number_2 = phone_number_2
        self.email_address = email_address

    def validate_address(self):
        """A method to validate a user's inputted email address"""

        ## Declaring a list of characters that are not allowed in the user's address
        bad_chars = ["!", "\"", "\'", "@", "$", "%", "^", "&","*", "_", "=", "+", "<",">", "?", ";", "[", "]", "{", "}"]
        if self.address.rstrip():
            ## Checking the user's address for bad characters
            for char in self.address:
                ## If bad characters are found re-prompt
                if char in bad_chars:
                    print("You have provided an invalid address. Please check your formatting and try again.")
                    return False
                        
                else:
                    address_valid = True

            if address_valid == True:
                print("The inputted address is: " + "\"" + self.address.title()+ "\".")
                return True

        ## if no input is provided re-prompt
        else:
            print("You have not provided an address. Please try again.")
            return False
        

    def validate_cityInfo(self, option, passed_info):
        """A method to validate a user's city and county"""

        good_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", "\'", " "]
        if passed_info.rstrip():
            for char in passed_info.lower():
                if char in good_characters:
                    info_valid = True

                else:
                    print("You have entered an invalid character. Please try again.")
                    return False

            if info_valid == True:
                print("The inputted " + option + " name is: " + "\"" + passed_info.title() + "\".")
                return True
        else:
            print("Invalid entry. Please try again.")
            return False

    def validate_companyName(self):
        """A method to validate a user's inputted company name"""

        if self.company_name.rstrip() and self.company_name.upper().rstrip() != "N/A":
            print("The inputted company name is: " + "\"" + self.company_name.title() + "\".")
            self.crm_company_name = self.company_name.title()
            return True

        elif self.company_name.upper().rstrip() == "N/A":
            print("The inputted company name is: " + "\"" + self.company_name.upper() + "\".")
            self.crm_company_name = ""
            return True
            
        ## if no input is provided re-prompt
        else:
            print("\nYou have not entered a company name. Please Try again.")
            return False

    def validate_emailAddress(self):
        """A method to validate a user's inputted email address"""

        ## Declaring a list of characters that are not allowed in the user's email address
        bad_chars = ["!", "\"", "#", "$", "%", "^", "&", "*","(", ")", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        if self.email_address:
            ## Checking email address for bad characters
            for char in self.email_address:
                ## If bad characters are found re-prompt
                if char in bad_chars or char.isspace() or "@" not in self.email_address or "." not in self.email_address:
                    print("You have provided an invalid email address. Please check your formatting and try again.")
                    return False
                        
                else:
                    email_valid = True

            if email_valid == True:
                print("The inputted email is: " + "\"" + self.email_address + "\".")
                return True

        ## if no input is provided re-prompt
        else:
            print("You have not provided an email address. Please try again.")
            return False

    def validate_NamePart(self, option, passed_name):
        """A method to validate a user's inputted first and last name"""

        good_characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "-", "\'"]
        if passed_name.rstrip():
            for char in passed_name.lower():
                if char in good_characters:
                    name_valid = True

                else:
                    print("You have entered an invalid character. Please try again.")
                    return False

            if name_valid == True:
                print("The inputted " + option + " is: " + "\"" + passed_name.title() + "\".")
                return True

        else:
            print("Invalid entry. Please try again.")
            return False
            
    def validate_phoneNumber(self, option, phone_number_part):
        """A method to validate a user's inputted phone number"""

        ## Need to add in an option to allow blank secondary phone number if data going to CRM database!!!!

        ## A list of acceptable characters for the phone number
        number_check = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]
        if phone_number_part:
            for num in phone_number_part:
                if num in number_check and len(phone_number_part) == 12 and "-" == phone_number_part[3] and "-" == phone_number_part[7]:
                    phone_valid = True
                
                else:
                    print("Please enter a 10 digit phone number including \"-\" in their correct locations.")
                    return False

            if phone_valid == True:
                print("The inputted " + option + " phone number is: " + "\"" + phone_number_part + "\".")
                return True
                
        elif not phone_number_part and option == "secondary":
            print("No secondary phone number has been input. Skipping entry.")
            return True
        
        else:
            print("You have enetered an invalid phone number. Please try again.")
            return False

    def validate_State(self):
        """A method to validate a user's inputted State Code"""

        ## Taking in a user's state code and checking to verify it contains no illegal characters
        valid_states = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY", "AS", "DC", "FM", "GU", "MH", "MP", "PW", "PR", "VI"]
        if self.state_code.isalpha():
            if self.state_code.upper() in valid_states and len(self.state_code) == 2:
                print("The inputted state code is: " + "\"" + self.state_code.upper() + "\".")
                return True

            else:
                print("The state code you have entered is either not of valid length or is not an acceptable abbreviation for the state you provided. A state abbreviation must be two characters only (example: MI). Please try again.")
                return False
     
        else:
            print("Your inputted state code contains an invalid character(s). Please try again.")
            return False
                

    def validate_zipCode(self):
        """A method to validate a user's inputted Zip Code"""

        ## Taking in a user's zip code (int) and checking if it is equal in length to 4 or 5
        if self.zip_code.isdigit():
            if len(self.zip_code) == 4 or len(self.zip_code) == 5:
                print("The inputted zip code is: " + "\"" + str(self.zip_code) + "\".")
                return True

            else:
                print("The zip code you have entered is not of valid length. Please try again. ")
                return False
                
        else:
            print("You have not input a valid zip code. Please try again.")
            return False
                

