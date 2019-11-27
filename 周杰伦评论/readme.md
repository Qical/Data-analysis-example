## 周杰伦的音乐评论分析

- 关于周杰伦的评论的分词和处理
- jay_data的数据代码全部在jay_data.py中，
- 局部的实现和展现放在jupyter中

- 涉及的知识点：jieba，tolist(),sorted(),列表的降维

```python 
# 涉及的模块
import jieba
from pyecharts.globals import SymbolType
from pyecharts.charts import Bar, WordCloud
import jieba.posseg as pseg
import pandas as pd
import re
from collections import Counter
```








数据源资源来自于[GitHub](https://github.com/zhouwei713/data_analysis/tree/master/Jay_Chou)
