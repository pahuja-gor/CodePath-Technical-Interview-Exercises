def removes_less_than_k(arr, k):
  """Given an array of numbers, removes all numbers less than k.
  
  For instance, [0, 4, 3, 2, 1, 5], 3 -> [4, 3, 5]
  
  Hint: You can create a new array to return if you think it will help
  """
  return [val for val in arr if val >= k]


def run_tests():
  assert removes_less_than_k([0, 4, 3, 2, 1, 5], 3) == [4, 3, 5]
  # Write your own tests
