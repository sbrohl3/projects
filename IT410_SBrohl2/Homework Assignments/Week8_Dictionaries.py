## Week 8 - Dictionaries Assignment
## IT 410 - Walsh College
## 05/25/2019
## BROHL, STEVEN


## Declaring a list containing a collection of employee data
employee_data = [1121, "Jackie Grainger", 22.22, 1122, "Jignesh Thrakkar", 25.25, 1127, "Dion Green", 28.75, False, 24.32, 1132, "Jacob Gerber", "Sarah Sanderson", 23.45, 1137, True,"Brandon Heck", 1138, 25.84, True,  1152, "David Toma", 22.65, 23.75, 1157, "Charles King", False, "Jackie Grainger", 1121, 22.22, False, 22.65, 1152, "David Toma"]

## Created new empty lists to filter employee_data into three categories 
## (Employee_Numbers = Integers, Employee_Names = Strings, Employee_Salary = Floats)
employee_numbers = []
employee_names = []
employee_salary = []

## Filtering all values from employee_data into separate lists
for data in employee_data:
    if data not in employee_numbers and data not in employee_names and data not in employee_salary:
        if type(data) is int:
            employee_numbers.append(data)

        elif type(data) is str:
            employee_names.append(data)
      
        elif type(data) is float:
            employee_salary.append(data)
             

## Printing the newly populated lists to screen
print("Employee Number")
print("==================")
for number in employee_numbers:
    print("--",number) 
    
    
print("\nEmployee Name")
print("==================")
for name in employee_names:
    print("--",name)


print("\nEmployee Salary")
print("==================")
for salary in employee_salary:
    print("-- ",str(salary) + " * 1.3 = " + str(salary * 1.3))


## Declaring list total_hourly_rate
total_hourly_rate = []
for rate in employee_salary:
    ## Multiplying rate in employee_salary by 1.3 and appending to list
    total_hourly_rate.append(rate * 1.3)

## Determining max in list total_hourly_rate
max_rate = max(total_hourly_rate)
print("\nThe maximum rate is: " + str(max_rate))     
## If the max rate is over 37.30 print alert message
if max_rate > 37.30:
    print("\n" + str(max_rate) + " is over 37.30. This may be a budget concern!")

## Declaring list underpaid_salaries
underpaid_salaries = []
for rate in total_hourly_rate:
    ## If any rates are between 28.15 amd 30.65 append to list
    if 28.15 <= rate <= 30.65:   
        underpaid_salaries.append(rate)    

## Declaring list company_raises
company_raises = []     
for salary in employee_salary:
    ## If salary is between 26 and 28 multiply by 3% and append to list
    if 26 <= salary < 28:       
        salary_raise = (salary * 1.03)
        company_raises.append(salary_raise)
    ## If salary is between 24 and 26 multiply by 4% and append to list
    elif 24 <= salary < 26:     
        salary_raise = (salary * 1.04)
        company_raises.append(salary_raise)
    ## If salary is between 22 and 24 multiply by 5% and append to list
    elif 22 <= salary < 24:     
        salary_raise = (salary * 1.05)
        company_raises.append(salary_raise)
    ## Multiply all other salaries by 2% and append to list
    else:
        salary_raise = (salary * 1.02)
        company_raises.append(salary_raise)

print("\n")
## Declaring an empty list to store employee data dictionaries
employee_database = []
## Creating a counter variable called count and set to 0
count = 0
## creating a for loop to loop employee numbers
for number in employee_numbers:
    ## Appending employee data to employee database using employee number for order
    employee_database.append({"number" : number, "name" : employee_names[count], "salary" : employee_salary[count], "total_hourly_rate" : total_hourly_rate[count], "company_raises" : company_raises[count]})
    ## Counter variable is incrementing each time the loop goes through
    count+= 1
## Once the loop hits an end, the employee database dictionary is printed
print(employee_database)
