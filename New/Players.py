#!/usr/bin/python
#
# Copyright 2015 - Jakob Cordua Thibodeau
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
# KIND, either express or implied.

from collections import deque
from common import *


class Player:
	def __init__(self, name):
		self.name = name
		self.tableau = [] # all the players played cards
		self.war_losses = 0 # war wins/losses
		self.shields = 0 #Shield/military points
		self.resources = { #This only counts fixed ressources
			RESOURCE_GOLD : 3, #Yes, gold is a resource
			RESOURCE_WOOD 	: 0,
			RESOURCE_ORE 	: 0,
			RESOURCE_STONE 	: 0,
			RESOURCE_BRICK 	: 0,
			RESOURCE_GLASS 	: 0,
			RESOURCE_LOOM 	: 0,
			RESOURCE_PAPYRUS 	: 0
		}
		self.conditional_resources = [] #For brown cards with /
		self.free_conditional_resources = {#For yellow card and wonders with W/B/S/O or G/P/L #Untradable
			COLOR_BROWN:0,
			COLOR_GREY:0
		} 
		self.east_trade_prices = 2 #for brown resources <
		self.west_trade_prices = 2 #for brown resources >
		self.grey_trade_prices = 2 #for both player <>
		self.west_player = None
		self.east_player = None
		self.wonder = None
		self.personality = None
		self.points = {
			POINTS_RED:0,
			POINTS_GOLD:0,
			POINTS_WONDER:0,
			POINTS_BLUE:0,
			POINTS_YELLOW:0,
			POINTS_PURPLE:0,
			POINTS_GREEN:0
		}
		self.science = {
			SCIENCE_GEAR:0,
			SCIENCE_COMPASS:0,
			SCIENCE_TABLET:0,
			"any":0 #for conditional sciences, used at the end when calculating points
		}
		self.color_count = {	#Amount of cards of that color players owns
			COLOR_BROWN:0,
			COLOR_GREY:0,
			COLOR_RED:0,
			COLOR_YELLOW:0,
			COLOR_BLUE:0,
			COLOR_GREEN:0,
			COLOR_PURPLE:0
		}
		self.endgame_scoring_functions = [] #For cards that give points at the end of the game
	
	def set_personality(self, persona):
		self.personality = persona
	
	def get_name(self):
		return self.name
	
	def get_cards(self):
		return self.tableau
	
	def get_color_count(self,color): 
		return self.color_count[color] #int, number of cards built of that color
	
	def add_resource(self, resource, amount=1):
		self.resources[resource] += amount

	def add_conditional_resource(self,conditional_resource):
		self.conditional_resources.append(conditional_resource)
	
	def add_free_conditional_resource(self,color):
		self.free_conditional_resources[color]+=1 #color = "brown" or "grey"

	def add_points(self,category,amount):
		self.points[category] += amount
		
	
	#For coins only, points are at the end
	#Bazar and Vineyard (that use this) should be put at the end of queue when played	
	def add_coins_per_card(self,amount,card_color,me=True,east=False,west=False):
		if me:
			self.resources[RESOURCE_GOLD] += amount * self.get_color_count(card_color) 
		if east:
			self.resources[RESOURCE_GOLD] += amount * self.east_player.get_color_count(card_color)
		if west:
			self.resources[RESOURCE_GOLD] += amount * self.west_player.get_color_count(card_color)  
	
	#point_card_color = card from which points are awarded
	#played_card_color = color/category of card build
	def add_points_per_card(self,amount,played_card_color,point_card_color,me=True,east=False,west=False):
		if me:
			self.points[played_card_color] += amount * self.get_color_count(point_card_color) 
		if east:
			self.points[played_card_color] += amount * self.east_player.get_color_count(point_card_color)
		if west:
			self.points[played_card_color] += amount * self.west_player.get_color_count(point_card_color)

	def lower_trading_cost(self,trade_type):
		if trade_type == "east": #east brown cards
			self.east_trade_prices = 1
		elif trade_type == "west": #west brown cards
			self.west_trade_prices = 1
		else: #if "grey"
			self.grey_trade_prices = 1

	def add_shields(self, amount): #shields for war
		self.shields += amount
	
	def add_science(self, symbol):
		self.science[symbol]+=1 #"any" for a conditional science card/wonder"

	def add_endgame_function(self,function):
		self.endgame_scoring_functions.append(function)

	def shipowners_guild(self):
		self.add_endgame_function(self.add_points_per_card(1,POINTS_PURPLE,COLOR_BROWN))
		self.add_endgame_function(self.add_points_per_card(1,POINTS_PURPLE,COLOR_GREY))
		self.add_endgame_function(self.add_points_per_card(1,POINTS_PURPLE,COLOR_PURPLE))

	
	def play_hand(self, hand, west_player, east_player):
		''' return the card and action done'''
		options = []
		for card in hand:
			#print card.get_name(), self.is_card_in_tableau(card)
			if not self.is_card_in_tableau(card): #cannot play 2 cards with same name
				if self.can_build_with_chain(card): #can build free card
					options.append((ACTION_PLAYCARD, card))
				elif self.buy_card(card, west_player, east_player):
					options.append((ACTION_PLAYCARD, card))
			options.append((ACTION_DISCARD, card)) #Every card can be discarded for 3 coins

			#TODO
			#Make wonder first option
			if False:#self.wonder.built_stages < 3: #FIXMEself.wonder.stages:
				options.append((ACTION_STAGEWONDER, card))
		i = 0
		print("-=================-")
		
		#TODO make wonder first option
		options = sorted(options, key=lambda x: {CARDS_GREY:0, CARDS_BROWN:1, CARDS_YELLOW:2, CARDS_BLUE:3, CARDS_RED:4, CARDS_GREEN:5, CARDS_PURPLE:6}[x[1].get_colour()])
		for o in options:
			actions = { ACTION_PLAYCARD:"Play", ACTION_DISCARD:"Discard", ACTION_STAGEWONDER:"Stage" }
			card = o[1]
			print("[%d]: %s\t%s\t%s" % (i, actions[o[0]], card.get_cost_as_string(), card.pretty_print_name()))
			i += 1
		print("-=================-")

		return options[self.personality.make_choice(options)]
	
	def print_tableau(self):
		cards = { CARDS_BROWN:[], CARDS_GREY:[], CARDS_YELLOW:[], CARDS_BLUE:[], CARDS_RED:[], CARDS_GREEN:[], CARDS_PURPLE:[] }
		print("You have $%d" % (self.money))
		#print("War points: %s" % (self.military)) #Change to 
		print(self.west_trade_prices)
		print(self.east_trade_prices)
		for c in self.get_cards():
			cards[c.get_colour()].append(c)
		
		biggest_deck = 0
		for colour in cards.keys():
			count =  len(cards[colour])
			if count > biggest_deck:
				biggest_deck = count
		for i in range(biggest_deck):
			line = { CARDS_BROWN:"\t", CARDS_GREY:"\t", CARDS_YELLOW:"\t", CARDS_BLUE:"\t", CARDS_RED:"\t", CARDS_GREEN:"\t", CARDS_PURPLE:"\t" }
			for colour in [CARDS_BROWN, CARDS_GREY, CARDS_YELLOW, CARDS_BLUE, CARDS_RED, CARDS_GREEN, CARDS_PURPLE]:
				if len(cards[colour]) > biggest_deck - 1 - i:
					line[colour] = "%s" % (cards[colour][biggest_deck - 1 - i].pretty_print_name())
				else:
					line[colour] = "        "
			
			print("%s\t%s\t%s\t%s\t%s\t%s\t%s" % ( line[CARDS_BROWN], line[CARDS_GREY], line[CARDS_YELLOW], line[CARDS_BLUE], line[CARDS_RED], line[CARDS_GREEN],line[CARDS_PURPLE]))
		
	
	def set_wonder(self, wonder):
		self.wonder = wonder
	
	def is_card_in_tableau(self, card):
		return find_card(self.get_cards(), card.get_name()) != None

	def can_build_with_chain(self, card):
		for precard in card.prechains:
			if find_card(self.get_cards(), precard):
				return True
		return False
		
	def buy_card(self, card, west_player, east_player):
		missing = []
		money_spent = 0
		trade_east = 0
		trade_west = 0
		options = []
		if len(card.cost) == 0:
			return [CardPurchaseOption([], 0, [], [])]
		for i in range(len(card.cost)):
			cost = deque(card.cost)
			cost.rotate(i)
			for east_first in [True, False]:
				x = self._find_resource_cards(list(cost), west_player.get_cards(), east_player.get_cards(), east_first)
				if x and x not in options:
					options.append(x)
		# we now remove any of the options which we cant afford to pay for trades
		legal_options = []
		for o in options:
			cost = o.coins
			for c in o.east_trades:
				o.east_cost = self.east_trade_prices[c.resource] * c.count
				cost += o.east_cost
			for c in o.west_trades:
				o.west_cost = self.west_trade_prices[c.resource] * c.count
				cost += o.west_cost
			if cost <= self.money:
				o.set_total(cost)
				legal_options.append(o)
			# Setting the total cost is buggy
		#print sorted(legal_options, key=lambda x: x.total_cost)
		return sorted(legal_options, key=lambda x: x.total_cost)

	def _find_resource_cards(self, needed_resources, west_cards, east_cards, east_first=True):
		def __is_card_used(card, used_cards_array):
			for x in used_cards_array:
				if card == x.card:
					return True
			return False
		def __check_tableau(r, tableau, used_cards, tradeable_only):
			for c in tableau: # FIXME: WONDER too
				if not __is_card_used(c, used_cards):
					is_resource, tradeable = c.is_resource_card()
					if is_resource and ((not tradeable_only) or (tradeable_only == tradeable)):
						count = c.provides_resource(r)
						if count == 0:
							continue
						return (c, count)
			return (None, 0)

		used_cards = []
		coins = 0
		east_trades = []
		west_trades = []
		card_sets = [(self.get_cards(), used_cards, False)]
		if east_first:
			card_sets += [(east_cards, east_trades, True), (west_cards, west_trades, True)]
		else:
			card_sets += [(west_cards, west_trades, True), (east_cards, east_trades, True)]
		
		while len(needed_resources):
			r = needed_resources[0]
			found = False
			if r == RESOURCE_MONEY:
				coins += 1
				needed_resources.remove(r)
				continue
			for cards, used, tradeable_only in card_sets:
				card, count = __check_tableau(r, cards, used, tradeable_only)
				if card and count > 0:
					found = True
					needed_count = 0
					for i in range(0, count):
						if r not in needed_resources:
							break
						needed_count += 1
						needed_resources.remove(r)
					used.append(CardPurchaseUse(card, r, needed_count))
					break
			if not found:
				return None
		return CardPurchaseOption(used_cards, coins, west_trades, east_trades)

