import numpy as np
import matplotlib
import matplotlib.pylab as plt
import cv2

matplotlib.use('TkAgg')
# Harris角点检测
img = plt.imread("123.jpg").copy()
img_ = img.copy()
gray = np.float32(cv2.cvtColor(img, cv2.COLOR_BGR2GRAY))
harris = cv2.cornerHarris(gray, 2, 3, 0.04)
harris = cv2.dilate(harris, None)  # 膨胀，方便显示
img[harris > 0.01 * harris.max()] = [255, 0, 0]

plt.subplot(1, 2, 1)
plt.axis("off")
plt.imshow(img_)
plt.subplot(1, 2, 2)
plt.axis("off")
plt.imshow(img)
plt.show()
# ORB特征点提取
img = plt.imread("1234.jpg").copy()

orb = cv2.ORB_create()  # 可以自定义很多参数
kp = orb.detect(img)  # 特征点

kp_img = cv2.drawKeypoints(img, keypoints=kp, outImage=None, color=300)

# 绘制
plt.subplot(1, 2, 1)
plt.axis("off")
plt.imshow(img)
plt.subplot(1, 2, 2)
plt.axis("off")
plt.imshow(kp_img)
plt.show()

# ORB特征点匹配
img1 = plt.imread("123.jpg").copy()
img2 = plt.imread("1234.jpg").copy()
orb = cv2.ORB_create()
# 特征点、描述子
kp1, des1 = orb.detectAndCompute(img1, None)
kp2, des2 = orb.detectAndCompute(img2, None)
# 匹配
match = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True).match(des1, des2)
match = sorted(match, key=lambda x: x.distance)
# 取最近的minN个绘制
minN = len(match)
# minN = 40
img3 = cv2.drawMatches(img1, kp1, img2, kp2, match[:minN], None)
plt.imshow(img3)
plt.show()
