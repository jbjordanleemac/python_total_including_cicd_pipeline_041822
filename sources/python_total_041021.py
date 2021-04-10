#!/usr/bin/python

import json
import sys
import mymodule_041021
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-f", "--file", action="store", type="string", dest="file", help="<file>")

(options, args) = parser.parse_args()

if options.file == None:
  print("Please use help for options: ")
  sys.exit(1)
else:
  p = open("item", "ro")
  print(p.read())

print("Good Morning, Jordan !!!")

class longweekend():
  extra_time = "yes extra time"
  extra_stuff_done = "yes extra stuff done"
  
  def __init__(self, whatday, dowhat):
    self.whatday = whatday
    self.dowhat = dowhat
 
  def location(self, where):
    print("Activity like " + self.dowhat + " during longweekend on " + self.whatday + " at " + where + " is quite awesome ")

l1 = longweekend("Sat", "Hiking")
print(l1.dowhat)

l1.location("El Corte at Pennisa")

class longweekend2(longweekend):
  pass

l2 = longweekend2("Sun", "Go Church")
print(l2.whatday)

l2.location("Home")

# dict

thisdict = {
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

for a in thisdict:
  print(a)

for b in thisdict:
  print(thisdict[b])

for c in thisdict.keys():
  print(c)

for d in thisdict.values():
  print(d)

for e,f in thisdict.items():
  print(e,f)

print(thisdict)

thisdict["Thurs"] = "Four"
print(thisdict)

thisdict.update({"Thu": "Fou"})
print(thisdict)

thisdict.pop("Thu")
print(thisdict)

if "Thurs" in thisdict:
  print("Great news, Thurs is in the dict")
else:
  print("Well, it's fine that Thurs is NOT in the dict")

duplicated_dict = thisdict.copy()

print("dupicated copy of thisdict is " + str(duplicated_dict))

# length of dict

print("print out the length of thisdict " + str(len(thisdict)))

# list

thatlist = ["apple", "ball", "cat"]

for g in thatlist:
  print(g)

# reverse list

thatlist.reverse()
print(thatlist)

# append list

thatlist.append("door")
print(thatlist)

thatlist.remove("door")
print("after pop the last item on list now list becomes " + str(thatlist))

# how to append two lists 

h = ["A", "B", "C"]
i = ["D", "E", "F"]

for j in i:
  h.append(j)

print("so after append item on second list the origin first list becomes " + str(h))


# how to get rid of duplicate items in list

k = [5, 4, 3, 3, 5, 2, 1, 4, 5, 8, 9, 4]

print("All right the original list is " + str(k))


l = []

for m in k:
  if m not in l:
    l.append(m)

print("So after get rid of duplicated items list becomes " + str(l)) 

today = "Sat"

if today == "Sat":
  print("Today is a Sat")
else:
  print("Today is NOT a Sat")
  
# try except statement

try:
  print(today)
except:
  print("today is NOT defined")

try:
  print(ttoday)
except:
  print("ttoday is NOT defined")

# function

def hello(first, last):
  print("your name is " + str(first) + " " + str(last))

hello("Tom", "Hanks")
 
# arithmetics function

def addthemup(F, S):
  return F + S

print(addthemup(3, 4))

# run method from an imported module

mymodule_041021.greeting("Jordan")

# while loop

grade = 7

print("now youre in grade " + str(grade))

while grade <= 12:
  grade += 1
  print("you will be attending grade " + str(grade) + " next")

print("Congrats, you are ready for college next")


hour = 9

while hour <= 18:
  hour += 1
  print(" now we are at hour " + str(hour))
  if hour == 12:
    print("We're ready break for lunch")
    break

# format 1

firstname = "John"
lastname = "Doh"

print("Using format way 1 your name is {} {}".format(firstname, lastname))

# format 2

print("your name is %s" % firstname)

# json

n = '{"mon":"one", "tue":"two", "wed":"three"}'
o = json.loads(n)
print("Here is your json dict value: " + str(o["mon"]))

print("Here is your dict json value " +str(json.dumps(thisdict)))
