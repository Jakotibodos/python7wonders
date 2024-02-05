from Players import Player
from common import *
from random import randint, choice, shuffle
from Wonders import Wonder
from Cards import Card

discard_pile = []
queue = []

def main():
    #TODO
    nbplayers = int(input("Enter number of players: "))
    while (nbplayers < 3 and nbplayers > 6):
        print("Player count must be between 3 and 6")
        nbplayers = int(input("\nEnter number of player: "))

    players = players_setup() #Includes wonder setup

    for age in range(1,4):
        for turn in range(6):
            for player in players:
                play_turn(player) 
            if turn == 5: #last turn
                if player.has_double_last_cards():
                    player.play_turn(player)
                else:
                    discard_last_card(player)

            for effect in queue: #For cards that give coins depending on card counts (and Halikarnassos discard play)
                effect() #maybe these will be (effect,player) in queue
            queue = []
            
            switch_hands(players)

        for player in players:
            player.war((age*2)-1) #1, 3 and 5
                    
def switch_hands(playerlist,age):
    player = playerlist[0]
    temp_hand = player.hand
    if age == 2: #for age 2, counterclockwise switching
        for _ in range(len(playerlist)-1):
            player.hand = player.west_player.hand
            player = player.west_player
        player.hand = temp_hand    
    else: #for age 1 and 3, clockwise switching
        for _ in range(len(playerlist)-1):
            player.hand = player.east_player.hand
            player = player.east_player
        player.hand = temp_hand 

def discard_last_card(player):
    discard_pile.append(player.hand.pop())

def play_turn(player):
    player.show_available_cards() #TODO
    card = select_card(player) #Add card count at this stage
    card.effect(player)
    if hasattr(card,"effect_2"): #For cards that give coins depending on card counts
        add_effect_to_queue(card.effect_2)


def add_effect_to_queue(player,name):
    if name == "Vineyard":
        queue.insert(0,(lambda p : p.add_coins_per_card(1,COLOR_BROWN,True,True,True),player))
    elif name == "Bazar":
        queue.insert(0,(lambda p : p.add_coins_per_card(2,COLOR_GREY,True,True,True),player))
    elif name == "Halikarnassos":
        if player.wonder.side == "B":
            player.add_resource(RESOURCE_GOLD,2-player.wonder.stages_completed)
        queue.append((lambda p : p.play_card_from_discard(),player))


