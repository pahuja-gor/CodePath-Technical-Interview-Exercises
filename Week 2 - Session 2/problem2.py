"""
Given an array containing some duplicated numbers, return the sum of all instances of a duplicated number.
"""
def find_duplicate(arr):
  pass


# DO NOT MODIFY
def run_tests():
    for args, expected in [
        (test_1, result_1),
        (test_2, result_2),
        (test_3, result_3),
    ]:
        result = find_duplicate(args)
        if result != expected:
            raise ValueError(
                f'For arguments {args}, we expected {expected} but your code gave {result}'
            )
        else:
          print("Test case passed for find_duplicate")


test_1 = [1,1,2,2,3,4,4]
test_2 = [1,2,3,1,3]
test_3 = [1,2,3,4,5,1,2,4,5]

result_1 = 14
result_2 = 8
result_3 = 24
