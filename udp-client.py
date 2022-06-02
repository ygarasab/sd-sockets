import socket
from time import sleep

HOST = "127.0.0.1"  
PORT = 4000  

server = (HOST, PORT)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while 1:
    s.sendto(b"Hello, world", server)
    data = s.recv(1024)

    print(f"Received {data!r}")
    sleep(5)

