#!/usr/bin/python

import sys
import calc

#print(len(sys.argv))

argnum = len(sys.argv) - 1

if argnum == 2:
  print(calc.add2(sys.argv[1], sys.argv[2]))
  sys.exit(0)
else:
  print("add2val usage is ./add2val arg1 arg2 !!!")
  sys.exit(1)
 
