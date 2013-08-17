#!/usr/bin/env python
# Wed 2013-07-31 00:12:37 -0400
# Copyright (c) 2013 by Ken Guyton.  All Rights Reserved.

"""Play the game of Monopoly."""

import argparse
import sys

from kmg.monopoly import game
from kmg.monopoly import player
from kmg.monopoly import property as game_property

__author__ = 'Ken Guyton'

PIECE_MAP = {
  'hat': player.HAT,
  'car': player.CAR,
  'dog': player.DOG,
  'shoe': player.SHOE,
  'thimble': player.THIMBLE}

parser = argparse.ArgumentParser()
parser.add_argument('-p', '--players',
                    help=('A comma-separated list of players'
                          ' name:piece combinations.'))


def make_player_list(player_arg):
  """Take the player arg and make a list of players.

  Takes input like 'Kirk:Thimble,Spock:Car,McCoy:Hat' and turns it into
  a list of Player objects.

  Args:
    player_arg: str.  The input str.  A comma-delimited list of names.

  Returns:
    A list of str which are the players.
  """

  players = []

  names_pieces = player_arg.split(',')
  for name_piece in names_pieces:
    player_name, piece_name = name_piece.split(':')
    piece = PIECE_MAP[piece_name]
    players.append(player.Player(player_name, piece))

  return players


def play(the_game):
  """Roll and move the next player on their turn."""

  print('-' * 50)
  print('')
  player = the_game.player_list[the_game.turn]
  print('     Turn {0} as {1}'.format(player.name, player.piece.name))
  print('     Rolling...\n')
  die1, die2, roll = the_game.roll()

  print('     {0} + {1} = {2}!'.format(die1, die2, roll))

  if the_game.dice.doubles:
    print('** D O U B L E S ! **\n')
    if player.in_jail:
      print('*** GET OUT OF JAIL ***')
      player.leave_jail()
      player.doubles = 0

    if player.doubles == 2:
      player.doubles = 0
      player.go_to_jail()
      print('*** DOUBLES THIRD TIME.  GO TO JAIL! ***\n')
      the_game.next_turn()
    else:
      player.doubles += 1
      if player.doubles == 1:
        print('Doubles First time')
      elif player.doubles == 2:
        print('Doubles Second time')
  else:
      player.doubles = 0

  if player.in_jail:
    player.position = 10

  if player.passed_go and not (player.doubles == 2 and the_game.dice.doubles):
    print('\n     $$$ {0} Passed GO! $$$\n'.format(player.name))
    player.passed_go = False
    player.receive(200)

  print('     {0} Landed on {1}.'.format(
      player.name, the_game.board.location(player.position).name))

def display(the_game):
  """Display the status."""

  print('')
  print('')
  for player in the_game.player_list:
    print('{0} ({1}) on {2}: ${3}  (${4})'.format(
        player.name, player.piece.name,
        the_game.board.location(player.position).name,
        player.balance, player.net_worth())),
    if player.in_jail:
      print(' [IN JAIL]')
    else:
      print

    print('{0}\n'.format(player.properties))
  print('')


def handle_command(command, players_dict, all_properties):
  """Process a command string with a command and args.

  Args:
    command: str.  Space-delimited words.
    players_dict: dict. Indexed by lower() of player's name with the player
      objects as the values.
    all_properties: property.Properties.  The object containing all properties
      in the game.

  Returns:
    A str which is 'end' or 'roll' to indicate the next action.
  """

  if command == '':
    return 'roll'

  words = command.split()
  cmd = words[0]
  args = words[1:]

  if cmd == 'end':
    return 'end'
  elif cmd == 'pay':
    amount = int(args[2])
    if args[0] != 'bank':
      player_pay = players_dict[args[0].lower()]
      player_pay.pay(amount)
      player_pay_name = player_pay.name
    else:
      player_pay_name = 'BANK'

    if args[1] != 'bank':
      player_receive = players_dict[args[1].lower()]
      player_receive.receive(amount)
      player_receive_name = player_receive.name
    else:
      player_receive_name = 'BANK'
      
    print('\n     *** {0} paid {1} ${2} ***\n'.format(
        player_pay_name, player_receive_name, amount))

    return 'paid'
  elif cmd == 'bought':
    player_name = args[0]
    player = players_dict[args[0].lower()]

    short_name = args[1]
    the_property = all_properties.get(short_name)

    player.receive_property(the_property)

    print('\n     *** {0} bought {1} ***\n'.format(
        player.name, the_property.name))
  elif cmd == 'price':
    short_name = args[0]
    the_property = all_properties.get(short_name)

    print 'Price of {0} is ${1}.'.format(the_property.name, the_property.price)
  elif cmd == 'leave':
    player_name = args[1]
    player = players_dict[args[1].lower()]
    dist = args[2]
    player.position = 10 + int(dist)
    player.leave_jail()


def main():
  """Play."""

  args = parser.parse_args()
  players_list = make_player_list(args.players)
  players_dict = dict([(p.name.lower(), p) for p in players_list])
  all_properties = game_property.Properties()

  the_game = game.Game(players_list)

  display(the_game)
  command = raw_input('Command or Enter to roll: ')

  try:
    result = handle_command(command, players_dict, all_properties)
  except Exception as msg:
    print 'Exception: {}'.format(msg)
    
  while result != 'end':
    play(the_game)
    display(the_game)

    result = ''
    while result not in ('end', 'roll'):
      command = raw_input('Command or Enter to roll: ')
      try:
        result = handle_command(command, players_dict, all_properties)
      except Exception as msg:
        print 'Exception: {}'.format(msg)


if __name__ == '__main__':
  main()
