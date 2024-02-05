#!/usr/bin/python
#
# Copyright 2024 - Jakob Cordua Thibodeau
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
from itertools import product
from random import choice

class Player:
	def __init__(self, name):
		self.name = name
		self.tableau = [] # all the players played cards
		self.hand = None
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
		#If True, player can play the last card of an age instead of discarding it
		#Still has to pay cost (can also use it to complete wonder or discard for 3 coins)
		self.double_last_cards = False 

		self.endgame_scoring_functions = [] #For cards that give points at the end of the game
	
	def set_personality(self, persona):
		self.personality = persona
	
	def set_wonder(self,wonder):
		self.wonder = wonder
	
	def set_east_player(self,east_player):
		self.east_player = east_player
	
	def set_west_player(self,west_player):
		self.west_player = west_player

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
		if card_color == "wonder":
			self.resources[RESOURCE_GOLD] += amount * self.wonder.stages_completed
			return
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

	def add_points_per_wonder(self,amount,played_card_color,me=True,east=False,west=False):
		if me:
			self.points[played_card_color] += amount * self.wonder.stages_completed
		if east:
			self.points[played_card_color] += amount * self.east_player.wonder.stages_completed
		if west:
			self.points[played_card_color] += amount * self.west_player.wonder.stages_completed

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

	def can_double_last_cards(self):
		self.double_last_cards = True

	def get_total_score(self):
		return sum(self.points.values())

	def print_score(self):
		print(f"{self.name}'s score breakdown:")
		print("-------------------------------")
		print(f"{ANSI[COLOR_RED]}War Points: {self.points[POINTS_RED]} pts")
		print(f"{ANSI[COLOR_BROWN]}Gold Points: {self.points[POINTS_GOLD]} pts")
		print(f"{ANSI[COLOR_WONDER]}Wonder Points: {self.points[POINTS_WONDER]} pts")
		print(f"{ANSI[COLOR_BLUE]}Blue Points: {self.points[POINTS_BLUE]} pts")
		print(f"{ANSI[COLOR_YELLOW]}Yellow Points: {self.points[POINTS_YELLOW]} pts")
		print(f"{ANSI[COLOR_PURPLE]}Purple Points: {self.points[POINTS_PURPLE]} pts")
		print(f"{ANSI[COLOR_GREEN]}Green Points: {self.points[POINTS_GREEN]} pts")
		print(f"{ANSI['default']}-------------------------------")
		print(f"Total: {self.get_total_score()} pts")

	def show_available_cards(self):
		cost = []
		for card in self.hand:
			cost.append(get_cost(card))

		#TODO
			
		return 
	

	

