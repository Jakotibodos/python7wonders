
from Players import Player
from common import *
import game

class Card:
	def __init__(self, id,name,color,age,cost,prechains=None,postchains=None):
		self.id = id
		self.name = name
		self.color = color
		self.age = age
		self.prechains = []
		self.postchains = []
		self.cost = cost

	def __str__(self) -> str:
		return f"{ANSI[self.color]}{self.name}\033[0m"
	def __repr__(self) -> str:
		return f"{ANSI[self.color]}{self.name}\033[0m"
	
	def get_cost(self):
		return self.cost

class LumberYard(Card):
	def __init__(self, id):
		super().__init__(1,"Lumber Yard",COLOR_BROWN,1,None)
	
	def effect(player):
		player.add_resource(RESOURCE_WOOD)

class StonePit(Card):
    def __init__(self):
        super().__init__(2, "Stone Pit", COLOR_BROWN, 1, None)
    
    def effect(self, player):
        player.add_resource(RESOURCE_STONE)

class ClayPool(Card):
    def __init__(self):
        super().__init__(3, "Clay Pool", COLOR_BROWN, 1, None)
    
    def effect(self, player):
        player.add_resource(RESOURCE_BRICK)

class OreVein(Card):
    def __init__(self):
        super().__init__(4, "Ore Vein", COLOR_BROWN, 1, None)
    
    def effect(self, player):
        player.add_resource(RESOURCE_ORE)

class TreeFarm(Card):
    def __init__(self):
        super().__init__(5, "Tree Farm", COLOR_BROWN, 1, [RESOURCE_GOLD])
    
    def effect(self, player):
        player.add_conditional_resource((RESOURCE_WOOD, RESOURCE_BRICK))

class Excavation(Card):
    def __init__(self):
        super().__init__(6, "Excavation", COLOR_BROWN, 1, [RESOURCE_GOLD])
    
    def effect(self, player):
        player.add_conditional_resource((RESOURCE_STONE, RESOURCE_BRICK))

class ClayPit(Card):
    def __init__(self):
        super().__init__(7, "Clay Pit", COLOR_BROWN, 1, [RESOURCE_GOLD])
    
    def effect(self, player):
        player.add_conditional_resource((RESOURCE_ORE, RESOURCE_BRICK))

class TimberYard(Card):
    def __init__(self):
        super().__init__(8, "Timber Yard", COLOR_BROWN, 1, [RESOURCE_GOLD])
    
    def effect(self, player):
        player.add_conditional_resource((RESOURCE_WOOD, RESOURCE_STONE))

class ForestCave(Card):
    def __init__(self):
        super().__init__(9, "Forest Cave", COLOR_BROWN, 1, [RESOURCE_GOLD])
    
    def effect(self, player):
        player.add_conditional_resource((RESOURCE_WOOD, RESOURCE_ORE))

class Mine(Card):
    def __init__(self):
        super().__init__(10, "Mine", COLOR_BROWN, 1, [RESOURCE_GOLD])
    
    def effect(self, player):
        player.add_conditional_resource((RESOURCE_STONE, RESOURCE_ORE))

class Glassworks(Card):
    def __init__(self):
        super().__init__(11, "Glassworks", COLOR_GREY, 1, None)
    
    def effect(self, player):
        player.add_resource(RESOURCE_GLASS)

class Press(Card):
    def __init__(self):
        super().__init__(12, "Press", COLOR_GREY, 1, None)
    
    def effect(self, player):
        player.add_resource(RESOURCE_PAPYRUS)

class Loom(Card):
    def __init__(self):
        super().__init__(13, "Loom", COLOR_GREY, 1, None)
    
    def effect(self, player):
        player.add_resource(RESOURCE_LOOM)

class Pawnshop(Card):
    def __init__(self,id):
        super().__init__(id, "Pawnshop", COLOR_BLUE, 1, None)
    
    def effect(self, player):
        player.add_points(POINTS_BLUE, 3)

