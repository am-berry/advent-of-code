#!/usr/bin/env python3

def opcode_params(code):
  formatted_code = str(code).zfill(5)
  op = int(formatted_code[-2:])
  params = [int(x) for x in list(formatted_code)[:-2][::-1]]
  return op, params

def program_alarm_2(intcode, inp):
  intcode = [int(x) for x in intcode]
  ptr = 0

  while True:
    digits = [int(x) for x in str(intcode[ptr])]
    op = (0 if len(digits)==1 else digits[-2])*10+digits[-1]
    digits = digits[:-2]
    if op == 1:
      while len(digits) <3:
        digits = [0] + digits
      i1, i2, i3 = intcode[ptr+1], intcode[ptr+2], intcode[ptr+3]
      intcode[i3] = (intcode[i1] if digits[2]==0 else i1) + (intcode[i2] if digits[1]==0 else i2)
      ptr += 4
    elif op == 2:
      while len(digits) <3:
        digits = [0] + digits  
      i1, i2, i3 = intcode[ptr+1], intcode[ptr+2], intcode[ptr+3]          
      intcode[i3] = (intcode[i1] if digits[2]==0 else i1) * (intcode[i2] if digits[1]==0 else i2)
      ptr += 4
    elif op == 3:
      i1 = intcode[ptr+1]
      intcode[i1] = inp
      ptr += 2
    elif op == 4:
      i1 = intcode[ptr+1]
      print(intcode[i1])
      ptr += 2
    elif op == 5:
      while len(digits) <2:
        digits = [0] + digits
      i1, i2 = intcode[ptr+1], intcode[ptr+2]
      if (i1 if digits[1] == 1 else intcode[i1])!=0:
        ptr = (i2 if digits[0] == 1 else intcode[i2])
      else:
        ptr += 3
    elif op == 6:
      while len(digits) < 2:
        digits = [0] + digits
      if (intcode[ptr+1] if digits[1] == 1 else intcode[intcode[ptr+1]])==0:
        ptr = (intcode[ptr+2] if digits[0] == 1 else intcode[intcode[ptr+2]])
      else:
        ptr += 3
    elif op == 7:
      while len(digits) <3:
        digits = [0] + digits
      if (intcode[ptr+1] if digits[2] == 1 else intcode[intcode[ptr+1]]) < (intcode[ptr+2] if digits[1] == 1 else intcode[intcode[ptr+2]]):
        intcode[intcode[ptr+3]] = 1
      else:
        intcode[intcode[ptr+3]] = 0
      ptr += 4
    elif op == 8:
      while len(digits) <3:
        digits = [0] + digits
      if (intcode[ptr+1] if digits[2] == 1 else intcode[intcode[ptr+1]]) == (intcode[ptr+2] if digits[1] == 1 else intcode[intcode[ptr+2]]):
        intcode[intcode[ptr+3]] = 1
      else:
        intcode[intcode[ptr+3]] = 0
      ptr += 4
    else:
      assert op == 99
      break


with open('day5_input.txt') as f:
  inpt = f.readline().split(',')
  print(program_alarm_2(intcode = inpt, inp = 1))
  print(program_alarm_2(intcode = inpt, inp = 5))
