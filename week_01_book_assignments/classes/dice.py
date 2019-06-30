from random import randint

class Die():
    """ A standard class for a single die """
    
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, self.sides)

        return roll
