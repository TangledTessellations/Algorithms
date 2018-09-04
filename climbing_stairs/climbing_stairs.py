#!/usr/bin/python

import sys

# With recursion/memoization
def climbing_stairs(n, cache=None):
  if not cache:   
    cache = [0 for i in range(n+1)] # If cache has no value, default cache to an array of zeroes
  if n < 2:
      return 1
  elif n ==2:
      return 2
  elif cache[n] > 2: # If more than 2 steps, return the value of cache
      return  cache[n] # cache[n] is number of ways we can get to n
  cache[n] = climbing_stairs(n-1, cache) + climbing_stairs(n-2, cache) + climbing_stairs(n-3, cache) # figure it out yourself, god
  return cache[n]

# Using iteration, arrayIn not used but necessary to meet testing requirements
def climbing_stairs_iter(n, arrayIn=None):
  answer = 0
  first = 1
  second = 1
  third = 2
  if n == 2:
    return 2
  elif n <= 1:
    return 1
  for i in range(2, n):
    answer = first + second + third
    first = second
    second = third
    third = answer
  return answer

  
if __name__ == "__main__":
  # Test out your implementation from the command line
  # with `python climbing_stairs.py [n]` with different n values
  stairs_object = ClimbingStairs()
  if len(sys.argv) > 1:
    num_stairs = int(sys.argv[1])
    print("There are {ways} ways for a child to jump {n} stairs.".format(ways=stairs_object.climbing_stairs_iter(num_stairs), n=num_stairs))
  else:
    print('Usage: climbing_stairs.py [num_stairs]')