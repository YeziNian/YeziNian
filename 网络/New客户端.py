import socket
import sys
import threading
import time
port = 50113
def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((socket.gethostbyname(socket.gethostname()), port))
    while True:
        data = input("What dou you want to ask:")
        sock.send(data.encode())
        print(sock.recv(1024).decode())
        if data.lower() == "bye":
            break
    sock.close()

if __name__ == '__main__':
    try:
        main()
    except:
        print("Sth wrong!")
