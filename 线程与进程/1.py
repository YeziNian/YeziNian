import threading
import time
import os
def rand(x):
    for i in range(x, 10):
        print(i)
    time.sleep(1)

X1 = threading.Thread(target=rand, args=(4, ))
X2 = threading.Thread(target=rand, args=(5, ))

class Mythread(threading.Thread):

    def __init__(self, num, threadname):
        threading.Thread.__init__(self, name=threadname)
        self.num = num

    def run(self):
        time.sleep(self.num)
        print(self.num)

"""t1 = Mythread(1, "t1")
t2 = Mythread(3, "t2")
t2.daemon = True
print(t1.daemon)
print(t2.daemon)
t1.start()
t2.start()

"""
def Write(filename, content):

    if not os.path.exists("data.txt"):
        with open(filename, "w") as fp:
            pass
    with open(filename, "a") as fp:
        fp.write(content)


class thread(threading.Thread):

    def __init__(self):
        threading.Thread.__init__(self)

    def run(self):

        global x
        #lock.acquire()
        x += 3
        print(x)
        #lock.release()

lock = threading.Lock()

"""t1e = []
for e in range(10):
    t = thread()
    t1e.append(t)
x = 0
for i in t1e:
    i.start()"""

def task():
    time.sleep(1)
    print("当前线程:", threading.current_thread().name)
lis = []
def Input(m):
    global lis
    lis.append(m)
    print(lis)

def get_value(index):

    lock.acquire()
    my_list = [1, 2, 3, 4]
    if index > 3:
        print("Wrong!")
        lock.release()
        return
    print(my_list[index])
    time.sleep(0.2)
    lock.release()

if __name__ == "__main__":

    #for _ in range(5):
        #sub = threading.Thread(target=task)
       # sub.start()

   """ t1111 = threading.Thread(target=Input, args=(1, ))
    t12 = threading.Thread(target=Input, args=(2, ))
    t1111.start()
    t12.start()"""
   for i in range(30):
        one = threading.Thread(target=get_value, args=(i, ))
        one.start()