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
            print("\n================================")
            print(f"TURN {turn+1}")
            print("================================\n")
            temp_queue = []
            for player in players:
                print()
                player.print_tableau()
                print("West: "+str(player.west_trade_prices)+" East: "+str(player.east_trade_prices)+" Grey: "+str(player.grey_trade_prices))
                print(player.conditional_resources)
                print("Free Brown: "+str(player.free_conditional_resources[COLOR_BROWN])+" Free Grey: "+str(player.free_conditional_resources[COLOR_GREY]))
                print(player.resources)
                play_turn(player,temp_queue)  
                
            if turn == 5: #last turn
                if player.has_double_last_cards:
                    print()
                    play_turn(player)
                else:
                    discard_last_card(player)

            for card,player,cost in temp_queue: #normal card play queue
                if card == "wonder":
                    player.play_wonder(cost)
                else:
                    player.play_card(card,cost)
                   
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


def play_turn(player,temp_queue):
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
        temp_queue.append(("wonder",player,wonder_price))
        return
    elif input_option<=len(available_cards)*2:
        if input_option % 2 == 1: #play card
            card = available_cards[input_option//2]
            temp_queue.append((card,player,cost[input_option//2]))
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
        print(playerlist[i].name+"west: "+playerlist[i].west_player.name)
    
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
        print(f"{player.name}'s hand: {player.hand}")
        i += 1

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
        wonder = Halikarnassos(player,queue,discard_pile)
    elif wonder_name == "Rhodos":
        wonder = Rhodos(player)
    else:
        wonder = Wonder()

    player.set_wonder(wonder)
    print(player.name,player.wonder.name,player.wonder.side)

def deck_setup_age_3(player_count):
    deck = []
    purple_cards = [WorkersGuild(),CraftmensGuild(),TradersGuild(),\
                    PhilosophersGuild(),SpiesGuild(),StrategistsGuild(),\
                    ShipownersGuild(),ScientistsGuild(),MagistratesGuild(),BuildersGuild()] 
    shuffle(purple_cards) #Not all of them are used. Only #player+2

    deck.append(Pantheon())  #7 blue points
    deck.append(Gardens())  #5 blue points
    deck.append(TownHall())  #6 blue points
    deck.append(Palace())  #8 blue points
    deck.append(Senate())  #6 blue points
    deck.append(Haven())  # point + coin per brown card
    deck.append(Lighthouse())  #point + coin per yellow card
    deck.append(Arena())  #3 coins, 1 point per wonder
    deck.append(Fortifications())  #3 shields
    deck.append(Arsenal())  #3 shields
    deck.append(SiegeWorkshop())  #3 shields
    deck.append(Lodge())  #Compass
    deck.append(Observatory())  #Gear
    deck.append(University())  #Tablet
    deck.append(Academy()) #Compass
    deck.append(Study())  #Gear
    deck.append(purple_cards[0])
    deck.append(purple_cards[1])
    deck.append(purple_cards[2])
    deck.append(purple_cards[3])
    deck.append(purple_cards[4])
    if player_count >= 4:
        deck.append(Gardens())  #5 blue points
        deck.append(Haven())  #point + coin per brown card
        deck.append(ChamberOfCommerce())  #2 points + 2 coins per grey card
        deck.append(Circus())  #3 shields
        deck.append(Arsenal())  #3 shields
        deck.append(University()) #Tablet
        deck.append(purple_cards[5])
        if player_count >= 5:
            deck.append(TownHall())  #6 blue points
            deck.append(Senate())  #6 blue points
            deck.append(Arena())  #1 points + 3 coin per wonder
            deck.append(Circus())  #3 shields
            deck.append(SiegeWorkshop())  #3 shields
            deck.append(Study()) #gear
            deck.append(purple_cards[6])
            if player_count >= 6:
                deck.append(Pantheon()) #7 blue points
                deck.append(TownHall())  #6 blue points
                deck.append(Lighthouse())  #point + coin per yellow card
                deck.append(ChamberOfCommerce())  #2 points + 2 coins per grey card
                deck.append(Circus())  #3 shields
                deck.append(Lodge()) # Compass
                deck.append(purple_cards[7])
                 
    return deck
def deck_setup_age_2(player_count):
    deck = []
    deck.append(Sawmill())  #2 wood
    deck.append(Quarry())  #2 stone
    deck.append(Brickyard())  #2 bricks
    deck.append(Foundry())  #2 ore
    deck.append(Loom())  # loom
    deck.append(Glassworks())  # glass
    deck.append(Press())  #papyrus
    deck.append(Aqueduct())  #5 blue points
    deck.append(Temple())  #3 blue points
    deck.append(Statue())  #4 blue points
    deck.append(Courthouse())  #4 blue points
    deck.append(Forum())  #Free grey resource
    deck.append(Caravansery())  #free brown resource
    deck.append(Vineyard(queue))  #Gold for brown cards <^>
    deck.append(Walls()) #2 shields
    deck.append(Stables())  #2 shields
    deck.append(ArcheryRange())  #2 shields
    deck.append(Dispensary()) #compass
    deck.append(Laboratory()) #gear
    deck.append(Library())  #tablet
    deck.append(School())  #tablet
    if player_count >= 4:
        deck.append(Sawmill())  #2 wood
        deck.append(Quarry())  #2 stone
        deck.append(Brickyard())  #2 bricks
        deck.append(Foundry())  #2 ore
        deck.append(Bazar(queue))  #2 Gold for grey cards <^>
        deck.append(TrainingGround()) #2 shields
        deck.append(Dispensary())  #compass
        if player_count >= 5:
            deck.append(Loom())  # loom
            deck.append(Glassworks())  # glass
            deck.append(Press())  #papyrus
            deck.append(Courthouse())  #4 blue points
            deck.append(Caravansery())  #Free brown resource
            deck.append(Stables()) #2 shields
            deck.append(Laboratory())  #gear
            if player_count >= 6:
                deck.append(Temple()) # 3 blue points
                deck.append(Forum()) 
                deck.append(Caravansery())  #Free brown resource
                deck.append(Vineyard())  #Gold for brown cards <^>
                deck.append(TrainingGround())  #2 shields
                deck.append(ArcheryRange()) #2 shields
                deck.append(Library()) #tablet
                 
    return deck

def deck_setup_age_1(player_count):
    deck = []
    deck.append(LumberYard())  #wood
    deck.append(StonePit())  #stone
    deck.append(ClayPool())  #bricks
    deck.append(OreVein())  #ore
    deck.append(ClayPit())  # ore\bricks
    deck.append(TimberYard())  # wood\stone
    deck.append(Loom())  #glass
    deck.append(Glassworks())  #papyrus
    deck.append(Press())  #loom
    deck.append(Baths())  #3 blue points
    deck.append(Altar())  #2 blue points
    deck.append(Theatre())  #2 blue points
    deck.append(EastTradingPost())  #lower east brown trading costs
    deck.append(WestTradingPost()) #lower west brown trading costs
    deck.append(MarketPlace())  #lower both grey trading costs
    deck.append(Stockade())  #lower brown trading costs
    deck.append(Barracks()) 
    deck.append(GuardTower()) 
    deck.append(Apothecary())  #compass
    deck.append(Workshop())  #gear
    deck.append(Scriptorium())  #tablet
    if player_count >= 4:
        deck.append(LumberYard())  #wood
        deck.append(OreVein())  #ore
        deck.append(Excavation())  # stone\bricks
        deck.append(Pawnshop())  #3 blue points
        deck.append(Tavern())  #5 coins
        deck.append(GuardTower())
        deck.append(Scriptorium())  #tablet
        if player_count >= 5:
            deck.append(StonePit())  #stone
            deck.append(ClayPool())  #bricks
            deck.append(ForestCave())  # wood\ore
            deck.append(Altar())  #2 blue points
            deck.append(Tavern())  #5 coins
            deck.append(Barracks())
            deck.append(Apothecary())  #compass
            if player_count >= 6:
                deck.append(TreeFarm()) # wood\bricks
                deck.append(Mine())  # stone\ore
                deck.append(Loom())  #loom
                deck.append(Glassworks())  #glass
                deck.append(Press())  #papyrus
                deck.append(MarketPlace())
                deck.append(Theatre())
                 
    return deck


if __name__ == "__main__":
    main()