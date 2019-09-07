## Lecture: Working with Functions
## IT 410 - Walsh College
## 06/02/2019
## BROHL, STEVEN

def divideTwoNumbers(passed_list):
    divide_results = []
    numbers_ok = True
    passed_number1 = 1
    passed_number2 = 1

    for divide_vals in passed_list:
        numbers_ok = True
        try:
            passed_number1 = int(divide_vals["top_number"])
        except:
            print("The first parameter is not an integer")
            numbers_ok = False
        try:
            passed_number2 = int(divide_vals["bottom_number"])
        except:
            print("The second parameter is not an integer")
            numbers_ok = False
        
        if numbers_ok:
            divide_result = passed_number1 / passed_number2
            divide_results.append(divide_result)

    return divide_results


division_list = [{"top_number": "square", "bottom_number": 2,}, {"top_number": 5, "bottom_number": 8,}]
the_result = divideTwoNumbers(division_list)
print("The result of division is:")
print(the_result)