#!/usr/bin/python

def conv(val):
  try:
    return int(val)
  except ValueError:
    try:
      return float(val)
    except ValueError:
      return str(val)

def add2(arg1, arg2):
  arg1conv = conv(arg1)
  arg2conv = conv(arg2)

  if isinstance(arg1conv, str) or isinstance(arg2conv, str):
    arg1conv = str(arg1conv)    
    arg2conv = str(arg2conv)
  
  return arg1conv + arg2conv    
  
