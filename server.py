import socket


udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
udp_server_socket.bind(('',8080))


