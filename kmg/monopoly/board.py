#!/usr/bin/env python
# Tue 2013-07-30 01:47:19 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.


"""A Monopoly Board."""

BOARD = (
   (0, 'Go'),
   (1, 'Mediterranean'),
   (2, 'Community Chest'),
   (3, 'Baltic'),
   (4, 'Income Tax'),
   (5, 'Reading RR'),
   (6, 'Oriental'),
   (7, 'Chance'),
   (8, 'Vermont'),
   (9, 'Connecticut'),
   (10, 'Jail'),
   (11, 'St Charles'),
   (12, 'Electric'),
   (13, 'States'),
   (14, 'Virginia'),
   (15, 'Pennsylvania RR'),
   (16, 'St James'),
   (17, 'Community Chest'),
   (18, 'Tennessee'),
   (19, 'New York'),
   (20, 'Free Parking'),
   (21, 'Kentucky'),
   (22, 'Chance'),
   (23, 'Indiana'),
   (24, 'Illinois'),
   (25, 'B and O RR'),
   (26, 'Atlantic'),
   (27, 'Ventnor'),
   (28, 'Water'),
   (29, 'Marvin'),
   (30, 'Go to Jail'),
   (31, 'Pacific'),
   (32, 'North Carolina'),
   (33, 'Community Chest'),
   (34, 'Pennsylvania Ave'),
   (35, 'Short Line RR'),
   (36, 'Chance'),
   (37, 'Park'),
   (38, 'Luxury Tax'),
   (39, 'Boardwalk'),
)

class Location(object):
  """A particular location on the board."""

  def __init__(self, pos, name):
    """Set attributes to defaults.

    Args:
      pos: int.  From 0 to 39.
      name: str.  E.g., 'Go', 'Electric', 'Reading RR'.
    """

    self.name = name
    self.pos = pos


class Board(object):
  """A Monopoly Board with properties and other locations."""

  def __init__(self):
    """Initialize the board with names at their usual locations."""

    self.locations = []

    for index, name in BOARD:
      self.locations.append(Location(index, name))

  def location(self, position):
    """Return the location object for a position.

    Args:
      position: int. Starting with GO=0.
    """

    return self.locations[position]
