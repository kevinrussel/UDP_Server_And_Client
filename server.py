import socket
import struct


udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server_socket.bind(('',8080))

num = 1
while True:
    message,address = udp_server_socket.recvfrom(1024)

    header = message[:1]
    header = struct.unpack("!B",header)[0]
    message = message[1:]
    message = message.decode("utf-8")
    print(f' This packet is {header}')
    print(message)                   
    print(f'Total Num of Recived packet is {num}\n')
    num = num + 1