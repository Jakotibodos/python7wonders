from Players import Player
import Cards
from common import *
from random import randint, choice
from Wonders import Wonder

#The game has #players amount of hands
#Players are assigned a hand number
#After cards are played, hand numbers are switched by 1
card_hands = []



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
                    discard_card()

            for effect in queue: #For cards that give coins depending on card counts (and Halikarnassos discard play)
                effect() #maybe these will be (effect,player) in queue
            queue = []
            
            switch_hands(players)

        #Free discard wonder
        for player in players:
            if player.get_free_discards>0:
                play_turn()
        for effect in queue: #For cards that give coins depending on card counts
            effect() #maybe these will be (effect,player) in queue
        queue = []

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
    show_available_cards()
    card = select_card(player) #Add card count at this stage
    card.build()
    if hasattr(card,"effect_2"): #For cards that give coins depending on card counts
        add_effect_to_queue(card.effect_2)



def cards_setup(nbplayers):
    




def players_setup(nbplayers = 3): #max 6
    cards_setup(nbplayers)
    wonders_list = ["Alexandria","Babylon","Ephesos","Gizah","Halikarnassos","Rhodos"]
    playerlist = []
    for i in range(nbplayers):
        player = Player("player "+str(i))
        player.set_wonder(Wonder(wonders_list.pop(randint(0,5)),choice(["A","B"]),player)) 
        playerlist.append(player)
    for i in range(nbplayers):
        playerlist[i].set_east_player(playerlist[i-1])
        playerlist[i].set_west_player(playerlist[(i+1)%nbplayers])

    return playerlist



if __name__ == "__main__":
    main()