# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 13:10:32 2021
"""

from enum import Enum
from card import Color, Card
from random import shuffle

class CardCount(Enum):
    ZERO = (0, 1)
    ONE = (1, 2)
    TWO = (2, 2)
    THREE = (3, 2)
    FOUR = (4, 2)
    FIVE = (5, 2)
    SIX = (6, 2)
    SEVEN = (7, 2)
    EIGHT = (8, 2)
    NINE = (9, 2)
    DRAW2 = ("draw2", 2)
    REVERSE = ("reverse", 2)
    SKIP = ("skip", 2)
    WILD = ("wild", 4)
    WILD4 = ("wild4", 4)

class Deck():
    
    
    def __init__(self,):
        self.drawpile = []
        for clr in Color:
            for val in CardCount:
                for x in val[1]:
                    self.drawpile.append(Card(clr, val[0]))

        shuffle.shuffle(self.drawpile)
        self.lastplayed = self.drawpile.draw()
        self.discardpile = []
    
    def draw(self,):
        return self.drawpile.pop()
        