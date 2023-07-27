import time

import numpy as np
import pandas as pd
import multiprocessing

from multiprocessing import Pool, Pipe, Value, Array, Manager
from statistics import mean
import os
#hhe = multiprocessing.Queue()

def hehe(i):
    return i.append(10)
"""lie = [[1, 2], [2, 3]]
with Pool(2) as fp:
    print(fp.map(hehe, lie))"""
event = multiprocessing.Event()

def send1(conn, messsage):
    global event
    #event.wait()
    event.set()
    if event.is_set():
        conn.send(messsage)
        conn.close()
if __name__ == '__main__':
    """    lie = [[1, 2], [2, 3]]
    with Pool(2) as fp:
        print(fp.map(hehe, lie))"""
    message = input("What do you wang to say>>")
    parent, chile = Pipe()
    m = multiprocessing.Process(target=send1, args=(chile, message))
    m.start()
    m.join()
    print(parent.recv())
    parent.close()