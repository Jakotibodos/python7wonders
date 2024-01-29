
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
c7 =   Card(7,"Clay_Pit",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_ORE,RESOURCE_BRICK)))  # ore\bricks
c8 =   Card(8,"Timber Yard",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_STONE)))  # wood\stone
c9 =   Card(9,"Forest Cave",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_ORE)))  # wood\ore
c10 =   Card(10,"Mine",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_STONE,RESOURCE_ORE)))  # stone\ore

 #Age 1 Grey cards
c11 =   Card(11,"Glassworks",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_GLASS))  #glass
c12 =   Card(12,"Press",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_PAPYRUS))  #papyrus
c13 =   Card(13,"Loom",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_LOOM))  #loom

 #Age 1 Blue cards
c14 = Card(14,"Pawnshop",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,3))  #3 blue points
c15 = Card(15,"Baths",COLOR_BLUE,1,[RESOURCE_STONE],lambda p : p.add_points(POINTS_BLUE,3))  #3 blue points
c16 = Card(16,"Altar",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2))  #2 blue points
c17 = Card(17,"Theatre",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2))  #2 blue points

 #Age 1 Yellow cards
c18 = Card(18,"Tavern",COLOR_YELLOW,1,None,lambda p : p.add_resource(RESOURCE_GOLD,5))  #5 coins
c19 = Card(19,"Marketplace",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost(COLOR_GREY))  #lower both grey trading costs
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
c32 = Card(32,"Glassworks",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_GLASS))  #glass
c33 = Card(33,"Press",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_PAPYRUS))  #papyrus
c34 = Card(34,"Loom",COLOR_GREY,2,None,lambda p : p.add_resource(RESOURCE_LOOM))  #loom

 #Age 2 Blue cards
c35 = Card(35,"Statue",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_points(POINTS_BLUE,4))  #4 Blue Points
c36 = Card(36,"Aqueduct",COLOR_BLUE,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_points(POINTS_BLUE,5))  #5 Blue Points
c37 = Card(37,"Temple",COLOR_BLUE,2,[RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_GLASS],lambda p : p.add_points(POINTS_BLUE,4))  #4 Blue Points
c38 = Card(38,"Courthouse",COLOR_BLUE,2,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_LOOM],lambda p : p.add_points(POINTS_BLUE,4))  #4 Blue Points

 #Age 2 Yellow cards
c39 = Card(39,"Caravansery",COLOR_YELLOW,2,[RESOURCE_WOOD,RESOURCE_WOOD],lambda p : p.add_free_conditional_resource(COLOR_BROWN)) #Brown resources composition
c40 = Card(40,"Forum",COLOR_YELLOW,2,[RESOURCE_BRICK,RESOURCE_BRICK],lambda p : p.add_free_conditional_resource(COLOR_GREY))  #Grey ressources composition

#TODO make these go to end of queue
c41 = Card(41,"Vineyard",COLOR_YELLOW,2,None,lambda p : p.add_coins_per_card(1,COLOR_BROWN,True,True,True))  #Add coins = brown cards of you and neighbors
c42 = Card(42,"Bazar",COLOR_YELLOW,2,None,lambda p : p.add_coins_per_card(2,COLOR_GREY,True,True,True)) #Add coins = 2 x grey cards of you and neighbors

 #Age 2 Red cards
c43 = Card(43,"Stables",COLOR_RED,[RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_ORE],2,lambda p : p.add_shields(2))
c44 = Card(44,"Archery Range",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_ORE],lambda p : p.add_shields(2))
c45 = Card(45,"Walls",COLOR_RED,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_shields(2))
c46 = Card(46,"Training Ground",COLOR_RED,2,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE],lambda p : p.add_shields(2))

 #Age 2 Green cards
c47 = Card(47,"Dispensary",COLOR_GREEN,2,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_COMPASS))  #compass
c48 = Card(48,"Laboratory",COLOR_GREEN,2,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_GEAR))  #gear
c49 = Card(49,"Library",COLOR_GREEN,2,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_TABLET))  #tablet
c50 = Card(50,"School",COLOR_GREEN,2,[RESOURCE_WOOD,RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_TABLET))  #tablet


 #AGE 3 CARDS

 #Age 3 Blue cards
c51 = Card(51,"Pantheon",COLOR_BLUE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_ORE,RESOURCE_GLASS,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_points(POINTS_BLUE,7))  #7 Blue Points
c52 = Card(52,"Gardens",COLOR_BLUE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_WOOD],lambda p : p.add_points(POINTS_BLUE,7))  #5 Blue Points
c53 = Card(53,"Town Hall",COLOR_BLUE,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE,RESOURCE_GLASS],lambda p : p.add_points(POINTS_BLUE,6))  #6 Blue Points
c54 = Card(54,"Palace",COLOR_BLUE,3,[RESOURCE_STONE,RESOURCE_ORE,RESOURCE_WOOD,RESOURCE_BRICK,RESOURCE_GLASS,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_points(POINTS_BLUE,8))  #8 Blue Points
c55 = Card(55,"Senate",COLOR_BLUE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_STONE,RESOURCE_ORE],lambda p : p.add_points(POINTS_BLUE,6))  #6 Blue Points

 #Age 3 Yellow cards
