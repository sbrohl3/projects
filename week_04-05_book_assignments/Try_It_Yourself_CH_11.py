## TRY IT YOURSELF CHAPTER 11
## IT412
## 07/20/2019
## BROHL, STEVEN

## 11-1:
from functions.city_functions import get_formatted_location

program_run = True

while program_run == True:
    city = input("Please enter the name of a city or \"q\" to quit: ")
    if city.lower() == "q":
        break

    country = input("Please enter the name of the country associated with that city or \"q\" to quit: ")
    if country.lower() == "q":
        break

    formatted_location = get_formatted_location(city.title(), country.title())
    print(formatted_location)


## 11-2:

from functions.city_functions import get_formatted_location_and_pop

program_run = True

while program_run == True:
    city = input("Please enter the name of a city or \"q\" to quit: ")
    if city.lower() == "q":
        break

    country = input("Please enter the name of the country associated with that city or \"q\" to quit: ")
    if country.lower() == "q":
        break

    population = input("Please enter the population of " + str(city.title()) + ", " + str(country.title()) + ": ")
    if country.lower() == "q":
        break

    formatted_location = get_formatted_location_and_pop(city.title(), country.title(), population)

    print(formatted_location)

## 11-3:

from classes.employee import Employee

program_run = True

while program_run == True:
    first_name = input("Please enter the employee's first name or \"q\" to quit: ")
    if first_name.lower() == "q":
        break

    last_name = input("Please enter the employee's last name or \"q\" to quit: ")
    if last_name.lower() == "q":
        break

    salary = input("Please enter " + str(first_name.title()) + " " + str(last_name.title()) + "'s salary: ")
    if salary.lower() == "q":
        break

    employee = Employee(first_name, last_name, int(salary))
    employee.give_raise()
    

