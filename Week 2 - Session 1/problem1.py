""" Given a string representing a stock ticker, return the stocks alphabetized.

Example: 
Given the following input:
"AAPL 313 GOOG 513 TSLA 58 BBY 22"

Your function should return:
"AAPL 313 BBY 22 GOOG 513 TSLA 58"
["AAPL 313", "BBY 22", "GOOG 513", "TSLA 58"]
1. Split out pairs of stock names, prices 
2. Sort by name 
3. Return as a string

"""
def alphabetical_stocks(stock_ticker):
  elems = stock_ticker.split(" ")
  return elems
    

def run_tests():
  for args, expected in [
    (test_1, result_1),
    (test_2, result_2),
    (test_3, result_3),
  ]:
    result = alphabetical_stocks(args)
    if result != expected:
      raise ValueError(f'For arguments {args}, we expected {expected} but your code gave {result}')
    else: 
      print("Test case for alphabetical_stocks passed")

test_1 = "AAPL 313 GOOG 513 TSLA 58 BBY 22"
test_2 = "BBOY 278 AAPL 313 GOOG 513 TSLA 58 BBY 22"
test_3 = "BBOY 2 AAPL 313 GOOG 1400 TSLA 58 BBY 22" 

result_1 = "AAPL 313 BBY 22 GOOG 513 TSLA 58"
result_2 = "AAPL 313 BBOY 278 BBY 22 GOOG 513 TSLA 58"
result_3 = "AAPL 313 BBOY 2 BBY 22 GOOG 1400 TSLA 58"

