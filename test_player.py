#!/usr/bin/env python
# Mon 2013-07-29 06:49:26 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the player class."""

import unittest
from kmg.monopoly import player
from kmg.monopoly import property as game_property

__author__ = 'Ken Guyton'

NAME = 'John'


class TestPiece(unittest.TestCase):
  def test_created(self):
    self.assertEqual(player.Piece('Car'), player.CAR)

  def test_eq(self):
    piece1 = player.Piece('Hat')
    piece2 = player.Piece('Hat')
    self.assertEqual(piece1, piece2)


class TestPlayer(unittest.TestCase):
  def setUp(self):
    self.player = player.Player(NAME, player.HAT)

  def test_create(self):
    self.assertNotEqual(self.player, None)
    self.assertEqual(self.player.balance, 1500)
    self.assertEqual(self.player.position, 0)
    self.assertEqual(self.player.piece, player.HAT)
    self.assertTrue(isinstance(self.player.properties,
                               game_property.PlayerProperties))
    self.assertFalse(self.player.in_jail)
    self.assertFalse(self.player.passed_go)
    self.assertEqual(self.player.doubles, 0)

  def test_pay(self):
    self.player.pay(100)
    self.assertEqual(self.player.balance, 1400)

  def test_receive(self):
    self.player.receive(100)
    self.assertEqual(self.player.balance, 1600)

  def test_moveto(self):
    self.player.move_to(10)
    self.assertEqual(self.player.position, 10)

  def test_move(self):
    self.player.move_to(10)
    self.player.move(5)
    self.assertEqual(self.player.position, 15)

  def test_go_to_jail(self):
    self.player.go_to_jail()
    self.assertTrue(self.player.in_jail)
    self.player.leave_jail()
    self.assertFalse(self.player.in_jail)

  def test_receive_property(self):
    properties = game_property.Properties()
    self.player.receive_property(properties.get('stjames'))
    self.assertEqual(self.player.properties.get('stjames'),
                     properties.get('stjames'))

  def test_give_property(self):
    properties = game_property.Properties()
    self.player.receive_property(properties.get('stjames'))
    self.player.give_property('stjames')
    self.assertFalse(self.player.properties.has('stjames'))

  def test_net_worth(self):
    properties = game_property.Properties()
    self.assertEqual(self.player.net_worth(), 1500)
    self.player.receive_property(properties.get('stjames'))
    self.assertEqual(self.player.net_worth(), 1680)


if __name__ == '__main__':
  unittest.main()



