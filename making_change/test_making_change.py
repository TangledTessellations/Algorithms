import unittest
from making_change import MakingChange 

class Test(unittest.TestCase):

  def setUp(self):
    self.denominations = [1, 5, 10, 25, 50]

  def test_making_change_small_amount(self):
    change_maker = MakingChange()
    
    self.assertEqual(change_maker.making_change_recursive(0, self.denominations), 1)
    self.assertEqual(change_maker.making_change_recursive(1, self.denominations), 1)
    self.assertEqual(change_maker.making_change_recursive(5, self.denominations), 2)
    self.assertEqual(change_maker.making_change_recursive(10, self.denominations), 4)
    self.assertEqual(change_maker.making_change_recursive(20, self.denominations), 9)
    self.assertEqual(change_maker.making_change_recursive(30, self.denominations), 18)
    self.assertEqual(change_maker.making_change_recursive(100, self.denominations), 292)
    self.assertEqual(change_maker.making_change_recursive(200, self.denominations), 2435)
    self.assertEqual(change_maker.making_change_recursive(300, self.denominations), 9590)

  def test_making_change_large_amount(self):
    change_maker = MakingChange()

    self.assertEqual(change_maker.making_change(350, self.denominations), 16472)
    self.assertEqual(change_maker.making_change(400, self.denominations), 26517)
    self.assertEqual(change_maker.making_change(1000, self.denominations), 801451)
    self.assertEqual(change_maker.making_change(2000, self.denominations), 11712101)
    self.assertEqual(change_maker.making_change(5000, self.denominations), 432699251)
    self.assertEqual(change_maker.making_change(10000, self.denominations), 6794128501)


if __name__ == '__main__':
  unittest.main()