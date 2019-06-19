import pymysql
import csv


# 连接库的操作
db = pymysql.connect(host='IP',
                     user='root',
                     password='password',
                     port = 3306,
                     db = 'spider')


# 创建游标
cursor = db.cursor()

sql = """
            insert into students(id,name,age) values (%s, %s, %s) on duplicate key update  
            id= %s,name= %s,age= %s
       """

with open('test.csv',mode='rt' ) as f:
    reader = csv.reader(f)
    head_row = next(reader)
    # print(tuple(head_row))
    for item in reader:
        print(item)
        cursor.execute(sql, tuple(item)*2)

    db.commit()
    cursor.close()
    db.close()

