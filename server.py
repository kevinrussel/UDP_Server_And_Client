
class udp_server:
    import socket
    import struct
    import time

    

    def handle_recieved_message(self,message):
        header = message[:9]
        packet_num = self.struct.unpack("!Bd", header)[0]
        timestamp = (self.time.time()) - self.struct.unpack("!Bd", header)[1]
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


    def start_udp_server(self):
        self.udp_server_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        self.udp_server_socket.bind(('',8080))
        self.udp_server_listen()


udp = udp_server()
udp.start_udp_server()