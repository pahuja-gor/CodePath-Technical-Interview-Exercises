""" Given a string representing a stock ticker, return the cheapest priced stock symbol.

Example: 
Given the following input:
"AAPL 313 GOOG 513 TSLA 58 BBY 22"

Your function should return:
"BBY"
"""
def cheapest_stock(stock_ticker):
  pass

def run_tests():
  for args, expected in [
    (test_1, result_1),
    (test_2, result_2),
    (test_3, result_3),
  ]:
    result = cheapest_stock(args)
    if result != expected:
      raise ValueError(f'For arguments {args}, we expected {expected} but your code gave {result}')
    else: 
      print("Test case for cheapest stock passed")

test_1 = "AAPL 313 GOOG 513 TSLA 58 BBY 22"
test_2 = "NBA 12 AAPL 313 GOOG 513 TSLA 58 BBY 222"
test_3 = "NBA 11 AAPL 55 GOOG 22 TSLA 44 BBY 22" 

result_1 = "BBY"
result_2 = "NBA"
result_3 = "NBA"