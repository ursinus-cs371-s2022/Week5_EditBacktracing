import numpy as np

LEFT = 0
UP = 1
DIAG = 2

def backtrace(s1, s2, moves, path, solution = []):
    """
    Recursively backtrace through the arrows, and branch off
    if there are multiple options (ties) at particular locations

    Parameters
    ----------
    s1: string(M)
        First string
    s2: string(N)
        Second string
    moves: 3d array (M, N, [])
        A 2D array of lists of possible moves
    path: list of [i, j]
        A stack holding the path being recursively built
    solution: list of string
        A verbal description of the solution
    """
    [i, j] = path[-1]
    if i == 0 and j == 0:
        print("SOLUTION")
        for s in solution[::-1]:
            print("\t", s)
    else:
        for move in moves[i][j]:
            # Forks in the road (possible arrows to visit)
            inew = i
            jnew = j
            if move == LEFT:
                jnew -= 1
                solution.append("Adding {} to s1 (+1)".format(s2[jnew]))
            elif move == UP:
                inew -= 1
                solution.append("Deleting {} from s1 (+1)".format(s1[inew]))
            else:
                inew -= 1
                jnew -= 1
                if s1[i-1] != s2[j-1]:
                    solution.append("Swapping in {} for {} in s1 (+1)".format(s2[j-1], s1[i-1]))
                else:
                    solution.append("Matching {}".format(s2[j-1]))
            # Add this option
            path.append([inew, jnew])
            # recursively explore the next choices after this
            backtrace(s1, s2, moves, path, solution)
            # Pop off this option and try something else
            path.pop()
            solution.pop()

def edit(s1, s2):
    """
    An iterative, dynamic programming version of the string
    edit distance

    Parameters
    ----------
    s1: string of length M
        The first string to match
    s2: string of length N
        The second string to match
    
    Returns
    -------
    cost: int
        The cost of an optimal match
    paths: list of lists
        Each list 
    """
    M = len(s1)
    N = len(s2)
    # Create a 2D array with M+1 rows and N+1 columns
    # to store the costs
    table = np.zeros((M+1, N+1))
    # Fill in the base cases
    table[0, :] = np.arange(N+1)
    table[:, 0] = np.arange(M+1)

    # Make 2D array that stores a list of optimal moves.  There
    # will be multiple elements in the list if there are ties
    moves = []
    for i in range(M+1):
        moves.append([])
        for j in range(N+1):
            moves[i].append([])
    # Fill in the base cases
    for j in range(N+1):
        moves[0][j] = [0] # Move left if we're at the top row
    for i in range(M+1):
        moves[i][0] = [1] # Move up if we're at the left column
    
    # Do the dynamic programming to fill in the table and moves
    for i in range(1, M+1):
        for j in range(1, N+1):
            cost1 = table[i, j-1] + 1 # Delete the last character from s2
            cost2 = table[i-1, j] + 1 # Delete the last character from s1
            cost3 = table[i-1, j-1] # Match or swap both characters at the end
            if s1[i-1] != s2[j-1]:
                cost3 += 1
            table[i][j] = min(cost1, cost2, cost3)
            if table[i][j] == cost1:
                moves[i][j].append(LEFT)
            if table[i][j] == cost2:
                moves[i][j].append(UP)
            if table[i][j] == cost3:
                moves[i][j].append(DIAG)
    
    backtrace(s1, s2, moves, [[M, N]])

edit("school", "fools")
