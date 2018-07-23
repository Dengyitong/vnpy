# encoding: UTF-8

"""
导入MC导出的CSV历史数据到MongoDB中
"""
from vnpy.trader.app.ctaStrategy.ctaHistoryData import loadWindPlusCsv

if __name__ == '__main__':
    loadWindPlusCsv('IF0_DAILY.xlsx', 'VnTrader_Daily_Db', 'IF0')




