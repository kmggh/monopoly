#!/usr/bin/env python
# Tue 2013-07-30 21:31:59 -0400
# Copyright (c) 2012, 2013 by Ken Guyton. All Rights Reserved.

"""Run all tests."""

import os

TESTS = ('dice', 'player', 'board', 'game', 'property')


def run_test(test_name):
  """Run a particular test."""

  print 'Running test_%s...' % test_name
  os.system('./test_%s.py' % test_name)
  print


def main():
  """Run all tests."""

  for test_name in TESTS:
    run_test(test_name)


if __name__ == '__main__':
  main()
