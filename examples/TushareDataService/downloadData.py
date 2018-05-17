# encoding: UTF-8

"""
立即下载数据到数据库中，用于手动执行更新操作。
"""

from dataService import *


if __name__ == '__main__':
    downloadAllMinuteBar('D')#需要下载日级别历史数据填"D",分钟级别数据填"1min"
    
