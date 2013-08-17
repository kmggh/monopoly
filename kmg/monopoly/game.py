#!/usr/bin/env python
# Tue 2013-07-30 22:06:42 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.


"""A Game."""

from kmg.monopoly import board
from kmg.monopoly import dice

class Game(object):
  """A Monopoly game."""

  def __init__(self, player_list):
    """Initialize the game.

    Args:
      player_list: list of Player.
    """

    self.player_list = player_list
    self.board = board.Board()
    self.turn = 0
    self.dice = dice.Dice()

  def next_turn(self):
    """Step the turn player index to the next player."""

    self.turn += 1
    if self.turn >= len(self.player_list):
      self.turn = 0

  def roll(self):
    """Roll and move the next player."""

    die1, die2, roll = self.dice.roll()
    self.current_player.move(roll)
    if not self.dice.doubles:
      self.next_turn()

    return die1, die2, roll

  @property
  def current_player(self):
    """The current player who's turn it is.

    Returns:
      The Player object.
    """

    return self.player_list[self.turn]
