import sys
import os
import random

for x in range(0,10) :
    print(x)

for y in range (0,10,2):
    print(y)

adj = ['red', 'green', 'black']
objects = ['ball', 'phone', 'book']
for a in adj:
    for b in objects:
        print(a,b)

random_num = random.randrange(0,100)
while(random_num != 23):
    print(random_num)
    random_num = random.randrange(0,100)

i = 1
while(i < 6) :
    print(i)
    if i == 3:
        break
    i += 1

i = 1
while(i < 6) :
    i += 1
    if i == 3:
        continue
    print(i)

def tri_recursion(k):
  if(k>0):
    result = k+tri_recursion(k-1)
    print(result)
  else:
    result = 0
  return result

print("\n\nRecursion Example Results")
tri_recursion(3)