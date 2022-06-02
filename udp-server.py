import socket
import os

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
host = '127.0.0.1'
port = 4000

try:
    server.bind((host, port))
except socket.error as e:
    print(str(e))

print('Waitiing for a Connection..')


while True:

    data, address = server.recvfrom(1024)
    print('Connected to: ' + address[0] + ':' + str(address[1]))
    reply = 'Server Says: ' + data.decode('utf-8')
    if not data:
        break
    else:
        print(f"Received {data} from {address}")
    server.sendto(str.encode(reply), address)
server.close()

