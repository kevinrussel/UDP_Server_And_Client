import socket
import struct
import time
import threading
from  concurrent.futures import ThreadPoolExecutor

class udp_server:
    
    def handle_recieved_message(self,message):
        header = message[:10]
        packet_num,timestamp = struct.unpack("!Hd", header)
        timestamp = time.time() - timestamp
        message = (message[10:]).decode("utf-8")
                   
        return packet_num,timestamp,message 
    

    def calculate_graph_values(self,num,futures):
        future_value = futures[0].result()
        min_value = future_value[1]
        max_value = future_value[1]
        total = future_value[1]
        for index in range(1,num):
            future_value = futures[index].result()
            if(future_value[1] < min_value):
                min_value = future_value[1]
            if(future_value[1] > max_value):
                max_value = future_value[1]
            total = total + future_value[1]
        average = total / num

        return min_value,max_value,average
        

    def udp_server_listen(self):
        num = 0
        futures = []
        with ThreadPoolExecutor(max_workers=8) as executor:
            
            while True:
                try:
                    message,address = self.udp_server_socket.recvfrom(100)
                    futures.append(executor.submit(self.handle_recieved_message,message))
                    num = num + 1
                except KeyboardInterrupt:
                    break
        print("\n")
        print(len(futures))
        print(futures[1].result())
        print(num)
        self.calculate_graph_values(num,futures)

    def start_udp_server(self):
        self.udp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

        self.udp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_RCVBUF, 4 * 1024 * 1024)
        self.udp_server_socket.bind(('',8080))
        self.udp_server_listen()


udp = udp_server()
udp.start_udp_server()