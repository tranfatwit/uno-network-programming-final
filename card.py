# -*- coding: utf-8 -*-
"""
Created on Fri Oct 22 12:46:28 2021
"""

from enum import Enum

class Color(Enum):
    RED = "red"
    GREEN = "green"
    BLUE = "blue"
    YELLOW = "yellow"
    WILD = "wild"

class Card:
    
    def __init__(self, clr, val):
        color = clr
        value = val
        print("{0} {1}".format(color.value , value))
        
    def match(c1, c2):
        if(c1.color == c2.color or c1.value == c2.value):
            return True
        else:
            return False
        
        
        