from Players import Player
from common import *
from random import randint, choice, shuffle
from Wonders import *
from Cards import *
import gym
from gym import spaces
import numpy as np

class SevenWondersEnv(gym.Env):
    metadata = {'render.modes': ['human']}

    def __init__(self,nb_players = 3, verbose=False, manual= False):
        super(SevenWondersEnv, self).__init__()
        self.name = "7wonders"
        self.manual = manual
        self.n_players = nb_players
        self.card_types = 75
        self.action_space = gym.spaces.Discrete(15)
        self.observation_space = gym.spaces.Box(0,1,(322,))
        self.verbose = verbose
        self.cards_per_player = 7
        

    @property
    def observation(self):
        obs = np.zeros(322,dtype=int)
        player = self.current_player

        #This is from play_turn in game.py
        hand_cost = player.get_hand_cost()
        hand = player.hand
        card_counts = {}
        for card in hand:
            card_counts[card.id] = card_counts.get(card.id, 0) + 1

        for card_id, count in card_counts.items(): #obs 1-532 (cards in hand)
            obs[card_id+1] = 1/count
        
        wonder_available = False
        wonder_price = player.get_price(player.wonder)
        if not player.wonder.all_done and wonder_price != -1:
            wonder_available = True
        
        obs[0] += int(wonder_available) #obs 0 (wonder available)

        for card in player.tableau: #obs 533-607 (cards built)
            obs[533+card.id] += 1

        obs[608] = self.current_age/3 #TODO
        obs[609] = min(player.resources[RESOURCE_GOLD]/20,1) #gold over 20 is just useless
        obs[610] = player.wonder.id/6

    @property
    def legal_actions(self):
        legal_actions = np.zeros(15)
        player = self.current_player
        
        
        hand_cost = player.get_hand_cost()

        wonder_available = False
        if not player.wonder.all_done and player.get_price(player.wonder) != -1:
            wonder_available = True
        legal_actions[0] += int(wonder_available)

        for i in range(len(hand_cost)):
            if hand_cost[i]!=-1:
                legal_actions[(i*2)+1] += 1
            legal_actions[(i+1)*2] += 1
    
        return legal_actions






        