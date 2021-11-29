# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 00:35:02 2021

@author: Peter Garrity
"""

import socket
import player

def host_players(numplayers, socket_, players):
    """"Waits for specified number of players to join and fills players with the player info"""
    connections = 0

    while(connections != numplayers):
        try:
            sc, address = socket_.accept()
            request = sc.recv(4096).decode().splitlines()
            if request[0] == "CONNECT":
                username = "User" + str(connections)
                for line in request:
                    header = line.split(' ')
                    if(header[0] == "Username:"):
                        username = header[1]

                connections += 1
                usr = player.Player((sc, address), username)
                players.append(usr)
                print("Added " + username)
                sc.sendall(b"ACCEPTED")
        except socket.error as msg:
            print('Connection failed: ' + str(msg[0]) + ' Message ' + msg[1])
            sc.close()

def give_turn(usr: player.Player, playable):
    message = "TURN\nCards: "
    for index, cards in enumerate(playable):
        if(index != 0):
            message += ';'
        message += str(cards)
    
    print("Sent:\n" + message)
    usr.ip_address[0].sendall(message.encode())
    response = usr.ip_address[0].recv(4096).decode().splitlines()
    return response
    
def get_turn(usr: player.Player):
    message = usr.ip_address[0].recv(4096).decode().splitlines()
    return message

def send_update(socket, message, hand, winner):
    update = "UPDATE\n"
    update += "Update: " + message + "\nCards:"
    for index, card in enumerate(hand):
        if(index != 0):
            update += ';'
        update += str(card)
    if(winner):
        update += "\nEnd: True"
    print("Update:\n" + update)
    socket.sendall(update.encode())
