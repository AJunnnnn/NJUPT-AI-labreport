import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_openml
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# 步骤2：导入必要的库

# 步骤3：加载数据集
mnist = fetch_openml('mnist_784', parser='auto', data_home='local_directory')
X, y = mnist.data.astype('float32') / 255.0, mnist.target.astype('int')

# 步骤4：拆分数据集
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 步骤5：训练贝叶斯分类器
clf = MultinomialNB()
clf.fit(X_train, y_train)

# 步骤6：调整训练样本数量并评估性能
train_sizes = [1000, 2000, 4000, 6000, 8000, 10000, 12000, 14000, 16000]
accuracies = []

for size in train_sizes:
    clf.partial_fit(X_train[:size], y_train[:size], classes=np.unique(y))

    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    accuracies.append(accuracy)

# 步骤7：绘制曲线图
plt.plot(train_sizes, accuracies, marker='o')
plt.title('Training Sample Size vs Accuracy')
plt.xlabel('Training Sample Size')
plt.ylabel('Accuracy')
plt.show()
