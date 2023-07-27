import numpy as np
import pandas as pd
import random
"""path = r"D:\Project\Practice\porject\housing.csv"
housing = pd.read_csv(path)

data = pd.DataFrame(np.arange(25).reshape(5, 5), columns=list("ABCDE"))
print(data)"""
from sklearn.cluster import KMeans
#rt cv2 as cv
"""small = cv.imread("0.jpg")
sift = cv.SIFT_create()"""
# 用SIFT算法在图像中检测关键点及其描述符
#keypoints, descriptors = sift.detectAndCompute(small, None)
#print(descriptors)
"""# 假设我们需要转换为100维特征向量
#de = np.asarray(descriptors)
kmeans = KMeans(n_clusters=100, random_state=42)
kmeans.fit(descriptors)

# 从kmeans中获取聚类中心
centroids = kmeans.cluster_centers_

# 获取每个特征向量到聚类中心的距离，即特征向量对应的最近邻聚类中心的下标
labels = kmeans.predict(descriptors)

# 统计每个聚类出现次数，并将其归一化为概率
hist, _ = np.histogram(labels, bins=range(101))
hist = hist.astype(float) / np.sum(hist)

# 将归一化后的聚类出现次数作为代表性数字
representative_num = hist
print(representative_num)
"""
from PIL import Image
import matplotlib.pyplot as plt

# 打开图片
image_path = "0.jpg"
image = Image.open(image_path)

# 获取直方图数据
histogram_data = image.histogram()

# 将直方图数据分成三个通道：红，绿，蓝
r = histogram_data[0:256]
g = histogram_data[256:512]
b = histogram_data[512:768]
data = np.concatenate((r, g, b)).reshape((1, -1))

# 绘制直方图
from skimage.feature import local_binary_pattern
from skimage.io import imread_collection
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# 读取数据集图片
data_path = '0.jpg'# 修改为你的数据集路径
image_collection = imread_collection(data_path)

# 为每张图片生成LBP特征
lbp_data = []
for i, image in enumerate(image_collection):
    # 生成LBP特征
    lbp_features = local_binary_pattern(image[:, :, 1], 8, 1, 'uniform').ravel()
    lbp_data.append(lbp_features)
print(len(lbp_features))

