import math

class Negyzet:
    def __init__(self, a = 0):
        self.a = a 

        def setA(self, a):
            self.a = a

        def getKerulet(self):
            return 4 * self.a 

        def getTerulet(self):
            return math.pow(self.a, 2)
