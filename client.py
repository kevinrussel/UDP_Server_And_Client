class UDP_Client:
    import socket
    import struct
    import random
    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        
    
    
    def test(self,server_address= "127.0.0.1", port=8080):
        i = 0
        count = 0

        for i in range(0,100):
            num = self.random.randint(0,100)
            print(num)
            if(num <= 10):
                count +=1
                continue
            
            message = self.struct.pack('!B',i) + b"Hello World"
            self.udp_client_socket.sendto(message,(server_address,port))
        print(f'count is {count}')

    def send(self, server_address = "127.0.0.1",port=8080):
        message = b"Hello world"
        self.udp_client_socket.sendto(message,(server_address,port))
