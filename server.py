import socket
from threading import Thread
from rich.console import Console
import json
# Дополнительно
import api_method as apim

console = Console()
console.rule("Логи")

class cfg:
    bind_settings = ("", 2021)
    connects_max = 10

class tmp:
    users = {}
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(cfg.bind_settings)
    sock.listen(cfg.connects_max)

class func:
    def user_work(address, connect, tcp, ids_progress: int):
        handler = apim.server(tcp, connect, address)
        while True:
            try:
                request_data = handler.get_data()
                console.print("[gray][[/][yellow]{0}[/]:[blue]{1}[/][gray]][/] [#20f785]->[/] {2}".format(address[0], address[1], request_data))

                try:
                    # API запросы
                    if request_data["command"] == "test":
                        request_answer = handler.send_data({"answer": {"type": "data", "data": True}, "status": True})
                    
                    else:
                        request_answer = handler.send_data({"answer": {"type": "error", "data": 0}, "status": False})

                except:
                    request_answer = handler.send_data({"answer": {"type": "error", "data": 2}, "status": False})
                
                console.print("[gray][[/][yellow]{0}[/]:[blue]{1}[/][gray]][/] [#ff3b3b]<-[/] {2}".format(address[0], address[1], request_answer))
            except:
                console.print("[gray][[/][yellow]{0}[/]:[blue]{1}[/][gray]][/] [yellow]is[/] [red]disconnect[/]".format(address[0], address[1]))
                del tmp.users["{0}:{1}".format(address[0], address[1])]
                connect.close()
                exit()

    def terminal_commander():
        while True:
            try:
                command = console.input()
            except KeyboardInterrupt:
                exit()
            try:
                console.print(eval(str(command)))
            except:
                try:
                    console.print(exec(str(command)))
                except:
                    console.print_exception()

sock_info = tmp.sock.getsockname()
console.print("[blue]*[/] [yellow]Start is server in[/] {0}:{1}".format(sock_info[0], sock_info[1]))

Thread(target=func.terminal_commander, args=(), daemon=True).start()
while True:
    try:
        conn, addr = tmp.sock.accept()
        console.print("[gray][[/][yellow]{0}[/]:[blue]{1}[/][gray]][/] [yellow]is[/] [green]connected[/]".format(addr[0], addr[1]))
        tmp.users["{0}:{1}".format(addr[0], addr[1])] = {"thread": Thread(target=func.user_work, args=(addr, conn, tmp.sock, len(tmp.users)), daemon=True)}
        tmp.users["{0}:{1}".format(addr[0], addr[1])]["thread"].start()
    except:
        console.print_exception()