import threading

import pymysql
class heh:

    def __init__(self, name):
        self.name = name
    @property
    def size(self):
        return len(self.name)

de = heh('heheh')
#print(de.size)

"""class new:

    @property
    def run(self):
        print('@property')
    @run.setter
    def run(self, value):
        print(value)
    @run.deleter
    def run(self):
        print("@run.deleter")
he = new()
he.run
he.run = 10
del he.run"""

"""class new:
    def __init__(self):
        self.ori = 100
        self.discount = 0.8
    @property
    def price(self):
        new_price = self.ori * self.discount
        return new_price
    @price.setter
    def price(self, value):
        self.ori = value
    @price.deleter
    def price(self):
        del self.ori
heh1 = new()
print(heh1.price)
heh1.price = 1001
print(heh1.price)
del heh1.price"""

class ui:

    def get_bar(self):
        return 'laowang'
    Bar = property(get_bar, doc='Hello thiasd')
obj = ui()
result = obj.Bar.__doc__



from pathlib import Path as path
deee = path(r"/新时代新青年/杂项/DB_Gui.py")
#print(path.cwd(), path.home(), path.stat(deee))



class ConnectMysql:
    def __init__(self, host='localhost', port=3306, user='root', passwd='xingxing',
                db='test', filename: str = 'test.sql'):
        """
        :param host:
        :param port:
        :param user:
        :param passwd:
        :param db:
        :param filename:
        """
        self._host: str = host
        self._port: int = port
        self._user: str = user
        self._password: str = passwd
        self.database: str = db
        self._file_path = path(__file__).parent.joinpath(filename)

class ok:

    @property
    def change(self):
        print("Hello")

    def __enter__(self):
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        print(1)

import time
text = 'Hello World'
"""for i in range(len(text)):
    time.sleep(0.5)
    print("\r"+text[:len(text)-1-i], end='')"""


