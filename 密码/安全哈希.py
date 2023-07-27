import hashlib
data = "abc"
"""print(hashlib.md5("abc".encode()).hexdigest())
print(hashlib.sha512(data.encode()).hexdigest())
print(hashlib.sha256(data.encode()).hexdigest())"""

import sys
import os
"""filename = "凯撒.py"
if os.path.isfile(filename):
    with open(filename, "rb") as fp:
        contents = fp.read()
    print(hashlib.md5(contents).hexdigest())
else:
    print("No such file!")"""
"""from string import ascii_letters, digits
from itertools import permutations
from time import time
all_letters = ascii_letters+digits+",.;"
def decrypt(mad5):
    if len(mad5) != 32:
        print("error!")
        return
    mad5 = mad5.lower()
    for k in range(5, 10):
        for item in permutations(all_letters, k):
            item = "".join(item)
            print(".", end="")
            if hashlib.md5(item.encode()).hexdigest() == mad5:
                return item
mad = "e7d057704ea5206d8cb61280741238f5"
start = time()
result = decrypt(mad)
if result:
    print("\nsuccess:"+mad+">>>"+result)
print("time used:", time()-start"""
import psutil
import datetime
c = psutil.pids()
for k in c:
    h = psutil.Process(k)
    if h.name().startswith("QQ."):
        print(h.name())
        h.kill()