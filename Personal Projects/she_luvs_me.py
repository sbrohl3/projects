import random


class Flower():

    ''' A Class to represent a flower '''

    def __init__(self):

        ''' A constructor to initialize all of the variables used in the flower class '''

        self.luv_me_not = ["She loves me", "She loves me not"]



    def flowerPetal(self, petals):

        ''' A method representing a flower petal '''

        ans = random.choice(self.luv_me_not)
        out = ans
        
        if petals == 1 and out == "She loves me not":
            print(out + " :'(")

        elif petals == 1 and out == "She loves me":
            print(out + "!! <3 :)") 

        else:
            print(out) 

f = Flower()

petals = 12

InitInt = input("Press enter to start: \n")

while petals  > 0:
    f.flowerPetal(petals)
    cont = input("\n")
    petals -= 1
