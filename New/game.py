from Players import Player
from common import *
from random import randint, choice, shuffle
from Wonders import Wonder
from Cards import *
from Wonders import *

discard_pile = []
queue = []

def main():
    nbplayers = int(input("Enter number of players: "))
    while (nbplayers < 3 or nbplayers > 6):
        print("Player count must be between 3 and 6")
        nbplayers = int(input("\nEnter number of player: "))

    players = players_setup(nbplayers) #Includes wonder setup

    for age in range(1,4): #each age
        assign_cards(players,age) #Create decks and assign them to players

        for turn in range(6):
            for player in players:
                print()
                play_turn(player) 
            if turn == 5: #last turn
                if player.has_double_last_cards:
                    print()
                    play_turn(player)
                else:
                    discard_last_card(player)

            for effect,player in queue: #For cards that give coins depending on card counts (and Halikarnassos discard play)
                effect(player)
            queue.clear()
            
            switch_hands(players,age)

        print("war time")
        for player in players:
            player.war((age*2)-1) #1, 3 and 5
        
    #game end
    for player in players:
        for endgame_function in player.endgame_scoring_functions:
            endgame_function(player)

        player.print_tableau()
        print()
        player.print_score()
        print()

    

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
    
    wonder_available = False
    wonder_price = player.get_price(player.wonder)
    if not player.wonder.all_done and wonder_price != -1:
        wonder_available = True
        player.print_wonder_option(wonder_price)
   

    player.print_available_cards(available_cards,cost)
    
    #TODO Gym action space

    card_selected = False
    while(not card_selected):
        try:
            input_option = int(input(f"{player.name}'s turn: "))
            if input_option < 1-wonder_available or input_option > len(available_cards)*2+(len(player.hand)-len(available_cards)):
                print("Invalid option")
            else:
                card_selected = True
        except ValueError:
            print("Invalid option")
    
    if input_option == 0:
        player.play_wonder()
        return
    elif input_option<=len(available_cards)*2:
        if input_option % 2 == 1: #play card
            card = available_cards[input_option//2]
            player.play_card(card)
        else: #discard card (that could be played)
            card = available_cards[input_option//2 - 1]
            player.resources[RESOURCE_GOLD] += 3
            discard_pile.append(card)
    else:	#discard cards (that cannot be played)
        card = unavailable_cards[input_option-len(available_cards)*2-1]
        player.resources[RESOURCE_GOLD] += 3
        discard_pile.append(card)
    
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
    
    for i in range(player_count):
        playerlist[i].set_east_player(playerlist[i-1])
        playerlist[i].set_west_player(playerlist[(i+1)%player_count])

    return playerlist

def assign_cards(players_list, age=1):
    if age == 1:
        deck = deck_setup_age_1(len(players_list))
    elif age == 2:
        deck = deck_setup_age_2(len(players_list))
    else:
        deck = deck_setup_age_3(len(players_list))

    shuffle(deck)
    # Separate the list into lists of 7 elements each
    separated_deck = [deck[i:i+7] for i in range(0, len(deck), 7)]
    i = 0
    for player in players_list:
        player.hand = separated_deck[i]
        i += 1

def set_wonder(player,wonders_list):
    wonder_name = wonders_list.pop(randint(0,len(wonders_list)-1))
    wonder_name = "Halikarnassos"
    if wonder_name == "Alexandria":
        wonder = Alexandria(player)
    elif wonder_name == "Babylon":
        wonder = Babylon(player)
    elif wonder_name == "Ephesos":
        wonder = Ephesos(player)
    elif wonder_name == "Gizah":
        wonder = Gizah(player)
    elif wonder_name == "Halikarnassos":
        wonder = Halikarnassos(player,queue,discard_pile)
    elif wonder_name == "Rhodos":
        wonder = Rhodos(player)
    else:
        wonder = Wonder()

    player.set_wonder(wonder)

def deck_setup_age_3(player_count):
    deck = []
    purple_cards = [WorkersGuild(119),CraftmensGuild(120),TradersGuild(121),\
                    PhilosophersGuild(122),SpiesGuild(123),StrategistsGuild(124),\
                    ShipownersGuild(125),ScientistsGuild(126),MagistratesGuild(127),BuildersGuild(128)] 
    shuffle(purple_cards) #Not all of them are used. Only #player+2

    deck.append(Pantheon(85))  #7 blue points
    deck.append(Gardens(86))  #5 blue points
    deck.append(TownHall(87))  #6 blue points
    deck.append(Palace(88))  #8 blue points
    deck.append(Senate(89))  #6 blue points
    deck.append(Haven(90))  # point + coin per brown card
    deck.append(Lighthouse(91))  #point + coin per yellow card
    deck.append(Arena(92))  #3 coins, 1 point per wonder
    deck.append(Fortifications(93))  #3 shields
    deck.append(Arsenal(94))  #3 shields
    deck.append(SiegeWorkshop(95))  #3 shields
    deck.append(Lodge(96))  #Compass
    deck.append(Observatory(97))  #Gear
    deck.append(University(98))  #Tablet
    deck.append(Academy(99)) #Compass
    deck.append(Study(100))  #Gear
    deck.append(purple_cards[0])
    deck.append(purple_cards[1])
    deck.append(purple_cards[2])
    deck.append(purple_cards[3])
    deck.append(purple_cards[4])
    if player_count >= 4:
        deck.append(Gardens(101))  #5 blue points
        deck.append(Haven(102))  #point + coin per brown card
        deck.append(ChamberOfCommerce(103))  #2 points + 2 coins per grey card
        deck.append(Circus(104))  #3 shields
        deck.append(Arsenal(105))  #3 shields
        deck.append(University(106)) #Tablet
        deck.append(purple_cards[5])
        if player_count >= 5:
            deck.append(TownHall(107))  #6 blue points
            deck.append(Senate(108))  #6 blue points
            deck.append(Arena(109))  #1 points + 3 coin per wonder
            deck.append(Circus(110))  #3 shields
            deck.append(SiegeWorkshop(111))  #3 shields
            deck.append(Study(112)) #gear
            deck.append(purple_cards[6])
            if player_count >= 6:
                deck.append(Pantheon(113)) #7 blue points
                deck.append(TownHall(114))  #6 blue points
                deck.append(Lighthouse(115))  #point + coin per yellow card
                deck.append(ChamberOfCommerce(116))  #2 points + 2 coins per grey card
                deck.append(Circus(117))  #3 shields
                deck.append(Lodge(118)) # Compass
                deck.append(purple_cards[7])
                 
    return deck
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
                deck.append(Temple(78)) # 3 blue points
                deck.append(Forum(79)) 
                deck.append(Caravansery(80))  #Free brown resource
                deck.append(Vineyard(81))  #Gold for brown cards <^>
                deck.append(TrainingGround(82))  #2 shields
                deck.append(ArcheryRange(83)) #2 shields
                deck.append(Library(84)) #tablet
                 
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
    main()