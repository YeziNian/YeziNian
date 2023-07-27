
import string

table = str.maketrans("1123", "abcd")
data = "The mam se we h112"
#print(data.translate(table))

#模板
meme = string.Template("${mark} ${missing}hello!")
dic = {"mark": "Jack"}
#print(meme.substitute(dic))

"""try:
    print(meme.substitute(dic))
except KeyError as fp:
    print("error", fp)"""
#print("safe_substitute", meme.safe_substitute(dic))
#高级模板
class Mytemplate(string.Template):
    delimiter = "%"
    idpattern = "[a-z]+_[a-z]+"
my = Mytemplate("%{de_a} %{me}")
aa = {"de_a": "cc", "me": "aa"}
#print(my.safe_substitute(aa))

shape = """            \$(?:
              (?P<escaped>\$)  |   # Escape sequence of two delimiters     转义界定符
              (?P<named>(?a:[_a-z][_a-z0-9]*))       |   # delimiter and a Python identifier   命名变量
              {(?P<braced>(?a:[_a-z][_a-z0-9]*))} |   # delimiter and a braced identifier   大括号括住的变量
              (?P<invalid>)             # Other ill-formed delimiter exprs   不合法的定界符模式
            )"""
#print(meme.pattern.pattern)
class My(string.Template):
    delimiter = "{{"

#文本格式
import textwrap
dae = "sdasds wd wd asd sd asdw" \
      "asdasdasd" \
      "asdasdasd" \
      "sadsdsad" \
      "sdsd"
#print(textwrap.fill(dae, initial_indent="   ", subsequent_indent="", width=50))

#正则表达式
import re
pattern = "this"
#print(re.search(pattern, "this dog this").group())
pae = re.compile("this")
#print(pae.findall("this this this"))
for k in pae.finditer("this this this"):
    #print(k.group())
    pass
import numpy as np
from sklearn import svm

dee = {1: 2, 3: 4}
# def he(m):
    # if m > 1:
    #     return True    else:
    #     return False
#print(list(filter(he, [1, 2])))

from collections import Counter

de = Counter("aaa")
p = Counter("eaeaewddwddd")
#print(p.elements())
"""for m, n in p.most_common():
    print(m, n)
"""
c1 = Counter("aaabb")
c2 = Counter("abce")
"""print(c1-c2)
print(c1 & c2)  #取两个中小的值
"""


from collections import defaultdict
def fuc():
    return "False key"
name = defaultdict(fuc, foo="bar")
#print(name["f"])

import struct
import binascii
se = struct.Struct('I 2s f')
nanaa = (1, 'ac', 2.3)
#pee = se.pack(*nanaa)
#print(se.size)

import functools

def my(a, b=2):
    print(a, b)
def shouw(name, f, is_partial=False):
    if not is_partial:
        print(f.__name__)
    else:
        print(f.func, f.args, f.keywords)
"""shouw("my", my)
my("aa")"""
p1 = functools.partial(my, b=4)
shouw("partial", p1, True)
p1("passing a ")