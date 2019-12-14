#!/usr/bin/env python3

import sys

# run with '2' argument for part2 result.
part2 = (len(sys.argv) == 2 and sys.argv[1] == '2')

class IntComp:
  def __init__(self, instructions, id):
    self.instructions = instructions
    self.pcounter = 0
    self.finished = 0
    self.ampid = id
    self.inputs = []
    self.relbase = 0

  def terminated(self):
    return self.finished

  def r(self, pos, mode):
    wantedpos = None
    if mode == 0:
      wantedpos = self.instructions[pos]
    elif mode == 1:
      wantedpos = pos
    elif mode == 2:
      wantedpos = self.relbase + self.instructions[pos]
    else:
      print ("Invalid mode!", mode)
      exit(1)

    # Allow reading from 'new' memory.
    if wantedpos >= len(self.instructions):
      for i in range(len(self.instructions), wantedpos+1):
        self.instructions.append(0)

    return int(self.instructions[wantedpos])


  def w(self, pos, v, mode):
    wantedpos = None
    if mode == 0:
      wantedpos = self.instructions[pos]
    elif mode == 1:
      wantedpos = pos
    elif mode == 2:
      wantedpos = self.relbase + self.instructions[pos]
    else:
      print ("Invalid mode!", mode)
      exit(1)

    # Allow writing to 'new' memory.
    if wantedpos >= len(self.instructions):
      for i in range(len(self.instructions), wantedpos+1):
        self.instructions.append(0)

    self.instructions[wantedpos] = v

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
        print ("input:", self.inputs)
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

      # adjust-relbase
      elif opcode == 9:
        c = self.r(pos_c, mode_c)
        self.relbase += c
        self.pcounter += 2

      # stop
      elif opcode == 99:
        self.finished = 1
        break

    return (outputs, self.finished)

def turnleft(dir):
  if dir == "U":
    return "L"
  elif dir == "L":
    return "D"
  elif dir == "D":
    return "R"
  elif dir == "R":
    return "U"

def turnright(dir):
  if dir == "U":
    return "R"
  elif dir == "R":
    return "D"
  elif dir == "D":
    return "L"
  elif dir == "L":
    return "U"

def moverobot(pos, dir):
  print("move:", pos)
  if dir == "U":
    pos[1] += 1
  elif dir == "L":
    pos[0] -= 1
  elif dir == "D":
    pos[1] -= 1
  elif dir == "R":
    pos[0] += 1
  print("move->:", pos)
  return pos

for line in sys.stdin:
    instructions = line.rstrip().split(',')

    ints = []
    grid = {0: {0: 0}}

    if part2:
      grid[0][0] = 1

    currentdir = "U"
    currentpos = [0,0]
    seen = {}
    minX = None
    maxX = None
    minY = None
    maxY = None

    for j in instructions:
      ints.append(int(j))

    robot = IntComp(ints,0)

    while not robot.terminated():
      #print("grid:", grid)
      currentcolour = 0
      if currentpos[0] in grid:
        if currentpos[1] in grid[currentpos[0]]:
          currentcolour = grid[currentpos[0]][currentpos[1]]
          print(">>", currentcolour)

      print("cc:", currentcolour, "pos:", currentpos, "dir:", currentdir)

      colour = robot.perform([currentcolour])
      if robot.terminated():
        continue

      # paint
      if currentpos[0] in grid:
        grid[currentpos[0]][currentpos[1]] = colour[0][0]
      else:
        t = {}
        t[currentpos[1]] = colour[0][0]
        grid[currentpos[0]] = t
      xy = ("%d,%d" % (currentpos[0], currentpos[1]))
      seen[xy] = 1

      # turn
      direction = robot.perform([])
      if direction[0][0] == 0:
        print("LEFT")
        currentdir = turnleft(currentdir)
      else:
        print("RIGHT")
        currentdir = turnright(currentdir)
      print("nc1:", colour[0][0], "npos", currentpos, "dir:", currentdir)

      # move
      currentpos = moverobot(currentpos, currentdir)
      print("nc2:", colour[0][0], "npos", currentpos, "dir:", currentdir)
      print("==============")

      if minX is None or currentpos[0] < minX:
        minX = currentpos[0]
      if minY is None or currentpos[1] < minY:
        minY = currentpos[1]
      if maxX is None or currentpos[0] > maxX:
        maxX = currentpos[0]
      if maxY is None or currentpos[1] > maxY:
        maxY = currentpos[1]

    if part2: 
      for y in range(maxY, minY-1, -1):
        row = ""
        for x in range(minX, maxX+1):
          currentcolour = 0
          if x in grid:
            if y in grid[x]:
              currentcolour = grid[x][y]
          if currentcolour == 1:
            row = row + "#"
          else:
            row = row + " "
        print(row)

    else:
      print(len(seen))

