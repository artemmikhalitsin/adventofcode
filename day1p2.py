
with open("day1input.txt") as input:
    directions = input.read().split(', ')
    #0 = N, 1 = E, 2 = S, 3 = W
    compass = 0
    blocks = [0,0,0,0]
    location = [0,0]
    visited = list()
    for direction in directions:
        turn = direction[0]
        steps = int(direction[1:])
        if (turn == 'R'):
            compass += 1
        if (turn == 'L'):
            compass -= 1
        #take steps one at a time
        while(steps > 0):
            blocks[compass % 4] += 1
            steps -= 1
            #store current location as (X, Y)
            location = [blocks[1]-blocks[3], blocks[0]-blocks[2]]
            if location in visited:
                print "Easter Bunny HQ Located..."
                print "...Sending coordinates...."
                print "...Calculating distance..."
                print "...HQ located %d blocks away" % (abs(location[0]) + abs(location[1]))
                quit()
            else:
                visited.append(location)
