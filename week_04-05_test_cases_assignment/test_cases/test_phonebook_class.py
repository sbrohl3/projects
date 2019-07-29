import unittest
from classes.phonebook import Phonebook

class TestPhoneBookClass(unittest.TestCase):
    """Test the PhoneBook Class"""

    def setUp(self):
        """Create an instance of the Pizza class for testing all class functions"""
        self.phone_book = Phonebook()

    def test_valid_first_name(self):
        """Here are some name checks I know will validate"""
        valid_names_to_test = ["Steven", "steven", "STEVEN", "StEvEn", "sTeVeN", "STEven"]
        
        for name in valid_names_to_test:
            self.assertTrue(self.phone_book.validateNamePart(name))

    def test_invalid_first_name(self):
        """Here are some name checks I know will not validate"""
        invalid_names_to_test = ["123Steven", " steven", "!@11STEVEN", " StEvEn123", "sTeVeN 123", "STEven!234"]
        
        for name in invalid_names_to_test:
            self.assertFalse(self.phone_book.validateNamePart(name))

    def test_valid_last_name(self):
        """Here are some last name checks I know will validate"""
        valid_names_to_test = ["Brohl", "brohl", "BROHL", "BrOhL", "bROhL", "BROhl"]
        
        for name in valid_names_to_test:
            self.assertTrue(self.phone_book.validateNamePart(name))

    def test_invalid_last_name(self):
        """Here are some last name checks I know will not validate"""
        invalid_names_to_test = ["Brohl ", " brohl", " BROHL ", "123BrOhL", "12!bROhL", "#!@123BROhl"]
        
        for name in invalid_names_to_test:
            self.assertFalse(self.phone_book.validateNamePart(name))

    def test_valid_phone_number(self):
        """Here are some phone number checks I know will validate"""
        valid_numbers_to_test = ["5864431259", "5867712848", "5861234567", "8007511563", "5551432565", "3135256525"]
        
        for number in valid_numbers_to_test:
            self.phone_book.phone_number = number
            self.assertTrue(self.phone_book.validatePhoneNumber())

    def test_invalid_phone_number(self):
        """Here are some phone number checks I know will not validate"""
        invalid_numbers_to_test = ["586", "586771", "586abcde", "abcde123456", "5551432565856", "@31352565251aa!"]
        
        for number in invalid_numbers_to_test:
            self.phone_book.phone_number = number
            self.assertFalse(self.phone_book.validatePhoneNumber())

    def test_valid_phone_number_type(self):
        """Here are some phone number type checks I know will validate"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list
            self.assertIn(number_type, self.phone_book.valid_phone_number_types)
            
    def test_valid_phone_number_type2(self):
        """Here are some phone number type checks I know will validate"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list and evaluates to True
            self.assertTrue(self.phone_book.validatePhoneNumberType())
            
    def test_invalid_phone_number_type(self):
        """Here are some phone number type checks I know will not validate"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not matche one in the valid list
            self.assertNotIn(number_type, self.phone_book.valid_phone_number_types)

    def test_invalid_phone_number_type2(self):
        """Here are some phone number type checks I know will not validate"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not matche one in the valid list and evaluates to False
            self.assertFalse(self.phone_book.validatePhoneNumberType())
            
            
            
            

            
            
            
           
            
