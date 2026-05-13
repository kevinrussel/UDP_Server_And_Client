class UDP_Client:
    import socket
    import struct
    import random
    import time
    import json

    def __init__(self):
        self.udp_client_socket = self.socket.socket(self.socket.AF_INET,self.socket.SOCK_DGRAM)
        self.ip = None 
        self.port  = None
        self.packets_after_dropped = 100

    def open_json_at_idex(self,index: int):
        with open("connections.json") as file:
            connections = self.json.load(file)
            connections = connections["connections"][index]
            return connections["ip"], connections["port"]
        

    def create_header(self,header_packet_num):
        timestamp = self.time.time()
        header = self.struct.pack('!Bd',header_packet_num,timestamp)
        return header

    def set_known_json_value(self,index):
        ip,port = self.open_json_at_idex(index)
        self.ip = ip
        self.port = port
        return ip,port


    def set_udp_values(self,ip,port) -> None:
        data = {"ip": ip, "port": port}
        with open("connections.json", "r") as file:
            file_data = self.json.load(file)
        
        file_data["connections"].append(data)
        with open("connections.json","w") as f:
            self.json.dump(file_data,f, indent=4)
        
        ip,port = self.set_known_json_value(-1)
        return
  

    def get_udp_values(self):
        return self.ip, self.port

    def set_drop_packets(self,packets):
        self.packets_after_dropped = 100 - packets
    
    def get_drop_packets(self):
        return self.packets_after_dropped

    def send_packets(self):
        sending_packets = self.get_drop_packets()
        server_address, port = self.get_udp_values()
        total_dropped_count = 0
        for header_num in range(0,101):
            num = self.random.randint(0,100)
            if (num > sending_packets):
                total_dropped_count +=1
                continue
            message = self.create_header(header_num) + b"This is a Test Packet"
            self.udp_client_socket.sendto(message,(server_address,port))
        print(f"total packet drop count is {total_dropped_count}")

 

    def send_hello(self):
        server_address,port = self.get_udp_values()
        header = self.create_header(0)
        message = header + b"This is a handshake test."
        self.udp_client_socket.sendto(message,(server_address,port))
