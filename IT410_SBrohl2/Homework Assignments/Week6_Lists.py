## Week 6 - Working with Lists Assignment
## IT 410 - Walsh College
## 05/13/2019
## BROHL, STEVEN

## Declaring a list of all of the courses I have taken at Walsh and then sorting that list
walsh_courses = ["it402","it460","it408","it410","it422","mgmt201"] 

walsh_courses.sort()

## A for loop that prints out each course I have taken that is in the list
for course in walsh_courses:
    print("I have taken",course.upper(),"at Walsh College.") 

## Adding courses to the list I plan to take next term, then resorting the list
walsh_courses.append("it406")
walsh_courses.append("it461")
walsh_courses.append("it412")
walsh_courses.append("it490")

walsh_courses.sort()

print(walsh_courses)
## A for loop that lists each course along with the courses I have added above
print("This is my course of study with upcoming courses added.")
for course in walsh_courses:
    print("\t-",course.upper())

## Declaring a list to store removed courses, then removing courses already taken and adding them to that newly created list
removed_courses = []

removed_courses1= walsh_courses.pop(0)
removed_courses2= walsh_courses.pop(5)
removed_courses3= walsh_courses.pop(1)
removed_courses4= walsh_courses.pop(1)
removed_courses5= walsh_courses.pop(2)
removed_courses6= walsh_courses.pop(4)

## A print statement that says I do not have to take those courses I previously removed, followed by a for loop which outputs those previously removed courses
print("I do not have to take these courses.")
print(removed_courses1)
print(removed_courses2)
print(removed_courses3)
print(removed_courses4)
print(removed_courses5)
print(removed_courses6)

## This for loop prints out the remainder of classes in the walsh_courses list that were not removed
print("I plan to take the following courses next term.")
for course in walsh_courses:
    print("\t-",course.upper())


## Creates a list of numbers between 1 to 1000 divisible by 6
numbers = list(range(6,1001,6))

## Prints out the first 20 numbers divisible by 6 on its own line along with a print message
print("Here are twenty numbers divisible by 6")
for number in numbers[0:20]:
    print(number)

## Calculate the maximum number of the numbers list
max_numbers = max(numbers)

## Print out the maximum number variable in the list inside a message
print("The maximum value in the list is: ", max_numbers)

## Calculate the sum of values in the numbers list between 10 and 50 and print in a message
sum_numbers = sum(numbers[9:49])
print("Here is the sum of several values in the list:", sum_numbers)

## Copy the numbers list into the walsh_courses list
walsh_courses.append(numbers)