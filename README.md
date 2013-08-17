A Monopoly Helper
=================

This is a simulator for the dice, money exchange and board movements
in the game of Monopoly, done as a programming exercise.  At the same
time, it might serve as an illustration of how a program evolves as
features are added and the code has to be re-simplified and
refactored.


To run
======

    ./play_monopoly --players John:hat,Marsha:thimble,Kirk:ship,Spock:shoe


Commands
========

When running **play_monopoly.py**, the game prompts for commands to be
entered, presumably by the banker.


Pay
---

**pay** *player1* *player2* *amount*

The **bank** can also be a player (paying or being paid).

pay john marsha 25


Bought
------

**bought**  *player*  *property*



Release Notes
=============


Release 0.1  
-----------

Banking, dice rolls, moving and buyging mostly work.  The play and
command handler code in the play_monopoly.py file is long and awkward.
It needs to be organized into smaller functions and classes.



Author
======

Ken Guyton
2013-08-16



