import base64
import json
import time

class functions:
    class decoding:
        class base64:
            def encode(data):
                return base64.urlsafe_b64encode(json.dumps(data).encode())
        
            def decode(data: bytes):
                return json.loads(base64.urlsafe_b64decode(data).decode())

class tmp:
    pass

class server():
    def __init__(self, sock, conn, addr):
        self.socket = sock
        self.connect = conn
        self.address = addr

    def get_data(self):
        data_size = functions.decoding.base64.decode(self.connect.recv(1024))
        return functions.decoding.base64.decode(self.connect.recv(data_size))

    def send_data(self, data):
        base_data = functions.decoding.base64.encode(data)
        self.connect.sendall(functions.decoding.base64.encode(len(base_data)))
        self.connect.sendall(base_data)
        return data

    def get_hostname(self):
        info = self.socket.getsockname()
        return {"host": info[0], "port": info[1]}

class client():
    def __init__(self, sock):
        self.socket = sock

    def get_data(self):
        data_size = functions.decoding.base64.decode(self.socket.recv(1024))
        return functions.decoding.base64.decode(self.socket.recv(data_size))

    def send_data(self, data):
        base_data = functions.decoding.base64.encode(data)
        self.socket.sendall(functions.decoding.base64.encode(len(base_data)))
        self.socket.sendall(base_data)