class Baths(Card):
    def __init__(self,id):
        super().__init__(id,"Baths",COLOR_BLUE,1,[RESOURCE_STONE],postchains=["Baths"])
    
    def effect(self, player):
        player.add_points(POINTS_BLUE, 3)

class Altar(Card):
    def __init__(self,id):
        super().__init__(id,"Altar",COLOR_BLUE,1,None,postchains=["Temple"])
    
    def effect(self, player):
        player.add_points(POINTS_BLUE, 2)

class Theatre(Card):
    def __init__(self,id):
          super().__init__(id,"Theatre",COLOR_BLUE,1,None,postchains=["Statue"])
    
    def effect(self,player):
        player.add_points(POINTS_BLUE, 2)
    
class Tavern(Card):
    def __init__(self,id):
        super().__init__(id,"Tavern",COLOR_YELLOW,1,None)
    def effect(self,player):
         player.add_resource(RESOURCE_GOLD,5)

class MarketPlace(Card):
    def __init__(self,id):
          super().__init__(id,"MarketPlace",COLOR_YELLOW,1,None,postchains=["Caravansery"])
    
    def effect(self,player):
         player.lower_trading_cost(COLOR_GREY)

class WestTradingPost(Card):
    def __init__(self,id):
        super().__init__(id,"West Trading Post",COLOR_YELLOW,1,None,postchains=["Forum"])
    
    def effect(self,player):
         player.lower_trading_cost("west")
        
class EastTradingPost(Card):
    def __init__(self,id):
        super().__init__(id,"East Trading Post",COLOR_YELLOW,1,None,postchains=["Forum"])
    def effect(self,player):
        player.lower_trading_cost("east")

class Stockade(Card):
    def __init__(self,id):
        super().__init__(id,"Stockade",COLOR_RED,1,[RESOURCE_WOOD])
    
    def effect(self,player):
        player.add_shields(1)

class Barracks(Card):
    def __init__(self,id):
        super().__init__(id,"Barracks",COLOR_RED,1,[RESOURCE_ORE])

    def effect(self,player):
         player.add_shields(1)

class GuardTower(Card):
    def __init__(self,id):
        super().__init__(id,"Guard Tower",COLOR_RED,1,[RESOURCE_BRICK])
    
    def effect(self,player):
         player.add_shields(1)

class Apothecary(Card):
    def __init__(self,id):
        super().__init__(id,"Apothecary",COLOR_GREEN,1,[RESOURCE_LOOM],postchains=["Stables","Dispensary"])
    
    def effect(self,player):
        player.add_science(SCIENCE_COMPASS)

class Workshop(Card):
    def __init__(self,id):
        super().__init__(id,"Workshop",COLOR_GREEN,1,[RESOURCE_GLASS],postchains=["Laboratory","Archery Range"])

    def effect(self,player):
        player.add_science(SCIENCE_GEAR)

class Scriptorium(Card):
    def __init__(self,id):
        super().__init__(id,"Scriptorium",COLOR_GREEN,1,[RESOURCE_PAPYRUS],postchains=["Courthouse","Library"])
    
    def effect(self,player):
        player.add_science(SCIENCE_TABLET)

#AGE 2 CARDS
        
#BROWN CARDS
class Sawmill(Card):
    def __init__(self,id):
        super().__init__(id,"Sawmill",COLOR_BROWN,2,[RESOURCE_GOLD])
    def effect(self,player):
        player.add_resource(RESOURCE_WOOD,2)

class Quarry(Card):
    def __init__(self,id):
        super().__init__(id,"Quarry",COLOR_BROWN,2,[RESOURCE_GOLD])
    def effect(self,player):
        player.add_resource(RESOURCE_STONE,2)

class Brickyard(Card):
    def __init__(self,id):
        super().__init__(id,"Brickyard",COLOR_BROWN,2,[RESOURCE_GOLD])
    
    def effect(self,player):
        player.add_resource(RESOURCE_BRICK,2)

