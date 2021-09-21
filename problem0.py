def find_largest_element(num_1, num_2, num_3):
  """Given three numbers, return the largest."""

  return max([num_1, num_2, num_3])
  

# DO NOT MODIFY
def run_tests():
  for args, expected in [
    ([1, 2, 3], 3),
    ([1, 2, 1], 2),
    ([5, 2, 3], 5),
    ([1, 1, 1], 1),
    ([-1, -1, -1], -1),
  ]:
    result = find_largest_element(*args)
    if result != expected:
      raise ValueError(f'For arguments {args}, we expected {expected} but your code gave {result}')
