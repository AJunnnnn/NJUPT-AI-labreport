from matplotlib import pyplot as plt
import numpy as np

import matplotlib as mpl

mpl.rcParams['font.family'] = 'sans-serif'
mpl.rcParams['font.sans-serif'] = [u'SimHei']

plt.figure(1)
data = [0.05, 0.10, 0.10, 0.65, 0.05, 0.05]
plt.pie(data, explode=[0, 0, 0, 0.2, 0, 0], labels=['娱乐', '育儿', '饮食', '房贷', '交通', '其他'], autopct='%.0f%%')
plt.show()

plt.figure(2)
rect = plt.bar((0,1,2,3,4,5),height = (0.05, 0.10, 0.10, 0.65, 0.05, 0.05),width=0.35, align='center',alpha = .5)
plt.bar_label(rect)
plt.xticks((0,1,2,3,4,5),(u'娱乐', u'育儿', u'饮食', u'房贷', u'交通', u'其他'))
plt.xlabel(u'类别')
plt.ylabel(u'占比')
plt.plot((0,1,2,3,4,5),data,color='red')
plt.show()
