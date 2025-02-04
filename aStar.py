neighbours = {
    0 : (1, 3),
    1 : (0, 2, 4),
    2 : (1, 5),
    3 : (0, 4, 6),
    4 : (1, 3, 5, 7),
    5 : (2, 4, 8),
    6 : (3, 7),
    7 : (4, 6, 8),
    8 : (5, 7)
}    

class State:
    def __init__(self, state):
        self.prevState = None
        self.state = state
        self.f = 0
        self.g = 0
        self.h = heuristic(state)

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

def swap(lst, i, j):
    temp = []
    for k in range(len(lst)):
        if k == i:
            temp.append(lst[j])
        elif k == j:
            temp.append(lst[i])
        else:
            temp.append(lst[k])
    
    return tuple(lst)

def possibleStates(state):
    match state.index(0):
        case 0:
            return [
                swap(state, 0, 1),
                swap(state, 0, 3)
            ]
        case 1:
            return [
                swap(state, 1, 0),
                swap(state, 1, 2),
                swap(state, 1, 4)
            ]
        case 2:
            return [
                swap(state, 2, 1),
                swap(state, 2, 5)
            ]
        case 3:
            return [
                swap(state, 3, 0),
                swap(state, 3, 4),
                swap(state, 3, 6)
            ]
        case 4:
            return [
                swap(state, 4, 1),
                swap(state, 4, 3),
                swap(state, 4, 5),
                swap(state, 4, 7)
            ]
        case 5:
            return [
                swap(state, 5, 2),
                swap(state, 5, 4),
                swap(state, 5, 8)
            ]
        case 6:
            return [
                swap(state, 6, 3),
                swap(state, 6, 7)
            ]
        case 7:
            return [
                swap(state, 7, 4),
                swap(state, 7, 6),
                swap(state, 7, 8)
            ]
        case 8:
            return [
                swap(state, 8, 5),
                swap(state, 8, 7)
            ]

def heuristic(current, goal):
    return 6

def solve(start, goal):
    current = State(start)