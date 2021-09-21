def find_largest_index(arr):
  """Given an array of numbers, return the index of the largest number. Otherwise, return `None`.
  
  Break ties using the earliest index: [3, 5, 4, 5] should return 1, not 3
  """
  if arr:
    return arr.index(max(arr))
  else:
    return None

# DO NOT MODIFY
def run_tests():
  for args, expected in [
    ([[4, 5, 6]], 2),
    ([[]], None),
    ([[2]], 0),
    ([[1, -4, -1]], 0),
    ([[1, 2, 3, 4, 5, 4, 3, 2, 1]], 4),
  ]:
    result = find_largest_index(*args)
    if result != expected:
      raise ValueError(f'For arguments {args}, we expected {expected} but your code gave {result}')
