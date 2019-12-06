#!/usr/bin/env python3

import sys

start = 125730
end = 579381

for x in range(start, end+1):
  s = str(x)
  fail=False
  double=False
  matchcount = 1
  for n in range(0,5):
    if s[n] > s[n+1]:
      fail = True
      break
    if s[n] == s[n+1]:
      matchcount += 1
    else:
      if matchcount == 2: 
        double = True
      matchcount = 1

  if matchcount == 2: 
    double = True
  if double and not fail:
    print(x)