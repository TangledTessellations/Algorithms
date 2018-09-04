#!/usr/bin/python

import sys

class MakingChange:
  def __init__(self):
    self.cache = []
  
  # Iterative solution
  def making_change(self, amount, denominations):
    self.cache = [0 for i in range(amount + 1)]
    self.cache[0] = 1
    for coin in denominations:
      for higher_amount in range(coin, amount + 1):
        self.cache[higher_amount] = self.cache[higher_amount] + self.cache[higher_amount - coin]
    return self.cache[amount]

  # Recursive solution
  def making_change_recursive(self, amount, denominations):
    # If we get to zero, we've found a solution
    if amount == 0:
      return 1
    # If we've gone past zero, we haven't found a solution
    if amount < 0:
      return 0
    # We're out of coins but there's still amount left, no solution
    if (len(denominations) <= 0 and amount > 0):
      return 0
    
    return self.making_change_recursive(amount - denominations[0], denominations) + self.making_change_recursive(amount, denominations[1:])

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  change_maker = MakingChange()
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=change_maker.making_change_recursive(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")