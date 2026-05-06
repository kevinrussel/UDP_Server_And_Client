class UDP_Client:
    import socket
    import struct
    import random
    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        
    def create_header(self,header_packet_num):
        header = self.struct.pack('!B',header_packet_num)
        return header
    
    def test(self,server_address= "127.0.0.1", port=8080):
        i = 0
        count = 0
        for i in range(0,100):
            num = self.random.randint(0,100)
            if(num <= 10):
                count +=1
                continue            
            message = self.create_header(i) + b"Hello World"
            self.udp_client_socket.sendto(message,(server_address,port))
        print(f'count is {count}')

    def send(self, server_address = "127.0.0.1",port=8080):
        message = b"Hello world"
        self.udp_client_socket.sendto(message,(server_address,port))
