import functools
def myfunc(a, b=2):
    """
    My func !
    :param a:
    :param b:
    :return:
    """
    print(a, b)
    return
def show_detail(name, f, is_partial=False):
    """
    Show details of the func！
    :param name:
    :param f:
    :param is_partial:
    :return:
    """
    print(name)
    print("object:", f)
    if not is_partial:
        print("__name__", f.__name__)
    else:
        print(f.func(), f.keywords, f.args)
    return
#show_detail("myfunc", myfunc)
#myfunc("a,", 3)
def hehe(a, b=3):
    """
    This is the production of the func
    :param a:
    :param b:
    :return:
    """
    return

#p1 = functools.partial(myfunc, a="hee", b=1)
#show_detail("default a", p1, True)

p2 = functools.partial(hehe, b=2)
functools.WRAPPER_ASSIGNMENTS = ('__module__', '__qualname__', '__doc__', '__annotations__')
functools.update_wrapper(p2, hehe) #更新新函数的信息
#print(p1.args)

def hehee(func):
    @functools.wraps(func)  #保留被装饰函数的信息
    def decorate(*args, **kwargs):
        """WHew"""
        pass
    return decorate
@hehee
def my(a=1, b=2):
    """hehe"""
    myfunc(1, 2)
#print(my.__doc__, my.__name__)


import inspect
from pprint import pprint
@functools.total_ordering
class Myobject:
    def __init__(self, val):
        self.val = val
    def __eq__(self, other):
        print("Testing __eq__ %s %s" % (self.val, other.val))
        return self.val == other.val
    def __gt__(self, other):
        print("Testing __qt__ %s %s" % (self.val, other.val))
        return self.val > other.val
"""pprint(inspect.getmembers(Myobject, inspect.ismethod))
a = Myobject(1)
b = Myobject(2)
for ex in ["a<b", "a<=b", "a==b", "a>=b", "a>b"]:
    result = eval(ex)
    print(ex, result, sep=",")"""

from itertools import *
"""for i in chain([1, 2, 3], ["a", "b", "c"]):
    print(i)"""
for i in islice(count(), 4):
    #print(i)
    pass
#print(slice([1, 2, 3], 1))
r = islice(count(), 4)
i1, i2 = tee(r)
print(list(i1), list(i2))