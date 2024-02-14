from Players import *
from common import *
from Cards import *

p1 = Player("Player 1")
east = Player("East Player")
west = Player("West Player")

p1.set_east_player(east)
p1.set_west_player(west)
p1.lower_trading_cost("west")
p1.lower_trading_cost("both")

p1.add_resource(RESOURCE_GOLD,5) #Total 8
#p1.add_resource(RESOURCE_WOOD,1)
west.add_resource(RESOURCE_ORE,1)
#p1.add_resource(RESOURCE_BRICK,1)
east.add_resource(RESOURCE_STONE,1)
p1.add_resource(RESOURCE_LOOM,1)
p1.add_resource(RESOURCE_PAPYRUS,1)
east.add_resource(RESOURCE_GLASS,1)

p1.add_free_conditional_resource(COLOR_BROWN)
east.add_conditional_resource((RESOURCE_STONE,RESOURCE_WOOD))
west.add_conditional_resource((RESOURCE_ORE,RESOURCE_STONE))
east.add_conditional_resource((RESOURCE_ORE,RESOURCE_STONE))


#cards
craftsmen = CraftmensGuild(1) #2 ore 2 stone
palace = Palace(2) #one of each

print(p1.get_price(palace))