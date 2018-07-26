# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 20:33:49 2018
十年期国债期货CTA策略回测优化。
@author: Administrator
"""

from __future__ import division


from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, DAILY_DB_NAME, OptimizationSetting


if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategy_TL8 import DoubleMaStrategy
    
    # 创建回测引擎
    engine = BacktestingEngine()
    
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20160701',initDays=100)
    
    
    # 设置产品相关参数
    engine.setSlippage(0.005)     # 滑点
    engine.setRate(0)   # 手续费
    engine.setSize(10000)         # 合约大小 
    engine.setPriceTick(0.005)    # 最小价格变动
    
    # 设置使用的历史数据库
    engine.setDatabase(DAILY_DB_NAME, 'TL8')
    
    # 跑优化
    setting = OptimizationSetting()                 # 新建一个优化任务设置对象
    setting.setOptimizeTarget('calmar')            # 设置优化排序的目标是策略净盈利
    setting.addParameter('fastWindow', 1, 4, 1)    # 增加第一个优化参数atrLength，起始12，结束20，步进2
    setting.addParameter('slowWindow', 5, 60, 5)        # 增加第二个优化参数atrMa，起始20，结束30，步进5
  
    
    # 性能测试环境：I7-3770，主频3.4G, 8核心，内存16G，Windows 7 专业版
    # 测试时还跑着一堆其他的程序，性能仅供参考
    import time    
    start = time.time()
    
    # 运行单进程优化函数，自动输出结果，耗时：359秒
    engine.runOptimization(DoubleMaStrategy, setting)            
    
    # 多进程优化，耗时：89秒
    #engine.runParallelOptimization(DoubleMaStrategy, setting)
    
    print u'耗时：%s' %(time.time()-start)
    
#%%测试模块

