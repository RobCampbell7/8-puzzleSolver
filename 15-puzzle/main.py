import os
import time
from aStar import solve, solvable

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

if __name__=="__main__":
    start = (
         5,  3,  7, 15, 
         1, 10,  4,  9,
         0, 13,  2,  6,
         8, 12, 11, 14
    )
    goal = (
         0,  1,  2,  3, 
         4,  5,  6,  7,
         8,  9, 10, 11,
        12, 13, 14, 15
    )

    if solvable(start, goal):
        solution = solve(start, goal)
        stepNo = len(solution.path())
        print("Solving complete - " + repr(stepNo - 1) + " moves to solve")
        input("press enter to view solution...")
        for state in solution.path():
            os.system("cls")
            printState(state)
            time.sleep(0.5)
    else:
        print("This permutation is not solvable")