#returns the cost in gold of buying this card
	#if 0, the card is free
	#if 1, card costs 1 TO THE BANK
	#if -1 the card cannot be bought (won't be available)
	#if [w,e] w is amount paid to west player and e to east player

	def get_price(self,card):
		possible_prices = []
		#TODO 
		if is_free_prechains():
			return 0

		cost = card.get_cost()
	
		#If the card is free, price is 0
		if cost is None:
			return 0
		
		#If the card costs 1 gold, can either afford it (1 gold) or not (-1)
		if cost[0] == RESOURCE_GOLD:
			if self.resources[RESOURCE_GOLD]>0:
				return 1
			return -1
		
    	# Create a copy of the player's resources dictionary
		available_resources = self.resources.copy()

		#Seperate into brown and grey (easier for conditional resources)
		new_cost_brown = []
		new_cost_grey = []
		#Go through set resources
		for resource in cost:
			if available_resources[resource] > 0:
				available_resources[resource] -= 1 
			else:
				new_cost_brown.append(resource) if resource in BROWN_RESOURCES else new_cost_grey.append(resource)
		
		#If could be paid with basic resources and/or yellow conditional resources
		if max(len(new_cost_brown)-self.free_conditional_resources[COLOR_BROWN],0)\
		  + max(len(new_cost_grey)-self.free_conditional_resources[COLOR_GREY],0) == 0:
			return 0

		
		if new_cost_brown == 0: #Only grey resources left and have to buy some
			return self.buy_grey_from_neighbors(new_cost_grey)
		
		elif new_cost_grey == 0: #Only brown resources left 
			for combo in list(product(*self.conditional_resources)): 
				new_new_cost_brown = new_cost_brown.copy()
				for resource in new_cost_brown:
					if resource in combo:
						combo.remove(resource) 
					else:
						new_new_cost_brown.append(resource)
				if len(new_new_cost_brown) - self.free_conditional_resources[BROWN_RESOURCES] < 1:
					return 0
				else:
					price = buy_brown_from_neighbors(new_new_cost_brown)
					if price == {'east':self.east_trade_prices,'west':0} or {'east':0,'west':self.west_trade_prices}: #it doesn't get better than this
						return price
					possible_prices.append()
		else:
			#Generates all combinations of conditional resources
			for combo in list(product(*self.conditional_resources)): 

				#For each combination, check if can be paid with those resources
				new_new_cost_brown = new_cost_brown.copy()
				for resource in new_cost_brown:
					if resource in combo:
						combo.remove(resource) 
					else:
						new_new_cost_brown.append(resource)

				#Here we know there is at least one grey resource missing
				grey_price = buy_grey_from_neighbors(new_cost_grey)

				#If could be brown paid with basic resources and/or yellow conditional resources
				if len(new_new_cost_brown) - self.free_conditional_resources[BROWN_RESOURCES] < 1:
					return self.buy_grey_from_neighbors(new_cost_grey)
				else:
					
					possible_prices.append(buy_both_from_neighbors(new_new_cost_brown,new_cost_grey))
		
		#TODO
		return min(possible_prices)
	
	#Even for wonders that need 2 grey ressources, you'll never need to buy more than one per type
	def buy_grey_from_neighbors(self,grey_cost):
		both = 0
		east_cost = 0
		west_cost = 0
		free_grey = self.free_conditional_resources[COLOR_GREY]

		east_resources = self.east_player.resources.copy()
		west_resources = self.west_player.resources.copy()
		for resource in grey_cost:
			if east_resources[resource]>0 and west_resources[resource]>0:
				both += 1 #This is "amount of resources both have" not price
			elif east_resources[resource]>0:
				east_cost += self.grey_trade_prices
			elif west_resources[resource]>0:
				west_cost += self.grey_trade_prices
			else:#if none of them have it
				if free_grey > 0: #"Use" a free conditional free resource if you have any left
					free_grey -= 1
				else: #If nobody has the resource and you don't have any free ones, you can't buy the card
					return -1
		
		#Time to use those free conditional resources if you haven't already
		#Here you are guaranteed to have something to pay
		both,west_cost,east_cost = self.assign_free_grey(free_grey,both,west_cost,east_cost)

		cost = {"east":east_cost,"west":west_cost}

		if both > 1: #if 2 or 3
			cost["west"] += self.grey_trade_prices 
			cost["east"] += self.grey_trade_prices
		if both%2 == 1: #if 1 or 3
			#Give the player with the least coins more coins OR
			#Give a random player more coins 
			#This is a compromise for AI, could be changed later for players
			#FIXME
			if cost["east"] > cost['west']:
				cost["west"] += self.grey_trade_prices
			elif cost["east"] < cost['west']:
				cost["west"] += self.grey_trade_prices
			else:
				cost[choice(["east","west"])] += self.grey_trade_prices

		return cost


	def assign_free_grey(self,free_grey,both,west_cost,east_cost):
		#FIXME players should be able to choose
		#Made to avoid the "both" logic later
		#But also made to distribute equally (if [1,2,0] it will transform to [1,1,0])
		for _ in range(free_grey):
			if both == west_cost or both == east_cost: #[1,1,1] or [1,1,0] or [1,0,1]
				both-=1
			elif west_cost == east_cost: #[0,1,1]
				if choice([True,False]):
					west_cost -= self.grey_trade_prices
				else:
					east_cost -= self.grey_trade_prices
			else:
				max_value = max(both,west_cost,east_cost)
				if both == max_value: 
					both -= 1
				elif west_cost == max_value:
					west_cost -= self.grey_trade_prices
				else:
					east_cost -= self.grey_trade_prices

		return both,west_cost,east_cost
	

	def buy_brown_from_neighbors(self,brown_cost):
		both = 0
		east_cost = 0
		west_cost = 0
		free_brown = self.free_conditional_resources[COLOR_BROWN]

		east_resources = self.east_player.resources.copy()
		west_resources = self.west_player.resources.copy()