from Players import Player
from common import *
import deque


class Wonder_Stage:
	def __init__(self,cost,effect):
		self.cost = cost
		self.effect = effect

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
			self.stages.append(Wonder_Stage([RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_points(POINTS_BLUE,3)))
			self.stages.append(Wonder_Stage([RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_free_conditional_resource(COLOR_BROWN)))
			self.stages.append(Wonder_Stage([RESOURCE_GLASS,RESOURCE_GLASS],lambda p : p.add_points(POINTS_BLUE,7)))



	def setup_Babylon(self,player):
	def setup_Ephesos(self,player):
	def setup_Gizah(self,player):
	def setup_Halikarnassos(self,player):
    def setup_Olympia(self,player):
	def setup_Rhodos(self,player):
    
	
	
	
	
