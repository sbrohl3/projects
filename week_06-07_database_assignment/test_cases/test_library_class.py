import unittest
from classes.library import library

class TestLibraryClass(unittest.TestCase):
    """Test the library Class"""

    def setUp(self):
        """An instance of the Phonebook class for testing all the other class functions"""
        self.library = library()

    def test_valid_book_title(self):
        """Here are some book_title checks I know will validate to True"""
        valid_names_to_test = ["Steven", "steven", "STEVEN", "StEvEn", "sTeVeN", "STEven"]
        
        for name in valid_names_to_test:
            self.assertTrue(self.phone_book.validateNamePart(name))

    def test_invalid_book_title(self):
        """Here are some book_title checks I know will not validate to True"""
        invalid_names_to_test = ["123Steven", " steven", "!@11STEVEN", " StEvEn123", "sTeVeN 123", "STEven!234"]
        
        for name in invalid_names_to_test:
            self.assertFalse(self.phone_book.validateNamePart(name))

    def test_valid_Author(self):
        """Here are some last name checks I know will validate to True"""
        valid_names_to_test = ["Brohl", "brohl", "BROHL", "BrOhL", "bROhL", "BROhl"]
        
        for name in valid_names_to_test:
            self.assertTrue(self.phone_book.validateNamePart(name))

    def test_invalid_Author(self):
        """Here are some last name checks I know will not validate to True"""
        invalid_names_to_test = ["Brohl ", " brohl", " BROHL ", "123BrOhL", "12!bROhL", "#!@123BROhl"]
        
        for name in invalid_names_to_test:
            self.assertFalse(self.phone_book.validateNamePart(name))

    def test_valid_ISBN(self):
        """Here are some phone number checks I know will validate to True"""
        valid_numbers_to_test = ["5864431259", "5867712848", "5861234567", "8007511563", "5551432565", "3135256525"]
        
        for number in valid_numbers_to_test:
            self.phone_book.phone_number = number
            self.assertTrue(self.phone_book.validatePhoneNumber())

    def test_invalid_ISBN(self):
        """Here are some phone number checks I know will not validate to True"""
        invalid_numbers_to_test = ["586", "586771", "586abcde", "abcde123456", "5551432565856", "@31352565251aa!"]
        
        for number in invalid_numbers_to_test:
            self.phone_book.phone_number = number
            self.assertFalse(self.phone_book.validatePhoneNumber())

    def test_valid_copies_purchased(self):
        """Here are some phone number type checks I know will match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list
            self.assertIn(number_type, self.phone_book.valid_phone_number_types)
            
    def test_valid_copies_purchased_type2(self):
        """Here are some phone number type checks I know will validate to True"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to True
            self.assertTrue(self.phone_book.validatePhoneNumberType())
            
    def test_invalid_copies_purchased_type(self):
        """Here are some phone number type checks I know will not match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not match one in the valid list
            self.assertNotIn(number_type, self.phone_book.valid_phone_number_types)

    def test_invalid_copies_purchased_type2(self):
        """Here are some phone number type checks I know will not validate to True"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to false
            self.assertFalse(self.phone_book.validatePhoneNumberType())
    
    def test_valid_copies_checked(self):
        """Here are some phone number type checks I know will match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list
            self.assertIn(number_type, self.phone_book.valid_phone_number_types)
            
    def test_valid_copies_checked_type2(self):
        """Here are some phone number type checks I know will validate to True"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to True
            self.assertTrue(self.phone_book.validatePhoneNumberType())
            
    def test_invalid_copies_checked_type(self):
        """Here are some phone number type checks I know will not match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not match one in the valid list
            self.assertNotIn(number_type, self.phone_book.valid_phone_number_types)

    def test_invalid_copies_checked_type2(self):
        """Here are some phone number type checks I know will not validate to True"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to false
            self.assertFalse(self.phone_book.validatePhoneNumberType())
            
    def test_valid_retail_price(self):
        """Here are some phone number type checks I know will match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list
            self.assertIn(number_type, self.phone_book.valid_phone_number_types)
            
    def test_valid_retail_price_type2(self):
        """Here are some phone number type checks I know will validate to True"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to True
            self.assertTrue(self.phone_book.validatePhoneNumberType())
            
    def test_invalid_retail_price_type(self):
        """Here are some phone number type checks I know will not match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not match one in the valid list
            self.assertNotIn(number_type, self.phone_book.valid_phone_number_types)

    def test_invalid_retail_price_type2(self):
        """Here are some phone number type checks I know will not validate to True"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to false
            self.assertFalse(self.phone_book.validatePhoneNumberType())        


    def test_valid_add_book(self):
        """Here are some phone number type checks I know will match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list
            self.assertIn(number_type, self.phone_book.valid_phone_number_types)
            
    def test_valid_add_book_type2(self):
        """Here are some phone number type checks I know will validate to True"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to True
            self.assertTrue(self.phone_book.validatePhoneNumberType())
            
    def test_invalid_add_book_type(self):
        """Here are some phone number type checks I know will not match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not match one in the valid list
            self.assertNotIn(number_type, self.phone_book.valid_phone_number_types)

    def test_invalid_add_book_type2(self):
        """Here are some phone number type checks I know will not validate to True"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to false
            self.assertFalse(self.phone_book.validatePhoneNumberType())      
   
    def test_valid_edit_book(self):
        """Here are some phone number type checks I know will match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list
            self.assertIn(number_type, self.phone_book.valid_phone_number_types)
            
    def test_valid_edit_book_type2(self):
        """Here are some phone number type checks I know will validate to True"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to True
            self.assertTrue(self.phone_book.validatePhoneNumberType())
            
    def test_invalid_edit_book_type(self):
        """Here are some phone number type checks I know will not match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not match one in the valid list
            self.assertNotIn(number_type, self.phone_book.valid_phone_number_types)

    def test_invalid_edit_book_type2(self):
        """Here are some phone number type checks I know will not validate to True"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to false
            self.assertFalse(self.phone_book.validatePhoneNumberType())      
    
    def test_valid_remove_book(self):
        """Here are some phone number type checks I know will match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type matches one in the valid list
            self.assertIn(number_type, self.phone_book.valid_phone_number_types)
            
    def test_valid_remove_book_type2(self):
        """Here are some phone number type checks I know will validate to True"""
        valid_number_types_to_test = ["cell", "home", "office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to True
            self.assertTrue(self.phone_book.validatePhoneNumberType())
            
    def test_invalid_remove_book_type(self):
        """Here are some phone number type checks I know will not match a value in valid_phone_number_types"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type does not match one in the valid list
            self.assertNotIn(number_type, self.phone_book.valid_phone_number_types)

    def test_invalid_remove_book_type2(self):
        """Here are some phone number type checks I know will not validate to True"""
        valid_number_types_to_test = ["cell1", "home2", "office ", "cell ", " home", " office", "123cell", "123home", "123office"]
        
        for number_type in valid_number_types_to_test:
            self.phone_book.phone_number_type = number_type
            ## Checks to see if the phone type function evaluates to false
            self.assertFalse(self.phone_book.validatePhoneNumberType())      

    
    
            
           
            
