#!/usr/bin/env python3

def manhattan(a):
  return abs(a[0])+abs(a[1])

def wire_locations(path_list):
  x, y = 0, 0
  loc_list = set()

  for instr in path_list.split(','):
    operations = int(instr[1:].strip())
    for i in range(operations):
      if instr[0] == 'R':
        x+=1
      elif instr[0] == 'L':
        x-=1
      elif instr[0] == 'U':
        y+=1
      else:
        y-=1
      loc_list.add((x,y))
  return loc_list

def min_intersection(a, b):
  pos_1 = wire_locations(a)
  pos_2 = wire_locations(b)
  intersections = pos_1.intersection(pos_2)
  return min([manhattan(x) for x in intersections])

def wire_locations_count(path_list):
  x, y = 0, 0
  loc_list = set()
  steps_dict = {}
  cts_count = 0
  
  for instr in path_list.split(','):
    operations = int(instr[1:].strip())
    for i in range(operations):
      if instr[0] == 'R':
        x+=1
      elif instr[0] == 'L':
        x-=1
      elif instr[0] == 'U':
        y+=1
      else:
        y-=1
      cts_count += 1
      loc_list.add((x,y))
      steps_dict[(x,y)] = cts_count
  return loc_list, steps_dict

def min_intersection_count(a,b):
  pos_1, steps_1 = wire_locations_count(a)
  pos_2, steps_2 = wire_locations_count(b)
  intersections = pos_1.intersection(pos_2)
  curr_min_steps = max(steps_1.values()) + max(steps_2.values())
  for intersection in intersections:
    if steps_1[intersection] + steps_2[intersection] < curr_min_steps:
      curr_min_steps = steps_1[intersection] + steps_2[intersection]
  return curr_min_steps

with open('day3_input.txt') as f:
  inp = f.readlines()
  a = inp[0] 
  b = inp[1]
  print(min_intersection(a,b))
  print(min_intersection_count(a,b))
