import threading
import time
import random
import matplotlib.pyplot as plt
import numpy as np
lie = [k for k in range(30)]
lock = threading.Lock()
Dad_data = []
Son_data = []
def Dad():
    lock.acquire()
    rand = random.randint(0, 29)
    Fruit = lie[rand]
    if Fruit in Son_data:
        print("Sorry, 你抢到了{Fruit}，但是你没抢过儿子!")
        lock.release()
        return
    Dad_data.append(Fruit)
    print(f"Dad抢到了{Fruit}.")
    lock.release()

def Son():
    lock.acquire()
    rand = random.randint(0, 2)
    Fruit = lie[rand]
    if Fruit in Dad_data:
        print(f"Sorry, 你抢到了{Fruit},但是你没抢过父亲!")
        lock.release()
        return
    Son_data.append(Fruit)
    print(f"Son抢到了{Fruit}.")
    lock.release()

lock1 = threading.Lock()
lock2 = threading.Lock()

"""Input = input("> the admin:")
Output = input("> the pwd:")
"""
def First(admin, pwd):
    tie = time.time()
    print(time.time())
    if admin == "admin" and pwd == "123":
        print(time.time())
        print("Yes,耗时", round(time.time()-tie, 10))

def Second(admin):
    if admin == "admin":
        pass
def Third(pwd):
    if pwd == "123":
        pass

"""a = threading.Thread(target=Second, args=("admin", ))
b = threading.Thread(target=Third, args=("123", ))
ti = time.time()
a.start()
b.start()
ie = time.time()-ti
First("admin", "123")
print("The time is :", ie)
"""
class Circle:
    i = 0
    def __init__(self, lis):
        self.lie = lis

    def __iter__(self):
        return self

    def __call__(self, *args, **kwargs):
        Circle.i += 1

    def __next__(self):
        if len(self.lie) == 0:
            print("Sorry, No data exists!")
        else:
            if Circle.i % len(self.lie) <= len(self.lie) - 1:
                return self.lie[Circle.i % len(self.lie)]
            else:
                raise StopIteration

"""data = np.arange(0., 4.2, 0.01)
func1 = lambda x: (1-(abs(x)-1)**2)**0.5
func2 = lambda x: -2*(1-abs(x)*0.5)**0.5
plt.plot(data, np.array(list(map(lambda x: func1(x-2), data))))
plt.plot(data, np.array(list(map(lambda x: func2(x-2), data))))
plt.show()

"""


cond = threading.Condition()

def ye():
    with cond:
        while True:
            try:
                print(zi.pop(0))
                cond.notify()
                cond.wait()
            except IndexError:
                print("zi NO data")
                break
            cond.acquire()
li = [1, 3, 5, 7, 9]
zi = [2, 4, 6, 8, 10]
def he():
    with cond:
        while True:
            try:
                print(li.pop(0))
                cond.wait()
                cond.notify()
            except IndexError:
                print("li No data")
                break

"""b = threading.Thread(target=he)
c = threading.Thread(target=ye)
b.start()
c.start()"""


myevent = threading.Event()

class event(threading.Thread):

    def __init__(self, threadname):
        threading.Thread.__init__(self, name=threadname)
    def run(self):
        global myevent
        if myevent.is_set():
            myevent.clear()
            myevent.wait()
            print(self.name+'set')
        else:
            print(self.name+"not set")
            myevent.set()
"""myevent.set()
for i in range(10):
    ee = event(f"第{i}次:")
    ee.start()"""


class heh(threading.Thread):

    def __init__(self, threadname, be, tie):
        threading.Thread.__init__(self, name=threadname, daemon=be)
        self.ti = tie

    def run(self):
        time.sleep(self.ti)
        for i in range(5):
            print(i)

io = heh("t1", True, 2)
ie = heh("t2", False, 1)
io.start()
ie.start()
time.sleep(4)

if __name__ == "__main__":

    #for i in range(10):
        #ti = threading.Thread(target=Dad)
        #t2 = threading.Thread(target=Son)
        #ti.start()
        #t2.start()
    pass