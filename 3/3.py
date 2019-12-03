#!/usr/bin/env python3

import sys

cgrid = {}
grids = []

for line in sys.stdin:
  grid = {}

  instructions = line.rstrip().split(',')
  pos_x = 0
  pos_y = 0
  steps = 0
      
  for i in instructions:
    dir = i[0]
    num = int(i[1:])
    for j in range(0,num):
      steps += 1
      if dir == 'U':
        pos_y += 1
      elif dir == 'D':
        pos_y -= 1
      elif dir == 'L':
        pos_x -= 1
      elif dir == 'R':
        pos_x += 1
      s = "%d,%d" % (pos_x, pos_y)
      if s not in grid:
        grid[s] = steps
    #print (dir, num, "grid:", pos_x, pos_y)

  grids.append(grid)
  # curses, it's possible for a wire to cross itself. Dirty bodge. 
  for pos, c in grid.items():
    if pos in cgrid:
      cgrid[pos] += 1
    else:
      cgrid[pos] = 1

least = None
leastSteps = None
for pos, c in cgrid.items():
  if c > 1: 
    coords = pos.split(',')
    dist = abs( int(coords[0]) ) + abs( int(coords[1]) )
    allsteps = grids[0][pos] + grids[1][pos]

    if least is None or dist < least:
      least = dist
    if leastSteps is None or allsteps < leastSteps:
      leastSteps = allsteps
    #print(c, coords, dist, least, leastSteps)

print(least, leastSteps)