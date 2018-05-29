# encoding: UTF-8

"""
立即下载数据到数据库中，用于手动执行更新操作。
"""

from dataService import *


if __name__ == '__main__':
    downloadAllMinuteBar('D')#需要下载日级别历史数据填"D",分钟级别数据填"1min"
   
#%%测试模块
import pandas as pd
from WindPy import w
w.start()
rdata=w.wsd("IFI.WI", "open,high,low,close,volume", "2013-10-18", "2018-05-28", "")
df=pd.DataFrame(rdata.Data).T
