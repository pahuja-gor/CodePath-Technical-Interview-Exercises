# This function has an O(N^2) runtime. Can you rewrite it such that it has an O(N) runtime, but the same input and output?

def f(my_list):
  total = 0
  for i in range(len(my_list)):
    for j in range(i, len(my_list)):
      total += my_list[j]
  return total

def new_f(my_list):
  return