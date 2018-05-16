# -*- coding: utf-8 -*-
"""
Created on Thu May 10 11:41:23 2018
#直接获取在市的所有合约，选择需要的合约，最后更新到配置json
@author: Administrator
"""
#%%导入需要的库
import datetime
import tushare as ts
#%%全局对象
today=datetime.date.today()#今天日期
yesterday=today-datetime.timedelta(days=1)#昨天日期
#%%业务模块
#%%-----获取在市的所有合约(当天)
symbol_shfe=ts.get_shfe_daily(yesterday)['symbol'].tolist()#获取上期所的合约
symbol_shfe=ts.get_dce_daily(yesterday)['symbol'].tolist()#获取大商所的合约
symbol_shfe=ts.get_czce_daily(yesterday)['symbol'].tolist()#获取郑商所的合约
#symbol.extend(ts.get_cffex_daily(date)['symbol'].tolist())#获取中金所的合约

#%%信息栏
'''
合约代码需要大写
'''