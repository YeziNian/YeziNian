from skimage import io, data, exposure
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
import numpy as np
coffee = data.coffee()
font = FontProperties(fname=r"C:\windows\fonts\simsun.ttc", size=12)
"""a = 200
b = 50
d = 0
for i in range(100, 250):
    for m in range(20, 100):
        d = max(abs(i-a), abs(m-b)) #D8距离 正方形
        #d = abs(i-a) + abs(m-b)  D4距离 菱形
        if d <= 20:
            coffee[i, m, :] = (255, 255, 255)
"""
def change(data, a):
    da = np.zeros(shape=data.shape, dtype="uint8")
    for i in range(data.shape[0]):
        for m in range(data.shape[1]):
            for k in range(data.shape[2]):
                if data[i, m, k]*a >= 255:
                    da[i, m, k] = 255
                elif data[i, m, k]*a < 0:
                    da[i, m, k] = 0
                else:
                    da[i, m, k] = data[i, m, k]*a
    return da
d = change(coffee, 1.2)
plt.figure()
plt.subplot(221)
plt.imshow(coffee[:, :, 0])
plt.subplot(222)
img = exposure.adjust_gamma(coffee, 0.2)
ee = exposure.equalize_hist(coffee)
plt.imshow(ee)
plt.subplot(223)
img1 = exposure.adjust_gamma(coffee, 1.7)
plt.hist(coffee.flatten(), bins=256, edgecolor='None', facecolor='red')
plt.subplot(224)
plt.hist(ee.flatten(), bins=256, edgecolor='None', facecolor='red')
plt.show()
#hie = exposure.histogram(coffee[:, :, 0], nbins=256)