class Foundry(Card):
    def __init__(self,id):
        super().__init__(id,"Foundry",COLOR_BROWN,2,[RESOURCE_GOLD])

    def effect(self,player):
        player.add_resource(RESOURCE_ORE,2) 

#Blue cards
        
class Statue(Card):
    def __init__(self,id):
        super().__init__(id,"Statue",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE],["Theatre"],["Gardens"])
    
    def effect(self,player):
        player.add_points(POINTS_BLUE,4)

class Aqueduct(Card):
    def __init__(self,id):
        super().__init__(id,"Aqueduct",COLOR_BLUE,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],["Baths"])
    
    def effect(self,player):
        player.add_points(POINTS_BLUE,5)

class Temple(Card):
    def __init__(self,id):
        super().__init__(id,"Temple",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_GLASS],["Altar"],["Pantheon"])

    def effect(self,player):
        player.add_points(POINTS_BLUE,4)

class Courthouse(Card):
    def __init__(self,id):
        super().__init__(id,"Courthouse",COLOR_BLUE,2,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_LOOM],["Scriptorium"])

    def effect(self,player):
        player.add_points(POINTS_BLUE,4)

# YELLOW CARDS
        
class Caravansery(Card):
    def __init__(self,id):
        super().__init__(id,"Caravansery",COLOR_YELLOW,2,[RESOURCE_WOOD,RESOURCE_WOOD],["East Trading Post","West Trading Post"],["Lighthouse"])

    def effect(self,player):
        player.add_free_conditional_resource(COLOR_BROWN)

class Forum(Card):
    def __init__(self,id):
        super().__init__(id,"Forum",COLOR_YELLOW,2,[RESOURCE_BRICK,RESOURCE_BRICK],["Marketplace"],["Haven"])

    def effect(self,player):
        player.add_free_conditional_resource(COLOR_GREY)

class Vineyard(Card):
    def __init__(self,id,queue):
        super().__init__(id,"Vineyard",COLOR_YELLOW,2,None)
        self.queue = queue
    def effect(self,player):
        self.queue.insert(0,player.add_coins_per_card(1,COLOR_BROWN,True,True,True))

class Bazar(Card):
    def __init__(self,id,queue):
        super().__init__(id,"Bazar",COLOR_YELLOW,2,None)
        self.queue = queue
    def effect(self,player):
        self.queue.insert(0,player.add_coins_per_card(2,COLOR_GREY,True,True,True))

#Red Cards
        
class Stables(Card):
    def __init__(self,id):
        super().__init__(id,"Stables",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_ORE],["Apothecary"])
    
    def effect(self,player):
        player.add_shields(2)

class ArcheryRange(Card):
    def __init__(self,id):
        super().__init__(id,"Archery Range",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_ORE],["Workshop"])
    
    def effect(self,player):
        player.add_shields(2)

class Walls(Card):
    def __init__(self,id):
        super().__init__(id,"Walls",COLOR_RED,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],postchains=["Fortifications"])

    def effect(self,player):
        player.add_shields(2)

class TrainingGround(Card):
    def __init__(self,id):
        super().__init__(id,"Training Ground",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE],postchains=["Circus"])
    
    def effect(self,player):
        player.add_shields(2)

# Green Cards
        
class Dispensary(Card):
    def __init__(self,id):
        super().__init__(id,"Dispensary",COLOR_GREEN,2,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_GLASS],["Apothecary"],["Lodge","Arena"])
    
    def effect(self,player):
        player.add_science(SCIENCE_COMPASS)

class Laboratory(Card):
    def __init__(self,id):
        super().__init__(id,"Laboratory",COLOR_GREEN,2,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS],["Workshop"],["Observatory","Siege Workshop"])
    
    def effect(self,player):
        player.add_science(SCIENCE_GEAR)

