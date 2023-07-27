import numpy as np
import matplotlib.pyplot as plt
shape = ["房产", "婚姻", "年龄", "贷款"]
la = []
with open("data1.txt", "r") as fp:
    data = fp.readline().split()
    while data:
        die = dict.fromkeys(shape)
        for m, n in zip(die.keys(), data):
            die[m] = eval(n)
        data = fp.readline().split()
        la.append(die)

def Yu(da):
    # 年龄作为最优切分变量
    age = []
    for k in da:
        age.append(k[shape[2]])
    lenth = len(age)
    i = 1
    You = []
    while i <= lenth - 1:
        first = age[0:i]
        end = age[i:]
        first_ave = sum(first)/len(first)
        end_ave = sum(end)/len(end)
        total = sum([(m - first_ave) ** 2 for m in first]) + sum([(m - end_ave) ** 2 for m in end])
        You.append(total)
        i += 1
    return min(You)

def Gini(date):

    #房产
    Gi_home = [1 for m in date if m[shape[0]] == 1]
    Gi_home_T = 1 - 1