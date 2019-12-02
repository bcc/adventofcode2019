#!/usr/bin/env python3

import sys

def r(inst, pos):
  return inst[inst[pos]]

def w(inst, pos, v):
  inst[inst[pos]] = v

def perform(inst):
  pos = 0
  while 1:
    if inst[pos] == 1:
      w(inst, pos+3, (r(inst,pos+1) + r(inst,pos+2)))
    elif inst[pos] == 2:
      w(inst, pos+3, (r(inst,pos+1) * r(inst,pos+2)))
    elif inst[pos] == 99:
      break
    pos += 4
  return inst[0]

# run with '2' argument for part2 result.
part2 = (len(sys.argv) == 2 and sys.argv[1] == '2')

for line in sys.stdin:
  instructions = line.rstrip().split(',')

  sx = {12}
  sy = {2}

  if part2:
    sx = range(0,99)
    sy = range(0,99)

  for x in sx:
    for y in sy:
      # reset the list
      ints = []
      for i in instructions:
        ints.append(int(i))

      # override values
      ints[1] = x
      ints[2] = y
      res = perform(ints)
      if part2:
        if(res == 19690720):
          print((100*x)+y)
      else:
        print(res)