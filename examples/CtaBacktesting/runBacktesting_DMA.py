# encoding: UTF-8

"""
展示如何执行策略回测。
"""

from __future__ import division#python3总/表示真除，而python2带小数/才表示真除

from vnpy.trader.app.ctaStrategy.ctaBacktesting import BacktestingEngine, DAILY_DB_NAME


if __name__ == '__main__':
    from vnpy.trader.app.ctaStrategy.strategy.strategyDoubleMa import DoubleMaStrategy
    
    # 创建回测引擎
    engine = BacktestingEngine()
    
    # 设置引擎的回测模式为K线
    engine.setBacktestingMode(engine.BAR_MODE)

    # 设置回测用的数据起始日期
    engine.setStartDate('20170915',initDays=45)
    
    # 设置产品相关参数
    engine.setSlippage(0.5)     # 滑点
    engine.setRate(0.7/10000)   # 手续费
    engine.setSize(100)         # 合约大小 
    engine.setPriceTick(0.5)    # 最小价格变动
    engine.setCapital(20000)    #设置初始资金
    # 设置使用的历史数据库
    engine.setDatabase(DAILY_DB_NAME, 'I1809')
    
    # 在引擎中创建策略对象
    d = {'fastWindow':4,'slowWindow':2}
    engine.initStrategy(DoubleMaStrategy, d)
    
    # 开始跑回测
    engine.runBacktesting()
    
    # 显示回测结果
    engine.showBacktestingResult()#显示按照每笔统计的结果
    engine.showDailyResult()#显示按日统计的结果
