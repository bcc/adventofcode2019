#!/usr/bin/env python3

import sys, math

moonvel = ([0,0,0], [0,0,0], [0,0,0], [0,0,0])

# ex1
# <x=-1, y=0, z=2>
# <x=2, y=-10, z=-7>
# <x=4, y=-8, z=8>
# <x=3, y=5, z=-1>
moonpos = ([-1,0,2], [2,-10,-7], [4,-8,8], [3,5,-1])

# ex2
# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>
# moonpos = ([-8,-10,0], [5,5,10], [2,-7,3], [9,-8,-3])

# p2 ex
# <x=-8, y=-10, z=0>
# <x=5, y=5, z=10>
# <x=2, y=-7, z=3>
# <x=9, y=-8, z=-3>
moonpos = ([-8,-10,0], [5,5,10], [2,-7,3], [9,-8,-3])


# mine
# <x=5, y=13, z=-3>
# <x=18, y=-7, z=13>
# <x=16, y=3, z=4>
# <x=0, y=8, z=8>
moonpos = ([5,13,-3], [18,-7,13], [16,3,4], [0,8,8])

seen={}
axisperiod = {}
axisstart = {}
steps = 0
gotmoons = 0
go = True

while go:

    for axis in range(0, 3):
        # Save state for each axis, when we see a repeat then we probably have a period and offset for that moon.
        state = "%d: %d,%d,%d,%d,%d,%d,%d,%d" % (axis, moonpos[0][axis], moonpos[1][axis], moonpos[2][axis], moonpos[3][axis], moonvel[0][axis],moonvel[1][axis],moonvel[2][axis],moonvel[3][axis])
        if state in seen and not axis in axisperiod:
            print(steps, state, seen[state])
            axisperiod[axis] = (steps - seen[state])
            axisstart[axis] = seen[state]
            print(axis, axisstart[axis], axisperiod[axis])
            gotmoons += 1
        seen[state] = steps

    for moon in range(0, len(moonpos)):
        # Update velocity
        for pair in range(0, len(moonpos)):
            if pair == moon:
                continue
            for coord in range(0,3):
                if moonpos[moon][coord] < moonpos[pair][coord]:
                    moonvel[moon][coord] += 1
                elif moonpos[moon][coord] > moonpos[pair][coord]:
                    moonvel[moon][coord] -= 1

    # update position
    for moon in range(0, len(moonpos)):
        for coord in range(0,3):
            moonpos[moon][coord] += moonvel[moon][coord]

    steps += 1

    if steps % 100000 == 0:
        print("steps: " + str(steps) + "...")

    if gotmoons == 3:
        go = False

# inefficient, but it'll do.
def lcm(numbers):
    snum = sorted(numbers)
    bigly = snum.pop(-1)
    current = bigly
    c = range(0, len(snum))
    while True:
        test = True
        for n in c:
            if current % snum[n] != 0:
                test = False
            else:
                continue
        if test:
            return current
        current += bigly

print(lcm((axisperiod[0],axisperiod[1],axisperiod[2])))