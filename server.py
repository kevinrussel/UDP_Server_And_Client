import socket
import struct
import time
import threading
from  concurrent.futures import ThreadPoolExecutor

class udp_server:
    
    def handle_recieved_message(self,message):
        header = message[:10]
        packet_num,timestamp = self.struct.unpack("!Hd", header)
        timestamp = time.time() - timestamp
        message = (message[10:]).decode("utf-8")                   
        return packet_num,timestamp,message 
    

    def udp_server_listen(self):
        num = 1
        with ThreadPoolExecutor(max_workers=8) as executor:
            futures = []
            while True:
                try:
                    message,address = self.udp_server_socket.recvfrom(1024)
                    futures.append(executor.submit(self.handle_recieved_message,message))
                    num = num + 1
                except KeyboardInterrupt:
                    break
        print(num)

    def start_udp_server(self):
        self.udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        self.udp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, 4 * 1024 * 1024)
        self.udp_server_socket.bind(('',8080))
        self.udp_server_listen()


udp = udp_server()
udp.start_udp_server()