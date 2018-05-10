# encoding: UTF-8

"""
立即下载数据到数据库中，用于手动执行更新操作。
"""

from dataService import *


if __name__ == '__main__':
    downloadAllMinuteBar()
    
#%%测试模块
import tushare as ts
df = ts.bar('I1809', conn=ts.get_apis(),freq='D',asset='X',\
    start_date='2018-05-01',end_date='2018-05-05')

help(tushare.bar)

help(tushare.xapi)