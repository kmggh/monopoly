#!/usr/bin/env python
# Tue 2013-07-30 01:45:51 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the board class."""

import unittest
from kmg.monopoly import board

__author__ = 'Ken Guyton'


class TestLocation(unittest.TestCase):
  def test_go(self):
    location = board.Location(0, 'Go')
    self.assertEqual(location.name, 'Go')
    self.assertEqual(location.pos, 0)
  

class TestBoard(unittest.TestCase):
  def setUp(self):
    self.board = board.Board()

  def test_create(self):
    self.assertNotEqual(self.board, None)

  def test_go(self):
    self.assertEqual(self.board.location(0).name, 'Go')
    self.assertEqual(self.board.location(35).name, 'Short Line RR')
    self.assertEqual(self.board.location(39).name, 'Boardwalk')


if __name__ == '__main__':
  unittest.main()
