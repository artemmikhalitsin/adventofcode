with open("day1input.txt") as input:
    directions = input.read().split(', ')
    #0 = N, 1 = E, 2 = S, 3 = W
    compass = 0
    blocks = [0,0,0,0]
    for direction in directions:
        turn = direction[0]
        steps = int(direction[1:])
        if (turn == 'R'):
            compass += 1
        if (turn == 'L'):
            compass -= 1
        blocks[compass % 4] += steps
    #|N-S| + |E-W|
    print abs(blocks[0] - blocks[2]) + abs(blocks[1] - blocks[3])
