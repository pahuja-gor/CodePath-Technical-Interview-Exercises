# Talk about these problems and try to identify the runtimes.

def f1(my_list):
  if len(my_list) < 100:
    return False
  for i in range(100):
    if my_list[i] == 10:
      return True 
  return False

def f2(my_list):
  num_equal = 0
  n = len(my_list)
  for x in range(n):
    for y in range(n):
      if x == y:
        continue
      if my_list[x] == my_list[y]:
        num_equal += 1
  return num_equal

def f3(my_list):
  for i in range(len(my_list)):
    if my_list[i] == 10:
       break
  return my_list

def f4(my_list):
  for i in range(len(my_list)):
    if i == 10:
       break
  return my_list

def f5(my_list):
  pairs = []
  for i in range(len(my_list)):
    for j in range(i):
      pairs.append((my_list[j], my_list[i]))
  return pairs

def f6(my_list):
  total = 0
  n = len(my_list)
  while n > 0:
    for i in range(n):
      total += my_list[i]
    n = n // 2
  return total

def f7(my_list):
  total = 0
  i = 0
  while total < 100 and i < len(my_list):
    total += my_list[i]
    i += 1
  return total

def f8(my_list, index):
  if index >= len(my_list):
    return
  my_list[index] *= 100000000

def f9(my_list):
  total = 0
  n = 0
  while n < len(my_list):
    total += my_list[n]
    n += 2
  n = 1
  while n < len(my_list):
    total -= my_list[n]
    n += 2
  return total

def f10(my_list):
  total = 0
  for i in my_list:
    for j in range(5):
      total += i * j
  return total

def f11(my_list):
  total = 0
  for i in my_list:
    for j in my_list:
      for k in my_list:
        if i == j or i == k or j == k:
          continue
        total += i * j * k
  return total

def f12(my_list):
  i = 1000000
  total = 0
  while i < len(my_list):
    total += my_list[i]
  return total

def f13(n):
  i = 0
  s = 0
  while s <= n:
    i += 1
    s += i
  return i

def f14(my_list):
  total = 0
  for i in range(len(my_list)):
    for j in range(i * i):
      total += j
  return total

def f15(my_list):
  total = 0
  for i in my_list:
    for j in my_list:
      k = 1
      while k < len(my_list):
        total += i * j * k
        k *= 2
  return total

def f16(my_list):
  for element in my_list:
    if element - 5 in my_list:
      return True
  return False

def f17(my_list):
  return my_list.count(5)

def f18(my_list):
  return len(my_list)

def f19(my_list):
  return reversed(my_list)

def f20(my_list):
  return my_list.copy()