c56 = Card(56,"Lighthouse",COLOR_YELLOW,3,[RESOURCE_STONE,RESOURCE_GLASS],lambda p : p.add_endgame_function(lambda p: p.add_points_per_card(1,POINTS_YELLOW,COLOR_YELLOW))) #Add points = number of yellow cards (end of game) 
c56.effect_2 = lambda p : p.add_coins_per_card(1,COLOR_YELLOW) #Add coins = number of previous yellow cards (the lighthouse counts)

c57 = Card(57,"Haven",COLOR_YELLOW,3,[RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p: p.add_points_per_card(1,POINTS_YELLOW,COLOR_BROWN))) #Add points = number of brown cards (end of game) 
c57.effect_2 = lambda p : p.add_coins_per_card(1,COLOR_BROWN) #Add coins = number of previous brown cards 

c58 = Card(58,"Chamber of Commerce",COLOR_YELLOW,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS],lambda p : p.add_endgame_function(lambda p: p.add_points_per_card(2,POINTS_YELLOW,COLOR_GREY))) #Add points = number of grey cards (end of game) 
c58.effect_2 = lambda p : p.add_coins_per_card(2,COLOR_GREY) #Add coins = number of previous grey cards 

#TODO Make wonders work for this one
c59 = Card(57,"Haven",COLOR_YELLOW,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE],lambda p : p.add_endgame_function(lambda p: p.add_points_per_card(1,POINTS_YELLOW,"WONDER"))) #Add points = number of wonders (end of game) 
c59.effect_2 = lambda p : p.add_coins_per_card(3,"WONDER") #Add coins = number of previous

#Age 3 Red cards
c60 = Card(60,"Fortifications",COLOR_RED,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE],lambda p : p.add_shields(3))
c61 = Card(61,"Circus",COLOR_RED,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_ORE],lambda p : p.add_shields(3))
c62 = Card(62,"Arsenal",COLOR_RED,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_LOOM],lambda p : p.add_shields(3))
c63 = Card(63,"Siege Workshop",COLOR_RED,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_WOOD],lambda p : p.add_shields(3))

#Age 3 Green cards
c64 = Card(64,"Lodge",COLOR_GREEN,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_COMPASS))  #compass
c65 = Card(65,"Academy",COLOR_GREEN,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_STONE,RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_COMPASS))  #compass
c66 = Card(66,"Observatory",COLOR_GREEN,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_GLASS,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_GEAR))  #gear
c67 = Card(67,"Study",COLOR_GREEN,3,[RESOURCE_WOOD,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_GEAR))  #gear
c68 = Card(68,"University",COLOR_GREEN,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_PAPYRUS,RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_TABLET))  #tablet

#Age 3 purple cards
c69 = Card(69,"Workers Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_BRICK,RESOURCE_STONE,RESOURCE_WOOD],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_BROWN,False,True,True))) 
c70 = Card(70,"Craftmens Guild",COLOR_PURPLE,3,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE,RESOURCE_STONE],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(2,POINTS_PURPLE,COLOR_GREY,False,True,True)))
c71 = Card(71,"Magistrates Guild",COLOR_PURPLE,3,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_STONE,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_BLUE,False,True,True))) 
c72 = Card(72,"Traders Guild",COLOR_PURPLE,3,[RESOURCE_GLASS,RESOURCE_LOOM,RESOURCE_PAPYRUS],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_YELLOW,False,True,True))) 

#TODO make work with wonders 
c73 = Card(73,"Builders Guild",COLOR_PURPLE,3,[RESOURCE_STONE,RESOURCE_STONE,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_GLASS],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,"WONDER",True,True,True)))

c74 =   Card(74,"Spies Guild",COLOR_PURPLE,3,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_GLASS],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_RED,False,True,True))) 
c75 =   Card(75,"Philosophers Guild",COLOR_PURPLE,[RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_BRICK,RESOURCE_PAPYRUS,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p : p.add_points_per_card(1,POINTS_PURPLE,COLOR_GREEN,False,True,True))) 
c76 =   Card(76,"Strategists Guild",COLOR_PURPLE,[RESOURCE_ORE,RESOURCE_ORE,RESOURCE_STONE,RESOURCE_LOOM],lambda p : p.add_endgame_function(lambda p : p.add_points(POINTS_RED,p.west_player.war_losses+p.east_player.war_losses)))
c77 =   Card(77,"Scientists Guild",COLOR_PURPLE,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_ORE,RESOURCE_ORE,RESOURCE_PAPYRUS],lambda p : p.add_science("any"))  #Conditional science
c78 =   Card(78,"Shipowners Guild",COLOR_PURPLE,[RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_WOOD,RESOURCE_GLASS,RESOURCE_PAPYRUS],lambda p : p.shipowners_guild())
