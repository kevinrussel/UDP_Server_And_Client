class UDP_Client:
    import socket
    import struct
    import random
    import time
    import json

    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        self.ip = None 
        self.port  = None

    def open_json_at_idex(index: int):
        with open("connections.json") as file:
            connections = json.load(file)
            print(connections)
        
    def create_header(self,header_packet_num):
        timestamp = self.time.time()
        
        header = self.struct.pack('!Bd',header_packet_num,timestamp)
        return header

    def set_udp_values(self,ip,port) -> None:
        print(ip)
        print(port)
        self.ip = str(ip)
        self.port = int(port)


    def get_udp_values(self,ip,port):
        return self.ip, self.port



    def test(self,server_address, port):
        i = 0
        count = 0
        for i in range(1,101):
            num = self.random.randint(0,100)
            if(num <= 10):
                count +=1
                continue            
            message = self.create_header(i) + b"This is a Test Packet."
            self.udp_client_socket.sendto(message,(server_address,port))
        print(f'packet drop count is {count}')

    def send(self, server_address = "127.0.0.1",port=8080):
        header = self.create_header(0)
        message = header + b"This is a handshake test."
        self.udp_client_socket.sendto(message,(server_address,port))
