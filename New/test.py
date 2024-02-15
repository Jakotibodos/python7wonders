from Players import *
from common import *
from Cards import *
from Wonders import *

p1 = Player("Player 1")
east = Player("East Player")
west = Player("West Player")
p1.set_wonder(Ephesos(p1))

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


#cards
craftsmen = CraftmensGuild(1) #2 ore 2 stone
palace = Palace(2) #one of each


print(p1.get_price(p1.wonder))
p1.wonder.effect(p1)
print(p1.get_price(p1.wonder))
p1.wonder.effect(p1)
print(p1.get_price(p1.wonder))
p1.print_score()
