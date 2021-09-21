def sum_pairs(arr):
  """Given an array of numbers, sums each pair of elements from outermost
  to innermost parts of the array.
  
  For instance, [0, -2, 1, 2, -4, 10] -> [10, -6, 3]
    where 10 is is the sum of 0, 10
    where -6 is is the sum of -2, -4
    where 3 is is the sum of 1, 2
    
  Hint: You can create a new array to return if you think it will help
  """
  return [val + arr[::-1][arr.index(val)] for val in arr][:len(arr) // 2]

def run_tests():
  assert sum_pairs([0, -2, 1, 2, -4, 10]) == [10, -6, 3]
  # Write your own tests
