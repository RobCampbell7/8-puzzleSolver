import os
import time
from aStar import solve, solvable, printState


if __name__=="__main__":
    start = (5, 6, 7, 8, 0, 4, 2, 1, 3)
    # start = (
    #     0, 8, 7,
    #     6, 5, 4,
    #     3, 2, 1
    # )
    # start = (
    #     7, 2, 4,
    #     5, 0, 6,
    #     8, 3, 1
    # )
    goal = (
        0, 1, 2,
        3, 4, 5,
        6, 7, 8
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