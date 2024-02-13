from Players import Player
from common import *
from random import randint, choice, shuffle
from Wonders import Wonder
from Cards import *

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
    deck.append(LumberYard(1))  #wood
    deck.append(StonePit(2))  #stone
    deck.append(ClayPool(3))  #bricks
    deck.append(OreVein(4))  #ore
    deck.append(ClayPit(5))  # ore\bricks
    deck.append(TimberYard(6))  # wood\stone
    deck.append(Glassworks(7))  #glass
    deck.append(Press(8))  #papyrus
    deck.append(Loom(9))  #loom
    deck.append(Baths(10))  #3 blue points
    deck.append(Altar(11))  #2 blue points
    deck.append(Theatre(12))  #2 blue points
    deck.append(MarketPlace(13))  #lower both grey trading costs
    deck.append(WestTradingPost(14))  #lower east brown trading costs
    deck.append(EastTradingPost(15))  #lower west brown trading costs
    deck.append(Stockade(16))  #lower brown trading costs
    deck.append(Barracks(17)) 
    deck.append(GuardTower(18)) 
    deck.append(Apothecary(19))  #compass
    deck.append(Workshop(20))  #gear
    deck.append(Scriptorium(21))  #tablet
    if player_count > 3:
        deck.append(LumberYard(22))  #wood
        deck.append(OreVein(23))  #ore
        deck.append(Excavation(24))  # stone\bricks
        deck.append(Pawnshop(25))  #3 blue points
        deck.append(Tavern(26))  #5 coins
        deck.append(GuardTower(27))
        deck.append(Scriptorium(28))  #tablet
        if player_count > 4:
            deck.append(StonePit(29))  #stone
            deck.append(ClayPool(30))  #bricks
            deck.append(ForestCave(31))  # wood\ore
            deck.append(Altar(32))  #2 blue points
            deck.append(Tavern(33))  #5 coins
            deck.append(Barracks(34))
            deck.append(Apothecary(35))  #compass
            if player_count > 5:
                deck.append(TreeFarm(36)) # wood\bricks
                deck.append(Mine(37))  # stone\ore
                deck.append(Glassworks(38))  #glass
                deck.append(Press(39))  #papyrus
                deck.append(Loom(40))  #loom
                deck.append(MarketPlace(41))
                deck.append(Theatre(42))
                 
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