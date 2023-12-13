# -*- coding: gbk -*-

import jieba
import nltk
import re
from nltk.book import *
from nltk.corpus import PlaintextCorpusReader
import matplotlib.pyplot as plt


corpus_root = 'D:/QQ/1413679561/FileRecv/data'
# file_pattern = r'.*\.txt'
corpus_reader = PlaintextCorpusReader(corpus_root, '.*')
file_list = corpus_reader.fileids()
print(file_list)

# ����ͣ�ô��б�
stop_words = []
path = 'E:/NLP/stopword.txt'
for line in open(path, encoding='utf8'):
    # print(line)
    line = line.strip()
    stop_words.append(line)


# ȥ��ͣ�ô�
result = []
with open(file=r'D:\QQ\1413679561\FileRecv\data\��ӹ-�������.txt', mode='r', encoding="gbk") as f:
    content = f.read()
    cleaned_data = ''.join(re.findall('[\u4e00-\u9fa5]', content))
    content_list = jieba.lcut(cleaned_data, cut_all=False)
    for word in content_list:
        if word not in stop_words:
            result.append(word)
text = ''.join(result)
# print(text)

with open(file='��ӹ-�������1.txt', mode='w') as f:
    f.write(text)

with open('��ӹ-�������1.txt', 'r', encoding='gbk') as f:
    str = f.read()
    # len(set(str))
    # len(str)/len(set(str))

# cleaned_data = ''.join(re.findall('[\u4e00-\u9fa5]', str))
wordlist = jieba.lcut(str)
text = nltk.Text(wordlist)
print(text)

# (1)
text.similar(word='��Ī��',num=10)
print('\n')
# (2)
text.concordance(word='��',width=30,lines=3)
print('\n')
# (3)
text.collocations()
print('\n')
# (4)
text.common_contexts(['���','С��Ů'])
print('\n')
# (5)
print(len(str))
print('\n')
# (6)
print(set(str))
print('\n')
# (7)
sorted(set(str))
print(f'�ʻ���С:{len(set(str))}')
print(f'ÿ����ƽ��ʹ�ô���:{len(str)/len(set(str))}')
print('\n')
# (8)
print('���һ�ʳ��ֵĴ�����', end='')
print(str.count('���'))
fdist = FreqDist(str)
print('����Ƶ����ߵģ�')
print(fdist.most_common(30))
# (9)
print(sorted(set(str)))
# (10)
plt.rcParams['font.sans-serif'] = 'SimHei'
words = ['С��Ů', '���', '����', '����']
nltk.draw.dispersion.dispersion_plot(text, words, title='�ʻ���ɢͼ')
# (11)
fig = plt.figure()
plt.grid()
fdist1 = dict(fdist)
fdist1 = sorted(fdist.items(), key= lambda x: x[1], reverse=True)
x = []
y = []
for i in range(10):
    x.append(fdist1[i][0])
    y.append(fdist1[i][1])
t = 0
for i in range(len(y)):
    y[i] = y[i] + t
    t = y[i]
plt.plot(x, y)
plt.title('���ô��ۼ�Ƶ��ͼ')
plt.ylabel('�ۼ�Ƶ��')
plt.xlabel('���ô�')
plt.show()