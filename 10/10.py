#!/usr/bin/env python3

import sys, math

grid = []
for line in sys.stdin:
    line = line.rstrip()
    grid.append(line)

maxcount = 0
keepseen = {}
keepx = 0
keepy = 0

for x in range(0, len(grid[0])):
    for y in range(0, len(grid)):
        
        # skip space, as we're building on an asteroid.
        if grid[y][x] == ".":
            continue

        seen = {}
        count = 0

        for tx in range(0, len(grid[0])):
            for ty in range(0, len(grid)):
            
                # Well this is horrible, but we'll rethink later if it's too slow.

                # skip space.
                if grid[ty][tx] == ".":
                    continue
                
                # Skip self
                if tx == x and ty == y:
                    continue

                # Angle of the dangle
                asteroid_angle = math.atan2((y-ty),(x-tx))
                # rotate 90 degrees
                asteroid_angle = asteroid_angle - math.pi/2
                # wrap negative values
                if asteroid_angle < 0:
                    asteroid_angle = 2*math.pi + asteroid_angle

                asteroid_range = math.sqrt((x-tx)**2 + (y-ty)**2)

                if asteroid_angle in seen:
                    seen[asteroid_angle][asteroid_range] = 100*tx+ty # ("%d,%d" % (tx, ty))
                else: 
                    t = {}
                    t[asteroid_range] = 100*tx+ty # ("%d,%d" % (tx, ty))
                    seen[asteroid_angle] = t
                    count += 1

        # Note the best asteroid so far. 
        if count > maxcount:
            maxcount = count
            keepseen = seen
            keepx = x
            keepy = y

# part 1 answer.
print(maxcount)

zaps = 0
while len(keepseen) > 0:
    for laser in sorted(keepseen.keys()):
        zaps += 1
        this_angle = keepseen[laser]
        asteroids = sorted(this_angle)
        if zaps == 200:
            print(this_angle[asteroids[0]])
            exit
        #print(zaps, this_angle[asteroids[0]])
        del this_angle[asteroids[0]]
        if len(this_angle) == 0:
            del keepseen[laser]






            
                


