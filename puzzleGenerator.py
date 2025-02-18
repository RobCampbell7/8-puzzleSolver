from copy import deepcopy
from random import choice, randint, sample, uniform
from aStar import printState, heuristic, possibleStates, State

# def generatePuzzle(moves, goal = (0, 1, 2, 3, 4, 5, 6, 7, 8)):
#     position = deepcopy(goal)
#     lastPos = position
#     hValue = 0
#     for i in range(moves):
#         nextChoices = []
        
#         # for state in possibleStates(position):
#         #     if heuristic(state, goal) > hValue:
#         #         nextChoices.append(state)
#         position, lastPos = max(
#             [s for s in possibleStates(position) if s != lastPos],
#             key=lambda s : heuristic(s, goal)
#         ), position
#         # position = choice(nextChoices)
#         hValue = heuristic(position, goal)
#     return position

def makeMove(s):
    return choice(possibleStates(s))

def mutate(s):
    for i in range(randint(1, 10)):
        s = makeMove(s)
    return s

def tournamentSample(population, f):
    s1 = choice(population)
    s2 = choice(population)
    if f(s2) > f(s1):
        return s2
    else:
        return s1

def generatePuzzleAEA(goal=(0, 1, 2, 3, 4, 5, 6, 7, 8)):
    population = [mutate(goal) for i in range(2000)]
    
    maxPos = goal
    for i in range(10000):
        matingPool = [
            tournamentSample(population, lambda s : heuristic(s, goal))
            for i in range(1000)
        ]
        population = matingPool + [mutate(choice(matingPool)) for i in range(1000)]
        population = [mutate(s) if uniform(0, 1) < 0.05 else s for s in population]
        maxPos = max(population + [maxPos], key = lambda s : heuristic(s, goal))

    return maxPos

def insert(sLst, s):
    for i in range(len(sLst)):
        if sLst[i].f < s.f:
            return sLst[:i] + [s] + sLst[i:]
    return sLst + [s]

def generatePuzzle(start, goal):
    current = State(start, lambda s : heuristic(s, goal))
    bestFound = start
    frontier = []
    exploredStates = []
    for i in range(100000):
        # os.system("cls")
        # printState(current.state)
        # print("\nf:{0:>2} - g:{1:>2} - h:{2:>2}".format(current.f, current.g, current.h))
        for state in possibleStates(current.state):
            if state not in exploredStates:
                frontier = insert(frontier, current.createChild(state))

        current = frontier.pop(0)
        exploredStates.append(current.state)
        bestFound = max(current.state, bestFound, key = lambda s : heuristic(s, goal))

    # os.system("cls")
    # printState(current.state)
    # print("\nf:{0:>2} - g:{1:>2} - h:{2:>2}".format(current.f, current.g, current.h))
        
    return bestFound

if __name__=="__main__":
    p = generatePuzzle((0, 1, 2, 3, 4, 5, 6, 7, 8), (0, 1, 2, 3, 4, 5, 6, 7, 8))
    printState(p)
    print(repr(p))