import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox, Querybox
import threading
import random
import re
import time
import os
import pandas as pd
import numpy as np
import datetime
import socket
import sqlite3
import struct
import string
import sys
import ttkbootstrap.dialogs
import MySQLdb
"""root = ttk.Window(title="Yezi", size=(360, 340), themename="darkly")
root.resizable(False, False)
root.place_window_center()
def jiance():
    try:
        t1 = int(id.get())
        t2 = name.get()
        t3 = int(price.get())
    except Exception:
        Messagebox.show_error(message="Wrong!")
        return
    if t1 and t2 and t3:
        try:
            conn = MySQLdb.connect(host="localhost", user="root", passwd='xingxing', db='test', port=3306)
            cur = conn.cursor()
            all = cur.fetchall()
            print(all, type(all))
            if (t1, t2, t3) in all:
                Messagebox.show_error(title="Yezi", message="The message is exists!")
                return
            de = cur.execute("INSERT INTO yezi VALUES(%s, %s, %s)", (t1, t2, t3))
            #cur.execute("SELECT * FROM yezi")
            #print(he)
            conn.commit()
            cur.close()
            conn.close()
            Messagebox.show_info(title='Yezi', message="存入成功!")
        except MySQLdb.Error as s:
            print("Wrong!")
    else:
        Messagebox.show_error(title="Yezi", message="不能为空!")
id = ttk.Combobox(root, values=[str(i) for i in range(100)], state='readonly')
id.pack()
name = ttk.Entry(root)
name.pack()
price = ttk.Entry(root)
price.pack()
button = ttk.Button(root, text="submit", command=jiance)
button.pack()
root.mainloop()"""
"""
conn = MySQLdb.connect(host="localhost", user="root", passwd='xingxing', db='test', port=3306)
cur = conn.cursor()
#de = cur.execute("INSERT INTO yezi VALUES(%s, %s, %s)", (123, 'jgf', 1232))
cur.execute("SELECT * FROM yezi")
# print(he)
#conn.commit()
all = cur.fetchall()
print(all, type(all))
cur.close()
conn.close()
#Messagebox.show_info(title='Yezi', message="存入成功!")"""
import time
"""conn = MySQLdb.connect(host="localhost", user="root", passwd='xingxing', db='test', port=3306)
cur = conn.cursor()
#cur.execute("CREATE TABLE new(id INT, name VARCHAR(20), price INT)")
data = string.ascii_lowercase + string.ascii_uppercase
for i in range(100):
    name = "".join([random.choice(data) for k in range(4)])
    cur.execute("INSERT INTO new VALUES(%s, %s, %s)", (i, name, i+1000))
    conn.commit()
de = cur.execute("SELECT USER()")
print(de, cur.fetchall())
cur.close()
conn.close()"""
import requests
#response = requests.get("http://www.baidu.com")
##response.encoding = response.apparent_encoding
#print(str(response.status_code), response.text)
import hashlib
#print(hashlib.md5('hewllo'.encode()).hexdigest())
import socket

ip = socket.gethostbyname(socket.gethostname())
print(ip)
ip = ip.split('.')
result = 0
for m, n in enumerate(ip):
    result += int(n) * 256 ** (3-m)
print(result)