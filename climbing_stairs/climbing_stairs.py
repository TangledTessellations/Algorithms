#!/usr/bin/python

import sys

class ClimbingStairs:
  def __init__(self):
    self.cache = None

  def climbing_stairs(self, n, rangeIn=None):
    if rangeIn:
      self.cache = {i: 0 for i, val in enumerate(rangeIn)}
    else:
      self.cache = {i: 0 for i in range(n + 1)}

    return self.climbing_stairs_cache(n)

  def climbing_stairs_cache(self, n):
    if n < 2:
      self.cache[n] = 1
      return self.cache[n]
    elif n == 2:
      self.cache[2] = 2
      return self.cache[2]
    else:
      if self.cache[n] != 0:
        return self.cache[n]
      else:
        self.cache[n] = self.climbing_stairs_cache(n-1) + self.climbing_stairs_cache(n-2) + self.climbing_stairs_cache(n-3)
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