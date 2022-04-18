#!/usr/bin/python

import unittest
import calc

class TestCalc(unittest.TestCase):
  """
  Test the add function from the calc library
  """  

  def test_add_integers(self):
    """
    Test that the addition of two integers returns the correct total
    """
    result = calc.add2(3, 4)
    self.assertEqual(result, 7)

  def test_add_floats(self):
    """
    Test that the addition of two floats return the correct result
    """
    result = calc.add2("2.3", "4.5")
    self.assertEqual(result, 6.8)

  def test_add_strings(self):
    """
    Test adding two strings become one string
    """
    result = calc.add2("hello", "there")
    self.assertEqual(result, "hellothere")
 
  def test_add_string_integer(self):
    """
    Test add string and integer return them back as a concatened string in which interger being conver as string
    """
    result = calc.add2("join", 5)
    self.assertEqual(result, "join5")

  def test_add_string_float(self):
    """
    Test add one string and float number together return back as one concatened string in which float being convert to string
    """
    result = calc.add2("glue", "4.6")
    self.assertEqual(result, "glue4.6")

if __name__ == '__main__':
  unittest.main() 
