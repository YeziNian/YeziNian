import socket
import sys
import threading
import time
import multiprocessing
"""active = dict()
flag = 1
def main():
    global active
    global flag
    ip = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.IPPROTO_IP, socket.IP_HDRINCL, 1)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)
    while flag:
        c = s.recvfrom(65565)
        host = c[1][0]
        active[host] = active.get(host, 0) + 1
        if c[1][0] != ip:
            print(c)
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)
    s.close()
t = threading.Thread(target=main)
t.start()
time.sleep(40)
flag = 0
t.join()
for item in active.items():
    print(item)"""

def ports(ports_se):
    for port in list(range(1, 100)) + [143, 145, 113, 443, 445, 3389, 8080]:
        try:
            ports_se[port] = socket.getservbyport(port)
        except socket.error:
            pass
"""from flask import Flask
from flask.ext.mail import Mail, Message
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello world!"
if __name__ == '__main__':
    app.run()"""
def ports_scan(host, ports_ser):
    ports_open = []
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(0.01)
    except socket.error:
        print("socket creation error")
        sys.exit()
    for port in ports_ser:
        try:
            sock.connect((host, port))
            ports_open.append(port)
            sock.close()
        except socket.error:
            pass
    return ports_open
if __name__ == '__main__':
    m = multiprocessing.Manager()
    ports_service = dict()
    results = dict()
    ports(ports_service)
    pool = multiprocessing.Pool(processes=8)
    net = "10.2.1."
    for houst_number in map(str, range(8, 10)):
        host = net+houst_number
        results[host] = pool.apply_async(ports_scan, (host, ports_service))
        print("starting "+host+"...")
    pool.close()
    pool.join()
    for host in results:
        print("="*30)
        print(host, "."*10)
        for port in results[host].get():
            print(port, ":", ports_service[port])