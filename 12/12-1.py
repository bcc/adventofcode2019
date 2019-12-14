#!/usr/bin/env python3

import sys

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
moonpos = ([-8,-10,0], [5,5,10], [2,7,3], [9,-8,-3])

# mine
# <x=5, y=13, z=-3>
# <x=18, y=-7, z=13>
# <x=16, y=3, z=4>
# <x=0, y=8, z=8>
moonpos = ([5,13,-3], [18,-7,13], [16,3,4], [0,8,8])

for steps in range(0,1000):

    # Update velocity
    for moon in range(0, len(moonpos)):
        for pair in range(0, len(moonpos)):
            if pair == moon:
                continue
            for coord in range(0,3):
                if moonpos[moon][coord] < moonpos[pair][coord]:
                    moonvel[moon][coord] += 1
                elif moonpos[moon][coord] > moonpos[pair][coord]:
                    moonvel[moon][coord] -= 1

    # Update position
    for moon in range(0, len(moonpos)):
        for coord in range(0,3):
            moonpos[moon][coord] += moonvel[moon][coord]

total = 0
for moon in range(0, len(moonpos)):
    pot = abs(moonpos[moon][0]) + abs(moonpos[moon][1]) +  abs(moonpos[moon][2])
    kin = abs(moonvel[moon][0]) + abs(moonvel[moon][1]) +  abs(moonvel[moon][2])
    total += pot * kin
print (total)