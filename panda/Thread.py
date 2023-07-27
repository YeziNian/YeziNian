import threading
import time
import queue
#print(threading.stack_size(33 * 1024))
#print(threading.active_count())
#print(threading.current_thread())
#print(threading.enumerate())
def demo(v):
    print(v)
"""t = threading.Timer(1, demo, args=(5, ))
t.start()"""
#print(threading.current_thread())
"""m = threading.Thread(target=demo, name="hehe", args=(2, ))
m.start()
time.sleep(2)
print(m.is_alive(), m.ident)"""
lock = threading.Lock()
class My(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
    def run(self):
        global x
        lock.acquire()
        x += 3
        print(x)
        time.sleep(1)
        lock.release()
"""
t1 = []
x = 0
t2 = My()
t3 = My()
t2.start()
t3.start()"""
"""for i in range(10):
    t = My()
    t1.append(t)
x = 0
for k in t1:
    k.start()
"""
import random
x = []
cond = threading.Condition()
class Produce(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
    def run(self):
        global x
        while True:
            cond.acquire()
            if len(x) == 10:
                print("Procuder is full..")
                cond.wait()
            else:
                print("Procuder:", end=" ")
                x.append(random.randint(1, 1000))
                print(x)
                time.sleep(1)
                cond.notify()
            cond.release()
class my(threading.Thread):
    def __init__(self, name):
        threading.Thread.__init__(self, name=name)
    def run(self):
        global x
        while True:
            cond.acquire()
            if not x:
                print("Consumer is waiting...")
                cond.wait()
            else:
                print(x.pop(0))
                print(x)
                time.sleep(2)
                cond.notify()
            cond.release()
"""p = Produce("Procuder")
C = my("Create")
p.start()
C.start()
p.join()
C.join()"""

class mee(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global que
        que.put(self.name)
        print(self.name, " put ", self.name, " to queue.")
class he(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global que
        print(self.name, " get ", que.get(), " from queue.")
que = queue.Queue()
plist = []
clist = []
"""for i in range(10):
    p = mee("Procuder"+str(i))
    plist.append(p)
    c=he("Concumer"+str(i))
    clist.append(c)
for p, c in zip(plist, clist):
    p.start()
    p.join()
    c.start()
    c.join()
"""
myevent = threading.Event()
class Ev(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global myevent
        if myevent.is_set():
            myevent.clear()
            myevent.wait()  #会一直等待，知道信号为真
            print(self.name+" set.")
        else:
            print(self.name+" not set.")
            myevent.set()
"""myevent.set()
for i in range(10):
    t = Ev(str(i))
    t.start()
"""
import multiprocessing
import os
from multiprocessing import Pool, Pipe, Value, Array, Manager
from statistics import mean
def f(name):
    print(__name__)
    print(os.getppid()) #父进程的id
    print(os.getpid())  #当前进程的id
    print(name)
def cv(x):
    return mean(x)
def foo(q):
    q.put("Hello Jack!")
hehe = multiprocessing.Queue()


def fe(conn):
    conn.send("Hello world!")
    conn.close()

def ne(n, a):
    n.value = 3.1415926
    for i in range(len(a)):
        a[i] = a[i] ** 2

def ee(d, l, t):
    d["name"] = "Dong fu"
    d["age"] = 38
    d["ses"] = "man"
    d["affiliation"] = "SDIBT"
    l.reverse()
    t.value = 3
de = {}
de[1] = 2
de[1] = 3
a = de.setdefault(3)
print(de, a)
if __name__ == "__main__":
    """    p = multiprocessing.Process(target=f, args=("bobs", ))
    p.start()
    p.join()"""
    """    x = [list(range(10)), list(range(20, 30)), list(range(40, 59)), list(range(70, 80))]
    with Pool(2) as fp:
        result = [fp.apply_async(cv, args=(i,)) for i in x]
        #print(fp.map(cv, x))  #返回一个列表
        final_result = [r.get() for r in result]
        print(result)
        print(final_result)"""
    #multiprocessing.set_start_method("spawn")  #unix为fork， 这样会导致子进程无法继承父进程的状态和变量
    #ctx = multiprocessing.get_context("spawn") #进程上下文
    #q = ctx.Queue()
    """    p = multiprocessing.Process(target=foo, args=(hehe, ))
    p.start()
    p.join()+6
    print(hehe.get())
    """
    """    parent, child = Pipe()
    p = multiprocessing.Process(target=fe, args=(child, ))
    p.start()
    p.join()
    print(parent.recv())
    parent.close()"""

    """    num = Value("d", 0.0)
    arr = Array("i", range(10))
    p = multiprocessing.Process(target=ne, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])"""

    """    with Manager() as manager:
        d = manager.dict()
        l = manager.list(range(10))
        t = manager.Value("i", 0)
        p = multiprocessing.Process(target=ee, args=(d, l, t))
        p.start()
        p.join()
        for item in d.items():
            print(item)
        print(l)
        print(t.value)
    """