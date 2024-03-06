from Players import *
from common import *
from Cards import *
from Wonders import *
from game import *
from SevenWonders import SevenWondersEnv

env = SevenWondersEnv()






while not env.done:
    player = env.current_player
    player.print_tableau()
    print("West: "+str(player.west_trade_prices)+" East: "+str(player.east_trade_prices)+" Grey: "+str(player.grey_trade_prices))
    print(player.conditional_resources)
    print("Free Brown: "+str(player.free_conditional_resources[COLOR_BROWN])+" Free Grey: "+str(player.free_conditional_resources[COLOR_GREY]))
    print(player.resources)
    if env.turn_type == 0:
        cost = player.get_hand_cost()
        wonder_price = player.get_price(player.wonder)
        player.print_wonder_option(wonder_price, bool(env.observation[0]))
        player.print_available_cards(cost)
    elif env.turn_type == 1:
        cost = [-1 for _ in range(len(player.hand))]
        player.print_available_cards(cost)
    else:
        print(f"{player.name}, You can play a card from the discard pile for free:")
        for card in env.discard:
            print(f"[{card.id+1}] {str(card)}")
    
    action = int(input(f"{player.name}: "))
    print()
    env.step(action)




for player in env.players:
    player.print_score()
