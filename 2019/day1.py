#/usr/bin/env python

def mass_calculator(x):
  calc = (x // 3)
  calc -= 2
  return int(calc)

with open('input.txt') as fp:
  fuel_list = 0
  for line in fp:
    fuel_list += mass_calculator(int(line))
fp.close()
print(fuel_list)

def mass_calculator_recursive(x):
  fuel = mass_calculator(x)
  temp = fuel
  while temp > 5:
    fuel += mass_calculator(int(temp))
    temp = mass_calculator(int(temp))
  return fuel

with open('input.txt') as fp:
  fuel_cnt = 0
  for line in fp:
    fuel_cnt += mass_calculator_recursive(int(line))
fp.close()
print(fuel_cnt)

