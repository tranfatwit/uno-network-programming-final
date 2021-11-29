# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:57:12 2021
"""

import socket
import sys
import card

def send_update(socket, hand):
    action = input("Enter the card you would like to play or 'd' to draw: ")
    message = ""
    if(action == 'd'):
        message = "DRAW"
    else:
        message = "PLAY\nCard: " + action

    socket.sendall(message.encode())

def get_update(message, hand):
    update = message[1].split(' ', 1)[1]
    print("Update: " + update)
    new_hand = cards_to_list(update)
    hand.clear()
    hand.extend(new_hand)
    print(str(hand))
    
    # if the message has the End header the game is over
    if(len(message) > 3):
        return True
    return False

def cards_to_list(card_header):
    cards = card_header.split(' ', 1)[1]
    cards = cards.split(';')
    result = []
    for new_card in cards:
        print(str(new_card))
        result.append(card.Card.str_to_card(new_card))
    return result

def get_message(socket, hand):
    message = socket.recv(4096).decode().splitlines()
    if(message[0] == "UPDATE"):
        return get_update(message, hand)
    elif(message[0] == "TURN"):
        take_turn(socket, message, hand)
    return False
        
def take_turn(socket, message, hand):
    cards = cards_to_list(message[1])
    print("Playable cards: \n")
    for playable in cards:
        print(str(playable))
    send_update(socket, hand)

# ----- main -----

PORT = 11111

HOST = input("Input the server address: ")
if(HOST == ""):
    HOST = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

username = input("Enter your username: ")
username = "Username: " + username if len(username) > 0 else ""
s.sendall(("CONNECT\n" + username).encode())
message = s.recv(4096).decode()   
if(message.splitlines()[0] != "ACCEPTED"):
    print("Connection refused: " + message)
    sys.exit()

print(message)
message = s.recv(4096).decode()
print(message)

hand = []
while(True):
    # get the next message from the server if get_message returns true the game is over
    if(get_message(s, hand)):
        break
s.close()
