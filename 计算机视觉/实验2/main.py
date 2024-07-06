import cv2  # 导入 OpenCV库。
import numpy as np  # 导入 NumPy 库，用于高效的矩阵和数组操作。
import os  # 导入OS库，用于与操作系统交互。
import glob  # 导入 glob 库，用于文件路径名的模式匹配。

# 定义棋盘格的尺寸，这里是6x9。
CHECKERBOARD = (6, 9)
# 设置寻找角点的终止准则。
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# 创建列表以存储棋盘格的3D点。
objpoints = []
# 创建列表以存储棋盘格角点在图像中的2D点。
imgpoints = []
# 初始化3D点的坐标，这里仅初始化x和y，z设置为0。
objp = np.zeros((1, CHECKERBOARD[0] * CHECKERBOARD[1], 3), np.float32)
objp[0, :, :2] = np.mgrid[0:CHECKERBOARD[0], 0:CHECKERBOARD[1]].T.reshape(-1, 2)
prev_img_shape = None  # 初始化之前图像的尺寸。
# 使用glob模式匹配来获取所有棋盘格图片的路径。
# images = glob.glob('./images/IMG_20240402_160207.jpg')
# for fname in images:
img = cv2.imread('picture1.png')  # 读取每一张图片。
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # 将图片转换为灰度图，因为寻找角点在灰度图上进行。

# 寻找棋盘格角点。
ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD, cv2.CALIB_CB_ADAPTIVE_THRESH + cv2.CALIB_CB_FAST_CHECK + cv2.CALIB_CB_NORMALIZE_IMAGE)
# 如果找到足够数量的角点，则细化它们的位置并将它们添加到列表中。
if ret == True:
    objpoints.append(objp)
    corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
    imgpoints.append(corners2)

    # 将找到的角点绘制到图片上，以便可视化。
    img = cv2.drawChessboardCorners(img, CHECKERBOARD, corners2, ret)

cv2.imshow('img', img)  # 显示图片。
cv2.waitKey(0)  # 等待用户按键。

cv2.destroyAllWindows()  # 关闭所有OpenCV窗口。

h, w = img.shape[:2]  # 获取最后处理的图片的尺寸。

# 使用3D点和对应的2D图像点进行相机标定。
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None,
                                                   None)

# 打印相机标定的结果。
print("Camera matrix : \n")
print(mtx)  # 相机矩阵
print("dist : \n")
print(dist)  # 畸变系数
print("rvecs : \n")
print(rvecs)  # 旋转向量
print("tvecs : \n")
print(tvecs)  # 平移向量