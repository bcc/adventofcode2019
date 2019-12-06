#!/usr/bin/env python3

import sys

start = 125730
end = 579381

for x in range(start, end+1):
  s = str(x)
  fail=False
  double=False
  for n in range(0,5):
    if s[n] > s[n+1]:
      fail = True
      break
    if s[n] == s[n+1]:
      double = True
  if double and not fail:
    print(x)