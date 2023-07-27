from socket import *

Bufsize = 1024
PORT = 21521

soc = socket(AF_INET, SOCK_STREAM)
soc.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
soc.bind(("", PORT))
soc.listen(1)

while True:
    print("waiting for connection..")
    tcp, addr = soc.accept()
    print("connection from ", addr)
    while True:
        mark = tcp.recv(Bufsize).decode()
        if not mark:
            break
        tcp.send("你好".encode())
        print(mark)
    tcp.close()