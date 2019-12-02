#!/usr/bin/env python3

import sys

def calcmass (mass):
  mass = int(mass / 3) - 2
  return mass

# run with '2' argument for part2 result.
part2 = (len(sys.argv) == 2 and sys.argv[1] == '2')

sum = 0
for line in sys.stdin:
    line = int(line.rstrip())
    cm = calcmass(line)
    sum += cm
    if part2:
        while cm > 0:
            cm = calcmass(cm)
            if cm > 0:
                sum += cm

print(sum)
