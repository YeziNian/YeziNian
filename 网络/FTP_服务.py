import socket
import threading
import os
import struct
port = 50131
users = {"zhangsan": {"pwd": "zhangsan123", "home": r"c:\python 3.5"},
         "lisi": {"pwd": "lisi123", "home": r"c:\\"}}

def server(conn, addr, home):
    print("新客户端:"+str(addr))
    os.chdir(home)
    while True:
        data = conn.recv(1024).decode().lower()
        print(data)
        if data in ("quit", "q"):
            break
        elif data in ("list", "is", "dir"):
            files = str(os.listdir(os.getcwd()))
            files = files.encode()
            conn.send(struct.pack("I", len(files)))
            conn.send(files)
        elif "".join(data.split()) == "cd..":
            cwd = os.getcwd()
            newCwd = cwd[:cwd.rindex("\\")]
            if newCwd[-1] == ":":
                newCwd += "\\"
            if newCwd.lower().startswith(home):
                os.chdir(newCwd)
                conn.send(b"ok")
            else:
                conn.send(b"error")
        elif data in ("cwd", "cd"):
            conn.send(str(os.getcwd()).encode())
        elif data.startswith("cd "):
            data = data.split(maxsplit=1)
            if len(data) == 2 and os.path.isdir(data[1]) \
                and data[1] != os.path.abspath(data[1]):
                os.chdir(data[1])
                conn.send(b"ok")
            else:
                conn.send(b"error")
        elif data.startswith("get "):
            data = data.split(maxsplit=1)
            if len(data) == 2 and os.path.isfile(data[1]):
                conn.send(b"ok")
                fp = open(data[1], "rb")
                while True:
                    content = fp.read(4096)
                    if not content:
                        conn.send(b"overxxxx")
                        break
                    conn.send(content)
                    if conn.recv(10) == b"ok":
                        continue
                fp.close()
            else:
                conn.send(b"no")
        else:
            pass
    conn.close()
    print(str(addr)+"关闭连接")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("", port))
sock.listen()
while True:
    conn, addr = sock.accept()
    userid, userpwd = conn.recv(1024).decode().split(",")
    if userid in users and users[userid]["pwd"] == userpwd:
        conn.send(b"ok")
        home = users[userid]["home"]
        t = threading.Thread(target=server, args=(conn, addr, home))
        t.daemon = True
        t.start()
    else:
        conn.send(b"error")
