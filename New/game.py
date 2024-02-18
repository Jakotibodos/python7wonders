from Players import Player
from common import *
from random import randint, choice, shuffle
from Wonders import Wonder
from Cards import *
from Wonders import *

discard_pile = []
queue = []

def main():
    #TODO
    nbplayers = int(input("Enter number of players: "))
    while (nbplayers < 3 and nbplayers > 6):
        print("Player count must be between 3 and 6")
        nbplayers = int(input("\nEnter number of player: "))

    players = players_setup(nbplayers) #Includes wonder setup

    for age in range(1,4): #each age
        for turn in range(6):
            for player in players:
                player.play_turn() 
            if turn == 5: #last turn
                if player.has_double_last_cards():
                    player.play_turn()
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


def play_turn(player):
    available_cards, cost, unavailable_cards = player.show_available_cards()
    player.print_available_cards(available_cards,cost)
    
    #TODO Gym action space
    
    card_selected = False
    while(not card_selected):
        try:
            input_option = int(input(f"{player.name}'s turn: "))
            if input_option < 1 or input_option > len(available_cards)*2+(len(player.hand)-len(available_cards)):
                print("Invalid option")
            else:
                card_selected = True
        except ValueError:
            print("Invalid option")
    
    if input_option<=len(available_cards)*2:
        if input_option % 2 == 1: #play card
            card = available_cards[input_option//2]
            player.tableau.append(card)
            card.effect(player)
            player.color_count[card.color] += 1
        else: #discard card (that could be played)
            card = available_cards[input_option//2 - 1]
            player.resources[RESOURCE_GOLD] += 3
    else:	#discard cards (that cannot be played)
        card = unavailable_cards[input_option-len(available_cards)*2-1]
        player.resources[RESOURCE_GOLD] += 3
    
    if not isinstance(card, Wonder):
        player.hand.remove(card)
        
    


def discard_last_card(player):
    discard_pile.append(player.hand.pop())


def players_setup(player_count = 3): #max 6
    wonders_list = ["Alexandria","Babylon","Ephesos","Gizah","Halikarnassos","Rhodos"]
    playerlist = []
    for i in range(player_count):
        player = Player(input(f"Name of player {i}: ")) 
        set_wonder(player,wonders_list)
        playerlist.append(player)

    assign_cards(playerlist, age = 1)
    
    for i in range(player_count):
        playerlist[i].set_east_player(playerlist[i-1])
        playerlist[i].set_west_player(playerlist[(i+1)%player_count])

    return playerlist

def assign_cards(players_list, age):
    if age == 1:
        deck = deck_setup_age_1(len(players_list))
    elif age == 2:
        deck = deck_setup_age_2(len(players_list))
    else:
        deck = deck_setup_age_3(len(players_list))

    shuffle(deck)
    # Separate the list into lists of 7 elements each
    separated_deck = [deck[i:i+7] for i in range(0, len(deck), 7)]
    for player in players_list:
        player.hand = separated_deck[i]

def set_wonder(player,wonders_list):
    wonder_name = wonders_list.pop(randint(0,len(wonders_list)-1))
    if wonder_name == "Alexandria":
        wonder = Alexandria(player)
    elif wonder_name == "Babylon":
        wonder = Babylon(player)
    elif wonder_name == "Ephesos":
        wonder = Ephesos(player)
    elif wonder_name == "Gizah":
        wonder = Gizah(player)
    elif wonder_name == "Halikarnassos":
        wonder = Halikarnassos(player,queue)
    elif wonder_name == "Rhodos":
        wonder = Rhodos(player)
    else:
        wonder = Wonder()

    player.set_wonder(wonder)


def deck_setup_age_2(player_count):
    deck = []
    deck.append(Sawmill(43))  #2 wood
    deck.append(Quarry(44))  #2 stone
    deck.append(Brickyard(45))  #2 bricks
    deck.append(Foundry(46))  #2 ore
    deck.append(Loom(47))  # loom
    deck.append(Glassworks(48))  # glass
    deck.append(Press(49))  #papyrus
    deck.append(Aqueduct(50))  #5 blue points
    deck.append(Temple(51))  #3 blue points
    deck.append(Statue(52))  #4 blue points
    deck.append(Barracks(53))  #4 blue points
    deck.append(Forum(54))  #Free grey resource
    deck.append(Caravansery(55))  #free brown resource
    deck.append(Vineyard(56, queue))  #Gold for brown cards <^>
    deck.append(Walls(57)) #2 shields
    deck.append(Stables(58))  #2 shields
    deck.append(ArcheryRange(59))  #2 shields
    deck.append(Dispensary(60)) #compass
    deck.append(Laboratory(61)) #gear
    deck.append(Library(62))  #tablet
    deck.append(School(63))  #tablet
    if player_count >= 4:
        deck.append(Sawmill(64))  #2 wood
        deck.append(Quarry(65))  #2 stone
        deck.append(Brickyard(66))  #2 bricks
        deck.append(Foundry(67))  #2 ore
        deck.append(Bazar(68,queue))  #2 Gold for grey cards <^>
        deck.append(TrainingGround(69)) #2 shields
        deck.append(Dispensary(70))  #compass
        if player_count >= 5:
            deck.append(Loom(71))  # loom
            deck.append(Glassworks(72))  # glass
            deck.append(Press(73))  #papyrus
            deck.append(Courthouse(74))  #4 blue points
            deck.append(Caravansery(75))  #Free brown resource
            deck.append(Stables(76)) #2 shields
            deck.append(Laboratory(77))  #gear
            if player_count >= 6:
                deck.append(TreeFarm(36)) # wood\bricks
                deck.append(Mine(37))  # stone\ore
                deck.append(Glassworks(38))  #glass
                deck.append(Press(39))  #papyrus
                deck.append(Loom(40))  #loom
                deck.append(MarketPlace(41))
                deck.append(Theatre(42))
                 
    return deck

def deck_setup_age_1(player_count):
    deck = []
    deck.append(LumberYard(1))  #wood
    deck.append(StonePit(2))  #stone
    deck.append(ClayPool(3))  #bricks
    deck.append(OreVein(4))  #ore
    deck.append(ClayPit(5))  # ore\bricks
    deck.append(TimberYard(6))  # wood\stone
    deck.append(Loom(7))  #glass
    deck.append(Glassworks(8))  #papyrus
    deck.append(Press(9))  #loom
    deck.append(Baths(10))  #3 blue points
    deck.append(Altar(11))  #2 blue points
    deck.append(Theatre(12))  #2 blue points
    deck.append(EastTradingPost(13))  #lower east brown trading costs
    deck.append(WestTradingPost(14)) #lower west brown trading costs
    deck.append(MarketPlace(15))  #lower both grey trading costs
    deck.append(Stockade(16))  #lower brown trading costs
    deck.append(Barracks(17)) 
    deck.append(GuardTower(18)) 
    deck.append(Apothecary(19))  #compass
    deck.append(Workshop(20))  #gear
    deck.append(Scriptorium(21))  #tablet
    if player_count >= 4:
        deck.append(LumberYard(22))  #wood
        deck.append(OreVein(23))  #ore
        deck.append(Excavation(24))  # stone\bricks
        deck.append(Pawnshop(25))  #3 blue points
        deck.append(Tavern(26))  #5 coins
        deck.append(GuardTower(27))
        deck.append(Scriptorium(28))  #tablet
        if player_count >= 5:
            deck.append(StonePit(29))  #stone
            deck.append(ClayPool(30))  #bricks
            deck.append(ForestCave(31))  # wood\ore
            deck.append(Altar(32))  #2 blue points
            deck.append(Tavern(33))  #5 coins
            deck.append(Barracks(34))
            deck.append(Apothecary(35))  #compass
            if player_count >= 6:
                deck.append(TreeFarm(36)) # wood\bricks
                deck.append(Mine(37))  # stone\ore
                deck.append(Loom(38))  #loom
                deck.append(Glassworks(39))  #glass
                deck.append(Press(40))  #papyrus
                deck.append(MarketPlace(41))
                deck.append(Theatre(42))
                 
    return deck


if __name__ == "__main__":
    players = players_setup(3)
    players[0].print_hand()
    play_turn(players[0])
    players[0].print_hand()
    players[0].print_tableau()
    print(players[0].resources)
    players[0].print_score()
    #main()