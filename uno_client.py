# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:57:12 2021
"""

import socket
import sys
import card
import enums

PORT = 11111

HOST = input("Input the server address: ")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

username = input("Enter your username: ")
username = "Username: " + username if len(username) > 0 else ""
s.sendall(("CONNECT\n" + username).encode())
message = s.recv(50).decode()   
if(message.splitlines()[0] != "ACCEPTED"):
    print("Connection refused: " + message)
    sys.exit()

print(message)
message = s.recv(50).decode()
print(message)

s.close()

def send_update(socket, hand):
    action = input("Enter the card you would like to play or 'd' to draw: ")
    message = ""
    if(action == 'd'):
        message = "DRAW"
    elif(message.isdecimal()):
        message = "PLAY\nCard: " + action

    socket.sendall(message.encode())
    if(action == 'd'):
        receive_card(socket)
        
        
    print("Played")

def receive_card(socket, hand):
    result = socket.recv(50).decode().splitlines()
    for cards in result[1:]:
        new_card = card.Card.str_to_card(cards)
        hand.append(new_card)
            

def get_update():
    print("Received")
