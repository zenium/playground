'''
challenge question

You and your friends grab some powered swivel chairs and head out to a field. The goal of the game is to pass a ball from the lower left corner of the field to the upper right corner. How do you do this? The field is a 2-dimensional grid of people in swivel chairs. When two people next to each other in one of the four cardinal directions (up/down/left/right) are facing each other, they can pass the ball. Chairs swivel at a constant rate of 1/4 rotations (90 degrees) per second. However, some chairs may be broken or buggy - they might be spinning the wrong way or not at all. Given the spin states and starting orientations of the chairs, can you find the path with the fewest passes?

Input
=====

R: The number of rows in the field
C: The number of columns in each row

S: The spin direction of swivel chairs is given as a two-dimensional array of integers. The number at S[r][c] is 1 if the chair at (row: r, col: c) is rotating clockwise (the normal direction), 0 if not rotating (broken), or -1 if rotating counter-clockwise (the “wrong” direction).

O: The initial orientation of swivel chairs is given as a two-dimensional array of integers. The number at O[r][c] is 0 if the chair at (row: r, col: c) is initially facing right, 1 if up, 2 if left, or 3 if down.

Note: Assume that (0,0) represents the lower left corner, and that (r-1, c-1) represents the the upper right corner.

Output
======

An integer representing the minimum number of passes required to pass the ball from the lower left corner to the upper right corner.

If it is impossible to get to the upper left corner, return -1.

Example
=======

Example 1:

S:
1 1 1
1 1 1
1 1 1

O:
0 0 0
0 0 0
0 0 0

Answer: -1
Explanation: All chairs will always face the same way. No two people will ever face each other to allow a pass.


Example 2:

S:
0 1 0
0 1 0
0 1 0

O:
0 0 2
0 2 0
0 0 0

Answer: 4
Explanation: Pass right, up twice, right.

test cases

Input -› {"R": 3, "C": 3, "S": [[1, 1, 1], [1, 1, 1], [1, 1, 1]], "O": [[0, 0, 0], [0, 0, 0], [0, 0, 0]]}
Expected output -› -1
Input -› {"R": 3, "C": 3, "S": [[0, 1, 0], [0, 1, 0], [0, 1, 0]], "O": [[0, 0, 0], [0, 2, 0], [0, 0, 2]]}
Expected output -› 4
'''

import math
from copy import deepcopy

def answer(R, C, S, O):
    def has_path(r, c, d):
        if d == 0:
            t_r = r
            t_c = c+1
            t_d = 2
        else:
            t_r = r+1
            t_c = c
            t_d = 1
        # fix or spinning, fass pass
        if O[r][c] == d and O[t_r][t_c] == t_d:
            return True
        # source fixed, direction fail
        if S[r][c] == 0 and O[r][c] != d:
            return False
        # target fixed, direction fail
        if S[t_r][t_c] == 0 and O[t_r][t_c] != t_d:
            return False
        # source fixed, one side spinning pass
        if S[r][c] == 0 and S[t_r][t_c] != 0:
            return True
        # target fixed, one side spinning pass
        if S[t_r][t_c] == 0 and S[r][c] != 0:
            return True
        # both spinning, sync, wrong direction, fail
        # both spinning, sync, correct direction, pass
        if S[t_r][t_c] != 0 and S[r][c] != 0 and S[t_r][t_c] == S[r][c]:
            if abs(O[r][c] - O[t_r][t_c]) == 2:
                return True
        # both spinning, unsync pass
        if S[t_r][t_c] != 0 and S[r][c] != 0 and S[t_r][t_c] != S[r][c]:
            return True
        return False

    # get path matrix
    h_path = []
    for i in range(R):
        h_path += deepcopy([[0] * (C-1)])
    v_path = []
    for i in range(R-1):
        v_path += deepcopy([[0] * C])
    for i, m in enumerate(h_path):
        for j, v in enumerate(m):
            h_path[i][j] = has_path(i,j,0)
    for i, m in enumerate(v_path):
        for j, v in enumerate(m):
            v_path[i][j] = has_path(i,j,3)
    # print(h_path)
    # print(v_path)
    # walk through path matrix, O as touched points

    def walk(r, c, DR, count, oo):
        cc=count
        if DR == 'D':
            nbs = ((r+1,c,3), (r,c+1,0), (r,c-1,2), (r-1,c,1))
        if DR == 'R':
            nbs = ((r,c+1,0), (r+1,c,3), (r,c-1,2), (r-1,c,1))
        oo[r][c] = -1
        if r == R-1 and c == C-1:
            return -count
        for nb in nbs:
            if nb[0] <0 or nb[0]>=R or nb[1]<0 or nb[1]>=C or oo[nb[0]][nb[1]]<0:
                continue
            if nb[2] == 0 and not h_path[r][c]:
                continue
            elif nb[2] == 1 and not v_path[r-1][c]:
                continue
            elif nb[2] == 2 and not h_path[r][c-1]:
                continue
            elif nb[2] == 3 and not v_path[r][c]:
                continue
            else:                
                count = walk(nb[0], nb[1], DR, count+1, oo)
                if count<0 : return count
                else: count -= 1
        return count

    O2 = deepcopy(O)
    resultD = walk(0, 0, 'D', 0, O)
    resultR = walk(0, 0, 'R', 0, O2)
    result = min(-resultD, -resultR)
    if result == 0: return -1
    else: return result

def main():
    print(answer(3, 3, [[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 0], [0, 2, 0], [0, 0, 2]]))
    print(answer(3, 3, [[1, 1, 1], [1, 1, 1], [1, 1, 1]], [[0, 0, 0], [0, 0, 0], [0, 0, 0]]))
    print(answer(3, 3, [[0, 1, 0], [0, 1, 0], [0, 1, 0]], [[0, 0, 2], [0, 2, 0], [0, 0, 0]]))
    print(answer(5, 3, [[1, 1, 0], [1, 0, 0], [1,1,1],[0,0,1],[0, 1, 1]], [[0, 2, 2], [2,1,3],[0,2,0],[3, 2, 2], [0, 2, 0]]))
    print(answer(5,3, [[0,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,0]],[[0,2,0],[3,2,2],[0,2,0],[2,1,3],[0,2,2]]))

if __name__ == '__main__':
    main()

