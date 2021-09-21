import math

def factorial(num):
  """Given a number, calculate the factorial. All numbers >= 0
  
  The factorial of 4 is 4 * 3 * 2 * 1 == 24
  """
  return math.factorial(num)
  

# DO NOT MODIFY
def run_tests():
  for args, expected in [
    ([4], 24),
    ([3], 6),
    ([8], 40320),
    ([1], 1),
    ([0], 1),
  ]:
    result = factorial(*args)
    if result != expected:
      raise ValueError(f'For arguments {args}, we expected {expected} but your code gave {result}')
