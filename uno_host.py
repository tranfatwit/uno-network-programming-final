# -*- coding: utf-8 -*-
"""
Created on Sun Nov 28 19:25:07 2021

@author: peter
"""

import socket
from collections import deque
from uno_game import Game
from uno_server import host_players

HOST = ''
PORT = 11111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bound')
s.listen(10)

players = deque()

host_players(4, s, players)
for usr in players:
    connection = usr.ip_address[0]
    connection.sendall(b"Thanks for joining! The game is starting.")

game = Game(players)
game.run_game()

for usr in players:
    usr.ip_address[0].close()
s.close()
