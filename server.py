
class udp_server:
    import socket
    import struct
    import time
    import threading
    

    def handle_recieved_message(self,message,num):
        header = message[:10]
        packet_num = self.struct.unpack("!Hd", header)[0]
        timestamp = (self.time.time()) - self.struct.unpack("!Hd", header)[1]
        message = (message[10:]).decode("utf-8")
        print(f' This packet is {packet_num}')
        print(f'Time for packet travel: {timestamp}')
        print(message)                   
        print(f'Total Num of Recived packet is {num}\n')
        return packet_num,timestamp,message 
    

    def udp_server_listen(self):
        num = 1
        while True:
            message,address = self.udp_server_socket.recvfrom(1024)
            self.threading.Thread(target=self.handle_recieved_message, args = (message,num), daemon=True).start()
            num = num + 1


    def start_udp_server(self):
        self.udp_server_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        self.udp_server_socket.bind(('',8080))
        self.udp_server_listen()


udp = udp_server()
udp.start_udp_server()