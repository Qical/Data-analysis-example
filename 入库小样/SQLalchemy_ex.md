## SALAlchemy
对于关系型数据库来说非常的方便，列举我常用的入库的方法和使用注意事项

> 对象关系映射，即ORM技术，指的是把关系数据库的表结构映射到对象上，通过使用描述对象和数据库之间的映射的元数据，将程序中的对象持久化到
数据库中。在python中最有名的额ORM框架就是SQLAlchemy。
[相关学习网站](https://www.cnblogs.com/fuqia/p/8996033.html)
*******************************************
>我们需要以下三个库来实现Pandas读写MySQL数据库：
	- pandas
	- sqlalchemy
	- pymysql
SQLAlchemy模块提供了creat_engine()函数用来初始化数据库连接，SQlAlchemy用一个字符串表示连接信息：***‘数据库类型+数据库驱动名称://用户名:口令@机器地址:端口号/数据库名’***其中，pandas模块提供了read_sql_query()函数实现对数据库的查询，

*****************************
>to_sql()函数实现了对数据库的写入。并不需要实现新建MYSQL数据表。sqlalchemy模块实现了与不同数据库的连接，而***pymysql模块使得python能够操作mysql数据库。在写入库的时候，pymysql是没办法用的。***To_sql函数并不在pd之中，而在io.sql中，是sql脚本下的一个类！所以to_sql最好的写法是:pd.io.to_sql(df1,tablename,con=conn,if_exists='replace')
