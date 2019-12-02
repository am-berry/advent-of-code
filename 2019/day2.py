#!/usr/bin/env python 

def program_alarm(intcode, noun, verb):
  curr_ptr = 0
  a = len(intcode)
  intcode[1] = noun
  intcode[2] = verb
  while curr_ptr < a:
    if intcode[curr_ptr] == 1:
      new_idx = intcode[curr_ptr+3]
      intcode[new_idx] = intcode[intcode[curr_ptr+1]]+intcode[intcode[curr_ptr+2]]
      curr_ptr += 4
    elif intcode[curr_ptr] == 2:
      new_idx = intcode[curr_ptr+3]
      intcode[new_idx] = intcode[intcode[curr_ptr+1]]*intcode[intcode[curr_ptr+2]]
      curr_ptr += 4
    elif intcode[curr_ptr] == 99:
      return intcode[0]
    else:
      return "Something went wrong"
  return intcode[0]  

intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]

print(program_alarm(intcode, 12, 2))

for noun in range(0,100):
  for verb in range(0,100):
    intcode = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,10,19,1,6,19,23,1,13,23,27,1,6,27,31,1,31,10,35,1,35,6,39,1,39,13,43,2,10,43,47,1,47,6,51,2,6,51,55,1,5,55,59,2,13,59,63,2,63,9,67,1,5,67,71,2,13,71,75,1,75,5,79,1,10,79,83,2,6,83,87,2,13,87,91,1,9,91,95,1,9,95,99,2,99,9,103,1,5,103,107,2,9,107,111,1,5,111,115,1,115,2,119,1,9,119,0,99,2,0,14,0]
    if program_alarm(intcode, noun, verb) == 19690720:
      print(100*noun+verb)



