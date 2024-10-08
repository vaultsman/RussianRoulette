import random

class Revolver:
    chamber = list()
    life = bool()
    people = list()
    ## shot = random.randint inside the function
    def load(self):
        shot = random.randint(0,5)
        self.chamber[shot] = 1

    def __init__(self, p: list):
        self.chamber = [0]*6
        self.people = p
        self.life = True
        self.load()

class Game:
    def __init__(self):
        pass
    ## we get input later from gui
