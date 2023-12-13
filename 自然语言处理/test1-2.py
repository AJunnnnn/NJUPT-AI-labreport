# -*- coding: gbk -*-

import jieba
import nltk
import re
from nltk.book import *
# 加载停用词列表
stop_words = []
path = 'E:/NLP/stopword.txt'
for line in open(path, encoding='utf8'):
    # print(line)
    line = line.strip()
    stop_words.append(line)
# 增添特殊停用词
added_stopword = ['具体来说','再其次','分期分批','切莫','到目前为止','猛然间','$']
stop_words.extend(added_stopword)
# 去除非正文段落
with open(file=r'D:\QQ\1413679561\FileRecv\data\金庸-天龙八部.txt', mode='r', encoding="gbk") as f:
    content_list = f.readlines()
    content_list = content_list[52:]
    content_list = content_list[:-40]
with open(file='金庸-天龙八部1.txt',mode='w') as f:
    content_str = ''.join(content_list)
    f.write(content_str)
# 去除停用词
result = []
chinese_result = []
with open(file='金庸-天龙八部1.txt', mode='r', encoding="gbk") as f:
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
print(f'总用词量：{len(set(str))}')
print(f'平均每个词的使用次数{len(str)/len(set(str))}')
# (3)
print(f'乔峰一次的使用次数：{str.count("乔峰")}')
print(f'段誉一次的使用次数：{str.count("段誉")}')
print(f'虚竹一次的使用次数：{str.count("虚竹")}')
# (4)
fdist =FreqDist(str)
print(fdist.most_common(30))
# (5)
# print(content_str.split('。')[0:10])
tensentences = content_str.split('。')[0:10]
for sentence in tensentences:
    splited_sentence = jieba.lcut(sentence)
    print(splited_sentence)
# (6)
fdist = FreqDist(chinese_str)
print(fdist.most_common(30))