#!/usr/bin/env python3

import sys

# run with '2' argument for part2 result.
part2 = (len(sys.argv) == 2 and sys.argv[1] == '2')

objects = {}
orbits = {}

for line in sys.stdin:
  line = line.rstrip()
  bodies = line.split(')')
  objects[bodies[0]] = 1
  objects[bodies[1]] = 1
  orbits[bodies[1]] = bodies[0]

traces = {}

count = 0
for object in objects:
  trace = []
  if object == "COM":
    continue
  n = orbits[object]
  ocount = 1
  trace.append(object)
  trace.append(n)
  while n != "COM":
    n = orbits[n]
    trace.append(n)
    ocount += 1
  count += ocount
  traces[object] = trace

print(count)

want1='YOU'
want2='SAN'
if want1 in traces and want2 in traces:
  pos = -1
  t1 = traces[want1][pos]
  t2 = traces[want2][pos]
  # work from COM (array[-1]) towards each planet, until we find the point they diverge
  while t1 == t2:
    pos -= 1
    t1 = traces[want1][pos]
    t2 = traces[want2][pos]
  # then return the remaining length of each branch
  len1 = len(traces[want1]) + pos
  len2 = len(traces[want2]) + pos
  print(len1+len2)