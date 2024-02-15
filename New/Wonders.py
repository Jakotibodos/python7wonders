from Players import Player
from common import *
from random import choice
#from game import add_effect_to_queue

class Wonder:
	def __init__(self):
		self.side = choice(["A","B"]) #"A" or "B"
		self.stages_completed = 0
		self.stages = []
		self.all_done = False
	
	def get_cost(self):
		return self.cost
	

class Ephesos(Wonder):
	def __init__(self,player):
		super().__init__()
		player.add_resource(RESOURCE_PAPYRUS)
		self.cost = [RESOURCE_STONE,RESOURCE_STONE]
	
	def effect(self, player):
		if self.side == "A":
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_WOOD,RESOURCE_WOOD]
			elif self.stages_completed == 1:
				player.add_resource(RESOURCE_GOLD,9)
				self.cost = [RESOURCE_PAPYRUS,RESOURCE_PAPYRUS]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True
		else: #B Side
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,2)
				player.add_resource(RESOURCE_GOLD,4)
				self.cost = [RESOURCE_WOOD,RESOURCE_WOOD]
			elif self.stages_completed == 1:
				player.add_points(POINTS_WONDER,3)
				player.add_resource(RESOURCE_GOLD,4)
				self.cost = [RESOURCE_LOOM,RESOURCE_GLASS,RESOURCE_PAPYRUS]
			else:
				player.add_points(POINTS_WONDER,5)
				player.add_resource(RESOURCE_GOLD,4)
				self.all_done = True

class Babylon(Wonder):
	def __init__(self,player):
		super().__init__()
		player.add_resource(RESOURCE_BRICK)
		if self.side == "A":
			self.cost = [RESOURCE_BRICK,RESOURCE_BRICK]
		else:
			self.cost = [RESOURCE_BRICK,RESOURCE_LOOM]

	def effect(self, player):
		if self.side == "A":
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD]
			elif self.stages_completed == 1:
				player.add_science("any")
				self.cost = [RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True
		else: #B Side
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_GLASS]
			elif self.stages_completed == 1:
				player.can_double_last_cards()
				self.cost = [RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS]
			else:
				player.add_science("any")
				self.all_done = True

class Gizah(Wonder):
	def __init__(self,player):
		super().__init__()
		player.add_resource(RESOURCE_STONE)
		if self.side == "A":
			self.cost = [RESOURCE_STONE,RESOURCE_STONE]
		else:
			self.cost = [RESOURCE_WOOD,RESOURCE_WOOD]

	def effect(self, player):
		if self.side == "A":
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD]
			elif self.stages_completed == 1:
				player.add_points(POINTS_WONDER,5)
				self.cost = [RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True
		else: #B Side
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE]
			elif self.stages_completed == 1:
				player.add_points(POINTS_WONDER,5)
				self.cost = [RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK]
			elif self.stages_completed == 2:
				player.add_points(POINTS_WONDER,5)
				self.cost = [RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_PAPYRUS]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True

#TODO: implement play from discard
class Halikarnassos(Wonder):
	def __init__(self,player,queue):
		super().__init__()
		player.add_resource(RESOURCE_LOOM)
		self.queue = queue
		if self.side == "A":
			self.cost = [RESOURCE_BRICK,RESOURCE_BRICK]
		else:
			self.cost = [RESOURCE_ORE,RESOURCE_ORE]
	
	#TODO: implement play from discard
	def effect(self, player):
		if self.side == "A":
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE]
			elif self.stages_completed == 1:
				#TODO self.queue.append((lambda p : p.play_from_discard))
				self.cost = [RESOURCE_LOOM,RESOURCE_LOOM]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True
		else: #B Side
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,2)
				#TODO self.queue.append((lambda p : p.play_from_discard))
				self.cost = [RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK]
			elif self.stages_completed == 1:
				player.add_points(POINTS_WONDER,1)
				#TODO self.queue.append((lambda p : p.play_from_discard))
				self.cost = [RESOURCE_GLASS,RESOURCE_PAPYRUS,RESOURCE_LOOM]
			else:	
				#TODO self.queue.append((lambda p : p.play_from_discard))
				self.all_done = True

class Alexandria(Wonder):
	def __init__(self,player):
		super().__init__()
		player.add_resource(RESOURCE_GLASS)
		if self.side == "A":
			self.cost = [RESOURCE_STONE,RESOURCE_STONE]
		else:
			self.cost = [RESOURCE_BRICK,RESOURCE_BRICK]

	def effect(self, player):
		if self.side == "A":
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_ORE,RESOURCE_ORE]
			elif self.stages_completed == 1:
				player.add_free_conditional_resource(COLOR_BROWN)
				self.cost = [RESOURCE_GLASS,RESOURCE_GLASS]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True
		else: #B Side
			if self.stages_completed == 0:
				player.add_free_conditional_resource(COLOR_BROWN)
				self.cost = [RESOURCE_WOOD,RESOURCE_WOOD]
			elif self.stages_completed == 1:
				player.add_free_conditional_resource(COLOR_GREY)
				self.cost = [RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True
		self.stages_completed += 1

class Rhodos(Wonder):
	def __init__(self,player):
		super().__init__()
		player.add_resource(RESOURCE_PAPYRUS)
		if self.side == "A":
			self.cost = [RESOURCE_WOOD,RESOURCE_WOOD]
		else:
			self.cost = [RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE]
	def effect(self, player):
		if self.side == "A":
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				self.cost = [RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK]
			elif self.stages_completed == 1:
				player.add_shields(2)
				self.cost = [RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE]
			else:
				player.add_points(POINTS_WONDER,7)
				self.all_done = True
		else: #B Side
			if self.stages_completed == 0:
				player.add_points(POINTS_WONDER,3)
				player.add_resource(RESOURCE_GOLD,3)
				player.add_shields(1)
				self.cost = [RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE]
			else:
				player.add_points(POINTS_WONDER,4)
				player.add_resource(RESOURCE_GOLD,4)
				player.add_shields(1)
				self.all_done = True
		self.stages_completed += 1

	
