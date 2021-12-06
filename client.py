import socket
import time
# More
import api_method as apim

class cfg:
    periodicity_send = 60

class tmp:
    sock = socket.socket()
    sock.connect(("localhost", 2021))
    time.sleep(3)
    sock_handler = apim.client(sock)

class work:
    GetConnectData = True

while work.GetConnectData:
    try:
        tmp.sock_handler.send_data({"command": "test"})
        print(tmp.sock_handler.get_data())
    except:
        pass
    time.sleep(1)