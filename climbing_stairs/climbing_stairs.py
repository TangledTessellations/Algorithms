#!/usr/bin/python

import sys

class ClimbingStairs:
  def __init__(self):
    self.cache = {0: 0, 1: 1, 2: 1}

  def climbing_stairs(self, n, uselessArray=None):
    if n < 2:
      return self.cache[n]
    elif n == 2:
      return self.cache[2]
    elif n in self.cache:
        return self.cache[n]
    else:
        self.cache[n] = self.climbing_stairs(n-1) + self.climbing_stairs(n-2) + self.climbing_stairs(n-3)
    return self.cache[n]

if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  stairs_object = ClimbingStairs()
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=stairs_object.climbing_stairs(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')