
# Brohl, Steven
# IT463
# 02/09/2020
# password_encrypt.py 
# Performs validation and decryption

from Crypto.Cipher import AES
from base64 import b64encode
from base64 import b64decode
import json

class decryptPassword():
    '''A class to decrypt a user's password stored on file'''

    def __init__(self, input_password="", key=""):
        '''Init method to define variables used within the decryptPassword Class'''

        self.input_password = input_password
        self.key = "6440777308024991" ## Key used to encrypt the password/ Also used for decryption

    def decryptPass (self):
        '''This method opens the my_password.json file for use in the decryption program'''

        with open("my_password.json", "r") as file_load:

            ## Encoding the key into bytes format
            key_bytes = self.key.encode('utf-8') 

            ## Loading my_password json file
            json_file = json.load(file_load)

            ## Decoding the ciphertext_password from my_password.json so it can be decrypted
            ciphertext_decrypt = b64decode(json_file["ciphertext_password"])
            
            ## Decoding the initialization vector from my_password.json
            iv_decrypt = b64decode(json_file["password_iv"])

            ## Setting up AES so it can decrypt a password using a provided IV and key
            cipher_decrypt = AES.new(key_bytes, AES.MODE_CFB, iv=iv_decrypt)

            ## Decrypting plaintext into bytes format
            decrypted_plaintext_bytes = cipher_decrypt.decrypt(ciphertext_decrypt)
            
            ## Decoding plaintext to remove bytes format
            decrypted_plaintext = decrypted_plaintext_bytes.decode()

            ## If the user's provided password matches the password decrypted from file, print to screen that a match was found and exit
            if self.input_password == decrypted_plaintext:
                print("\n" + self.input_password ," == ", decrypted_plaintext)
                print("\nThis password matches the password on file.\n")
                print("Exiting program...\n")
                return False

            ## If a match isn't found prompt the user to try again
            else:
                print("\nThis password does not match the password on file. Please try again.\n")
                return True

dp = decryptPassword()

program_run = True

while program_run:

    ## Taking user input and inserting it into the password encryption class
    dp.input_password = str(input("Enter a password to decrypt: "))
    
    if dp.input_password.lower() == "q":
        print("Exiting program...\n")
        program_run = False

    else:
        ## Run decryption method
        program_run = dp.decryptPass()

