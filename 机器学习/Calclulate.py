import numpy as np
import random
import re
import threading
pattern = r"[+*/-]"
pattern1 = r"([xX])(\d+)"

#秀实函数

class calculate:

    def __init__(self, eps):
        self.eps = eps

    def Trans(self):
        self.orignal = re.split(pattern, self.eps)
        #检查序列
        self.Xulie = []
        self.Xulie.append("-" if self.eps[0] == "-" else "+")
        for m in self.eps:
            if m == "+" or m == "-":
                self.Xulie.append(m)
        #计算最大元
        self.max = 0
        self.dic = []
        for m in self.orignal:
            for c in re.finditer(pattern1, m):
                self.max = self.max if int(c.group(2)) <= self.max else int(c.group(2))
        self.Ju = np.eye(self.max) * 0
        self.step = 0
        for m in self.orignal:
            self.sho = []
            for c in re.finditer(pattern1, m):
                if c.group(1) == 'X':
                    self.rod = m[:-2]
                    if self.rod:
                        self.Ju[0, int(c.group(2))-1] = int(self.rod) if self.Xulie[self.step] == "+" else -int(self.rod)
                        continue
                    else:
                        self.Ju[0, int(c.group(2)) - 1] = 1 if self.Xulie[self.step] == "+" else -1
                        continue
                if c.group(1) == "x":
                    self.sho.append(int(c.group(2)))
            if self.sho:
                self.mood = m[:-4]
                if self.mood:
                    self.Ju[self.sho[1]-1, self.sho[0]-1] = int(self.mood) if self.Xulie[self.step] == "+" else -int(self.mood)
                else:
                    self.Ju[self.sho[1]-1, self.sho[0]-1] = 1 if self.Xulie[self.step] == "+" else -1
            self.step += 1
        return self.Ju

    def Positive(self):

        self.me = calculate.Trans(self)
        self.positive = np.eye(self.max) * 0
        self.e = 0
        #对角线
        for k in self.me[0, :]:
            self.positive[self.e, self.e] = k
            self.e += 1
        #稀疏
        self.m, self.n = 1, 0
        while self.m <= self.max-1:
            self.n = 0
            for k in self.me[self.m, :]:
                if self.m == self.n:
                    continue
                else:
                    self.positive[self.m, self.n] = k / 2
                    self.positive[self.n, self.m] = k / 2
                    self.n += 1
            self.m += 1
        return self.positive


    def __call__(self, *args, **kwargs):

        for k in args:
            pass




    def Is_positive(self, pos):
        self.result = 0
        self.q = 0
        self.pos = pos
        self.row, self.col = self.pos.shape
        if self.row == 2:
            self.fli = self.pos.flat
            return self.fli[0]*self.fli[3]-self.fli[1]*self.fli[2]
        else:
            while self.q <= self.col-1:
                self.dicee = []
                self.Poss = np.split(self.pos[1:, :], self.col, axis=1)
                self.time = 0
                for k in self.Poss:
                    if self.time == self.q:
                        self.time += 1
                        continue
                    self.dicee.append(k)
                    self.time += 1
                #print(self.dicee)
                self.poss = np.hstack(self.dicee)
                print(self.poss)
                if self.q % 2 == 0:
                    self.result += self.pos[0, self.q]*calculate.Is_positive(self, self.poss)
                else:
                    self.result -= self.pos[0, self.q] * calculate.Is_positive(self, self.poss)
                self.q += 1
        return self.result




