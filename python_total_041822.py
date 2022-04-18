#!/usr/bin/python

import mymodule041822

class longweekend():
  extra_dayoff = "Yes extra day off!!!"
  extra_stuff_done = "Yes extra stuff done !!!"
 
  def __init__(self, whichday, dowhat):
    self.whichday = whichday
    self.dowhat = dowhat

  def location(self, where):
    print("During Easter Super Longweekend on " + self.whichday + " Activities like " + self.dowhat + " at " + where + " which is really meaningful ")

l1 = longweekend("Fri", "Vacuum, Clean All 4 bathrooms, and Clean side yard!!!") 

print(l1.dowhat)

l1.location("Home")

class longweekend2(longweekend):
  pass

l2 = longweekend2("Sat", "Hiking")
l2.location("Lake Chbot")
print(l2.whichday)

#function
# return is a keyword

#def addsum(a, b):
#  return a + b

#print(addsum(2, 3))

def hello(name):
  print("Your name is: " + name)

hello("Jordan")

# run method inside mymodule

mymodule041822.greeting("Peter")

# while

grade = 8 
print("You are in grade: " + str(grade) + "now")


while grade < 12:
  grade += 1
  print("You will be attending grade next: " + str(grade))

print("Congras, You ready for college next")

# dict

thisdict = {
  "Mon": "One",
  "Tue": "Two",
  "Wed": "Three"
}

#for loop

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

# add item in dict

thisdict["Thurs"] = "Four"
print(thisdict)

# remove dict item using pop method

thisdict.pop("Wed")
print(thisdict)

# find out length of a dict using length fuction

print(len(thisdict))

# test in dict

if "Thurs" in thisdict:
  print("Thurs in thisdict")
else:
  print("Thurs NOT in thisdict")

# try & except

today = "Mon"

try:
  print(today)
except:
  print("today is NOT defined")

# list

g = ["F", "G", "A"]
h = ["B", "G", "D"]

# get rif of duplicate items on both lists and generate a new list

for i in h:
  if i not in g:
    g.append(i)

print(g)
