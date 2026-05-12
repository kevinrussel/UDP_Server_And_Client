class UDP_Client:
    import socket
    import struct
    import random
    import time
    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        
    def create_header(self,header_packet_num):
        timestamp = self.time.time()
        
        header = self.struct.pack('!Bd',header_packet_num,timestamp)
        return header
    
    def test(self,server_address= "127.0.0.1", port=8080):
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
