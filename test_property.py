#!/usr/bin/env python
# Tue 2013-08-06 22:20:01 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Test the property class."""

import unittest
from kmg.monopoly import property

__author__ = 'Ken Guyton'


class TestProperty(unittest.TestCase):
  def setUp(self):
    self.property = property.Property('St. James', 'stjames', 180, 100)

  def test_create(self):
    self.assertNotEqual(self.property, None)
    self.assertTrue(isinstance(self.property, property.Property))
    self.assertFalse(self.property.mortgaged)
    self.assertEqual(self.property.name, 'St. James')
    self.assertEqual(self.property.short_name, 'stjames')
    self.assertEqual(self.property.price, 180)
    self.assertEqual(self.property.bldg_price, 100)


class TestProperties(unittest.TestCase):
  def setUp(self):
    self.properties = property.Properties()

  def test_create(self):
    self.assertNotEqual(self.properties, None)
    self.assertTrue(isinstance(self.properties, property.Properties))

  def test_stjames(self):
    a_property = self.properties.get('stjames')
    self.assertEqual(a_property.name, 'St. James')
    self.assertEqual(a_property.short_name, 'stjames')
    self.assertEqual(a_property.price, 180)
    self.assertEqual(a_property.bldg_price, 100)

  def test_bando(self):
    a_property = self.properties.get('bando')
    self.assertEqual(a_property.name, 'B and O RR')
    self.assertEqual(a_property.short_name, 'bando')
    self.assertEqual(a_property.price, 200)
    self.assertEqual(a_property.bldg_price, 0)


class TestPlayerProperties(unittest.TestCase):
  def setUp(self):
    self.player_properties = property.PlayerProperties()
    self.properties = property.Properties()

  def test_create(self):
    self.assertNotEqual(self.player_properties, None)
    self.assertTrue(isinstance(self.player_properties,
                               property.PlayerProperties))

  def test_load(self):
    a_property = self.properties.get('stjames')
    self.player_properties.load(a_property)
    again_property = self.player_properties.get('stjames')
    self.assertEqual(a_property, again_property)

  def test_has(self):
    a_property = self.properties.get('stjames')
    self.player_properties.load(a_property)
    self.assertTrue(self.player_properties.has('stjames'))

  def test_remove(self):
    a_property = self.properties.get('stjames')
    self.player_properties.load(a_property)
    self.player_properties.remove('stjames')
    self.assertFalse(self.player_properties.has('stjames'))

  def test_str(self):
    self.player_properties.load(self.properties.get('stjames'))
    self.player_properties.load(self.properties.get('newyork'))
    self.player_properties.load(self.properties.get('tenn'))

    self.assertEqual(str(self.player_properties),
                     'St. James, New York, Tennessee')


if __name__ == '__main__':
  unittest.main()
    
