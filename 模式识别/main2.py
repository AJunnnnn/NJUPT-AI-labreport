import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn import datasets

# 加载MNIST数据集
mnist = datasets.fetch_openml('mnist_784',parser='auto',data_home='local_directory')
X = np.array(mnist.data.astype('float32'))
y = np.array(mnist.target.astype('int'))

# 将像素值缩放到 [0, 1] 范围
X /= 255.0

# 划分数据集为训练集和测试集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 初始化SVM分类器
classifier = SVC()

# 训练分类器
classifier.fit(X_train, y_train)

# 在测试集上进行预测
accuracy = classifier.score(X_test, y_test)
print(f"Accuracy: {accuracy}")

# 绘制训练样本数量与分类器识别精度的关系曲线图
train_sizes = [100, 500, 1000, 3000, 5000, 10000, 20000]
accuracies = []

for size in train_sizes:
    X_subset, _, y_subset, _ = train_test_split(X_train, y_train, train_size=size, random_state=42)
    classifier.fit(X_subset, y_subset)
    accuracy_subset = classifier.score(X_test, y_test)
    accuracies.append(accuracy_subset)

# 绘制曲线图
plt.plot(train_sizes, accuracies, marker='o')
plt.title('Training Sample Size vs Accuracy (SVM)')
plt.xlabel('Training Sample Size')
plt.ylabel('Accuracy')
plt.show()
