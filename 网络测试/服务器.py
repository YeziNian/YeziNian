import socket
import threading
import os
port = 51259
ip = ""
tup = (ip, port)
if not os.path.exists("data.txt"):
    with open("data.txt", "w") as fp:
        pass
def Go(conn, addr):
    print(f"客户端{addr}已连接!")
    while True:
        mark = conn.recv(1024).decode()
        if mark == "1":  #1为登录
            lie = []
            with open("data.txt", "r") as fp:
                Message = fp.readline().strip()
                while Message:
                    lie.append(Message.split(","))
                    Message = fp.readline().strip()
            if not lie:
                conn.send(b"no")
                break
            try:
                data = conn.recv(1024).decode().strip().split(",")
                if data in lie:
                    conn.send(b"ok")
                else:
                    conn.send(b"no")
                conn.close()
            except:
                pass
            break
        elif mark == "2": #2为注册
            try:
                data = conn.recv(1024).decode().split(",")
                with open("data.txt", "a") as fp:
                    fp.write(data[0] + "," + data[1] + "\n")
                conn.send("ok".encode())
                conn.close()
                break
            except:
                pass
    print(f"客户端{addr}已断开连接!")
soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soc.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
soc.bind(tup)
soc.listen()

while True:
    try:
        conn, addr = soc.accept()
        t = threading.Thread(target=Go, args=(conn, addr))
        t.start()
    except:
        pass
soc.close()