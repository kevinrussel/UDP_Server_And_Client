class UDP_Client:
    import socket
    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        
    
    
    def send(self, server_address = "127.0.0.1",port=8080):
        message = b"Hello world"
        print(type(server_address))
        self.udp_client_socket.sendto(message,(server_address,port))
