import socket
import os
from _thread import *

ServerSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '127.0.0.1'
port = 3000
ThreadCount = 0
try:
    ServerSocket.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')
ServerSocket.listen()


def threaded_client(connection, addr):
    while True:
        data = connection.recv(1024)
        reply = 'Server Says: ' + data.decode('utf-8')
        if not data:
            break
        else:
            print(f"Received {data} from {addr}")
        connection.sendall(str.encode(reply))
    print('Closed connection to', addr)
    connection.close()

while True:
    Client, address = ServerSocket.accept()
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    start_new_thread(threaded_client, (Client, address, ))
    ThreadCount += 1
    print('Thread Number: ' + str(ThreadCount))
ServerSocket.close()
