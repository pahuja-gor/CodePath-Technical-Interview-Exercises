"""
Given an array that contains mostly unordered duplicates and one number that occurs only once, find the integer in the array that only occurs once and return that integer.

1. Find the elements that appear twice 
2. Find the element that appears once 
3. Return the element that appears once 

"""
def find_integer_in_array(arr):
  pass

# DO NOT MODIFY
def run_tests():
    for args, expected in [
        (test_1, result_1),
        (test_2, result_2),
        (test_3, result_3),
    ]:
        result = find_integer_in_array(args)
        if result != expected:
            raise ValueError(
                f'For arguments {args}, we expected {expected} but your code gave {result}'
            )
        else:
          print("Test case passed for find_integer_in_array")


test_1 = [1,1,2,2,3,4,4]
test_2 = [1,2,2,1,3]
test_3 = [1,2,3,4,5,1,2,3,5]

result_1 = 3
result_2 = 3
result_3 = 4
