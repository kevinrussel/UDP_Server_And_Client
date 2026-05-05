class UDP_Client:
    import socket
    import struct
    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        
    
    
    def test(self,server_address= "127.0.0.1", port=8080):
        i = 0
        while(i < 10):
            message = self.struct.pack('!B',i) + b"Hello World"
            self.udp_client_socket.sendto(message,(server_address,port))
            i +=1

    def send(self, server_address = "127.0.0.1",port=8080):
        message = b"Hello world"
        self.udp_client_socket.sendto(message,(server_address,port))
