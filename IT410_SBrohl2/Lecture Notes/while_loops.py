## Lecture: Working with While Loops
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN

program_running = True
phone_numbers = []

print(phone_numbers)

while program_running:
    area_code = input("Please enter your area code: ")

    area_code_ok = False

    while not area_code_ok:
        if area_code:
            try:
                int(area_code)
                if len(area_code) == 3:
                    print("Your area code is: " + area_code)
                    area_code_ok = True
                else:
                    area_code_ok = False
            except:
                area_code_ok = False
        else:
            area_code_ok = False

        if not area_code_ok:
            area_code = input("Area Code was not properly formatted. Please try again:")

    #end area code processing
    #begin processing first part of phone number
    phone_first_part = input("Please enter the first three digits of your phone number: ")

    phone_first_part_ok = False

    while not phone_first_part_ok:
        if phone_first_part:
            try:
                int(phone_first_part)
                if len(phone_first_part) == 3:
                    print("The first part of your phone number is: " + phone_first_part)
                    phone_first_part_ok = True
                else:
                    phone_first_part_ok = False
            except:
                phone_first_part_ok = False
        else:
            phone_first_part_ok = False

        if not phone_first_part_ok:
            phone_first_part = input("The first part of your phone number was not properly formatted. Please try again:")

    #end processing first part of the phone number
    #begin processing second part of phone number
    phone_second_part = input("Please enter the last four digits of your phone number: ")

    phone_second_part_ok = False

    while not phone_second_part_ok:
        if phone_second_part:
            try:
                int(phone_second_part)
                if len(phone_second_part) == 4:
                    print("The second part of your phone number is: " + phone_second_part)
                    phone_second_part_ok = True
                else:
                    phone_second_part_ok = False
            except:
                phone_second_part_ok = False
        else:
            phone_second_part_ok = False

        if not phone_second_part_ok:
            phone_second_part = input("The second part of your phone number was not properly formatted. Please try again:")

    phone_numbers.append({'area_code': area_code, 'first_part': phone_first_part, 'second_part':phone_second_part})

    add_another_number = input("Do you wish to add another phone number (Y or N)? ")
    if add_another_number == "N":
        break
    else:
        continue

print(phone_numbers)