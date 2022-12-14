# -*- coding: utf-8 -*-
"""Text-based Adventure Game.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cCxbzzdeyGGN1Lq1LSppnoBXNzZPdqIB
"""

# Create a local variable dictionary to hold all the location number with their description.

locationMap = {}

#read and open file locations.txt
file = open('locations.txt', 'r')
for i in file:
  l = i.split(',')
  locationMap[int(l[0])] = l[1]

direction = {}
directionFile = open('directions.txt', 'r')
for i in directionFile:
  l = i.split(',')
  if int(l[0]) in direction:
    direction[int(l[0])][l[1]] = l[2]
  else:
    direction[int(l[0])] = {l[1]: l[2]}

#@title Default title text
direction

current_location = 25

while(True):
  print(locationMap[current_location])

  available = direction[current_location]

  for i in available:
    print('You can go ' + i[0])

  user_input = input('where do you want to go?')
  if user_input not in available:
    print('direction is not available for you')
  else:
    current_location = int(available[user_input].strip())

  if current_location == 0:
    print('game over')
    break

