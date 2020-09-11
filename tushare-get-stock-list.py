

import time
import datetime
import random


import tushare
import pandas


stock_list_file = 'stock_list.csv'

tushare_token =  '0370492e57677283dc7172bd6db8b55fda5f57d9339a05f6106b2b61'


# 股票列表
def get_stock_basic():
    print('开始下载股票列表数据')

    # 获取tushare
    pro = tushare.pro_api()

    # 下载
    data = pro.stock_basic(fields='ts_code,symbol,name,fullname,list_status,list_date,delist_date')
    # 保存到csv文件
    data.to_csv(stock_list_file)
    return 1

'''
    # 入库    
    engine = sqlalchemy.create_engine(db_url)

    try:
        # 先一次性入库，异常后逐条入库
        pandas.io.sql.to_sql(data, 'stock_basic', engine, schema='quantum.dbo', if_exists='append', index=False)
    except:
        # 逐行入库
        print('批量入库异常，开始逐条入库.')
        for indexs in data.index:
            line = data.iloc[indexs:indexs + 1, :]

            try:
                pandas.io.sql.to_sql(line, 'stock_basic', engine, schema='quantum.dbo', if_exists='append', index=False,
                                     chunksize=1)
            except:
                print('股票列表数据入库异常：')
                print(line)
            finally:
                pass
    finally:
        pass

'''

# 全量下载所有股票列表数据
if __name__ == '__main__':
    print('开始...')

    # 初始化tushare
    tushare.set_token(tushare_token)

    print('获取股票列表')
    get_stock_basic()

    print('结束')

print(tushare.__version__)