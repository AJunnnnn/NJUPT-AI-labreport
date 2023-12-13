# -*- coding: gbk -*-

import jieba
import nltk
import re
from nltk.book import *
# ����ͣ�ô��б�
stop_words = []
path = 'E:/NLP/stopword.txt'
for line in open(path, encoding='utf8'):
    # print(line)
    line = line.strip()
    stop_words.append(line)
# ��������ͣ�ô�
added_stopword = ['������˵','�����','���ڷ���','��Ī','��ĿǰΪֹ','��Ȼ��','$']
stop_words.extend(added_stopword)
# ȥ�������Ķ���
with open(file=r'D:\QQ\1413679561\FileRecv\data\��ӹ-�����˲�.txt', mode='r', encoding="gbk") as f:
    content_list = f.readlines()
    content_list = content_list[52:]
    content_list = content_list[:-40]
with open(file='��ӹ-�����˲�1.txt',mode='w') as f:
    content_str = ''.join(content_list)
    f.write(content_str)
# ȥ��ͣ�ô�
result = []
chinese_result = []
with open(file='��ӹ-�����˲�1.txt', mode='r', encoding="gbk") as f:
    content = f.read()
    cleaned_data = ''.join(re.findall('[\u4e00-\u9fa5]', content))
    content_list = jieba.lcut(content, cut_all=False)
    chinese_content_list = jieba.lcut(cleaned_data, cut_all=False)
    for word in content_list:
        if word not in stop_words:
            result.append(word)
    for word in chinese_content_list:
        if word not in stop_words:
            chinese_result.append(word)
str = ''.join(result)
chinese_str = ''.join(chinese_result)

# wordlist = jieba.lcut(str)
# text = nltk.Text(wordlist)
# print(text)

# (2)
print(f'���ô�����{len(set(str))}')
print(f'ƽ��ÿ���ʵ�ʹ�ô���{len(str)/len(set(str))}')
# (3)
print(f'�Ƿ�һ�ε�ʹ�ô�����{str.count("�Ƿ�")}')
print(f'����һ�ε�ʹ�ô�����{str.count("����")}')
print(f'����һ�ε�ʹ�ô�����{str.count("����")}')
# (4)
fdist =FreqDist(str)
print(fdist.most_common(30))
# (5)
# print(content_str.split('��')[0:10])
tensentences = content_str.split('��')[0:10]
for sentence in tensentences:
    splited_sentence = jieba.lcut(sentence)
    print(splited_sentence)
# (6)
fdist = FreqDist(chinese_str)
print(fdist.most_common(30))