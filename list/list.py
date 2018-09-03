import sys
import os
import random

grocery_list = ['juice', 'milk', 'egg',
               'tomato']

print('first item', grocery_list[0])
print('first item', grocery_list[1:3])

another_list = ['coffee', 'bread']
total_list = [grocery_list, another_list]
print(total_list)

del another_list[1]
print(total_list)

print(total_list[1][0])