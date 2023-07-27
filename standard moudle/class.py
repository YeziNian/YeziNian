

class A:
    def __init__(self):
        print("This is class A!")
        print("Jack!")
    def run(self):
        a = 1
class C:
    def __init__(self):
        print("This is class C!")
        print("Lucy!")

class B(A):

    def __init__(self):
        super().__init__()
        print("B")
    def run(self):
        pass
#e = B()
#e.run()
index = 0


import struct
de = struct.pack(">I", 123)
print(struct.unpack(">I", de))
