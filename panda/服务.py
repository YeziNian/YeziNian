import socket
import threading
import time
port = 51037
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", port))
print("Listening...")
sock.listen()
class my(threading.Thread):
    lis = []
    Run = 1
    def __init__(self, conn, name, addr):
        self.conn = conn
        self.addr = addr
        if name not in my.lis:
            threading.Thread.__init__(self, name=name)
            my.lis.append(name)
        else:
            raise Exception
    def run(self):
        if self.conn.recv(1024) == b"bye":
            print(f"客户端{self.addr}已断开连接!")
            my.Run = 0

def little(conn):
    if conn.recv(1024) == b"bye":
        print(f"客户端{addr}已断开连接!")
def lianjie(conn, addr):
    print(f"客户端{addr}已连接!")
    i = 1
    while True:
        try:
            print(f"客户端已经连接{i}秒!")
            try:
                c = my(conn, str(i), addr)
                c.start()
                if c.Run == 0:
                    break
            except Exception:
                pass
            time.sleep(1)
            i += 1
        except ConnectionResetError:
            print(f"客户端{addr}已断开连接!")
            break
    conn.close()
while True:
    conn, addr = sock.accept()
    t = threading.Thread(target=lianjie, args=(conn, addr))
    t.start()
