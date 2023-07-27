"""import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import numpy as np
# 准备数据
x = [1, 2, 3, 4, 5]
y = [6, 7, 8, 9, 10]
z = [11, 12, 13, 14, 15]

# 创建子图和三维坐标轴
fig = plt.figure()
ax = fig.add_subplot(projection='3d')

# 绘制散点图
ax.plot(np.linspace(0, 4, 100), np.linspace(0, 4, 100), np.linspace(0, 4, 100)**2)
ax.scatter(x, y, z)

# 添加轴标签
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')

plt.show()"""
"""import pymysql
db_config = {
    'host': 'localhost',
    'user': 'root',
    'passwd': 'xingxing',
    'port': 3306,
    'db': 'test'
}
conn = pymysql.connect(**db_config)
cur = conn.cursor()
cur.execute("SELECT * FROM new")
#print(cur.fetchmany(4))
cur.close()
conn.close()"""
class My:
    def __init__(self):
        pass
    def __enter__(self):
        print(2)
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(1)
de = My()
with My() as p:
    pass