import jieba
import jieba.posseg as pseg # 统计词性
import pandas as pd
import re
from collections import Counter # 用于字典类型的计数

# 生成echarts类库表的调用
from pyecharts.globals import SymbolType
from pyecharts.charts import Bar,WordCloud

# 读取下载好的文件
df = pd.read_csv("Jay_comment_data.csv")
# 将评论这一列提取出来并且转换成列表,\
# 这里需要注意的是df[].values是ndarray的格式，还需要添加tolist()的方法
comment_list = df['comment'].values.tolist()

# 创建字典，拆词计数
word_dict = {}

for line in comment_list:
    words = jieba.cut(line) #这里的word是迭代器
    for word in words:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1

# 处理分词
stop_word = pd.read_csv("Chinese_Stopwords.txt",encoding='utf-8',header = None)
# 因为是pandas读取，帮其更新相应的列名
stop_word.columns = ['word']
stop_word = [' '] +list(stop_word['word'])

# 将常用的“废词”去掉
for i in range(len(stop_word)):
    if stop_word[i] in word_dict:
        word_dict.pop(stop_word[i])

# 按照词频出现的次数进行排序,sorted要传入一个可迭代的对象，所以使用word_dict.items()构建列表
word_dict_sort = sorted(word_dict.items(),key = lambda x:x[1],reverse=True )

# 取前100的词频
word = word_dict_sort[:100]

# 制作词云图
wordcloud = WordCloud()
# 添加注释 
wordcloud.add("Jay",words,word_size_range=[20,100],shape='circle')



