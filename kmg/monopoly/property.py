#!/usr/bin/env python
# Tue 2013-08-06 22:23:04 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Monopoly property."""

import collections

PROPERTIES = (
   ('Mediterranean', 'mediterranean', 60, 50),
   ('Baltic', 'baltic', 60, 50),
   ('Reading RR', 'readingrr', 200, 0),
   ('Oriental', 'oriental', 100, 50),
   ('Vermont', 'vermont', 100, 50),
   ('Connecticut', 'connecticut', 120, 50),
   ('st Charles', 'stcharles', 140, 100),
   ('Electric', 'electric', 150, 0),
   ('States', 'states', 140 , 100),
   ('Virginia', 'virginia', 160, 100),
   ('Pennsylvania RR', 'pennrr', 200, 0),
   ('St. James', 'stjames', 180, 100),
   ('Tennessee', 'tenn', 180, 100),
   ('New York', 'newyork', 200, 100),
   ('Kentucky', 'kentucky', 220, 150),
   ('Indiana', 'indiana', 220, 150),
   ('Illinois', 'illinois', 240, 150),
   ('B and O RR', 'bando', 200, 0),
   ('Atlantic', 'atlantic', 260, 150),
   ('Ventnor', 'ventnor', 260, 150),
   ('Water', 'water', 150, 0),
   ('Marvin Gardens', 'marvin', 280, 150),
   ('Pacific', 'pacific', 300, 200),
   ('North Carolina', 'northcarolina', 300, 200),
   ('Pennsylvania Ave', 'pennave', 320, 200),
   ('Short Line RR', 'shortline', 200, 0),
   ('Park Pl', 'park', 350, 200),
   ('Boardwalk', 'boardwalk', 400, 200),
)  


class Property(object):
  """A property in the Monopoly game."""

  def __init__(self, name, short_name, price, bldg_price):
    """Initialize the name and other attributes.

    Args:
      name: str. The Monopoly name of the property.
      short_name: str. A short, single-word name for the property, all
        lower case.
      price: int. Price of property on the board.
      bldg_price: int. Cost of each house and hotel.
    """

    self.name = name
    self.short_name = short_name
    self.mortgaged = False
    self.price = price
    self.bldg_price = bldg_price


class PlayerProperties(object):
  """An arbitrary collection of game properties."""

  def __init__(self):
    """Initialize the properties dict."""

    self.dict = collections.OrderedDict()

  def load(self, a_property):
    """Store a property indexed by its short name."""

    self.dict[a_property.short_name] = a_property

  def get(self, short_name):
    """Retrieve a property by its short name.

    Args:
      short_name: str.
    Returns:
      The property object.
    """

    return self.dict[short_name]

  def has(self, short_name):
    """Does this properties list contain a particular property.

    Args:
      short_name: str.
    Returns:
      A bool which is True if the short name is present.
    """

    return short_name in self.dict

  def remove(self, short_name):
    """Remove this property from the list.


    Args:
      short_name: str.
    """

    del self.dict[short_name]

  def __str__(self):
    """Return a str of a comma-separated list of the properties names."""

    return ', '.join([p.name for p in self.dict.values()])


class Properties(PlayerProperties):
  """The collection of all game properties."""

  def __init__(self):
    """Assign all of the properties."""

    self.dict = {}
    for name, short_name, price, bldg_price in PROPERTIES:
      self.load(Property(name, short_name, price, bldg_price))
