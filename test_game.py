#!/usr/bin/env python
# Tue 2013-07-30 22:01:05 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the game class."""

import unittest
from kmg.monopoly import game
from kmg.monopoly import player

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
    

class TestGame(unittest.TestCase):
  def setUp(self):
    self.player0 = player.Player('Kirk', player.HAT)
    self.player1 = player.Player('Spock', player.CAR)
    self.player2 = player.Player('McCoy', player.THIMBLE)

    self.game = game.Game([self.player0, self.player1, self.player2])
    self.random = FakeRandom()
    self.game.dice.random = self.random

  def test_start(self):
    self.assertNotEqual(self.game, None)
    self.assertEqual(self.game.turn, 0)

  def test_next(self):
    self.game.next_turn()
    self.assertEqual(self.game.turn, 1)
    self.game.next_turn()
    self.assertEqual(self.game.turn, 2)
    self.game.next_turn()
    self.assertEqual(self.game.turn, 0)
    self.game.next_turn()
    self.assertEqual(self.game.turn, 1)

  def test_roll(self):
    self.assertEqual(self.game.turn, 0)
    self.random.push(4)
    self.random.push(2)
    die1, die2, roll = self.game.roll()
    self.assertEqual(self.game.player_list[0].position, 6)
    self.assertEqual(self.game.turn, 1)

  def test_current_player(self):
    self.assertEqual(self.game.current_player, self.player0)
    self.game.turn = 1
    self.assertEqual(self.game.current_player, self.player1)
    self.game.turn = 2
    self.assertEqual(self.game.current_player, self.player2)

  def test_player_position_change(self):
    self.assertEqual(self.game.turn, 0)
    self.game.player_list[0].position = 11
    self.random.push(4)
    self.random.push(5)

    die1, die2, roll = self.game.roll()
    self.assertEqual(roll, 9)
    self.assertEqual(self.game.player_list[0].position, 20)


if __name__ == '__main__':
  unittest.main()

