# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:23:22 2018
#开发vnpy项目的个人经验库
@author: Administrator
"""

#%%数据接口问题
#%%-----Mongo数据库
#%%-----Tushare数据接口
#-----------1.原vnpy的Tushare下载函数bar()错误？
'''
下载日K线：freq="D"
下载分钟K线：freq="1min"(只能下载一天的分钟K线)
'''
import tushare as ts
df=ts.bar('I1809',conn=ts.get_apis(), freq='D',asset='X')

#%%策略回测问题
#-----1.跑参数优化回测的目标怎么全是0？

'''
优化目标字段不存在就会返回0，请参考一下目标字段。
'''
#-----2.跑参数优化回测的目标有那些？
'''
result = {
    'startDate': startDate,【开始日期】
    'endDate': endDate,【结束日期】
    'totalDays': totalDays,【总交易日】
    'profitDays': profitDays,【盈利交易日】
    'lossDays': lossDays,【亏损交易日】
    'endBalance': endBalance,【最后的权益：本金+净利润】
    'maxDrawdown': maxDrawdown,【最大回撤】
    'maxDdPercent': maxDdPercent,【百分比最大回撤】
    'totalNetPnl': totalNetPnl,【总损益】
    'dailyNetPnl': dailyNetPnl,【日均损益】
    'totalCommission': totalCommission,【总的手续费】
    'dailyCommission': dailyCommission,【日均手续费】
    'totalSlippage': totalSlippage,【总滑点】
    'dailySlippage': dailySlippage,【日均滑点】
    'totalTurnover': totalTurnover,【总成交金额】
    'dailyTurnover': dailyTurnover,【日均成交金额】
    'totalTradeCount': totalTradeCount,【总成交笔数】
    'dailyTradeCount': dailyTradeCount,【日均成交笔数】
    'totalReturn': totalReturn,【总收益】
    'annualizedReturn': annualizedReturn,【年化收益，240个交易日】
    'dailyReturn': dailyReturn,【日均收益】
    'returnStd': returnStd,【收益标准差】
    'sharpeRatio': sharpeRatio【夏普比率】
}
'''