import random


class Flower():

    ''' A Class to represent a flower '''

    def __init__(self):

        ''' A constructor to initialize all of the variables used in the flower class '''

        self.replies = ["", " me not."]



    def flowerPetal(self, startText):

        ''' A method representing a flower petal '''

        ans = random.choice(self.replies)
        startText = startText + ans

        print(startText) 




f = Flower()

startText = "She loves me"
start = input(startText)

while start != "q":
    start = input(startText)
    f.flowerPetal(startText)
    