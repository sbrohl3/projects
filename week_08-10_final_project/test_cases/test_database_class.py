import unittest
from classes.database import Database

class TestDatabaseClass(unittest.TestCase):
    """A Class to test the Database class's Validator"""

    def setUp(self):
        """An instance of the Library class for testing all the other class functions"""
        self.database = Database()

    def test_invalid_address(self):
        """Here are some invalid address checks I know will validate to False"""

        invalid_addresses_to_test = ["1234! fourth street @@", "APT# 32@1 E. Pe/nnsylvani&a Avenue", "14&21] Ammonia @venue! ", " ", "!2& Pet* P$ace", "4!% Pr0gr@mm!ng ln.", " 2!45_ C}loudy s;t."]

        for address in invalid_addresses_to_test:
            self.database.address = address
            self.assertFalse(self.database.validate_address())

    def test_valid_address(self):
        """Here are some address checks I know will validate to True"""

        valid_addresses_to_test = ["1234 fourth street", "APT# 321 E. Pennsylvania Avenue", "1421 Ammonia Avenue", "123 Petz Place", "412 Programming ln.", " 2145 Cloudy st."]
        
        for address in valid_addresses_to_test:
            self.database.address = address
            self.assertTrue(self.database.validate_address())

    def test_invalid_city(self):
        """Here are some invalid city checks I know will validate to False"""

        invalid_cities_to_test = [" Rosevill3 ", "W@rr3n", "St. Cl@!r Sh0r3s", " ", "_Tr0y", " W3st Br@nch", " !D3tr0!t"]
        option = "city"

        for city in invalid_cities_to_test:
            self.database.city = city
            self.assertFalse(self.database.validate_cityInfo(option, self.database.city))

    def test_valid_city(self):
        """Here are some valid city checks I know will validate to True"""

        valid_cities_to_test = ["Roseville", "Warren", "St Clair Shores", "Troy", "West Branch", "Detroit"]
        option = "city"

        for city in valid_cities_to_test:
            self.database.city = city
            self.assertTrue(self.database.validate_cityInfo(option, self.database.city))
    
    def test_invalid_county(self):
        """Here are some invalid county checks I know will validate to False"""

        invalid_county_to_test = ["M@c0mb", " S@g!n@w!^^", " Cl!nt0n", " ", " Cl@r3_-!", " 0@kl@nd ", " W@yn3&"]
        option = "county"

        for county in invalid_county_to_test:
            self.database.county = county
            self.assertFalse(self.database.validate_cityInfo(option, self.database.county))

    def test_valid_county(self):
        """Here are some valid county checks I know will validate to True"""

        valid_county_to_test = ["Macomb", "Saginaw", " Clinton", "Gratiot", "Ogemaw", "Huron", "Gladwin"]
        option = "county"

        for county in valid_county_to_test:
            self.database.county = county
            self.assertTrue(self.database.validate_cityInfo(option, self.database.county))

    def test_invalid_email_address(self):
        """Here are some invalid email address checks I know will validate to False"""

        invalid_email_addresses_to_test = ["!!phony#@phony.com", "steven!Ralf94@yahoocom( ", "$t3venr@lf94@gmail.com", " ", "&br0hl!@gmail.com ", " st!venralf_@gmail.com ", " Cl0udN!n3@f@k3mail.com"]

        for address in invalid_email_addresses_to_test:
            self.database.email_address = address
            self.assertFalse(self.database.validate_emailAddress())

    def test_valid_email_address(self):
        """Here are some email address checks I know will validate to True"""

        valid_email_addresses_to_test = ["phony@phony.com", "stevenralf94@gmail.com", "sbrohl2@academic.walshcollege.edu", "stevenralf94@yahoo.com", "borisgrishenko@gmail.com", "cloudnine@cloudmail.net"]
        
        for address in valid_email_addresses_to_test:
            self.database.email_address = address
            self.assertTrue(self.database.validate_emailAddress())

    def test_invalid_first_name(self):
        """Here are some invalid first name checks I know will validate to False"""

        invalid_name_to_test = ["!St3v3n", " T0m", " ", " N!ck", "@rthur", "Ry@n", "S@! ", "D@v3"]
        option = "first name"

        for name in invalid_name_to_test:
            self.database.first_name = name
            self.assertFalse(self.database.validate_NamePart(option, self.database.first_name))

    
    def test_valid_first_name(self):
        """Here are some valid first name checks I know will validate to True"""

        valid_name_to_test = ["Steven", "Tom", "Nick", "Arthur", "Ryan", "Sai", "Dave"]
        option = "first name"

        for name in valid_name_to_test:
            self.database.first_name = name
            self.assertTrue(self.database.validate_NamePart(option, self.database.first_name))


    def test_invalid_last_name(self):
        """Here are some invalid last name checks I know will validate to False"""

        invalid_name_to_test = ["Brohl", "Petz", "Vaillancourt", "Gibson", "Thomas", "Zaman", "Schippers"]
        option = "last name"

        for name in invalid_name_to_test:
            self.database.last_name = name
            self.assertFalse(self.database.validate_NamePart(option, self.database.last_name))

    
    def test_valid_last_name(self):
        """Here are some valid last name checks I know will validate to True"""

        valid_name_to_test = ["Brohl", "Petz", "Vaillancourt", "Gibson", "Thomas", "Zaman", "Schippers"]
        option = "last name"

        for name in valid_name_to_test:
            self.database.last_name = name
            self.assertTrue(self.database.validate_NamePart(option, self.database.last_name))


    
 

## python -m unittest test_cases.test_database_class


    
    
    
    
    
            
           
            