class Library(Card):
    def __init__(self,id):
        super().__init__(id,"Library",COLOR_GREEN,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_LOOM],["Scriptorium"],["Senate","University"])

    def effect(self,player):
        player.add_science(SCIENCE_TABLET)

class School(Card) :
    def __init__(self,id):
        super().__init__(id,"School",COLOR_GREEN,2,[RESOURCE_WOOD,RESOURCE_PAPYRUS],postchains=["Academy","Study"])
    
    def effect(self,player):
        player.add_science(SCIENCE_TABLET)

#AGE 3 Cards
        
# Blue cards
        
class Pantheon(Card):
    def __init__(self,id):
        super().__init__(id,"Pantheon",COLOR_BLUE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_ORE,RESOURCE_GLASS,RESOURCE_PAPYRUS,RESOURCE_LOOM],["Temple"])
    
    def effect(self,player):
        player.add_points(POINTS_BLUE,7)

class Gardens(Card):
    def __init__(self,id):
        super().__init__(id,"Gardens",COLOR_BLUE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_WOOD],["Statue"])

    def effect(self,player):
        player.add_points(POINTS_BLUE,5)

class TownHall(Card):
    def __init__(self,id):
        super().__init__(id,"Town Hall",COLOR_BLUE,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE,RESOURCE_GLASS])

    def effect(self,player):
        player.add_points(POINTS_BLUE,6)

class Palace(Card):
    def __init__(self,id):
        super().__init__(id,"Palace",COLOR_BLUE,3,[RESOURCE_STONE,RESOURCE_ORE,RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_GLASS,RESOURCE_PAPYRUS,RESOURCE_LOOM])

    def effect(self,player):
        player.add_points(POINTS_BLUE,8)

class Senate(Card):
    def __init__(self,id):
        super().__init__(id,"Senate",COLOR_BLUE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_STONE,RESOURCE_ORE],["Library"])
    
    def effect(self,player):
        player.add_points(POINTS_BLUE,6)

#Yellow Cards

class Lighthouse(Card):
    def __init__(self,id):
        super().__init__(id,"Lighthouse",COLOR_YELLOW,3,[RESOURCE_STONE,RESOURCE_GLASS],["Caravansery"])

    def effect(self,player):
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_YELLOW,COLOR_YELLOW))
        player.add_coins_per_card(1,COLOR_YELLOW)

class Haven(Card):
    def __init__(self,id):
        super().__init__(id,"Haven",COLOR_YELLOW,3,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_LOOM],["Forum"])
    
    def effect(self,player):
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_YELLOW,COLOR_BROWN))
        player.add_coins_per_card(1,COLOR_BROWN)

class ChamberOfCommerce(Card):
    def __init__(self,id):
        super().__init__(id,"Chamber of Commerce",COLOR_YELLOW,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS])
    
    def effect(self,player):
        player.add_endgame_function(lambda p : p.add_points_per_card(2,POINTS_YELLOW,COLOR_GREY))
        player.add_coins_per_card(2,COLOR_GREY)

class Arena(Card):
    def __init__(self,id):
        super().__init__(id,"Arena",COLOR_YELLOW,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE],["Dispensary"])
    
    def effect(self,player):
        player.add_endgame_function(lambda p : p.add_points_per_wonder(1,POINTS_YELLOW))
        player.add_coins_per_card(1,"wonder")

#Red Cards
        
class Fortifications(Card):
    def __init__(self,id):
        super().__init__(id,"Fortifications",COLOR_RED,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE],["Walls"])
    
    def effect(self,player):
        player.add_shields(3)

class Circus(Card):
    def __init__(self,id):
        super().__init__(id,"Circus",COLOR_RED,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE],["Training Ground"])

    def effect(self,player):
        player.add_shields(3)

class Arsenal(Card):
    def __init__(self,id):
        super().__init__(id,"Arsenal",COLOR_RED,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_LOOM])

    def effect(self,player):
        player.add_shields(3)

