class UDP_Client:
    import socket

    def send(self):
        udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        udp_server_address = ("127.0.0.1",8080)
        message = b"Hello world"

        udp_client_socket.sendto(message,udp_server_address)