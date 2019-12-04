#!/usr/bin/env python3

from collections import Counter

def is_ascending(x):
  a = [int(i) for i in str(x)]
  for x in range(0, len(a)-1):
    if a[x] > a[x+1]:
      return False
  return True

def is_double(x):
  a = [int(i) for i in str(x)]
  for x in range(0, len(a)-1):
    if a[x] == a[x+1]:
      return True
  return False

def password_count(x, y):
  cnt = 0
  num_list = []
  for i in range(x, y):
    if is_ascending(i) and is_double(i):
      num_list.append(i)
      cnt += 1
  return cnt, num_list

def password_count_part2(num_list):
  cnt = 0
  for i in num_list:
    a = [int(x) for x in str(i)]
    if 2 in list(Counter(a).values()):
      cnt += 1
  return cnt

cnt, num_list = password_count(284639, 748759)

print(cnt)
print(password_count_part2(num_list))
