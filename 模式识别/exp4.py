from PIL import Image
import cv2
import numpy as np
import os
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']

def load_images(directory):
    images = []
    for filename in os.listdir(directory):
        if filename.endswith(".jpg"):
            img_path = os.path.join(directory, filename)

            # 使用PIL库读取图片
            img = Image.open(img_path)

            # 将图片转换为NumPy数组
            img_array = np.array(img)

            images.append(img_array)
    return images


def kmeans_segmentation(image, k):
    # 将图像重新形状为像素的2D数组
    pixels = image.reshape((-1, 3))

    # 转换为float32类型
    pixels = np.float32(pixels)

    # 定义标准并应用K均值算法
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, labels, centers = cv2.kmeans(pixels, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # 转换回8位值
    centers = np.uint8(centers)

    # 将标签映射到中心
    segmented_image = centers[labels.flatten()]

    # 将图像重新形状为原始图像的形状
    segmented_image = segmented_image.reshape(image.shape)

    return segmented_image


def visualize_segmentation(original, k_values, segmented_images):
    num_k_values = len(k_values)

    # 创建子图
    fig, axes = plt.subplots(1, num_k_values + 1, figsize=(15, 5))

    # 在第一个子图上显示原始图像
    axes[0].imshow(original)
    axes[0].set_title('原始图像')

    # 在每个后续子图上显示分割图像和对应的K值
    for i in range(num_k_values):
        axes[i + 1].imshow(segmented_images[i])
        axes[i + 1].set_title(f'分割 (K={k_values[i]})')

    plt.show()


def main():
    image_directory = r'D:\QQ\1413679561\FileRecv\exp\exp\VOCdevkit\VOC2012\JPEGImages'
    k_values = [2, 4, 8, 16, 32]  # 你可以调整K的值进行实验

    images = load_images(image_directory)

    for image in images:
        segmented_images = [kmeans_segmentation(image, k) for k in k_values]
        visualize_segmentation(image, k_values, segmented_images)


if __name__ == "__main__":
    main()
