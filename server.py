import socket
import struct

class udp_server:


    def start_udp_server():
        udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        udp_server_socket.bind(('',8080))

    
    def udp_server_listen(self):
        num = 1
        while True:
            message,address = udp_server_socket.recvfrom(1024)

            header = message[:9]
            header = struct.unpack("!Bd",header)[1]
            
            message = message[9:]
            message = message.decode("utf-8")
            print(f' This packet is {header}')
            print(message)                   
            print(f'Total Num of Recived packet is {num}\n')
            num = num + 1

    if __name__ =='__main__':
        sart_udp_server()