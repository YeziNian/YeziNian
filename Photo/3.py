import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from skimage.feature import graycomatrix, graycoprops
from skimage import io
import numpy as np
import cv2
from PIL import Image
from scipy import ndimage

def Gray(name, method):
    """
    :param method: 0 为求各通道均值 1 为转为二位数组求
    :return:
    """
    if method == 0:
        #读取图像
        img = io.imread(name)
        step = 0
        contrast = 0
        energy = 0
        correlation = 0
        homogeneity = 0
        while step <= 2:
            img1 = img[:, :, step]
            # 计算灰度共生矩阵
            distances = [1]
            angles = [0, np.pi/4, np.pi/2, np.pi*3/4]
            GLCM = graycomatrix(img1, distances=distances, angles=angles, symmetric=True, normed=True)
            # 计算灰度共生矩阵的对比度、能量、相关性和均匀性特征
            contrast += graycoprops(GLCM, 'contrast')[0][0]
            energy += graycoprops(GLCM, 'energy')[0][0]
            correlation += graycoprops(GLCM, 'correlation')[0][0]
            homogeneity += graycoprops(GLCM, 'homogeneity')[0][0]
            step += 1
        # 输出特征
        return np.array([[contrast/3, energy/3, correlation/3, homogeneity/3]])
    elif method == 1:
        img = plt.imread(name)
        height, width, channels = img.shape
        gray_img = img.reshape(height * width, channels)
        img_int = gray_img.astype(np.uint8)
        distances = [1]
        angles = [0, np.pi / 4, np.pi / 2, np.pi * 3 / 4]
        GLCM = graycomatrix(img_int, distances=distances, angles=angles, symmetric=True, normed=True)
        # 计算灰度共生矩阵的对比度、能量、相关性和均匀性特征
        contrast = graycoprops(GLCM, 'contrast')[0][0]
        energy = graycoprops(GLCM, 'energy')[0][0]
        correlation = graycoprops(GLCM, 'correlation')[0][0]
        homogeneity = graycoprops(GLCM, 'homogeneity')[0][0]
    return np.array([[contrast, energy, correlation, homogeneity]])
i = 2
dae = Gray("1.jpg", 0)
while i <= 8:
    h = Gray(str(i)+".jpg", 0)
    dae = np.append(dae, h, axis=0)
    i += 1

ss = np.array([1, 1, 1, 1, 1, 0, 0, 0])

def Sift():
    img = io.imread('QQ截图20230506202835.jpg')
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    img_with_keypoints = cv2.drawKeypoints(img, keypoints, None)
    cv2.imshow('Image with keypoints', img_with_keypoints)
    cv2.waitKey(0)

def shehe():
    # 读取图像
    img = plt.imread('QQ截图20230506202835.jpg')

    # 将图像分为3个通道
    channel1 = img[:, :, 0]
    channel2 = img[:, :, 1]
    channel3 = img[:, :, 2]
    # 计算每个通道的颜色直方图
    hist1 = np.histogram(channel1.ravel(), 256, [0, 256])[0]
    hist2 = np.histogram(channel2.ravel(), 256, [0, 256])[0]
    hist3 = np.histogram(channel3.ravel(), 256, [0, 256])[0]
    # 合并三个直方图
    ccv = np.concatenate((hist1, hist2, hist3), axis=None)
    # 归一化，所有特征值除以总数
    ccv = ccv / np.sum(ccv)
    # 显示特征向量
    print(ccv)
# 加载Iris数据集
iris = load_iris()
X = iris.data
y = iris.target

# 将数据集分割成训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 训练SVM分类器
clf = svm.SVC(kernel='linear', C=1.0)
clf.fit(dae, ss)

# 预测测试集
y_pred = clf.predict(Gray("4.jpg", 0))
print(y_pred)
# 计算分类器模型的准确性，并输出
accuracy = accuracy_score(np.array([0]), y_pred)
print(accuracy)