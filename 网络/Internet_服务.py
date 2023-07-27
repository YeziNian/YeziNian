import socket

"""s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(("", 5000))
while True:
    data, addr = s.recvfrom(1024)
    print("received message:{0} from PORT {1} on {2}".format(data.decode(), addr[1], addr[0]))
    if data.decode().lower() == "bye":
        break
s.close()"""

"""import jieba
jieba.add_word("我操你妈的")
print(list(jieba.cut("我操你妈的小子")))
"""

words = {"how are you?": "Fine, thank you!", "how old are you?": "32",
         "what is your name?": "Yezi nian", "where do you work?": "No, i am a student."}
Host = ""
port = 40007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((Host, port))
s.listen(1)
print("Listening ar port:", port)
conn, addr = s.accept()
print("Connected by:", addr)
while True:
    data = conn.recv(1024).decode()
    if not data:
        break
    print("Received message:", data)
    conn.sendall(words.get(data, "Nothing").encode())
conn.close()
s.close()