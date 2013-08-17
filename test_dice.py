#!/usr/bin/env python
# Sun 2013-07-28 16:29:55 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test dice."""

import unittest
from kmg.monopoly import dice

__author__ = 'Ken Guyton'


class FakeRandom(object):
  """A fake random object for testing."""

  def __init__(self):
    """Keep a stack if numbers to return."""

    self.stack = []

  def push(self, value):
    """Push a value onto the stack."""

    self.stack.append(value - 1)

  def  randrange(self, limit):
    """Fake a randrange from random by popping the stack."""

    return self.stack.pop(0)
    

class DiceTest(unittest.TestCase):
  def setUp(self):
    self.dice = dice.Dice()
    self.random = FakeRandom()
    self.dice.random = self.random
    self.assertFalse(self.dice.doubles)

  def test_create(self):
    self.assertNotEqual(self.dice, None)

  def test_roll_one(self):
    self.random.push(6)
    self.assertEqual(self.dice._roll_one(), 6)

  def test_roll(self):
    self.random.push(6)
    self.random.push(4)
    self.assertEqual(self.dice.roll(), (6, 4, 10))
    self.assertFalse(self.dice.doubles)

  def test_roll(self):
    self.random.push(3)
    self.random.push(3)
    self.assertEqual(self.dice.roll(), (3, 3, 6))
    self.assertTrue(self.dice.doubles)


if __name__ == '__main__':
  unittest.main()

