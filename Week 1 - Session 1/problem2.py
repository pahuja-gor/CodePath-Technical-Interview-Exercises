def find_largest_element(arr):
  """Given an array of numbers, return the largest number. Otherwise, return `None`"""
  if not arr:
    return None
  return max(arr)
  

# DO NOT MODIFY
def run_tests():
  for args, expected in [
    ([[4, 5, 6]], 6),
    ([[]], None),
    ([[2]], 2),
    ([[1, -4, -1]], 1),
    ([[1, 2, 3, 4, 5, 4, 3, 2, 1]], 5),
  ]:
    result = find_largest_element(*args)
    if result != expected:
      raise ValueError(f'For arguments {args}, we expected {expected} but your code gave {result}')
