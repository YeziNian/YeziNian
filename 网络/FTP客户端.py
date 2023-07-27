import socket
import sys
import re
import struct
import getpass
port = 50121
def main(serverip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((serverip, port))
    userid = input("请输入用户名:")
    useepwd = getpass.getpass("请输入密码:")
    message = userid + "," + useepwd
    sock.send(message.encode())
    login = sock.recv(100)
    if login == b"error":
        print("用户名或密码错误!")
        return
    intSize = struct.calcsize("I")
    while True:
        command = input("##>").lower().strip()
        if not command:
            continue
        command = " ".join(command.split())
        sock.send(command.encode())
        if command in ("quit", "q"):
            break
        elif command in ("list", "ls", "dir"):
            loc_size = struct.unpack("I", sock.recv(intSize))[0]
            files = eval(sock.recv(loc_size).decode())
            for item in files:
                print(item)
        elif "".join(command.split()) == "cd..":
            print(sock.recv(100).decode())
        elif command in ("cwd", "cd"):
            print(sock.recv(1024).decode())
        elif command.startswith("get "):
            isFileExist = sock.recv(20)
            if isFileExist != b"ok":
                print("error")
            else:
                print("downloading.", end="")
                fp = open(command.split()[1], "wb")
                while True:
                    print(".", end="")
                    data = sock.recv(4096)
                    if data == b"overxxxx":
                        break
                    fp.write(data)
                    sock.send(b"ok")
                fp.close()
                print("ok")
        else:
            print("无效命令!")
    sock.close()

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("No")
        exit()
    servi = sys.argv[1]
    main(servi)