class CardPurchaseUse:
	def __init__(self, card, resource, count):
		self.card = card
		self.resource = resource
		self.count = count
	
	def __eq__(self, other):
		return self.resource == other.resource \
			and self.count == other.count \
			and self.card.get_name() == other.card.get_name()
	
	def __repr__(self):
		if len(self.card.get_info()) == 1:
			return "%s"% (self.card)
		return "%s -> %s * %d" % (self.card, self.resource, self.count)
			
class CardPurchaseOption:
	def __init__(self, cards, coins, west_trades, east_trades):
		self.cards = cards
		self.coins = coins
		self.west_trades = west_trades
		self.east_trades = east_trades
		self.total_cost = 0
		self.east_cost = 0
		self.west_cost = 0
	
	def set_total(self, cost):
		self.total_cost = cost

	def __eq__(self, other):
		if self.coins != other.coins:
			return False
		for us, them in [(self.cards, other.cards), \
						(self.west_trades, other.west_trades), \
						(self.east_trades, other.east_trades)]:
			if len(us) != len(them):
				return False
			for x in us:
				if x not in them:
					return False
				
		return True

	def __repr__(self):
		return "{ (total: $%d)\n\t%s\n\t$%d\n\tWEST:%s\n\tEAST:%s\n}" % (self.total_cost, self.cards, self.coins, self.west_trades, self.east_trades)
