import socket
import tkinter as tk
import threading 
import os
from pyngrok import ngrok


def recieve(socket):
    while True:
        try:
            data = socket.recv(16)
            if data:
                for i in connections:
                    i.sendall(bytes(data.decode(), 'utf-8'))
            else:
                print("They left?")
                connections.remove(socket)
                socket.close()
                return
        except ConnectionResetError:
            print("Connection closed by the client")
            connections.remove(socket)
            socket.close()
            return


connections = []
    
# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

hostname = socket.gethostname()
print(socket.gethostbyname(hostname))

# Bind the socket to a port
# server_address = (socket.gethostbyname(hostname), 10000)
server_address = ("localhost", 10000)

sock.bind(server_address)




# Listen for incoming connections
sock.listen(1)


while True:
    connection, client_address = sock.accept()
    print('Connection from', client_address) 
    connections.append(connection)
    thread = threading.Thread(target=recieve, args=(connection,),)
    thread.start()   

# Receive data in small chunks and print it


# Clean up
