#!/usr/bin/python

import sys

class MakingChange:
  def __init__(self):
    self.cache = []
  
  def making_change(self, amount, denominations):
    self.cache = [0 for i in range(amount + 1)]
    self.cache[0] = 1
    for coin in denominations:
      for higher_amount in range(coin, amount + 1):
        self.cache[higher_amount] = self.cache[higher_amount] + self.cache[higher_amount - coin]
    return self.cache[amount]


if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  change_maker = MakingChange()
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=change_maker.making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")