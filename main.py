import os
import time
from aStar import solve, solvable

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

if __name__=="__main__":
    start = ( 7, 2, 4,
              5, 0, 6,
              8, 3, 1 )
    # start = ( 3, 0, 8,
    #           6, 2, 1,
    #           7, 5, 4 )
    goal =  ( 0, 1, 2,
              3, 4, 5,
              6, 7, 8 )

    if solvable(start, goal):
        solution = solve(start, goal)
        input("Solving complete - press enter to view solution...")
        for state in solution.path():
            os.system("cls")
            printState(state)
            time.sleep(0.5)
    else:
        print("This permutation is not solvable")