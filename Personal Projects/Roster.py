import random

## A list of names
names = ["George", "Ryan", "Steven", "Shirley"]

## A function for building a team roster
def teamRoster(names):
    ## A variable used for count incrementation of a loop
    count = 0

    ## A loop that stops after the contents of the list have been iterated
    while count <= len(names):
        
        ## Choose two random names from the list
        name1 = random.choice(names)
        name2 = random.choice(names)
        
        ## If the two names chosen are not equal then print them and remove them from the list
        if name1 != name2:
            print(name1 + " vs. " + name2)
            ## Remove the names from the list so they are no reused
            names.remove(name1)
            names.remove(name2)
            
        ## If the two names chosen are equal then choose again
        else:
            while name1 == name2:
                ## Choose two random names 
                name1 = random.choice(names)
                name2 = random.choice(names)
                
                ## If the two names chosen are not equal then print them and remove them from the list
                if name1 != name2:
                    print(name1 + " vs. " + name2)
                    names.remove(name1)
                    names.remove(name2)
        
        ## Increment the counter variable by 1 each time the loop reaches this point
        count += 1


teamRoster(names)
        