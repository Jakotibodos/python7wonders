
from Players import Player
from common import *
import game

class Card:
	def __init__(self, id,name,color,age,cost,prechains=[],postchains=[]):
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

#Age 1 Cards
    
#Brown Cards 
    
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

#Grey Cards
        
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

#Blue Cards 
        
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
    
#Yellow 
        
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

#Red cards
        
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

#Green Cards 
         
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