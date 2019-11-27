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
wordcloud.render_notebook()

# 进行词性分类
def speech_cut(speech):
    word_list =[]
    for word in word_dict_sort:
        words = pseg.cut(word[0])
        for w,flag in words:
            if flag == speech:
                word_list.append(word)
    return word_list

# 动词 V
verb_word = speech_cut('v')
wordcloud = WordCloud()
wordcloud.add("",verb_word[:100],word_size_range=[20,100],shape='circle')
wordcloud.render_notebook()

# 名词 n
verb_word = speech_cut('n')
wordcloud = WordCloud()
wordcloud.add("",verb_word[:100],word_size_range=[20,100],shape='circle')
wordcloud.render_notebook()


# 表情分析,爬下来的文本会有emoji，我们需要将其过滤掉
"""
具体的mysql的处理方式可以通过如下的链接查看
https://blog.csdn.net/weixin_42812527/article/details/81876713
有时需要过滤掉四字节以上的字符（表情），比如MySQL数据库5.5.3以下的版本text字段不支持四字节以上字符
"""

def get_emoji(content):
    pattern = re.compile(u"[\U00010000-\U0010ffff]")
    result = re.findall(pattern,content)
    return result

# apply的传参方法需要注意一下：
df['emojis_list'] = df['comment'].apply(get_emoji)
# 转变成列表(没有emoji就是空列表，有emoji就是emoji表情
# eg:[[], [], ['😭'], ['😘'], [], [], [], ['😍'], ['😭'], ['🌹', '🌹', '🌹', '🌹']]
emojis = df['emojis_list'].values.tolist()

# 这个地方妙用了sum的方法，给例表实现了降维，并且去掉了空列表[],本应该用join的方式来实现
# https://blog.csdn.net/BF02jgtRS00XKtCx/article/details/89484064可以大致参考这个博客进行查看
emojis_list = sum(emojis,[])

# 对列表的元素进行计数，并且生成字典
# eg: {'😭': 261, '😍': 83, '😃': 79, '😂': 69, '👍': 67}
counter = Counter(emojis_list)
# most_common([n]):http://www.pythoner.com/205.html
# 返回一个TopN列表。如果n没有被指定，则返回所有元素。当多个元素计数值相同时，排列是无确定顺序的。
y_emojis, x_counts = zip(*counter.most_common())
bar = Bar()
bar.add_xaxis(y_emojis[:20])
bar.add_yaxis("", x_counts[:20])
bar.render_notebook()
