import socket
import sys
import threading
import time
port = 50131
lock = threading.Lock()
i = 0
def replyMessage(conn):
   # lock.acquire()
    global i
    while True:
        try:
            data = conn.recv(1024)
            conn.send(data)
            if data.decode().lower() == "bye":
                break
            if len(data.decode()) == 0:
                print(f"客户端{i}已经断开链接!")
                break
        except socket.error:
            break
    conn.close()
   # lock.release()

def main():
    global i
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    #sock.settimeout(5)
    sock.bind(("", port))
    sock.listen(200)
    while True:
        try:
            conn, addr = sock.accept()
            i += 1
            if addr[0] != onlyyou:
                print("必须是本机IP!")
                conn.close()
                continue
            #print(f"第{i}个用户已经连接到服务器!")
            t = threading.Thread(target=replyMessage, args=(conn, ))
            t.start()
            #print(threading.enumerate())
        except ConnectionResetError:
            print(f"客户端{i}已经断开链接!")
            conn.close()
        else:
            pass
if __name__ == '__main__':
    try:
        onlyyou = socket.gethostbyname(socket.gethostname())
        main()
    except:
        print("error!!")