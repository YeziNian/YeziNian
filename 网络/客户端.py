from socket import *
import os
import re
pattern = r"(?m).+(IPv4).+ (?P<IP>.+)"
with os.popen("ipconfig", "r") as fp:
    Ip = re.search(pattern, fp.read()).group("IP")

Bufsize = 1024
PORT = 21521
soc = socket(AF_INET, SOCK_STREAM)
soc.connect((Ip, PORT))
soc.send("heh".encode())
mark = soc.recv(Bufsize).decode()
print(mark)