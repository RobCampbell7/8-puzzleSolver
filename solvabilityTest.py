def inversionCount(state):
    invCount = 0
    for i in range(9):
        for j in range(i + 1, 9):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                invCount += 1
    return invCount

def solvable(start, goal):
    if inversionCount(start) % 2 == inversionCount(goal) % 2:
        return True
    else:
        return False

s1 = (0, 1, 2, 3, 4, 5, 6, 7, 8)
s2 = (0, 2, 1, 3, 4, 5, 6, 7, 8)
print("s1 - " + str(inversionCount(s1)))
print("s2 - " + str(inversionCount(s2)))