class SiegeWorkshop(Card):
    def __init__(self,id):
        super().__init__(id," Siege Workshop",COLOR_RED,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_WOOD],["Laboratory"])

    def effect(self,player):
        player.add_shields(3)

#Green Cards

class Lodge(Card) :
    def __init__(self,id) :
        super().__init__(id,"Lodge",COLOR_GREEN,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS,RESOURCE_LOOM],["Dispensary"])

    def effect(self,player) :
        player.add_science(SCIENCE_COMPASS)

class Academy(Card) :
    def __init__(self,id) :
        super().__init__(id,"Academy",COLOR_GREEN,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_GLASS],["School"])
    
    def effect(self,player) :
        player.add_science(SCIENCE_COMPASS)

class Observatory(Card) :
    def __init__(self,id) :
        super().__init__(id,"Observatory",COLOR_GREEN,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_GLASS,RESOURCE_LOOM],["Laboratory"])
    
    def effect(self,player) :
        p.add_science(SCIENCE_GEAR)

class Study(Card) :
    def __init__(self,id) :
        super().__init__(id,"Study",COLOR_GREEN,3,[RESOURCE_WOOD,RESOURCE_PAPYRUS,RESOURCE_LOOM],["School"])
    
    def effect(self,player) :
        player.add_science(SCIENCE_GEAR)

class University(Card):
    def __init__(self,id) :
        super().__init__(id,"University",COLOR_GREEN,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_PAPYRUS,RESOURCE_GLASS],["Library"])

    def effect(self,player) :
        player.add_science(SCIENCE_TABLET)

#Purple Cards
        
class WorkersGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Workers Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_BRICK,RESOURCE_STONE,RESOURCE_WOOD])

    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_BROWN,False,True,True))

class CraftmensGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Craftmen's Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE,RESOURCE_STONE])
    
    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_card(2,POINTS_PURPLE,COLOR_GREY,False,True,True))

class MagistratesGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Magistrates Guild",COLOR_PURPLE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_STONE,RESOURCE_LOOM])

    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_BLUE,False,True,True))

class TradersGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Traders Guild",COLOR_PURPLE,3,[RESOURCE_GLASS,RESOURCE_LOOM,RESOURCE_PAPYRUS])

    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_YELLOW,False,True,True))

class BuildersGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Builders Guild",COLOR_PURPLE,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_GLASS])

    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_wonder(1,POINTS_PURPLE,True,True,True))

class SpiesGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Spies Guild",COLOR_PURPLE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_GLASS])

    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_RED,False,True,True))

class PhilosophersGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Philosophers Guild",COLOR_PURPLE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS,RESOURCE_LOOM])

    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_GREEN,False,True,True))

class StrategistsGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Strategists Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE,RESOURCE_LOOM])

    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points(POINTS_RED,p.west_player.war_losses+p.east_player.war_losses))

class ScientistsGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Scientists Guild",COLOR_PURPLE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_PAPYRUS])
    
    def effect(self,player) :
        player.add_science("any")

class ShipownersGuild(Card) :
    def __init__(self,id) :
        super().__init__(id,"Shipowners Guild",COLOR_PURPLE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_GLASS,RESOURCE_PAPYRUS])
    def effect(self,player) :
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_BROWN))
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_GREY))
        player.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_PURPLE))



#c = Card("test","red",[0,0,0,1,0,0,0],lambda player: player.add_resource(RESOURCE_WOOD,1))
player = Player("Jakob")

#TODO Implement pre and post chains
#TODO test functionality of every card
#TODO Make cards that give coins go to end of queue
#Card(id,name,color,age,cost,function)
#{coins,wood,stone,bricks,ore,glass,papyrus,textile}
#AGE 1 CARDS

