""" 
Given an array of stock ticker strings, where one string represents a day of trading, write a function that finds the greatest window of return between two stocks and return the stock, the buy index, and the sell index

https://coolconversion.com/math/percentage-change-calculator/_23_to_34_percent-increase-or-decrease

Example: 
Given the following input:
"AAPL 114 GOOG 545 TSLA 33"
"AAPL 113 GOOG 533 TSLA 23"
"AAPL 112 GOOG 556 TSLA 34"

Your function should return:
"2 3 TSLA"
Which means, buy TSLA on day 1 and sell on day 2 for a 47% increase
"""


def best_trading_window(trading_days):
    pass


def run_tests():
    for args, expected in [
        (test_1, result_1),
        (test_2, result_2),
        (test_3, result_3),
    ]:
        result = best_trading_window(args)
        if result != expected:
            raise ValueError(
                f'For arguments {args}, we expected {expected} but your code gave {result}'
            )
        else:
          print("Test case for best_trading_window passed")


test_1 = [
    "AAPL 114 GOOG 545 TSLA 33", "AAPL 113 GOOG 533 TSLA 23",
    "AAPL 112 GOOG 556 TSLA 34"
]
test_2 = [
    "AAPL 112 GOOG 545 TSLA 42", "AAPL 150 GOOG 533 TSLA 23",
    "AAPL 132 GOOG 556 TSLA 30"
]
test_3 = [
    "AAPL 112 GOOG 545 TSLA 19", "AAPL 150 GOOG 533 TSLA 20",
    "AAPL 132 GOOG 556 TSLA 30"
]

result_1 = "2 3 TSLA"
result_2 = "1 2 AAPL"
result_3 = "1 3 TSLA"
