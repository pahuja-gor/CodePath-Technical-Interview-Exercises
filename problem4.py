def reverse_list(arr):
  """Given an array of numbers, reverse the list.

  Hint: You can create a new array to return if you think it will help
  """
  return arr[::-1]
  

# DO NOT MODIFY
def run_tests():
  for args, expected in [
    ([[4, 5, 6]], [6, 5, 4]),
    ([[]], []),
    ([[2]], [2]),
    ([[1, -4, -1]], [-1, -4, 1]),
    ([[1, 2, 3, 4, 5, 4, 3, 2, 0]], [0, 2, 3, 4, 5, 4, 3, 2, 1]),
  ]:
    result = reverse_list(*args)
    if result != expected:
      raise ValueError(f'For arguments {args}, we expected {expected} but your code gave {result}')
