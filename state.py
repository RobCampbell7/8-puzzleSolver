import random
from aStar import 
def heuristicPH(x):
    return random.randint(0, 100)

class State:
    def __init__(self, state):
        self.prevState = None
        self.state = state
        self.f = 0
        self.g = 0
        self.h = heuristicPH(state)

    def setDepth(self, g):
        self.g = g
        self.f = self.g + self.h

    def createChild(self, newState):
        newState = State(newState)
        newState.prevState = self
        newState.setDepth(self.g + 1)
        return newState
    
    def equals(self, otherState):
        return self.state == otherState
    
    def path(self):
        if self.prevState == None:
            return self.state
        else:
            return self.prevState.path() + self.state
