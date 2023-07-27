import threading
import random
import time

cond = threading.Condition()
lise = [i for i in range(1, 11)]
class My(threading.Thread):
    i = 0
    def __init__(self, threadname, filename=0):
        threading.Thread.__init__(self, name=threadname)
        self.filename = filename

    def run(self):
        #print(f"This process is {self.name}.", end=" ")
        with cond:
            self.p = random.randint(1, 10)
            My.i += 1
            if self.p <= 4:
                cond.wait()
                print(f"sorry,process {self.name} is exist now, {self.p}<=4，已经跳过！")
            else:
                print(f"process {self.name} "+str(self.p))
                #cond.notify()
e = []
for k in range(1, 10):
    e.append(My("t" + str(k)))

for m in e:
    m.start()
cond.acquire()
cond.notify_all()
print(threading.enumerate())
cond.release()

