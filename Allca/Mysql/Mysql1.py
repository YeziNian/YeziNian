#import pymysql
import os
import re
pa = re.compile(r"s", re.M)
pattern = r"(?m).+IPv4.+ (?P<ip>.+)"
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'xingxing',
    'port': 3306,
    'db': 'test'
}

#conn = pymysql.connect(**db_config)
import ttkbootstrap as ttk
class mysql_connect:

    def __init__(self, passwd, user, host, port, db):
        self.passwd = passwd
        self.root = user
        self.host = host
        self.port = port
        self.db = db
        self.connect()
    def connect(self):
        with os.popen(f"mysql -u{self.root} -p{self.passwd}", "r") as p:
            if p:
                print("Connect successfully!")
    def execute(self, sql_content :str):
        with os.popen(f"{sql_content}", "r") as p:
            return p.read()
    def quit(self):
        with os.popen("quit", "r") as p:
            pass
root = ttk.Window(size=(400, 400), themename="darkly")
root.place_window_center()
entry = ttk.Entry(root)
entry.pack()
def tijiao():
    content = entry.get()
    if content:
        conn = mysql_connect(**db_config)
        entry1.insert(0, conn.execute(content))
        conn.quit()
button = ttk.Button(root, text="Commit", command=tijiao)
button.pack()
entry1 = ttk.Text(root)
entry1.pack()
root.mainloop()