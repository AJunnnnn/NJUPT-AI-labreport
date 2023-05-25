import numpy as np

a = np.random.randint(0, 10, (3, 3))
print(a)
print('和： ', np.sum(a))
print('积： ', np.product(a))
print('平均值: ', np.average(a))
print('最大值: ', np.max(a))
print('最小值: ', np.min(a))
print('方差: ', np.var(a))
print('标准差: ', np.std(a))
for i in range(0, 3):
    a[i, i] = 11
print('将对角线的元素替换11后的数组：\n', a)
