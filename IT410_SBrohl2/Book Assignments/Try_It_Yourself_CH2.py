## Try it Yourself Excercises - Chapter 2
## IT 410 - Walsh College
## 05/13/2019
## BROHL, STEVEN


## Try it Yourself 2-1: Simple Message
############################################
message = "Hello, this is my message stored in a variable called 'message'."
print(message)

## Try it Yourself 2-1: Simple Message 2
############################################
message = "Hello my name is Steven and this is my message stored in a variable called 'message'."
print(message)

message = "I am changing the message that goes into my variable called, 'message'."
print(message)

## Try it Yourself 2-3: Personal Message
############################################
name = "Steven"
print("Hello ",name,", would you like to learn some Python today?")

## Try it Yourself 2-4: Name Cases
############################################
name = "steven"
print(name.upper())
print(name.lower())
print(name.title())

## Try it Yourself 2-5: Famous Quote
############################################
print("Philip K. Dick once said,“There will come a time when it isn't 'They're spying on me through my phone' anymore. Eventually, it will be 'My phone is spying on me'.\"")

## Try it Yourself 2-6: Famous Quote 2
############################################
name = "Philip K. Dick"
quote = "“There will come a time when it isn't 'They're spying on me through my phone' anymore. Eventually, it will be 'My phone is spying on me'.\""
print(name,"once said,",quote)

## Try it Yourself 2-7: Stripping Names
############################################
name = "\tSteven Brohl\n"

print("Showing whitespace")
print(name)

print("\nUsing lstrip()")
print(name.lstrip())

print("\nUsing rstrip()")
print(name.rstrip())

print("\nUsing strip()")
print(name.strip())

## Try it Yourself 2-8: Number Eight
############################################
print(6+2)
print(10-2)
print(4*2)
print(16/2)

## Try it Yourself 2-9: Favorite Number
############################################
fav_num = 333
message = "My favorite number is "
print(message + str(fav_num) + ".")