#Age 1 Brown cards
c1 =   Card(1,"Lumber Yard",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_WOOD))  #wood
c2 =   Card(2,"Stone Pit",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_STONE))  #stone
c3 =   Card(3,"Clay Pool",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_BRICK))  #bricks
c4 =   Card(4,"Ore Vein",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_ORE))  #ore
c5 =   Card(5,"Tree Farm",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_BRICK))) # wood\bricks
c6 =   Card(6,"Excavation",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_STONE,RESOURCE_BRICK)))  # stone\bricks
c7 =   Card(7,"Clay Pit",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_ORE,RESOURCE_BRICK)))  # ore\bricks
c8 =   Card(8,"Timber Yard",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_STONE)))  # wood\stone
c9 =   Card(9,"Forest Cave",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_ORE)))  # wood\ore
c10 =   Card(10,"Mine",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_STONE,RESOURCE_ORE)))  # stone\ore

 #Age 1 Grey cards
c11 =   Card(11,"Glassworks",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_GLASS))  #glass
c12 =   Card(12,"Press",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_PAPYRUS))  #papyrus
c13 =   Card(13,"Loom",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_LOOM))  #loom

 #Age 1 Blue cards
c14 = Card(14,"Pawnshop",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,3))  #3 blue points
c15 = Card(15,"Baths",COLOR_BLUE,1,[RESOURCE_STONE],lambda p : p.add_points(POINTS_BLUE,3),None,["Baths"])  #3 blue points
c16 = Card(16,"Altar",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2),None,["Temple"])  #2 blue points
c17 = Card(17,"Theatre",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2),None,["Statue"])  #2 blue points

#Age 1 Yellow cards
c18 = Card(18,"Tavern",COLOR_YELLOW,1,None,lambda p : p.add_resource(RESOURCE_GOLD,5))  #5 coins
c19 = Card(19,"Marketplace",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost(COLOR_GREY),None,["Caravansery"])  #lower both grey trading costs
c20 = Card(20,"West Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("east"),None,["Forum"])  #lower east brown trading costs
c21 = Card(21,"East Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("west"),None,["Forum"])  #lower west brown trading costs

 #Age 1 Red cards
c22 = Card(22,"Stockade",COLOR_RED,1,[RESOURCE_WOOD], lambda p : p.add_shields(1))
c23 = Card(23,"Barracks",COLOR_RED,1,[RESOURCE_ORE],lambda p : p.add_shields(1))
c24 = Card(24,"Guard Tower",COLOR_RED,1,[RESOURCE_BRICK],lambda p : p.add_shields(1))

 #Age 1 Green cards
c25 = Card(25,"Apothecary",COLOR_GREEN,1,[RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_COMPASS),None,["Stables","Dispensary"])  #compass
c26 = Card(26,"Workshop",COLOR_GREEN,1,[RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_GEAR),None,["Laboratory","Archery Range"])  #gear
c27 = Card(27,"Scriptorium",COLOR_GREEN,1,[RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_TABLET),None,["Courthouse","Library"])  #tablet

 #AGE 2 CARDS

 #Age 2 Brown cards
c28 = Card(28,"Sawmill",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_WOOD,2))  #2 wood
c29 = Card(29,"Quarry",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_STONE,2))  #2 stone
c30 = Card(30,"Brickyard",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_BRICK,2))  #2 brick
c31 = Card(31,"Foundry",COLOR_BROWN,2,[RESOURCE_GOLD],lambda p : p.add_resource(RESOURCE_ORE,2))  #2 ore

 #Age 2 Grey cards
c32 = Card(32,"Glassworks",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_GLASS))  #glass
c33 = Card(33,"Press",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_PAPYRUS))  #papyrus
c34 = Card(34,"Loom",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_LOOM))  #loom

 #Age 2 Blue cards
