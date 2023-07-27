from multiprocessing import Process
import os
import multiprocessing as mp
def f(name):
    print("Module name:", __name__)
    print("parent process:", os.getppid())
    print("process id:", os.getpid())
    print("hello,", name)

def foo(q):
    q.put("hello world")

def e(conn):
    conn.send("hello world")
    conn.close()


if __name__ == "__main__":
    """    p = Process(target=f, args=("bobs", ))
    p.start()
    p.join()"""
    """    mp.set_start_method("spawn")
    q = mp.Queue()
    print(q.get())
    p = Process(target=foo, args=(q, ))
    p.start()
    p.join()
    print(q.get())"""

    dad, son = mp.Pipe()
    p = Process(target=e, args=(son, ))
    p.start()
    p.join()
    print(dad.recv())
    dad.close()