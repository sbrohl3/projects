def emp_id(employee_id):
    """Processes a user input for an employee id
    Arguments:
    employee_id [user input] -- user input must be an integer <= 7
    Returns:
    A valid employee number
    """
    ## Declaring a Flag to control a while loop
    employee_id_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_id_ok:
        ## Asking for an ID (int) and checking if int not > 7
        if employee_id.isdigit():
            if len(employee_id) <= 7:
                employee_id_ok = True
            else:
                employee_id_ok = False
                return True
        else:
            employee_id_ok = False
            return False
    return employee_id 


def emp_name(employee_name):
    """Processes a user input for a name
    Arguments:
    employee_name [user input] -- An input for employee name containing no special characters or numbers
    Returns:
    A valid employee name
    """
    ## Declaring a Flag to control a while loop
    employee_name_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_name_ok:
        ## Declaring a list of characters that are not allowed in employee address
        bad_chars = ["!", "\"", "@","#", "$", "%", "^", "&", "*","(",")" "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        ## Asking for a name and checking if it has any defined bad characters
        if employee_name:
            ## Checking employee name for bad characters
            for char in employee_name:
                ## If bad characters are found, exit the program
                if char in bad_chars or char.isdigit() or employee_name.isspace():
                    employee_name_ok = False
                    return False
                else:
                    employee_name_ok = True
        ## if no input is provided exit the program
        else:
            employee_name_ok = False
            return False
    return employee_name


def emp_email(employee_email_address):
    """Processes a user input for an email address
    Arguments:
    emp_email [user input] -- An input for an employee email with no special characters except "@"
    Returns:
    A valid employee email adress
    """
    ## Declaring a Flag to control a while loop
    employee_email_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_email_ok:
        ## Declaring a list of characters that are not allowed in employee email address
        bad_chars = ["!", "\"", "#", "$", "%", "^", "&", "*","(", ")", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        if employee_email_address:
            ## Checking employee email address for bad characters
            for char in employee_email_address:
                ## If bad characters are found, exit the program
                if char in bad_chars or char.isspace():
                    employee_email_ok = False
                    return False

                else:
                    employee_email_ok = True
        ## if no input is provided exit the program
        else:
            employee_email_ok = False
            return False
    return employee_email_address
    


def emp_address(employee_address):
    """Processes a user input for an address
    Arguments:
    emp_address [user input] -- An input containing an employee address with no special characters
    Returns:
    A valid employee adress
    """
    ## Declaring a Flag to control a while loop
    employee_address_ok = False
    ## While loop to have user retry their input if they enter incorrectly
    while not employee_address_ok:
        ## Declaring a list of characters that are not allowed in employee address
        bad_chars = ["!", "\"", "@", "$", "%", "^", "&", "*", "_", "=", "+", ",", "<",">", "/", "?", ";", ":", "[", "]", "{", "}", "\\" ]
        if employee_address:
            ## Checking employee address for bad characters
            for char in employee_address:
                ## If bad characters are found, exit the program
                if char in bad_chars:
                    employee_address_ok = False
                    return False
                ## Else, add the address to a new employee_address variable
                else:
                    address = "Your address is " + employee_address + "."
                    employee_address_ok = True
        ## If no input is provided
        else:
            address = "You did not provide an address."
            employee_address_ok = True
    return(address, employee_address)

