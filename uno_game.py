# -*- coding: utf-8 -*-
"""
Contains game logic for UNO
Created on Mon Nov 22 17:21:27 2021

@author: Fabio Tran
"""

from deck import Deck
import uno_server
from player import Player
from card import Card

class Game():
    # constructor
    def __init__(self, player_queue):
        
        # creates and shuffles deck
        self.deck = Deck()
        self.deck.shuffle_deck()
        
        self.players = player_queue

        first_card = self.deck.draw()
        while(first_card.color == "Any"):
            self.deck.discard_pile.append(first_card)
            first_card = self.deck.draw()
            
        self.deck.last_played = first_card
        
        # deals cards to each player
        for x in range(7):
            for usr in self.players:
                usr.hand.append(self.deck.draw())

            
    # runs rounds of uno until there is a winner 
    def run_game(self):
        winner = False
        
        # continues while winner hasn't been determined
        while not winner:
            usr = self.players[0]
            playable = []
            # make a list of cards that the user may play
            last_card = self.deck.last_played
            for item in usr.hand:
                if(last_card.match_card(item)):
                    print(str(item))
                    playable.append(item)
            
            # Send the user a request for their turn and process it
            usr_turn = uno_server.give_turn(usr, playable)
            action = self.process_turn(usr, usr_turn)
            
            # checks if user's hand is empty and they won
            winner = self.check_winner(usr)

            if(winner):
                action += " Their hand is empty and they won!"
            
            # send a message to users saying what happened
            for usrs in self.players:
                uno_server.send_update(usrs.ip_address[0], action, usrs.hand, winner)
            
            if(winner):
                break
            # if no winner then proceed with round
            self.process_card()
    
    # processes events 
    def process_card(self):
        type = self.deck.last_played.type
        
        # Player who played the card
        usr = self.players.popleft()
        # Player being targeted by cards other than reverse
        target = None
        
        if type == 'Draw-Two':
            target = self.players.popleft()
            for x in range(2):
                target.hand.append(self.deck.draw())
        elif type == 'Reverse':
            # unlike other special cards reverse does not skip the next player
            self.players.appendleft(usr)
            self.reverse_order()
            return
        elif type == 'Skip':
            target = self.players.popleft()
        elif type == 'Wild 4':
            target = self.players.popleft()
            for x in range(4):
                target.hand.append(self.deck.draw())
        
        self.players.append(usr)
        self.players.append(target)
        
    # checks to see if there is a winner 
    def check_winner(self, user):
        winner = False
        
        # checks if the player has no cards left
        if(len(user.hand) == 0):
            winner = True
                
        return winner
    
    # used in event of a reverse card which will reverse the order of turns 
    def reverse_order(self):
        # used to temporarily store players in order to reverse order 
        temp_stack = []
    
        # moves every player from queue to a stack
        while(not len(self.players) == 0):
            temp_stack.append(self.players.popleft())
        # returns every player from stack to the queue now in reversed order
        while(not len(temp_stack) == 0):
            self.players.append(temp_stack.pop())
            
    def process_turn(self, usr: Player, message):
        action = ""
        if(message[0] == "DRAW"):
            usr.hand.append(self.deck.draw())
            action = " drew a card."
        elif(message[0] == "PLAY"):
            played = Card.str_to_card(message[1].split(' ', 1)[1])
            print("played: " + str(played))
            for hand_card in usr.hand:
                if(hand_card.color == played.color and hand_card.number == played.number and hand_card.type == played.type):
                    usr.hand.remove(hand_card)
                    break
            action = usr.name + " played a " + str(played) + "."
            if(played.color == "Any"):
                new_color = message[2].split(' ')[1]
                played.wild_color = new_color
                action = usr.name + " played a " + str(played) + " and changed the color to " + played.wild_color + "."
            self.deck.play(played)
        return action
        
