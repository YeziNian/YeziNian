import datetime
import threading
import numpy as np
import pandas as pd
import time
from sklearn import linear_model
"""def heh():
    while True:
        now = datetime.datetime.now()
        s = str(now.year) + "-" + str(now.month) + "-" + str(now.day) + " "
        s += str(now.hour) + ":" + str(now.minute) + ":" + str(now.second)
        print(s)
        time.sleep(1)
ma = threading.Thread(target=heh)
#ma.daemon = True
ma.start()
"""
import threading


def thread1(cond):
    print('Thread 1 is waiting for Thread 2 to notify...')
    with cond:
        cond.wait()
    print('Thread 1 resumed and acquired lock again.')
    with cond:
        print('Thread 1 is notifying Thread 2.')
        cond.notify()


def thread2(cond):
    print('Thread 2 is starting and sleeping for a while...')
    time.sleep(1)
    with cond:
        print('Thread 2 acquired lock.')
        cond.notify()
    time.sleep(1)
    print('Thread 2 released the lock.')


import multiprocessing

def worker(data):
    data.append(multiprocessing.current_process().name)
    print(data)

if __name__ == '__main__':
    # 创建一个 Manager 对象
    m = multiprocessing.Manager()

    # 使用 Manager 对象创建一个共享列表
    data = m.list([1, 2, 3, 4, 5])

    # 使用进程池共享列表
    with multiprocessing.Pool(processes=2) as pool:
       a = pool.map(worker, [data, data])
       print(a)

