#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  max_batches = float("inf")
  for ingredient_name in recipe.keys():
    if ingredient_name not in ingredients:
      return 0
    elif ingredients[ingredient_name] // recipe[ingredient_name] < max_batches:
      max_batches = ingredients[ingredient_name] // recipe[ingredient_name]
  return max_batches

if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 200, 'butter': 100, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))