def deck_setup_age_1(player_count):
    deck = []
    deck.append(Card(1,"Lumber Yard",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_WOOD)))  #wood
    deck.append(Card(2,"Stone Pit",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_STONE)))  #stone
    deck.append(Card(3,"Clay Pool",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_BRICK)))  #bricks
    deck.append(Card(4,"Ore Vein",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_ORE)))  #ore
    deck.append(Card(7,"Clay Pit",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_ORE,RESOURCE_BRICK))))  # ore\bricks
    deck.append(Card(8,"Timber Yard",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_STONE))))  # wood\stone
    deck.append(Card(11,"Glassworks",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_GLASS)))  #glass
    deck.append(Card(12,"Press",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_PAPYRUS)))  #papyrus
    deck.append(Card(13,"Loom",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_LOOM)))  #loom
    deck.append(Card(15,"Baths",COLOR_BLUE,1,[RESOURCE_STONE],lambda p : p.add_points(POINTS_BLUE,3),None,["Baths"]))  #3 blue points
    deck.append(Card(16,"Altar",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2),None,["Temple"]))  #2 blue points
    deck.append(Card(17,"Theatre",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2),None,["Statue"]))  #2 blue points
    deck.append(Card(19,"Marketplace",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost(COLOR_GREY),None,["Caravansery"]))  #lower both grey trading costs
    deck.append(Card(20,"West Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("east"),None,["Forum"]))  #lower east brown trading costs
    deck.append(Card(21,"East Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("west"),None,["Forum"]))  #lower west brown trading costs
    deck.append(Card(22,"Stockade",COLOR_RED,1,[RESOURCE_WOOD], lambda p : p.add_shields(1)))
    deck.append(Card(23,"Barracks",COLOR_RED,1,[RESOURCE_ORE],lambda p : p.add_shields(1)))
    deck.append(Card(24,"Guard Tower",COLOR_RED,1,[RESOURCE_BRICK],lambda p : p.add_shields(1)))
    deck.append(Card(25,"Apothecary",COLOR_GREEN,1,[RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_COMPASS),None,["Stables","Dispensary"]))  #compass
    deck.append(Card(26,"Workshop",COLOR_GREEN,1,[RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_GEAR),None,["Laboratory","Archery Range"]))  #gear
    deck.append(Card(27,"Scriptorium",COLOR_GREEN,1,[RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_TABLET),None,["Courthouse","Library"]))  #tablet
    if player_count > 3:
        deck.append(Card(1,"Lumber Yard",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_WOOD)))  #wood
        deck.append(Card(4,"Ore Vein",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_ORE)))  #ore
        deck.append(Card(6,"Excavation",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_STONE,RESOURCE_BRICK))))  # stone\bricks
        deck.append(Card(14,"Pawnshop",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,3)))  #3 blue points
        deck.append(Card(18,"Tavern",COLOR_YELLOW,1,None,lambda p : p.add_resource(RESOURCE_GOLD,5)))  #5 coins
        deck.append(Card(24,"Guard_Tower",COLOR_RED,1,[RESOURCE_BRICK],lambda p : p.add_shields(1)))
        deck.append(Card(27,"Scriptorium",COLOR_GREEN,1,[RESOURCE_PAPYRUS],lambda p : p.add_science(SCIENCE_TABLET),None,["Courthouse","Library"]))  #tablet
        if player_count > 4:
            deck.append(Card(2,"Stone Pit",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_STONE)))  #stone
            deck.append(Card(3,"Clay Pool",COLOR_BROWN,1,None,lambda p : p.add_resource(RESOURCE_BRICK)))  #bricks
            deck.append(Card(9,"Forest Cave",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_ORE))))  # wood\ore
            deck.append(Card(16,"Altar",COLOR_BLUE,1,None,lambda p : p.add_points(POINTS_BLUE,2),None,["Temple"]))  #2 blue points
            deck.append(Card(18,"Tavern",COLOR_YELLOW,1,None,lambda p : p.add_resource(RESOURCE_GOLD,5)))  #5 coins
            deck.append(Card(23,"Barracks",COLOR_RED,1,[RESOURCE_ORE],lambda p : p.add_shields(1)))
            deck.append(Card(25,"Apothecary",COLOR_GREEN,1,[RESOURCE_LOOM],lambda p : p.add_science(SCIENCE_COMPASS),None,["Stables","Dispensary"]))  #compass
            if player_count > 5:
                deck.append(Card(5,"Tree Farm",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_WOOD,RESOURCE_BRICK)))) # wood\bricks
                deck.append(Card(10,"Mine",COLOR_BROWN,1,[RESOURCE_GOLD],lambda p : p.add_conditional_resource((RESOURCE_STONE,RESOURCE_ORE))))  # stone\ore
                deck.append(Card(11,"Glassworks",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_GLASS)))  #glass
                deck.append(Card(12,"Press",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_PAPYRUS)))  #papyrus
                deck.append(Card(13,"Loom",COLOR_GREY,1,None,lambda p : p.add_resource(RESOURCE_LOOM)))  #loom
                deck.append(Card(20,"West Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("east"),None,["Forum"]))  #lower east brown trading costs
                deck.append(Card(21,"East Trading Post",COLOR_YELLOW,1,None,lambda p : p.lower_trading_cost("west"),None,["Forum"]))  #lower west brown trading costs
                deck.append(Card(22,"Stockade",COLOR_RED,1,[RESOURCE_WOOD], lambda p : p.add_shields(1)))
                deck.append(Card(26,"Workshop",COLOR_GREEN,1,[RESOURCE_GLASS],lambda p : p.add_science(SCIENCE_GEAR),None,["Laboratory","Archery Range"]))  #gear
    
    return deck





def players_setup(player_count = 3): #max 6
    deck = deck_setup_age_1()
    shuffle(deck)
    # Separate the list into lists of 7 elements each
    separated_deck = [deck[i:i+7] for i in range(0, len(deck), 7)]

    wonders_list = ["Alexandria","Babylon","Ephesos","Gizah","Halikarnassos","Rhodos"]
    playerlist = []
    for i in range(player_count):
        player = Player("player "+str(i))
        player.set_wonder(Wonder(wonders_list.pop(randint(0,5)),choice(["A","B"]),player)) 
        player.hand = separated_deck[i]
        playerlist.append(player)
    for i in range(player_count):
        playerlist[i].set_east_player(playerlist[i-1])
        playerlist[i].set_west_player(playerlist[(i+1)%player_count])

    return playerlist



if __name__ == "__main__":
    
    main()