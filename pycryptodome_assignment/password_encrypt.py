
# Brohl, Steven
# IT463
# 02/09/2020
# password_encrypt.py 
# Accepts input and performs encryption operations

from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
import json


class password_encrypt():
    '''A class for encrypting plaintext passed in via user input'''

    def __init__(self, plaintext="", key=""):
        '''init method for password encryption class'''
        
        self.plaintext = plaintext
        self.key = "6440777308024991" ## Key used to encrypt password
        self.info = {}

    def encryptPassword(self):
        '''encrypt user inputted plaintext'''

        ## Encoding the user's provided plaintext message
        plaintext_bytes = self.plaintext.encode('utf-8')
        
        key_bytes = self.key.encode('utf-8')

        ## Initializing AES encryption
        cipher_encrypt = AES.new(key_bytes, AES.MODE_CFB)

        ## Init vector in bytes format
        iv_bytes = cipher_encrypt.iv

        ## Decode initialization vector into a readable format
        self.init_vector = b64encode(iv_bytes).decode('utf-8')
        
        ## Encrypting user inputted plaintext
        cipher_text_bytes = cipher_encrypt.encrypt(plaintext_bytes)

        ## Decode the encrypypted plaintext from bytes into a human readable format
        self.cipher_text = b64encode(cipher_text_bytes).decode('utf-8')

        print("\n===============================================")

        ## Print the Cipher text to the terminal output
        print("\nCipher Text:", self.cipher_text)

        ## Print the initialization vector to the terminal output
        print("\nInitialization Vector: ", self.init_vector)

        print("\n===============================================")
        
    def saveInfo(self):
        ''' Save the contents of the Info dictionary to an external json file'''
        
        print("\nSaving Ciphertext and Initialzation Vector to \"my_password.json\" and Exiting program...\n")

        ## Packing the cipher text and initialization vector into a json file
        self.info = {"ciphertext_password" : self.cipher_text ,"password_iv": self.init_vector}
        with open("my_password.json", "w+") as file_store:
            json.dump(self.info, file_store)
            return False

## instantiate password encryption class
pe = password_encrypt()

## The Encryption Program runs so long as this flag is True
program_run = True

while program_run:

    ## Taking user input and inserting it into the password encryption class
    pe.plaintext = str(input("\nPlease input your password to encrypt: ")) 
    
    if pe.plaintext.lower() == "q":
        print("\nExiting program...\n")
        program_run = False

    else:
        pe.encryptPassword()
        program_run = pe.saveInfo()