class ProgressBar:
    def __init__(self):
        self.whole_percent = 100
    def run(self, step, name='Progress'):
        mark = '#' * step
        for i in range(self.whole_percent//step + 1):
            time.sleep(0.2)
            print(f"\r{name} :|{mark*i}{' ' * (self.whole_percent-step*i)}|{i*step}/{self.whole_percent}", end='')

class ok:
    def __init__(self):
        self.value = 1
    def change(self):
        return self.value
    def increase(self, value1):
        self.value = value1
    def deel(self):
        del self.value
    bar = property(change, increase, deel, "Hello world!")

hu = ok()
#print(hu.bar)
hu.bar = 10
from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def run(self):
        pass
class Alipay(Payment):
    def run(self):
        print(1)
class jiehsao:
    def __new__(cls, *args, **kwargs):
        pass

    def __init__(self, a):
        self.name = a
    @staticmethod
    def run():
        print(1)
    @classmethod
    def run_1(cls):
        print(2)
je = jiehsao('as')
#print(je.__dict__, jiehsao.__dict__, je.__class__, sep='\n')
import json
person = {"name": '1', "age": 19, "tel": ["12121", "aa23132"]}
jsone = json.dumps(person)










import queue
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox, Querybox
import pyautogui
cache = None
que = queue.Queue()
que.maxsize = 1
def Mesaage():
    content = que.get()
    Messagebox.show_info(title='Yezi', message=content)

def auto():
    pyautogui.write("Hello world!", interval=0.3)
class Ui:

    db_config = {
        'host': 'localhost',
        'user': 'root',
        'passwd': 'xingxing',
        'port': 3306,
        'db': 'test'
    }
    def __init__(self, name, size: tuple = (400, 400), Is_center: bool = True):
        self.Create_version()
        self.root = ttk.Window(themename="darkly", title=name, size=size)
        self.center = Is_center
        self.admin = ttk.StringVar(value='')
        self.password = ttk.StringVar(value='')
        self.Por_deal()
        self.Login()
        self.Update()
        #self.autoInput()
        h = threading.Thread(target=self.auto_prompt)
        h.daemon = True
        h.start()
        self.root.mainloop()

    def Por_deal(self):
        if self.center:
            self.root.place_window_center()

    def Login(self):
        def jiance():
            admin = self.admin.get()
            pwd = self.password.get()
            if admin and pwd:
                conn = pymysql.connect(**self.db_config)
                with conn.cursor() as cur:
                    try:
                        cur.execute("CREATE TABLE IF NOT EXISTS message(%s VARCHAR(12), %s VARCHAR(12))", ("admin", "password"))
                        conn.commit()
                    except:
                        conn.rollback()
                    #cur.execute("INSERT INTO message VALUES(%s, %s)", ("admin", "pwd"))
                    #conn.commit()
                    cur.execute("SELECT * FROM message")
                    data = cur.fetchall()
                    if data:
                        if (admin, pwd) in data:
                            Messagebox.show_info(title='Yezi', message="登录成功!")
                        else:
                            Messagebox.show_error(title="Yezi", message="登陆失败!")
                    else:
                        Messagebox.show_info(title='Yezi', message="请先注册!")
                conn.close()
            else:
                Messagebox.show_info(title="Yezi", message="Admin or password is empty!")
        def zhuce():
            def close():
                whether = Messagebox.yesnocancel(parent=new_root, title='Yezi', message='if close window?')
                if whether == "确认":
                    self.root.deiconify()
                    new_root.destroy()
            #self.root.state("iconic")
            def new_zhuce():
                a = admin.get()
                b = pwd.get()
                if a and b:
                    conn = pymysql.connect(**self.db_config)
                    with conn.cursor() as cur:
                        cur.execute("SELECT admin FROM message")
                        if (a, ) in cur.fetchall():
                            Messagebox.show_error(title='Yezi', message='The admin is exists!', parent=new_root)
                            conn.close()
                            return
                        else:
                            cur.execute("INSERT INTO message VALUES(%s, %s)", (a, b))
                            conn.commit()
                    conn.close()
                    Messagebox.show_info(title='Yezi', message='Welcome to Yezi!', parent=new_root)
                    new_root.destroy()
                    self.root.deiconify()
                else:
                    Messagebox.show_info(title="Yezi", message="Admin or password is empty!", parent=new_root)
            self.root.iconify()
            new_root = ttk.Toplevel(self.root, size=(300, 300))
            new_root.place_window_center()
            admin = ttk.StringVar(value='')
            pwd = ttk.StringVar(value='')
            label1 = ttk.Label(new_root, text='Admin:')
            label2 = ttk.Label(new_root, text='Password:')
            label1.place(x=10, y=20, width=80, height=40)
            label2.place(x=10, y=70, width=80, height=40)
            entry_1 = ttk.Entry(new_root, textvariable=admin)
            entry_2 = ttk.Entry(new_root, textvariable=pwd)
            entry_1.place(x=100, y=20, height=30, width=160)
            entry_2.place(x=100, y=80, height=30, width=160)
            button_1 = ttk.Button(new_root, text="Register", command=new_zhuce)
            button_1.place(x=110, y=160, width=90, height=40)
            new_root.protocol("WM_DELETE_WINDOW", close)

        self.label_admin = ttk.Label(self.root, text="Admin:", justify='right')
        self.label_pwd = ttk.Label(self.root, text="Password:", justify='right')
        self.entry_admin = ttk.Entry(self.root, textvariable=self.admin)
        self.entry_pwd = ttk.Entry(self.root, textvariable=self.password)
        self.label_admin.place(x=10, y=20, width=80, height=50)
        self.label_pwd.place(x=10, y=80, width=80, height=50)
        self.entry_admin.place(x=120, y=30, width=160, height=30)
        self.entry_pwd.place(x=120, y=90, width=160, height=30)
        self.button_Login = ttk.Button(self.root, text="Login", command=jiance)
        self.button_Login.place(x=100, y=180, width=80, height=40)
        self.button_Register = ttk.Button(self.root, text='Regis', command=zhuce)
        self.button_Register.place(x=210, y=180, width=80, height=40)

    def Update(self):
        self.la = ttk.Label(self.root, text=self.Get_version())
        self.la.place(x=300, y=360, width=80, height=40)

    def Create_version(self):
        conn = pymysql.connect(**self.db_config)
        with conn.cursor() as cur:
            try:
                cur.execute("CREATE TABLE IF NOT EXISTS versions(version_ye VARCHAR(10))")
                conn.commit()
            except:
                conn.rollback()
                return
            cur.execute("SELECT * FROM versions")
            if cur.fetchall():
                conn.close()
                return
            cur.execute("INSERT INTO versions VALUES(%s)", ('Yezi_1.0', ))
            conn.commit()
        conn.close()

    def Get_version(self):
        conn = pymysql.connect(**self.db_config)
        with conn.cursor() as cur:
            cur.execute("SELECT * FROM versions")
            data = cur.fetchall()
        conn.close()
        return data[0][0]

    def autoInput(self):
        self.entry_admin.focus()
        t = threading.Thread(target=auto)
        t.daemon = True
        t.start()

    def auto_prompt(self, interval=1):
        global cache
        other_cache = None
        conn = pymysql.connect(**Ui.db_config)
        with conn.cursor() as cur:
            while True:
                try:
                    cur.execute("CREATE TABLE IF NOT EXISTS xinxi (message VARCHAR(20))")
                    conn.commit()
                except:
                    conn.rollback()
                cur.execute("SELECT message FROM xinxi")
                data = cur.fetchall()[0][0]
                if not data:
                    time.sleep(interval)
                    continue
                if data != cache:
                    que.put(data)
                    self.root.after(0, Mesaage)
                    cache = data
                else:
                    time.sleep(2)
                    continue
                time.sleep(2)
        conn.close()

if __name__ == '__main__':
    Ui(name='Yezi')
