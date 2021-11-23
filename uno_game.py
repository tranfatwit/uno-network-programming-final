# -*- coding: utf-8 -*-
"""
Contains game logic for UNO
Created on Mon Nov 22 17:21:27 2021

@author: Fabio Tran
"""

from deck import Deck
from player import Player
#from uno_server import *

class Game():
    
    def __init__(self):
        # stores players
       # for x in range(4):
       #     self.players.append(players.pop())
       # for x in range(4):
       #     players.push(players[x])
        self.players =[]
        self.players.append(player1)
        self.players.append(player2)
        self.players.append(player3)
        self.players.append(player4)
        
        # creates deck
        self.deck = Deck()
        self.deck.shuffle_deck()
        
        # deals cards to each player
        
        for x in range(7):
            self.players[0].hand.append(self.deck.draw())
            self.players[1].hand.append(self.deck.draw())
            self.players[2].hand.append(self.deck.draw())
            self.players[3].hand.append(self.deck.draw())
        
player1 = Player(1,"Fabio")
player2 = Player(2,"Fabio2")
player3 = Player(3,"Fabio3")
player4 = Player(4,"Fabio4")
game = Game()

for player in game.players:
    print(player.hand[2])
