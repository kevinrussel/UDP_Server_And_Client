import socket


udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server_socket.bind(('',8080))


while True:
    message,address = udp_server_socket.recvfrom(1024)
    print(message)