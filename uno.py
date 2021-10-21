# -*- coding: utf-8 -*-
"""
Created on Tue Oct 12 16:57:12 2021
"""

import socket
import threading

def thread_recieve(name, sock, client):
    #print("Thread {0} starting:".format(name,))
    while True:
        try:
            sock.sendall(input("> ").encode())
        except socket.error:
            sock.close()
            break


HOST = ''
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bound')
s.listen(10)
while True:
    try:
        sc, address = s.accept()
        print('Connected with ' + address[0] + ':' + str(address[1]))
        
        rThread = threading.Thread(target = thread_recieve, args=(1, sc, address[0]), daemon=True)

        rThread.start()
        
        while True:            
            try:
                message = sc.recv(50).decode()
                    
                if(message == "logout") :
                    print("User {0} left.".format(address[0]))
                    sc.sendall(b"logout")
                    rThread.join()
                    sc.close()
                    break
                print("{0}: ".format(address[0]) + message)
            except socket.error:
                sc.close()
            
            
    except socket.error as msg:
        print('Bind failed: ' + str(msg[0]) + ' Message ' + msg[1])
        sc.close()
s.close()