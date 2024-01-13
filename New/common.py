#!/usr/bin/python
#
# Copyright 2015 - Jonathan Gordon
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
# KIND, either express or implied.

RESOURCE_GOLD 	= "$"
RESOURCE_WOOD 	= "W"
RESOURCE_ORE 	= "O"
RESOURCE_STONE 	= "S"
RESOURCE_BRICK 	= "B"
RESOURCE_GLASS 	= "G"
RESOURCE_LOOM 	= "L"
RESOURCE_PAPYRUS= "P"

#Victory points
POINTS_RED = "VPRed"
POINTS_GOLD = "VPGold"
POINTS_WONDER = "VPWonder"
POINTS_BLUE = "VPBlue"
POINTS_YELLOW = "VPYellow"
POINTS_PURPLE = "VPPurple"
POINTS_GREEN = "VPGreen"


ALL_RESOURCES = {	\
	RESOURCE_GOLD, RESOURCE_WOOD, RESOURCE_ORE,	\
	RESOURCE_STONE, RESOURCE_BRICK, RESOURCE_GLASS,	\
	RESOURCE_LOOM, RESOURCE_PAPYRUS }


SCIENCE_GEAR 	= "G"
SCIENCE_COMPASS = "C"
SCIENCE_TABLET 	= "T"

DIRECTION_EAST = "<"
DIRECTION_WEST = ">"
DIRECTION_SELF = "v"

ACTION_PLAYCARD = 0
ACTION_DISCARD	= 1
ACTION_STAGEWONDER	= 2

COLOR_BROWN		= "brown"
COLOR_GREY 		= "grey"
COLOR_YELLOW 	= "yellow"
COLOR_GREEN 	= "green"
COLOR_BLUE 		= "blue"
COLOR_RED 		= "red"
COLOR_PURPLE 	= "purple"

INFOPREFIX_TRADE = "trade"
INFOPREFIX_PROVIDER = "+"


def sort_cards(cards, reverse=False):
	return sorted(cards, key=lambda x: x.get_name(), reverse=reverse)


def find_card(cards, name):
	for c in cards:
		if c.get_name() == name:
			return c
	return None