c35 = Card(35,"Statue",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_points(POINTS_BLUE,4),["Theatre"],["Gardens"])  #4 Blue Points
c36 = Card(36,"Aqueduct",COLOR_BLUE,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_BLUE,5),["Baths"])  #5 Blue Points
c37 = Card(37,"Temple",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_GLASS],lambda p : p.add_points(POINTS_BLUE,4),["Altar"],["Pantheon"])  #4 Blue Points
c38 = Card(38,"Courthouse",COLOR_BLUE,2,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_LOOM],lambda p : p.add_points(POINTS_BLUE,4),["Scriptorium"])  #4 Blue Points

 #Age 2 Yellow cards
c39 = Card(39,"Caravansery",COLOR_YELLOW,2,[RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_free_conditional_resource(COLOR_BROWN),["East Trading Post","West Trading Post"],["Lighthouse"]) #Brown resources composition
c40 = Card(40,"Forum",COLOR_YELLOW,2,[RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_free_conditional_resource(COLOR_GREY),["Marketplace"],["Haven"])  #Grey ressources composition

#TODO make these go to end of queue
c41 = Card(41,"Vineyard",COLOR_YELLOW,2,None,game.add_effect_to_queue("Vineyard"))  #Add coins = brown cards of you and neighbors
c42 = Card(42,"Bazar",COLOR_YELLOW,2,None,game.add_effect_to_queue("Bazar")) #Add coins = 2 x grey cards of you and neighbors

 #Age 2 Red cards
c43 = Card(43,"Stables",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_ORE],lambda p : p.add_shields(2),["Apothecary"])
c44 = Card(44,"Archery Range",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_ORE],lambda p : p.add_shields(2),["Workshop"])
c45 = Card(45,"Walls",COLOR_RED,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_shields(2),None,["Fortifications"])
c46 = Card(46,"Training Ground",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_shields(2),None,["Circus"])

 #Age 2 Green cards
c47 = Card(47,"Dispensary",COLOR_GREEN,2,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_COMPASS),["Apothecary"],["Lodge","Arena"])  #compass
c48 = Card(48,"Laboratory",COLOR_GREEN,2,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_GEAR),["Workshop"],["Observatory","Siege Workshop"])  #gear
c49 = Card(49,"Library",COLOR_GREEN,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_TABLET),["Scriptorium"],["Senate","University"])  #tablet
c50 = Card(50,"School",COLOR_GREEN,2,[RESOURCE_WOOD,RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_TABLET),None,["Academy","Study"])  #tablet


 #AGE 3 CARDS

 #Age 3 Blue cards
c51 = Card(51,"Pantheon",COLOR_BLUE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_ORE,RESOURCE_GLASS,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_points(POINTS_BLUE,7),["Temple"])  #7 Blue Points
c52 = Card(52,"Gardens",COLOR_BLUE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_WOOD],lambda p : p.add_points(POINTS_BLUE,5),["Statue"])  #5 Blue Points
c53 = Card(53,"Town Hall",COLOR_BLUE,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE,RESOURCE_GLASS],lambda p : p.add_points(POINTS_BLUE,6))  #6 Blue Points
c54 = Card(54,"Palace",COLOR_BLUE,3,[RESOURCE_STONE,RESOURCE_ORE,RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_GLASS,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_points(POINTS_BLUE,8))  #8 Blue Points
c55 = Card(55,"Senate",COLOR_BLUE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_STONE,RESOURCE_ORE],lambda p : p.add_points(POINTS_BLUE,6),["Library"])  #6 Blue Points

 #Age 3 Yellow cards
c56 = Card(56,"Lighthouse",COLOR_YELLOW,3,[RESOURCE_STONE,RESOURCE_GLASS],lambda p : p.add_endgame_function(lambda p: p.add_points_per_card(1,POINTS_YELLOW,COLOR_YELLOW)),["Caravansery"]) #Add points = number of yellow cards (end of game) 
c56.effect_2 = lambda p : p.add_coins_per_card(1,COLOR_YELLOW) #Add coins = number of previous yellow cards (the lighthouse counts)

