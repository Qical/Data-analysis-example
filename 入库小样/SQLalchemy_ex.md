## SALAlchemy
对于关系型数据库来说非常的方便，列举我常用的入库的方法和使用注意事项

> 对象关系映射，即ORM技术，指的是把关系数据库的表结构映射到对象上，通过使用描述对象和数据库之间的映射的元数据，将程序中的对象持久化到
数据库中。在python中最有名的额ORM框架就是SQLAlchemy。
[相关学习网站](https://www.cnblogs.com/fuqia/p/8996033.html)
*******************************************
>SQLAlchemy模块提供了creat_engine()函数用来初始化数据库连接，SQlAlchemy用一个字符串表示连接信息：***‘数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名’*** 其中，pandas模块提供了read_sql_query()函数实现对数据库的查询

*****************************
>to_sql()函数实现了对数据库的写入。并不需要实现新建MYSQL数据表。sqlalchemy模块实现了与不同数据库的连接，而***pymysql模块使得python能够操作mysql数据库。在写入库的时候，pymysql是没办法用的。*** To_sql函数并不在pd之中，而在io.sql中，是sql脚本下的一个类！所以to_sql最好的写法是:pd.io.to_sql(df1,tablename,con=conn,if_exists='replace')


#### 常见的例子
```python 
# -*- coding: utf-8 -*-

import pandas as pd
from sqlalchemy import create_engine
import pymysql
import os
os.chdir(r'C:\Users\Administrator.DESKTOP-UNULF2U\Desktop\KNIME_file')

# 创建连接数据
engine = create_engine('mysql+pymysql://root:2212@192.168.0.200:3306/dy')

# 初始化数据库的连接，使用pymysql模块
df = pd.read_csv('date_d.csv',sep = ',')
print(df.head())

# 将新建的DATAFRAME存储为MySQL中的数据表，不存储为index列（index=False）

#if_exists:
#fail:如果表存在，啥也不做
#replace：如果表存在，删了表，在建立一个新表，把数据插入，
#append：如果表存在，把数据插入，如果不存在创建一个表

pd.io.sql.to_sql(df,
                 'example',
                 con=engine,
                 index =False,
                 if_exists='replace')

# df.to_sql('example',con=engine,if_exists='replace')
print('Write to MySql successfully!')
```
