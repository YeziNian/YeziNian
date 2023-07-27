from string import ascii_uppercase as uppercase
from itertools import cycle

table = dict()
for ch in uppercase:
    index = uppercase.index(ch)
    table[ch] = uppercase[index:] + uppercase[:index]
deTable = {"A":"A"}
start = "Z"
for ch in uppercase[1:]:
    index = uppercase.index(ch)
    deTable[ch] = chr(ord(start)+1-index)
