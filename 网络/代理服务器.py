import socket
import sys
import threading
import time
port = 50113
port1 = 50131
def middle(conn, addr):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    #sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    ip = socket.gethostbyname(socket.gethostname())
    sock.connect((ip, port1))
    while True:
        data = conn.recv(1024).decode()
        print("收到客户端的消息:"+data)
        if data == "不要发给服务器":
            conn.send("该消息已被代理服务器过滤!".encode())
            print("该消息已经过滤!")
        elif data.lower() == "bye":
            print(str(addr)+" 客户端关闭链接!")
            break
        else:
            sock.send(data.encode())
            print("已转发服务器!")
            data_fa = sock.recv(1024).decode()
            print("收到服务器的消息:"+data_fa)
            if data_fa == "不要发给客户端":
                conn.send("该消息已经被代理服务器修改!".encode())
                print("消息已被修改!")
            else:
                conn.send(b"Server reply:"+data_fa.encode())
                print("已转发服务器消息给客户端!")
    conn.close()
    sock.close()
def main():
    sockscr = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockscr.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockscr.bind(("", port))
    print("代理已启动!")
    sockscr.listen()
    while True:
        try:
            conn, addr = sockscr.accept()
            t = threading.Thread(target=middle, args=(conn, addr))
            t.start()
            print("新客户--"+str(addr))
        except:
            pass
if __name__ == '__main__':
    try:
        ip = socket.gethostbyname(socket.gethostname())
        main()
    except:
        print("Sth error")