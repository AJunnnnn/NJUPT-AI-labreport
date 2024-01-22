import os
from PIL import Image
import numpy as np
import cv2
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
def gif2png():
    path = "D:/QQ/1413679561/FileRecv/exp/exp/yale/train"
    savepath = "D:/QQ/1413679561/FileRecv/exp/exp/yale/train_png"

    testpath = "D:/QQ/1413679561/FileRecv/exp/exp/yale/eval"
    testsavepath = "D:/QQ/1413679561/FileRecv/exp/exp/yale/eval_png"

    filelist = os.listdir(path)
    for file in filelist:
        im = Image.open(os.path.join(path, file))
        filename = os.path.splitext(file)[0]
        im.save(os.path.join(savepath, filename + '.png'))

    filelist = os.listdir(testpath)
    for file in filelist:
        im = Image.open(os.path.join(testpath, file))
        filename = os.path.splitext(file)[0]
        im.save(os.path.join(testsavepath, filename + '.png'))


def data_process():
    folder_path = "D:/QQ/1413679561/FileRecv/exp/exp/yale/train_png"
    image_array_list = []

    for filename in os.listdir(folder_path):
        if filename.endswith(".png"):
            file_path = os.path.join(folder_path, filename)
            image = Image.open(file_path)
            image_array = np.array(image)
            image_array_list.append(image_array)


    images_np_array = np.array(image_array_list)
    # print(images_np_array.shape)
    # 每个人有7张图像，总共15个人
    num_images_per_person = 7
    num_people = 15
    label_np_array = np.array([i for i in range(1, num_people + 1) for _ in range(num_images_per_person)])

    # 计算平均脸
    average_face = np.mean(images_np_array, axis=0).astype(np.uint8)
    average_face_image = Image.fromarray(average_face)
    average_face_image.save("D:/QQ/1413679561/FileRecv/exp/exp/yale/average_face.png")

    return images_np_array, label_np_array, average_face


def load_test_images(test_folder_path):
    image_array_list = []
    image_label_list = []
    filename = os.listdir(test_folder_path)
    for file in filename:
        label = file[0:2]
        if '0' in label:
            label.rsplit('0')
        image_label_list.append(int(label))

    true_labels_np_array = np.array(image_label_list)
    for filename in os.listdir(test_folder_path):
        if filename.endswith(".png"):
            file_path = os.path.join(test_folder_path, filename)
            image = Image.open(file_path)
            image_array = np.array(image)
            image_array_list.append(image_array)

    test_images_np_array = np.array(image_array_list)
    return test_images_np_array, true_labels_np_array


def evaluate_model(recognizer, test_images_np_array, true_labels_np_array):
    correct_count = 0
    total_count = len(true_labels_np_array)

    for i in range(len(test_images_np_array)):
        label, confidence = recognizer.predict(test_images_np_array[i])
        if label == true_labels_np_array[i]:
            correct_count += 1

    accuracy = correct_count / total_count
    return accuracy


if __name__ == '__main__':
    gif2png()
    images_np_array, label_np_array, average_face = data_process()
    # print("数组维度:", images_np_array.shape)
    # print(images_np_array)

    # 显示生成的平均脸
    plt.imshow(average_face, cmap='gray')
    plt.title('平均脸')
    plt.axis('off')
    plt.show()

    # 准备验证集数据
    test_folder_path = "D:/QQ/1413679561/FileRecv/exp/exp/yale/eval_png"
    test_images_np_array, true_labels_np_array = load_test_images(test_folder_path)
    # print(len(true_labels_np_array))

    # 评估模型并记录准确率
    pca_dimensions = range(1, 200)
    accuracies = []

    for pca_dimension in pca_dimensions:
        i = 0;
        recognizer = cv2.face.EigenFaceRecognizer_create(num_components=pca_dimension)
        recognizer.train(images_np_array, label_np_array)

        accuracy = evaluate_model(recognizer, test_images_np_array, true_labels_np_array)
        accuracies.append(accuracy)
        i += 1

    # 绘制PCA维数与准确率的关系图
    plt.plot(pca_dimensions, accuracies)
    plt.title('PCA维数与准确率的关系')
    plt.xlabel('PCA维数')
    plt.ylabel('准确率')
    plt.show()
