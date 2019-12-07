#!/usr/bin/env python3

import sys

def r(inst, pos, mode):
  if mode == 0:
    return int(inst[inst[pos]])
  else: 
    return int(inst[pos])

def w(inst, pos, v, mode):
  if mode == 0:
    inst[inst[pos]] = v
  else:
    print("broken!", inst, pos, v, mode)

def perform(inst, inputs):
  pos = 0
  outputs = []
  while 1:
    incr = 4
    fullopcode = inst[pos]
    opcode = fullopcode % 100
    mode_c = (int(fullopcode/100) % 10)
    mode_b = (int(fullopcode/1000) % 10)
    mode_a = (int(fullopcode/10000) % 10)
    pos_c = pos+1
    pos_b = pos+2
    pos_a = pos+3

    #print("OP:", opcode, mode_c, mode_b, mode_a, pos_c, pos_b, pos_a)

    # add
    if opcode == 1:
      val = r(inst,pos_c,mode_c) + r(inst,pos_b,mode_b)
      w(inst, pos_a, val, mode_a)

    # multiply
    elif opcode == 2:
      val = r(inst,pos_c, mode_c) * r(inst,pos_b, mode_b)
      w(inst, pos_a, val, mode_a)

    # input
    elif opcode == 3:
      store = inputs.pop(0)
      w(inst, pos_c, store, mode_c)
      incr = 2

    # output
    elif opcode == 4:
      outputs.append(r(inst,pos_c, mode_c))
      incr = 2

    # jump-if-true
    elif opcode == 5:
      t = int(r(inst,pos_c, mode_c))
      if t != 0:
        pos = int(r(inst,pos_b, mode_b))
        incr = 0
      else:
        incr = 3

    # jump-if-false
    elif opcode == 6:
      t = int(r(inst,pos_c, mode_c))
      if t == 0:
        pos = int(r(inst,pos_b, mode_b))
        incr = 0
      else:
        incr = 3

    # less-than
    elif opcode == 7:
      c = int(r(inst,pos_c, mode_c))
      b = int(r(inst,pos_b, mode_b))
      if c < b:
        w(inst, pos_a, 1, mode_a)
      else:
        w(inst, pos_a, 0, mode_a)

    # equals
    elif opcode == 8:
      c = int(r(inst,pos_c, mode_c))
      b = int(r(inst,pos_b, mode_b))
      if c == b:
        w(inst, pos_a, 1, mode_a)
      else:
        w(inst, pos_a, 0, mode_a)

    # stop
    elif opcode == 99:
      break

    pos += incr
  return outputs

def runamps(ints, phase):
  r = [0]
  for i in range(0, 5):
    input = [phase[i], r[0]]
    r = perform(ints, input)
  return(r)

def permute(nums):
  result_perms = [[]]
  for n in nums:
    new_perms = []
    for perm in result_perms:
      for i in range(len(perm)+1):
        new_perms.append(perm[:i] + [n] + perm[i:])
        result_perms = new_perms
  return result_perms

inputs = []
for line in sys.stdin:
  for item in line.rstrip().split(','):
    inputs.append(item)

f = open(sys.argv[1], "r")
line = f.readline()
instructions = line.rstrip().split(',')

ints = []
for i in instructions:
  ints.append(int(i))

for a in permute([4,3,2,1,0]):
  ret = runamps(ints, a)
  print("%s %s" % (ret[0], a))
