# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:57:12 2021
"""

import socket
#import threading
import player

def host_players(numplayers, socket_, players):
    """"Waits for specified number of players to join and fills players with the player info"""
    connections = 0
    while(connections != numplayers):
        try:
            sc, address = socket_.accept()
            request = sc.recv(50).decode().splitlines()
            if request[0] == "CONNECT":
                username = "User" + connections
                for line in range(len(request)) + 1:
                    header = request[line].split(' ')
                    if(header[0] == "Username:"):
                        username = header[1]

                connections += 1
                usr = player.Player((sc, address), username)
                players.append(usr)
                sc.sendall(b"ACCEPTED")
        except socket.error as msg:
            print('Connection failed: ' + str(msg[0]) + ' Message ' + msg[1])
            sc.close()
    
    
def thread_recieve(name, sock, client):
    #print("Thread {0} starting:".format(name,))
    while True:
        try:
            sock.sendall(input("> ").encode())
        except socket.error:
            sock.close()
            break


HOST = ''
PORT = 11111

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bound')
s.listen(10)

players = []
host_players(4, s, players)
# TODO: Implement game.
s.close()