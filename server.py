import socket
import struct
import time
class udp_server:


    def start_udp_server(self):
        udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        udp_server_socket.bind(('',8080))
        self.udp_server_listen()

    def handle_recieved_message(self,message):
        header = message[:9]
        packet_num = struct.unpack("!Bd", header)[0]
        timestamp = (self.time.time()) - struct.unpack("!Bd", header)[1]
        message = (message[9:]).decode("utf-8")
        return packet_num,timestamp,message 
    def udp_server_listen(self):
        num = 1
        while True:
            message,address = self.udp_server_socket.recvfrom(1024)
            packet_num,timestamp,message = self.handle_recieved_message(message)
            print(f' This packet is {packet_num}')
            print(f'This is the time it took {timestamp}')
            print(message)                   
            print(f'Total Num of Recived packet is {num}\n')
            num = num + 1


udp = udp_server()
udp.start_udp_server()