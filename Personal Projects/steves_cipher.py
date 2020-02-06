## Steven's Cipher
## 01/18/2020
## IT463
####################
import life

class steves_cipher():
    ''' A class to encrypt and Decrypt plaintext and write it to file '''

    def __init__(self, input_encrypt="", input_decrypt=""):
        ''' This method initializes variables for the Steefer Cipher '''

        self.input_encrypt = input_encrypt
        self.input_decrypt = input_decrypt
    
    def encrypt(self):
        ''' This method encrypts text input into it '''
        
        ## Convert text string to binary
        binary = bin(int.from_bytes(self.input_encrypt.encode(), 'big'))
         
        ## Reverse the string
        rev = binary[::-1]

        ## Create a new string from the reversed text
        sub_num = " "
        
        ## Loop through each digit in "binary" and substitute digits
        for num in rev:

            ## If num is 1, change it to 0
            if num == "1":
                num = int(num)
                num -= 1
                sub_num += str(num)

            ## If num is 0, change it to 1
            elif num == "0":
                num = int(num)
                num += 1
                sub_num += str(num)

            elif num == "b":
                ## Replace "b" with an exclamation mark
                sub_num += str(num.replace("b","!"))

        ## Print encrypted string
        print("\nYour encrypted text is:\n",sub_num + str("\n\ndone."))

    def decrypt(self):
        ''' This method decrypts text input into it '''
  
        ## Reverse the string
        rev = self.input_decrypt[::-1]
        
        ## Place the reversed string into a new string in the unreversed order
        sub_num = " "

        ## Loop through each digit in "binary" and substitute digits
        for num in rev:
            for char in sub_num:

                ## If num is 1, change it to 0
                if num == "1":
                    num = int(num)
                    num -= 1
                    sub_num += str(num)

                ## If num is 0, change it to 1
                elif num == "0":
                    num = int(num)
                    num += 1
                    sub_num += str(num)

                elif num == "b":
                    ## Replace "!" with a "b"
                    sub_num += str(num.replace("!","b"))

        ## Prepare string to be converted from bytes to text
        try:
            bytes2Decrypt = int(sub_num, 2)
            ## Convert bytes to text
            print("\nYour decrypted text is: \n", bytes2Decrypt.to_bytes((bytes2Decrypt.bit_length() + 7) // 8, 'big').decode() + str("\n\ndone."))
            return False

        except:
            print("The string you entered is invalid and cannot be decrypted as entered. Please check your input and try again!")
            return True

## Instantiate the "steve_cipher" class
sc = steves_cipher() 

## Run the program
running = True

while running:
    option = str(input("\n\t- Steve's Cipher - \nDo you want to (E)ncrypt or (D)ecrypt a message: "))

    if option.lower() == "e":
        ## User input -- insert string to Encrypt
        sc.input_encrypt = input("\nInsert your message to encrypt: \n")
        ## Call the encryption method
        sc.encrypt()

    elif option.lower() == "d":

        decrypting = True
        while decrypting:
            ## User input -- insert decrypted string
            sc.input_decrypt = input("\nCopy and paste your message to decrypt: \n")
            if sc.input_decrypt.lower() == "q":
                print("\nReturning to the main menu...\n")
                decrypting = False
            
            else:
                ## Call the decryption method
                sc.decrypt()
            
    elif option.lower() == "q":
        ## Exit the program
        exit()

    else:
        ## User will be prompted if invalid input is provided at the main menu
        print("Please enter (E) to encrypt a message or (D) to decrypt a message. Enter (Q) to quit the program.")
    
