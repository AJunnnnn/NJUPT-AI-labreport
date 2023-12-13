import jieba

stop_words = []
path = 'E:/NLP/stopword.txt'
for line in open(path, encoding='utf8'):
    # print(line)
    line = line.strip()
    stop_words.append(line)
# print(stop_words)

# 去除停用词
result = []
with open(file=r'D:\QQ\1413679561\FileRecv\data\金庸-天龙八部.txt', mode='r', encoding="gbk") as f:
    content = f.read()
    content_list = jieba.lcut(content, cut_all=False)
    for word in content_list:
        if word not in stop_words:
            result.append(word)
text = ''.join(result)
print(text)