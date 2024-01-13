#!/usr/bin/python
#
# Copyright 2015 - Jonathan Gordon
#
# This program is free software you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation either version 2
# of the License, or (at your option) any later version.
#
# This software is distributed on an "AS IS" basis, WITHOUT WARRANTY OF ANY
# KIND, either express or implied.

from Players import Player
from common import *

class Card:
	def __init__(self, id,name,color,age,cost,effect):
		self.id = id
		self.name = name
		self.color = color
		self.age = age
		self.prechains = []
		self.postchains = []
		self.cost = cost
		self.build = effect

c = Card("test","red",[0,0,0,1,0,0,0],lambda player: player.add_resource(RESOURCE_WOOD,1))

#TODO Implement pre and post chains
#TODO Convert java cards to python
#TODO test functionality of every card
#Card(id,name,color,age,cost,function)
#{coins,wood,stone,bricks,ore,glass,papyrus,textile}
#AGE 1 CARDS

#Age 1 Brown cards
c1 =   Card(1,"Lumber Yard",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_WOOD,1))  #wood
c2 =   Card(2,"Stone Pit",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_STONE,1))  #stone
c3 =   Card(3,"Clay Pool",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_BRICK,1))  #bricks
c4 =   Card(4,"Ore Vein",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_ORE,1))  #ore
c5 =   Card(5,"Tree Farm",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_BRICK))) # wood\bricks
c6 =   Card(6,"Excavation",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_STONE,RESOURCE_BRICK)))  # stone\bricks
c7 =   Card(7,"Clay_Pit",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_ORE,RESOURCE_BRICK)))  # ore\bricks
c8 =   Card(8,"Timber Yard",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_STONE)))  # wood\stone
c9 =   Card(9,"Forest Cave",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_ORE)))  # wood\ore
c10 =   Card(10,"Mine",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_STONE,RESOURCE_ORE)))  # stone\ore

 #Age 1 Grey cards
c11 =   Card(11,"Glassworks",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_GLASS,1))  #glass
c12 =   Card(12,"Press",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_PAPYRUS,1))  #papyrus
c13 =   Card(13,"Loom",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_LOOM,1))  #loom

 #Age 1 Blue cards
c14 = Card(14,"Pawnshop",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,3))  #3 blue points
c15 = Card(15,"Baths",COLOR_BLUE,1,[RESOURCE_STONE],lambda p : p.add_points(POINTS_BLUE,3))  #3 blue points
c16 = Card(16,"Altar",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2))  #2 blue points
c17 = Card(17,"Theatre",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2))  #2 blue points

 #Age 1 Yellow cards
c18 = Card(18,"Tavern",COLOR_YELLOW,1,None,lambda p : p.add_resource(RESOURCE_GOLD,5))  #5 coins
c19 = Card(19,"Marketplace",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("grey"))  #lower both grey trading costs
c20 = Card(20,"West Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("east"))  #lower east brown trading costs
c21 = Card(21,"East Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("west"))  #lower west brown trading costs

 #Age 1 Red cards
c22 = Card(22,"Stockade",COLOR_RED,1,[RESOURCE_WOOD], lambda p : p.add_shields(1))
c23 = Card(23,"Barracks",COLOR_RED,1,[RESOURCE_ORE],lambda p : p.add_shields(1))
c24 = Card(24,"Guard_Tower",COLOR_RED,1,[RESOURCE_BRICK],lambda p : p.add_shields(1))

 #Age 1 Green cards
c25 = Card(25,"Apothecary",COLOR_GREEN,1,[RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_COMPASS))  #compass
c26 = Card(26,"Workshop",COLOR_GREEN,1,[RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_GEAR))  #gear
c27 = Card(27,"Scriptorium",COLOR_GREEN,1,[RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_TABLET))  #tablet

 #AGE 2 CARDS

 #Age 2 Brown cards
c28 = Card(28,"Sawmill",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_WOOD,2))  #2 wood
c29 = Card(29,"Quarry",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_STONE,2))  #2 stone
c30 = Card(30,"Brickyard",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_BRICK,2))  #2 brick
c31 = Card(31,"Foundry",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_ORE,2))  #2 ore

 #Age 2 Grey cards
c32 = Card(32,"Glassworks",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_GLASS,1))  #glass
c33 = Card(33,"Press",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_PAPYRUS,1))  #papyrus
c34 = Card(34,"Loom",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_LOOM,1))  #loom

 #Age 2 Blue cards
c35 = Card(35,"Statue",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_points(POINTS_BLUE,4))  #4 Blue Points
c36 = Card(36,"Aqueduct",COLOR_BLUE,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_BLUE,5))  #5 Blue Points
c37 = Card(37,"Temple",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_GLASS],lambda p : p.add_points(POINTS_BLUE,4))  #4 Blue Points
c38 = Card(38,"Courthouse",COLOR_BLUE,2,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_LOOM],lambda p : p.add_points(POINTS_BLUE,4))  #4 Blue Points

 #Age 2 Yellow cards
