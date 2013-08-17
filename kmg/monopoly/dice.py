# Sun 2013-07-28 16:43:40 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Emulate dice."""

import random

class Dice(object):
  """The dice emulator."""

  def __init__(self):
    """Initialize the random module, so it can be replaced for testing."""

    self.random = random
    self.doubles = False

  def _roll_one(self):
    """Randomly roll one die."""
    return self.random.randrange(6) + 1

  def roll(self):
    """Return the results of rolling two dice.

    Returns:
      A tuple of three, the first die, second die, and the sum.
    """

    die1 = self._roll_one()
    die2 = self._roll_one()
    self.doubles = die1 == die2

    return (die1, die2, die1 + die2)
