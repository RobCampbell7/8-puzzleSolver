from functools import cache
import os

goal = (
         0,  1,  2,  3, 
         4,  5,  6,  7,
         8,  9, 10, 11,
        12, 13, 14, 15
    )
neighbours = {
     0 : (1, 4),
     1 : (0, 2, 5),
     2 : (1, 3, 6),
     3 : (2, 7),
     4 : (0, 5, 8),
     5 : (1, 4, 6, 9),
     6 : (2, 5, 7, 10),
     7 : (3, 6, 11),
     8 : (4, 9, 12),
     9 : (5, 8, 10, 13),
    10 : (6, 9, 11, 14),
    11 : (7, 10, 15),
    12 : (8, 13),
    13 : (9, 12, 14),
    14 : (10, 13, 15),
    15 : (11, 14)
}    

class State:
    def __init__(self, state, heuristic):
        self.prevState = None
        self.state = state
        self.f = 0
        self.g = 0
        self.h = heuristic(state)
        self.heuristic = heuristic

    def setDepth(self, g):
        self.g = g
        self.f = self.g + self.h

    def createChild(self, newState):
        newState = State(newState, self.heuristic)
        newState.prevState = self
        newState.setDepth(self.g + 1)
        return newState
    
    def equals(self, otherState):
        return self.state == otherState
    
    def path(self):
        if self.prevState == None:
            return [self.state]
        else:
            return self.prevState.path() + [self.state]
    
    def __repr__(self):
        return str(self.state)

def swap(lst, i, j):
    temp = []
    for k in range(len(lst)):
        if k == i:
            temp.append(lst[j])
        elif k == j:
            temp.append(lst[i])
        else:
            temp.append(lst[k])
    
    return tuple(temp)

def possibleStates(state):
    i = state.index(0)
    return [swap(state, i, j) for j in neighbours[i]]

@cache
def inversionCount(state):
    invCount = 0
    for i in range(16):
        for j in range(i + 1, 16):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                invCount += 1
    return invCount

def solvable(start, goal):
    if inversionCount(start) % 2 == inversionCount(goal) % 2:
        return True
    else:
        return False

@cache
def manhattan(i, j):
    """
    Returns the manhattan distances between two indexes i and j in the grid:
    0 1 2
    3 4 5
    6 7 8
    """
    return abs((i % 4) - (j % 4)) + abs((i // 4) - (j // 4))
    # dx = abs((i % 3) + (j % 3))
    # dy = abs((i // 3) + (j // 3))
    # return dx + dy

@cache
def heuristic(current, goal):
    score = 0
    for i in range(9):
        score += manhattan(current.index(i), goal.index(i))
    return score

# @cache
# def heuristic(current, goal):
#     return abs(inversionCount(current) - inversionCount(goal))

# def heuristic(current, goal):
#     return 0

def insert(sLst, s):
    for i in range(len(sLst)):
        if sLst[i].f > s.f:
            return sLst[:i] + [s] + sLst[i:]
    return sLst + [s]

def printState(state):
    output = ""
    for i in range(16):
        if state[i] == 0:
            output += "  "
        elif state[i] < 10:
            output += " " + str(state[i])
        else:
            output += str(state[i])

        if i % 4 == 3:
            output += "\n"
        else:
            output += " "
        
    print(output)

def solve(start, goal):
    current = State(start, lambda s : heuristic(s, goal))
    frontier = []
    exploredStates = []
    while current.equals(goal) != True:
        # os.system("cls")
        # printState(current.state)
        # print("\nf:{0:>2} - g:{1:>2} - h:{2:>2}".format(current.f, current.g, current.h))
        for state in possibleStates(current.state):
            if state not in exploredStates:
                frontier = insert(frontier, current.createChild(state))

        current = frontier.pop(0)
        exploredStates.append(current.state)

    os.system("cls")
    printState(current.state)
    print("\nf:{0:>2} - g:{1:>2} - h:{2:>2}".format(current.f, current.g, current.h))
        
    return current