c39 = Card(39,"Caravansery",COLOR_YELLOW,2,[RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_free_conditional_resource("brown")) #Brown resources composition
c40 = Card(40,"Forum",COLOR_YELLOW,2,[RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_free_conditional_resource("grey"))  #Grey ressources composition
c41 = Card(41,"Vineyard",COLOR_YELLOW,2,
		(Player p )->{int coinsToAdd = p.getLeftPlayer().getCountColor(0)+p.getRightPlayer().getCountColor(0)+p.getCountColor(0)
				p.addResource(0, coinsToAdd)})  #Add coins = brown cards of you and neighbors
c42 = Card(42,"Bazar",COLOR_YELLOW,2,
		(Player p )->{int coinsToAdd = p.getLeftPlayer().getCountColor(1)+p.getRightPlayer().getCountColor(1)+p.getCountColor(1)
				p.addResource(0, coinsToAdd*2)})  #Add coins = 2 x grey cards of you and neighbors

 #Age 2 Red cards
c43 = Card(43,"Stables",COLOR_RED,  int[] {0,1,0,1,1,0,0,0},2,(Player p)->p.addShields(2))
c44 = Card(44,"Archery Range",COLOR_RED,  int[] {0,2,0,0,1,0,0,0},2,(Player p)->p.addShields(2))
c45 = Card(45,"Walls",COLOR_RED,  int[] {0,0,3,0,0,0,0,0},2,(Player p)->p.addShields(2))
c46 = Card(46,"Training Ground",COLOR_RED,  int[] {0,1,0,0,2,0,0,0},2,(Player p)->p.addShields(2))

 #Age 2 Green cards
c47 = Card(47,"Dispensary",COLOR_GREEN,  int[] {0,0,0,0,2,1,0,0},2,(Player p)->p.addScience(0))  #compass
c48 = Card(48,"Laboratory",COLOR_GREEN,  int[]{0,0,0,2,0,0,1,0},2,(Player p)->p.addScience(1))  #gear
c49 = Card(49,"Library",COLOR_GREEN,  int[]{0,0,2,0,0,0,0,1},2,(Player p)->p.addScience(2))  #tablet
c50 = Card(50,"School",COLOR_GREEN,  int[]{0,1,0,0,0,0,1,0},2,(Player p)->p.addScience(2))  #tablet


 #AGE 3 CARDS

 #Age 3 Blue cards
c51 = Card(51,"Pantheon",COLOR_BLUE,  int[] {0,0,0,2,1,1,1,1},3,(Player p )->p.addBluePoints(7))  #7 Blue Points
c52 = Card(52,"Gardens",COLOR_BLUE,  int[] {0,1,0,2,0,0,0,0},3,(Player p )->p.addBluePoints(5))  #5 Blue Points
c53 = Card(53,"Town Hall",COLOR_BLUE,  int[] {0,0,2,0,1,1,0,0},3,(Player p )->p.addBluePoints(6))  #6 Blue Points
c54 = Card(54,"Palace",COLOR_BLUE,  int[] {0,1,1,1,1,1,1,1},3,(Player p )->p.addBluePoints(8))  #8 Blue Points
c55 = Card(55,"Senate",COLOR_BLUE,  int[] {0,2,1,0,1,0,0,0},3,(Player p )->p.addBluePoints(6))  #6 Blue Points

 #Age 3 Yellow cards
c56 = Card(56,"Lighthouse",COLOR_YELLOW,  int[] {0,0,1,0,0,1,0,0},3,(Player p )->{
		p.addResource(0, p.getCountColor(3))  #Add coins = number of previous yellow cards
		p.addConditionalPointsToUpdate(  #Add points = number of previous yellow cards
			(Player q)-> {q.addYellowPoints(q.getCountColor(3))})}) 
c57 = Card(57,"Haven",COLOR_YELLOW,  int[] {0,1,0,0,1,0,0,1},3,(Player p )->{
		p.addResource(0, p.getCountColor(0))  #Add coins = number of previous brown cards
		p.addConditionalPointsToUpdate(  #Add points = number of previous brown cards
			(Player q)-> {q.addYellowPoints(q.getCountColor(0))})}) 
c58 = Card(58,"Chamber of Commerce",COLOR_YELLOW,  int[] {0,0,0,2,0,0,1,0},3,(Player p )->{
		p.addResource(0, 2*p.getCountColor(1))  #Add coins = 2x number of previous grey cards
		p.addConditionalPointsToUpdate(  #Add points = 2x number of previous grey cards
			(Player q)-> {q.addYellowPoints(2*q.getCountColor(1))})}) 
c59 = Card(59,"Arena",COLOR_YELLOW,  int[] {0,0,2,0,1,0,0,0},3,(Player p )->{
		p.addResource(0, 3*p.getWonderBoard().getWondersCompleted())  #Add coins = 3x number of completed wonders
		p.addConditionalPointsToUpdate(  #Add points = number of completed wonders
			(Player q)-> {q.addYellowPoints(p.getWonderBoard().getWondersCompleted())})})

#Age 3 Red cards
c60 = Card(60,"Fortifications",COLOR_RED,  int[] {0,0,1,0,3,0,0,0},3,(Player p)->p.addShields(3))
c61 = Card(61,"Circus",COLOR_RED,  int[] {0,0,3,0,1,0,0,0},3,(Player p)->p.addShields(3))
c62 = Card(62,"Arsenal",COLOR_RED,  int[] {0,2,0,0,1,0,0,1},3,(Player p)->p.addShields(3))
c63 = Card(63,"Siege Workshop",COLOR_RED,  int[] {0,1,0,3,0,0,0,0},3,(Player p)->p.addShields(3))

#Age 3 Green cards
c64 = Card(64,"Lodge",COLOR_GREEN,  int[] {0,0,0,2,0,0,1,1},3,(Player p)->p.addScience(0))  #compass
c65 = Card(65,"Academy",COLOR_GREEN,  int[]{0,0,3,0,0,1,0,0},3,(Player p)->p.addScience(0))  #compass
c66 = Card(66,"Observatory",COLOR_GREEN,  int[]{0,0,0,0,2,1,0,1},3,(Player p)->p.addScience(1))  #gear
c67 = Card(67,"Study",COLOR_GREEN,  int[]{0,1,0,0,0,1,0,1},3,(Player p)->p.addScience(1))  #gear
c68 = Card(68,"University",COLOR_GREEN,  int[] {0,2,0,0,0,1,1,0},3,(Player p)->p.addScience(2))  #tablet

#Age 3 purple cards
c69 = Card(69,"Workers Guild",COLOR_PURPLE,  int[] {0,1,1,1,2,0,0,0},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of brown cards of neighbors
			(Player q)-> {q.addPurplePoints(q.getLeftPlayer().getCountColor(0)+q.getRightPlayer().getCountColor(0))})}) 
