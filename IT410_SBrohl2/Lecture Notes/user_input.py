## Lecture: Gathering User Input Demonstration
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN

area_code = input("Please enter your area code: ")

if area_code:
    try:
        int(area_code)
        if len(area_code) == 3:
            print("Your area code is: " + area_code)
        else:
            print("Your inputted area code is not long enough")
    except:
        print("You did not provide a valid area code")
else:
    print("You did not enter an area code.")