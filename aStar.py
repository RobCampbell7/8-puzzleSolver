from functools import cache
import os

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
    def __init__(self, state, heuristic):
        self.prevState = None
        self.state = state
        self.f = 0
        self.g = 0
        self.h = 2 * heuristic(state)
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

def inversionCount(state):
    invCount = 0
    for i in range(9):
        for j in range(9):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                invCount += 1
    return invCount

def solvable(start, goal):
    if inversionCount(start) % 2 == inversionCount(goal) % 2:
        return True
    else:
        return False

def manhattan(i, j):
    """
    Returns the manhattan distances between two indexes i and j in the grid:
    0 1 2
    3 4 5
    6 7 8
    """
    return abs((i % 3) - (j % 3)) + abs((i // 3) - (j // 3))
    # dx = abs((i % 3) + (j % 3))
    # dy = abs((i // 3) + (j // 3))
    # return dx + dy

@cache
def heuristic(current, goal):
    score = 0
    for i in range(9):
        score += manhattan(current.index(i), goal.index(i))
    return score

def insert(sLst, s):
    for i in range(len(sLst)):
        if sLst[i].f > s.f:
            return sLst[:i] + [s] + sLst[i:]
    return sLst + [s]

def printState(state):
    output = ""
    for i in range(9):
        if state[i] == 0:
            output += " "
        else:
            output += str(state[i])

        if i == 2 or i == 5:
            output += "\n"
        else:
            output += " "
        
    print(output)

def solve(start, goal):
    current = State(start, lambda s : heuristic(s, goal))
    frontier = []
    exploredStates = []
    while current.equals(goal) != True:
        os.system("cls")
        printState(current.state)
        print("\nf:{0} - g:{1} - h:{2}".format(current.f, current.g, current.h))
        for state in possibleStates(current.state):
            if state not in exploredStates:
                frontier = insert(frontier, current.createChild(state))
            # print(state)
            # else:
            #     print("FUCK")
            #     input()
        # print(frontier)
        # input()
        
        # frontier.sort(key=lambda s : s.f)
        current = frontier.pop(0)
        exploredStates.append(current.state)

    return current