#!/usr/bin/env python3

import sys

class Amp:
  def __init__(self, instructions, id):
    self.instructions = instructions
    self.pcounter = 0
    self.finished = 0
    self.ampid = id
    self.inputs = []

  def terminated(self):
    return self.finished

  def r(self, pos, mode):
    if mode == 0:
      return int(self.instructions[self.instructions[pos]])
    else: 
      return int(self.instructions[pos])

  def w(self, pos, v, mode):
    if mode == 0:
      self.instructions[self.instructions[pos]] = v
    else:
      print("broken!", self.instructions, pos, v, mode)

  def perform(self, inputs):
    outputs = []

    for inp in inputs:
      self.inputs.append(inp)

    while 1:
      fullopcode = self.instructions[self.pcounter]
      opcode = fullopcode % 100
      mode_c = (int(fullopcode/100) % 10)
      mode_b = (int(fullopcode/1000) % 10)
      mode_a = (int(fullopcode/10000) % 10)
      pos_c = self.pcounter+1
      pos_b = self.pcounter+2
      pos_a = self.pcounter+3

      #print(self.ampid, "OP:", opcode, mode_c, mode_b, mode_a, pos_c, pos_b, pos_a)

      # add
      if opcode == 1:
        val = self.r(pos_c,mode_c) + self.r(pos_b,mode_b)
        self.w(pos_a, val, mode_a)
        self.pcounter += 4

      # multiply
      elif opcode == 2:
        val = self.r(pos_c, mode_c) * self.r(pos_b, mode_b)
        self.w(pos_a, val, mode_a)
        self.pcounter += 4

      # input
      elif opcode == 3:
        #print ("input:", self.inputs)
        store = self.inputs.pop(0)
        self.w(pos_c, store, mode_c)
        self.pcounter += 2

      # output
      elif opcode == 4:
        outputs.append(self.r(pos_c, mode_c))
        self.pcounter += 2
        #print("output:", outputs)
        return (outputs, self.finished)

      # jump-if-true
      elif opcode == 5:
        t = self.r(pos_c, mode_c)
        if t != 0:
          self.pcounter = self.r(pos_b, mode_b)
        else:
          self.pcounter += 3

      # jump-if-false
      elif opcode == 6:
        t = self.r(pos_c, mode_c)
        if t == 0:
          self.pcounter = self.r(pos_b, mode_b)
        else:
          self.pcounter += 3

      # less-than
      elif opcode == 7:
        c = self.r(pos_c, mode_c)
        b = self.r(pos_b, mode_b)
        if c < b:
          self.w(pos_a, 1, mode_a)
        else:
          self.w(pos_a, 0, mode_a)
        self.pcounter += 4

      # equals
      elif opcode == 8:
        c = self.r(pos_c, mode_c)
        b = self.r(pos_b, mode_b)
        if c == b:
          self.w(pos_a, 1, mode_a)
        else:
          self.w(pos_a, 0, mode_a)
        self.pcounter += 4

      # stop
      elif opcode == 99:
        self.finished = 1
        break

    return (outputs, self.finished)

def runamps(instructions, phase):
  amps = []
  r = [0]

  # Set up amps
  for i in range(0, 5):
    ints = []
    for j in instructions:
      ints.append(int(j))

    input = [phase[i], r[0]]
    a = Amp(ints,i)
    ret = a.perform(input)
    amps.append(a)
    r = ret[0]

  # Loop over amps until they're done processing.
  finished = 0
  while 1:
    if finished:
      break
    for i in range(0, 5):
      input = [r[0]]
      ret = amps[i].perform(input)
      if amps[i].terminated():
        finished = 1
      else:
        r = ret[0]
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

f = open(sys.argv[1], "r")
line = f.readline()
instructions = line.rstrip().split(',')

print(runamps(instructions,[9,7,8,5,6]))

for a in permute([5,6,7,8,9]):
  ret = runamps(instructions, a)
  print("%s %s" % (ret[0], a))
