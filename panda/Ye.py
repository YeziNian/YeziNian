import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data = pd.DataFrame(np.zeros(100).reshape(20, 5), columns=list("ABCDE"))
import os
"""data.plot(kind="scatter", x="A", y="B", alpha=0.1)
plt.show()
"""

p = np.zeros(10)
#print(list(map(lambda x: np.random.randint(0, 9), p)))

def create():

    a = 1
    if a <= 10:
        yield a
        a += 1
#print(np.linspace(0, 10, 3))  #生成等差数列
#print(np.array(create()))
#print(np.ones((1, 1)))
#(np.eye(4))
#print(np.identity(2))

date = np.array([1, 2, 3])
#print(data.transpose())  #转置#


#print(np.dot(date, date))
#向量内积  二维与一维 每行  一维和二维 按列
#c = np.random.randint(0, 2, 5)
#print(date[c])  #同时访问多个值
"""print(np.round(np.random.rand(10), 3))
print(np.floor([1.2, 2.3]), np.ceil([2.2, 3.01]))  #向下取整 向上取整
print(np.sum(date, axis=0)) #纵向求和 同理 mean
print(np.average(np.array([1, 2]), weights=[1, 2]))"""
new = np.random.randint(0, 10, size=(3, 3))
"""print(new>2)
print(new[new>2])  #a[a==b] """


a = np.arange(0, 20, 4).reshape(-1, 1) #列向量
b = np.arange(1, 7)
"""print(a+b)  #广播

print(np.where(date<2, 0, 1))
print(np.piecewise(date, [date>1, date<1], [lambda x: x+2, lambda x: x*2]))

c = np.matrix([[1, 2, 3], [2, 3, 4,], [7, 8, 9]])
print(c.diagonal())"""

"""d = np.array([[1, 2, 3]])
e = np.random.randint(0, 9, size=(3, 1))
print(d*e)
print(np.matrix(d)*np.matrix(e))
"""

from scipy import constants as o
from scipy import special
from scipy import signal

x = pd.Series([1, 2, 3, np.NAN])
#print(x)
datae = pd.date_range(start="20230101", end="20231231", freq="M")
#print(datae)

#在-1.96～+1.96范围内曲线下的面积等于0.9500(即取值在这个范围的概率为95%)，在-2.58～+2.58范围内曲线下面积为0.9900(即取值在这个范围的概率为99%)。
#rand 则[0, 1)
df = pd.DataFrame(np.random.randn(12, 4), index=datae, columns=list("ABCD"))
#print(df.iloc[1, :])
# df.head  df.tail

#print(df.describe()
#print(df.sort_values(by="A", ascending=False))  #返回一个新结构

#corr = df.corr()
#print(corr["A"].sort_values(ascending=False)) #计算相关性

#print(df[:2])
#print(df.loc[["2023-12-31"], :])
#(df.at["2023-12-31", "A"])  查看指定行 列的数据值
df.iat[0, 2] = 1 #修改数据

#缺失值处理
df1 = df.reindex(index=["zhang", "li", "zhou", "wang"], columns=list(df.columns)+["G"])  #必须加list  否则在后面添上G
df1.iat[0, 4] = 3
#print(pd.isnull(df1)) #返回新结构
#print(df1.dropna(axis=1)) #返回不包含缺失值的行
df1["G"].fillna(5, inplace=True)
#print(df1["G"].value_counts())
df2 = pd.DataFrame(np.random.randn(10, 4))
p1 = df2[:3]
p2 = df2[3:7]
p3 = df2[7:]
df3 = pd.concat([p1, p2, p3])
#print(df2 == df3)
#print(df3)
#print(df3.groupby(0).sum())

"""pe = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"]).cumsum() # ?????
pe["A"] = pd.Series(list(range(len(pe))))
#pe.plot(kind="scatter", x="A", y="B", alpha=0.1) #绘制的是散点图，不是曲线
pe.plot(x="A")
plt.show()"""
"""#柱状图
le = pd.DataFrame(np.random.randn(10, 4), columns=list("abcd"))
le.plot(kind="bar", stacked=True)
plt.show()"""
"""pe = pd.DataFrame(np.random.randn(1000, 2), columns=["B", "C"])
pe.to_csv("data.csv", sep=",", na_rep="NA", float_format='%.2f', columns=list(pe.columns), index=0) #no_rep 替换空值 保存两位小鼠 header=0不保存列名, columns保存列数据
dataee = pd.read_csv("data.csv")"""
#print(os.getcwd())



import os
print(os.listdir())