c70 = Card(70,"Craftmens Guild",COLOR_PURPLE,  int[] {0,0,2,0,2,0,0,0},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = 2x number of grey cards of neighbors
			(Player q)-> {q.addPurplePoints(2*(q.getLeftPlayer().getCountColor(1)+q.getRightPlayer().getCountColor(1)))})})
c71 = Card(71,"Magistrates Guild",COLOR_PURPLE,  int[] {0,3,1,0,0,0,0,1},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of blue cards of neighbors
			(Player q)-> {q.addPurplePoints(q.getLeftPlayer().getCountColor(2)+q.getRightPlayer().getCountColor(2))})}) 
c72 = Card(72,"Traders Guild",COLOR_PURPLE,  int[] {0,0,0,0,0,1,1,1},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of yellow cards of neighbors
			(Player q)-> {q.addPurplePoints(q.getLeftPlayer().getCountColor(3)+q.getRightPlayer().getCountColor(3))})}) 
c73 = Card(73,"Builders Guild",COLOR_PURPLE,  int[] {0,0,2,2,0,1,0,0},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of completed wonders of player and neighbors
			(Player q)-> {q.addPurplePoints(q.getLeftPlayer().getWonderBoard().getWondersCompleted()
					+q.getRightPlayer().getWonderBoard().getWondersCompleted()
					+q.getWonderBoard().getWondersCompleted())})}) 
Card c74 =   Card(74,"Spies Guild",COLOR_PURPLE,  int[] {0,0,0,3,0,1,0,0},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of red cards of neighbors
			(Player q)-> {q.addPurplePoints(q.getLeftPlayer().getCountColor(4)+q.getRightPlayer().getCountColor(4))})}) 
Card c75 =   Card(75,"Philosophers Guild",COLOR_PURPLE,  int[] {0,0,0,3,0,0,1,1},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of green cards of neighbors
			(Player q)-> {q.addPurplePoints(q.getLeftPlayer().getCountColor(5)+q.getRightPlayer().getCountColor(5))})}) 
Card c76 =   Card(76,"Strategists Guild",COLOR_PURPLE,  int[] {0,0,1,0,2,0,0,1},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of Minus Tokens of neighbors
			(Player q)-> {q.addPurplePoints(q.getLeftPlayer().getNumberMinusTokens()+q.getRightPlayer().getNumberMinusTokens())})}) 
Card c77 =   Card(77,"Scientists Guild",COLOR_PURPLE,  int[] {0,2,0,0,2,0,1,0},3,(Player p)->p.addScience(3))  #Conditional science
Card c78 =   Card(78,"Shipowners Guild",COLOR_PURPLE,  int[] {0,3,0,0,0,1,1,0},3,(Player p )->{
		p.addConditionalPointsToUpdate(  #Add points = number of brown, grey and purple cards owned
			(Player q)-> {q.addPurplePoints(q.getCountColor(0)+q.getCountColor(1)+q.getCountColor(6))})})

