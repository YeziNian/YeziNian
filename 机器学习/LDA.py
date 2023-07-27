import numpy as np
import matplotlib.pyplot as plt
with open(r"C:\Users\40437\Desktop\xigua.txt", "r") as fp:
    data = fp.readline().split()
    lie = []
    label = []
    while data:
        lie.append(list(map(lambda x: eval(x), data[:2])))
        label.append(int(data[2]))
        data = fp.readline().split()
Posi = np.array([lie[m] for m, n in enumerate(label) if n == 1])
negi = np.array([lie[m] for m, n in enumerate(label) if n == 0])
u1 = [sum(Posi[:, 0])/len(Posi), sum(Posi[:, 1])/len(Posi)]
u2 = [sum(negi[:, 0])/len(negi), sum(negi[:, 1])/len(negi)]
S1 = np.matrix(np.eye(2)*0)
for k in Posi:
    c = np.matrix(k)-np.matrix(u1)
    S1 += c.T*c
S2 = np.matrix(np.eye(2)*0)
for k in negi:
    c = np.matrix(k)-np.matrix(u1)
    S2 += c.T*c
Sw = S1+S2
D = np.matrix(u1).T-np.matrix(u2).T
Sw_ni = np.linalg.inv(Sw)
W = Sw_ni*D
w, b = W.flat
colors = ['blue', 'red', 'green']



x_axis = np.linspace(4, 8, 100)
y_axis = np.linspace(2, 5, 100)
y_proj = w * x_axis + b * y_axis
proj_X = np.column_stack((x_axis, y_proj))
plt.plot(x_axis, y_proj, 'k--', linewidth=2)
plt.scatter(proj_X[:, 0], proj_X[:, 1], s=100, c='yellow', edgecolors='black', alpha=0.5)
plt.show()