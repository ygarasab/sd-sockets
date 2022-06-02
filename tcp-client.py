import socket
from time import sleep

HOST = "127.0.0.1"  
PORT = 3000  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

while 1:
    s.sendall(b"Hello, world")
    data = s.recv(1024)

    print(f"Received {data!r}")
    sleep(5)
