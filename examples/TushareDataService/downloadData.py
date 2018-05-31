# encoding: UTF-8

"""
立即下载数据到数据库中，用于手动执行更新操作。
"""

from dataService import *
import datetime as dt
end_date=dt.datetime.today().date()
start_date=end_date-dt.timedelta(days=7)

if __name__ == '__main__':
    downloadAllMinuteBar('D',start_date,end_date)#需要下载日级别历史数据填"D",分钟级别数据填"1min"
   

