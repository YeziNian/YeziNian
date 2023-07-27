import numpy as np

m = np.array([[1, 2], [1, 2], [1, 2]])
mytype = np.dtype([('name', np.str_, 50), ('age', np.int32)])
b = np.arange(24).reshape(2, 3, 4)
"""print(b[0, ...])
print(b.flatten())
b.shape = (2, 3, 4)
b.resize((2, 3, 4))
print(np.where(b>12))"""

def func(m):
    return eval(m.decode().split("-")[0])
c = np.loadtxt(r"C:\Users\40437\Desktop\ss.csv", delimiter=",", usecols=(0, ), converters={0: func})