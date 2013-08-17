# Mon 2013-07-29 06:59:08 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Represent a player."""

import kmg.monopoly.property as game_property

class IllegalPieceError(Exception):
  """Raise if an illegal piece name was added."""


class Piece(object):
  """A game piece."""

  def __init__(self, name):
    """Create a game piece.

    Args:
      name: str.
    """

    if name in ('Hat', 'Car', 'Dog', 'Shoe', 'Thimble'):
      self.name = name
    else:
      raise IllegalPieceError('{0} is not a valid piece name.'.format(name))

  def __eq__(self, other):
    """Test if two pieces are equal.  Only the name matters."""

    return self.name == other.name


HAT = Piece('Hat')
CAR = Piece('Car')
DOG = Piece('Dog')
SHOE = Piece('Shoe')
THIMBLE = Piece('Thimble')


class Player(object):
  """A player with a name and piece on the board.

  Attributes:
    name: str. The name of the player.  Can be just a first name or whatever.
    piece: Piece. A piece object that's the player's chosen token.
    balance: int. The starting amount of money in dollars.
    location: int. The Board location.  0 = GO.
  """

  def __init__(self, name, piece):
    """Initialize the player.

    Args:
      name: str.
      piece. Piece.
    """

    self.name = name
    self.piece = piece
    self.balance = 1500
    self.position = 0
    self.properties = game_property.PlayerProperties()
    self.in_jail = False
    self.passed_go = False
    self.doubles = 0

  def pay(self, amount):
    """Remove money from the player's balance.

    Args:
      amount: int.  Dollars.
    """

    if amount > self.balance:
      raise NotEnoughMoneyError("The player doesn't have {0}.".format(amount))
    else:
      self.balance -= amount

  def receive(self, amount):
    """Add money to the player's balance.

    Args:
      amount: int.  Dollars.
    """

    self.balance += amount

  def move_to(self, position):
    """Move the player to a new position.

    Args:
      position: int.  : 
    """

    self.position = position

  def move(self, amount):
    """Move a number of steps to a new position."""

    self.position += amount
    if self.position > 39:
      self.position -= 40
      self.passed_go = True

  def go_to_jail(self):
    """Go to jail.  Change the in_jail state to True."""

    self.in_jail = True

  def leave_jail(self):
    """Leave jail.  Change in_jail to False."""

    self.in_jail = False

  def receive_property(self, a_property):
    """Receive a property.

    Args:
     property: game_property.Property.
    """

    self.properties.load(a_property)

  def give_property(self, short_name):
    """Give away a property.

    Args:
      short_name: str.  The short name of teh property.
    """

    self.properties.remove(short_name)

  def net_worth(self):
    """Report the net worth of the player.

    This is the total that doesn't consider mortgaged property.

    Returns:
      An int.
    """

    net = self.balance
    for a_property in self.properties.dict.values():
      net += a_property.price

    return net


    

