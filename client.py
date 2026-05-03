class UDP_Client:
    import socket
    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        self.udp_server_address = ("127.0.0.1",8080)
    
    
    def send(self):
        message = b"Hello world"
        self.udp_client_socket.sendto(message,self.udp_server_address)
