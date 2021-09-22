""" 
Given an array of stock ticker strings, where one string represents a day of trading, write a function that finds the max profit for that stock. 

Example: 
Given the following input:
"TSLA 33"
"TSLA 23"
"TSLA 34"

Your function should return:
"TSLA 11"
Because if you buy TSLA on day 2 and sell on day 3 you get a profit of 11
"""

def calculate_max_profit_for_stock(trading_days):
  pass

def run_tests():
    for args, expected in [
        (test_1, result_1),
        (test_2, result_2),
        (test_3, result_3),
    ]:
        result = calculate_max_profit_for_stock(args)
        if result != expected:
            raise ValueError(
                f'For arguments {args}, we expected {expected} but your code gave {result}'
            )
        else:
          print("Test case for calculate_max_profit_for_stock passed")


test_1 = [
    "TSLA 33", "TSLA 23",
    "TSLA 34"
]
test_2 = [
    "AAPL 114", "AAPL 113",
    "AAPL 112"
]
test_3 = [
    "GOOG 545", "GOOG 533",
    "GOOG 556"
]

result_1 = "TSLA 11"
result_2 = "AAPL 0"
result_3 = "GOOG 23"
