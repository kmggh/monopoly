#!/usr/bin/env python
# Sun 2013-07-28 23:02:13 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Keep rolling the dice to test the class."""

import argparse
import sys
from kmg.monopoly import dice

parser = argparse.ArgumentParser()
parser.add_argument('--nolist', help='List the rolls.', action='store_true')
parser.add_argument('--num', help='Number of times to roll', type=int,
                    default=100)
parser.add_argument('--freq', help='Report count frequencies',
                    action='store_true')


def report_counts(counts, num):
  """Report on the frequencies in counts."""

  for i in range(1, 12):
    index = i + 1
    count = counts[index] * 36.0 / num
    print('{0} {1:0.8f}'.format(index, count))


def main():
  args = parser.parse_args()
  my_dice = dice.Dice()

  counts = {}
  for i in range(12):
    counts[i + 1] = 0

  for unused_i in range(args.num):
    roll = my_dice.roll()
    counts[roll] += 1
    if not args.nolist:
      sys.stdout.write('{0} '.format(roll)),

  if not args.nolist:
    print('')

  if args.freq:
    report_counts(counts, args.num)


if __name__ == '__main__':
  main()
