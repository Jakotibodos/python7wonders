from Players import Player
from common import *
import deque


class Wonder_Stage:
	
	def __init__(self,cost,effect):
		self.cost = cost
		self.effect = effect

	def add_multiple(self,player,points=0,coins=0,war=0):
		player.add_points(POINTS_WONDER,points)
		player.add_resource(RESOURCE_GOLD,coins)
		player.add_shields(war)

class Wonder:

	def __init__(self,id,name,side,player):
		self.id = id
		self.name = name
		self.side = side #"A" or "B"
		self.stages_completed = 0
		self.stages = deque()

	def setup_Alexandria(self,player):
		player.add_resource(RESOURCE_GLASS)
		if self.side == "A":
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_WONDER,3)))
			self.stages.append(Wonder_Stage([RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_free_conditional_resource(COLOR_BROWN)))
			self.stages.append(Wonder_Stage([RESOURCE_GLASS,RESOURCE_GLASS],lambda p : p.add_points(POINTS_WONDER,7)))
			
		else: #side == "B"
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_free_conditional_resource(COLOR_BROWN)))
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_free_conditional_resource(COLOR_GREY)))
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_WONDER,7)))

	def setup_Babylon(self,player):
		player.add_resource(RESOURCE_BRICK)
		if self.side == "A":
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_points(POINTS_WONDER,3)))
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_science("any")))
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_points(POINTS_WONDER,7)))
			
		else: #side == "B"
			self.stages.append(Wonder_Stage([RESOURCE_LOOM,RESOURCE_BRICK],lambda p : p.add_free_conditional_resource(COLOR_BROWN)))
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_GLASS],lambda p : p.can_double_last_cards()))
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS],lambda p : p.add_science("any")))
			
	
	def setup_Ephesos(self,player):
		player.add_resource(RESOURCE_PAPYRUS)
		if self.side == "A":
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_WONDER,3)))
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_resource(RESOURCE_GOLD,9)))
			self.stages.append(Wonder_Stage([RESOURCE_PAPYRUS,RESOURCE_PAPYRUS],lambda p : p.add_points(POINTS_WONDER,7)))
			
		else: #side == "B"
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE],lambda w: w.add_multiple(player,2,4)))
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD],lambda w: w.add_multiple(player,3,4)))
			self.stages.append(Wonder_Stage([RESOURCE_PAPYRUS,RESOURCE_LOOM,RESOURCE_GLASS],lambda w: w.add_multiple(player,5,4)))

	def setup_Gizah(self,player):
		player.add_resource(RESOURCE_STONE)
		if self.side == "A":
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_WONDER,3)))
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_points(POINTS_WONDER,5)))
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_WONDER,7)))
			
		else: #side == "B"
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_points(POINTS_WONDER,3)))
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_WONDER,5)))
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_points(POINTS_WONDER,5)))
			self.stages.append(Wonder_Stage([RESOURCE_PAPYRUS,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_WONDER,7)))

	def setup_Halikarnassos(self,player):
		player.add_resource(RESOURCE_LOOM)
		if self.side == "A":
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_points(POINTS_WONDER,3)))
			#TODO make work with queue
			self.stages.append(Wonder_Stage([RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE],lambda p : p.play_card_from_discard()))
			self.stages.append(Wonder_Stage([RESOURCE_LOOM,RESOURCE_LOOM],lambda p : p.add_points(POINTS_WONDER,7)))
			
		else: #side == "B"
			#TODO make work with queue
			self.stages.append(Wonder_Stage([RESOURCE_ORE,RESOURCE_ORE],lambda p : p.play_card_from_discard())) #TODO 2 coins
			#TODO make work with queue
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.play_card_from_discard())) #TODO 1 coin
			#TODO make work with queue
			self.stages.append(Wonder_Stage([RESOURCE_PAPYRUS,RESOURCE_LOOM,RESOURCE_GLASS],lambda p : p.play_card_from_discard()))

	def setup_Rhodos(self,player):
		player.add_resource(RESOURCE_PAPYRUS)
		if self.side == "A":
			self.stages.append(Wonder_Stage([RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_points(POINTS_WONDER,3)))
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_shields(2)))
			self.stages.append(Wonder_Stage([RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_points(POINTS_WONDER,7)))
			
		else: #side == "B"
			self.stages.append(Wonder_Stage([RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda w: w.add_multiple(player,3,3,1)))
			self.stages.append(Wonder_Stage([RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE],lambda w: w.add_multiple(player,4,4,1)))
			
	
	
	
	
