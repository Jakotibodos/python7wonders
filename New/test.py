from Players import *
from common import *
from Cards import *
from Wonders import *
from game import *

p1 = Player("Player 1")
east = Player("East Player")
west = Player("West Player")
p1.set_wonder(Alexandria(p1))

p1.set_east_player(east)
p1.set_west_player(west)


p1.add_resource(RESOURCE_GOLD,-1) #Total 7
#east.add_resource(RESOURCE_WOOD,1)
#west.add_resource(RESOURCE_ORE,1)
p1.add_resource(RESOURCE_BRICK,1)
east.add_resource(RESOURCE_STONE,1)
east.add_conditional_resource((RESOURCE_STONE,RESOURCE_WOOD))
east.add_resource(RESOURCE_BRICK,2)
east.add_resource(RESOURCE_WOOD,1)
#east.add_resource(RESOURCE_STONE,4)
#east.add_resource(RESOURCE_LOOM,1)
#p1.add_resource(RESOURCE_PAPYRUS,1)
#p1.add_resource(RESOURCE_GLASS,1)
west.add_resource(RESOURCE_PAPYRUS,0)

p1.add_free_conditional_resource(COLOR_BROWN)
p1.add_free_conditional_resource(COLOR_GREY)
p1.add_free_conditional_resource(COLOR_BROWN)
#p1.add_free_conditional_resource(COLOR_GREY)
#p1.add_conditional_resource((RESOURCE_WOOD,RESOURCE_STONE))
p1.add_conditional_resource((RESOURCE_ORE,RESOURCE_BRICK))



#cards
craftsmen = CraftmensGuild(1) #2 ore 2 stone
palace = Palace(2) #one of each
library = Library() 
walls = Walls()
t = TownHall()
c = Caravansery()
dispensary = Dispensary()
pantheon = Pantheon()
lodge=Lodge()
study = Study()
p1.hand =[c,dispensary,lodge,study]

print(p1.free_conditional_resources)
print(p1.conditional_resources)
print(p1.resources)
print(p1.get_price(study))
p1.print_available_cards(p1.show_available_cards()[0],p1.show_available_cards()[1])

