#/usr/bin/env python3

def mass_calculator(x):
  calc = x // 3
  calc -= 2
  return calc

def mass_calculator_recursive(x):
  fuel = mass_calculator(x)
  temp = fuel
  while temp > 5:
    fuel += mass_calculator(temp)
    temp = mass_calculator(temp)
  return fuel

with open('day1_input.txt') as fp:
  fuel_cnt = 0
  recursive_fuel_cnt = 0
  for line in fp:
    fuel_cnt += mass_calculator(int(line))
    recursive_fuel_cnt += mass_calculator_recursive(int(line))
fp.close()

print(fuel_cnt)
print(recursive_fuel_cnt)