c57 = Card(57,"Haven",COLOR_YELLOW,3,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p: p.add_points_per_card(1,POINTS_YELLOW,COLOR_BROWN)),["Forum"]) #Add points = number of brown cards (end of game) 
c57.effect_2 = lambda p : p.add_coins_per_card(1,COLOR_BROWN) #Add coins = number of previous brown cards 

c58 = Card(58,"Chamber of Commerce",COLOR_YELLOW,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS],lambda p : p.add_endgame_function(lambda p: p.add_points_per_card(2,POINTS_YELLOW,COLOR_GREY))) #Add points = number of grey cards (end of game) 
c58.effect_2 = lambda p : p.add_coins_per_card(2,COLOR_GREY) #Add coins = number of previous grey cards 

c59 = Card(59,"Arena",COLOR_YELLOW,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE],lambda p : p.add_endgame_function(lambda p: p.add_points_per_wonder(1,POINTS_YELLOW)),["Dispensary"]) #Add points = number of wonders stages(end of game) 
c59.effect_2 = lambda p : p.add_coins_per_card(3,"wonder") #Add coins = number of wonders stages 

#Age 3 Red cards
c60 = Card(60,"Fortifications",COLOR_RED,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE],lambda p : p.add_shields(3),["Walls"])
c61 = Card(61,"Circus",COLOR_RED,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE],lambda p : p.add_shields(3),["Training Ground"])
c62 = Card(62,"Arsenal",COLOR_RED,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_LOOM],lambda p : p.add_shields(3))
c63 = Card(63,"Siege Workshop",COLOR_RED,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_WOOD],lambda p : p.add_shields(3),["Laboratory"])

#Age 3 Green cards
c64 = Card(64,"Lodge",COLOR_GREEN,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_COMPASS),["Dispensary"])  #compass
c65 = Card(65,"Academy",COLOR_GREEN,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_COMPASS),["School"])  #compass
c66 = Card(66,"Observatory",COLOR_GREEN,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_GLASS,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_GEAR),["Laboratory"])  #gear
c67 = Card(67,"Study",COLOR_GREEN,3,[RESOURCE_WOOD,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_GEAR),["School"])  #gear
c68 = Card(68,"University",COLOR_GREEN,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_PAPYRUS,RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_TABLET),["Library"])  #tablet

#Age 3 purple cards
c69 = Card(69,"Workers Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_BRICK,RESOURCE_STONE,RESOURCE_WOOD],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_BROWN,False,True,True))) 
c70 = Card(70,"Craftmens Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(2,POINTS_PURPLE,COLOR_GREY,False,True,True)))
c71 = Card(71,"Magistrates Guild",COLOR_PURPLE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_STONE,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_BLUE,False,True,True))) 
c72 = Card(72,"Traders Guild",COLOR_PURPLE,3,[RESOURCE_GLASS,RESOURCE_LOOM,RESOURCE_PAPYRUS],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_YELLOW,False,True,True))) 

c73 = Card(73,"Builders Guild",COLOR_PURPLE,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_GLASS],lambda p : p.add_endgame_function(lambda p : p.add_points_per_wonder(1,POINTS_PURPLE,True,True,True)))

c74 =   Card(74,"Spies Guild",COLOR_PURPLE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_GLASS],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_RED,False,True,True))) 
c75 =   Card(75,"Philosophers Guild",COLOR_PURPLE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_GREEN,False,True,True))) 
c76 =   Card(76,"Strategists Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p : p.add_points(POINTS_RED,p.west_player.war_losses+p.east_player.war_losses)))
c77 =   Card(77,"Scientists Guild",COLOR_PURPLE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_PAPYRUS],lambda p : p.add_science("any"))  #Conditional science
c78 =   Card(78,"Shipowners Guild",COLOR_PURPLE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_GLASS,RESOURCE_PAPYRUS],lambda p : p.shipowners_guild())
