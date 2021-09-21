import copy

def reverse_only_positives(arr):
  """Given an array of numbers, reverse only the positive numbers.
  
  For instance, [-3, -2, -1, 0, 1, 2, 3] -> [-3, -2, -1, 0, 3, 2, 1]

  Hint: l is a copy of arr, which I think will help solve the problem.
  """
  # TODO: Modify and return l
  l = copy.deepcopy(arr)
  pos_index = 0
  for val in l:
    if val > 0:
      pos_index = l.index(val)
      break
  return l[:pos_index] + l[pos_index:][::-1]

  

def run_tests():
  assert reverse_only_positives([-3, -2, -1, 0, 1, 2, 3]) == [-3, -2, -1, 0, 3, 2, 1]
  # Write your own tests
