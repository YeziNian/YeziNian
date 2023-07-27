import socket
import pygeoip
import sys
"""gi = pygeoip.GeoIP("GeoLiteCity.dat")
print(gi.record_by_name("10.128.175.150"))"""
ip = socket.gethostbyname(socket.gethostname())
"""import sys
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.sendto(sys.argv[0].encode(), ("10.128.175.150", 5000))
s.close()"""
Host = ip
port = 40007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    s.connect((Host, port))
except Exception as e:
    print("Severr not found or Open")
    sys.exit()
while True:
    c = input("What do you wang to send:")
    s.sendall(c.encode())
    data = s.recv(1024).decode()
    print("Received: ", data)
    if c.lower() == "bye":
        break
s.close()