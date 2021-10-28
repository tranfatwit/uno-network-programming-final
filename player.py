# -*- coding: utf-8 -*-
"""
Created on Wed Oct 27 10:46:49 2021

"""

class Player():
    
    def __init__(self, ip_address, name):
        self.hand = []
        self.ip_address = ip_address
        self.name = name 
        
    def add_card(self, card):
        self.hand.append(card)
        

