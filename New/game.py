import Players
import Cards
from common import *

#The game has #players amount of hands
#Players are assigned a hand number
#After cards are played, hand numbers are switched by 1
card_hands = []



def main():
    #TODO
    cards_setup()
    players_setup() #Includes wonder setup
    

    for age in range(1,4):
            for turn in range(6):
                for player in players:
                   play_turn(player) 
                if turn == 5: #last turn
                    if player.has_double_last_cards():
                        player.play_turn(player)
                    else:
                        discard_card()

                for effect in queue: #For cards that give coins depending on card counts
                    effect() #maybe these will be (effect,player) in queue
                queue = []
                
                switch_hands()

            #Free discard wonder
            for player in players:
                if player.has_free_discard>0:
                    play_turn()
            for effect in queue: #For cards that give coins depending on card counts
                effect() #maybe these will be (effect,player) in queue
            queue = []

            for player in players:
                player.war((age*2)-1)
                     
                     
            
def play_turn(player):
    show_available_cards()
    card = select_card(player) #Add card count at this stage
    card.build()
    if hasattr(card,"effect_2"): #For cards that give coins depending on card counts
        add_effect_to_queue(card.effect_2)




if __name__ == "__main__":
    main()