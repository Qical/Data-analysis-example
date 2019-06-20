'''
任务：将文件夹中的所有文件全部读取出来进行简单的数据清洗之后添加到数据库中
思路：首先遍历文件夹得到文件名称，由于文件名称中有日期，并且要作为文件的一列
    所以用正则取出来日期，进行保存使用

'''


import pandas as pd
from sqlalchemy import create_engine
import os
import re
# 忽略警告
import warnings

warnings.filterwarnings("ignore")

os.chdir(r'C:\Users\Administrator\Desktop\商品效果-日')

engine = create_engine('mysql+pymysql://user:password@192.168.0.230:3306/dy')

dir_list = os.listdir()

for sh in dir_list:
    # 利用正则找到文件日期，为后面的新列添加数据
    day_n = re.search('\d+-\d*-\d*',sh)
    day_t = day_n.group()

    # 读取excel，并且跳过前三行
    data = pd.read_excel(sh,skiprows=3)
    # print(list(data.columns))

    # 清洗里面的关于百分号的问题
    # 清洗百分号的列字符串实现数值转化,将所有的字段汇总
    pre_list = ['XXXXX', '下单转化率', '下单支付转化率', '支付转化率',
                '点击率', 'XXXX']

    for i in list(data.columns):
        if i in pre_list:
            # 清洗关于“%”存在导入的无法识别的脏数据
            data[i] = data[i].str.strip("%").astype(float) / 100
        else:
            continue

    # 添加时间周期,插入第一列
    data.insert(0,'周期',day_t)

    # 换成英文表头
    data.columns = ["createtime","channel_from","itemid","itemname","item_state","itemlink","pv","uv","stop_length","dap_roc",
                    "gmv_roc","gmv_alipay_roc","alipay_roc","gmv_trade_amt","gmv_auction_num","gmv_winner_num","alipay_trade_amt",
                    "alipay_auction_num","plus_num","uv_value","click_num","click_roc","impression","collect_winner",
                    "search_alipay_winner_num","perCustTrade","search_alipay_roc","search_uv","alipay_winner_num","refund_amt","refund_qty",
                    ]


    pd.io.sql.to_sql(data,
                     'items',
                     con=engine,
                     index =False,
                     if_exists='append')
    print('%s的数据已经入库完成'%day_t)
print('down')
