# -*- coding: utf-8 -*-
"""
Created on Fri May 18 10:23:22 2018
#开发vnpy项目的个人经验库
@author: Administrator
"""

#%%数据接口问题
#%%-----Mongo数据库
#-----------1.vnpy项目有那些数据库名称常量？
# 数据库名称
SETTING_DB_NAME = 'VnTrader_Setting_Db'#交易设置参数数据库
POSITION_DB_NAME = 'VnTrader_Position_Db'#仓位记录数据库

TICK_DB_NAME = 'VnTrader_Tick_Db'#tick数据库
DAILY_DB_NAME = 'VnTrader_Daily_Db'#日k线数据库
MINUTE_DB_NAME = 'VnTrader_1Min_Db'#分钟k想数据库
#%%-----Tushare数据接口
#-----------1.原vnpy的Tushare下载函数bar()错误？
'''
下载日K线：freq="D"
下载分钟K线：freq="1min"(只能下载一天的分钟K线)
'''
import tushare as ts
df=ts.bar('I1809',conn=ts.get_apis(), freq='D',asset='X')
#%%策略回测引擎问题
#-----1.如何理解CTA模块的回测引擎？
'''
CTA模块的回测引擎包含四个类：
BacktestingEngine（回测引擎类，整个回测过程由本类实现）
OptimizationSetting（优化参数类，优化时的参数配置由本类实现）
TradingResult（交易结果类，用于保存每一笔成交的详细信息）
DailyResult(按照日统计的交易结果类，用于保存每一天成交的详细信息)
'''

#-----2.CTA回测引擎BacktestingEngine有那些配置函数？
'''
def setBacktestingMode：设置回测模式：K线模式BAR_MODE和Tick模式TICK_MODE，需要有对应的数据

def setDatabase：设置加载历史数据所用的数据库和集合名，参数dbName为数据库名称，symbol为品种代码

def setStartDate：用于设置回测的启动日期和初始化策略时所需的数据天数,例如startDate='20100416', initDays=10

def setEndDate：设置回测的结束日期，若不设置则回测的结束日期会使用当前时间

def setSlippage：设置滑点，注意是具体的价格点数，如0.4点

def setRate：设置手续费，注意是成交金额的比例，如万0.3（0.3/10000）

def setSize：设置合约大小，如股指IF是300

def setPriceTick：设置合约的最小价格变动，如股指IF是0.2点

def setCapita：设置初始资金，只用于计算Sharpe Ratio，对策略开仓与否无影响
'''

#-----3.CTA回测引擎BacktestingEngine有那些回测函数？
'''
def initStrategy：初始化策略对象，传入的参数是策略类以及参数配置字典:如果使用类中写好的默认设置则可以不传该参数

def runBacktesting：运行回测，根据之前的配置加载历史数据回放，并将所有成交记录保存下来

def showDailyResult：基于逐日的方式统计成交结果，并显示相关图表

def showBacktestingResult：基于FIFO的原则配对买卖交易统计成交结果，并显示相关图表
'''

#-----4.CTA回测引擎BacktestingEngine有那些优化函数？
'''
def runOptimization：优化策略的参数，传入参数为策略类和优化参数配置

def runParallelOptimization：采用多进程的方式并行优化参数，根据CPU核心数量成倍提高优化速度
'''
#-----5.CTA模块的回测是怎样的一个过程？
'''
1.创建回测引擎
2.设置回测引擎的相关参数（回测模式，回测日期，数据库等）
3.设置产品或合约相关参数（滑点，佣金大小，合约大小）
4.在回测引擎中常见策略对象（策略类，参数设置）
5.跑回测
6.显示回测结果
'''

#-----6.回测开始的时间怎么对不上，第一个交易日延后了？
#%%策略回测下单问题
#-----1.下的限价单和停止单什么时候触发，触发顺序？
'''
下的限价单和停止单是在新的k线或者tick数据推送时候触发，在回调函数（onBar或者onTick）之前。

先撮合限价单，再撮合停止单
'''

#-----2.限价单是如何进行撮合的？
'''

'''
#%%策略回测参数优化问题
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


#-----3.回测优化参数设置类有那些定义函数？
'''
setOptimizeTarget(target):设置优化目标字段，详细看本章问题2.

addParameter( name, start, end=None, step=None):设置参数范围
'''

#-----4.策略回测如何自定义开仓手数？
'''
量化策略主要是从历史数据统计或者发现规律然后应用于实盘交易。当然历史不是简单的重复，
这就要求策略需要根据市场调整和优化参数。通过回测历史数据可以验证策略的有效性，
了解策略的历史收益、最大回撤和回撤时长，对策略参数进行优化等等。
CTA策略模块的主要回测目标是验证交易信号是否正确，仓位大小的问题在实盘中则由交易员来确定。

回测默认开仓数量为1手，可以进行自定义：
1.添加一个策略参数：volume=1
2.同时添加到参数列表
3.在交易时（buy,sell,short,cover）设置self.volume参数
'''

#-----5.策略参数优化回测（日K线）结果明显不正确，例如最大回测大得离谱？
'''
主要原因是多次回测中引擎中的回测结果没有清理干净，导致数据共享混乱。
回测结果清理的方法为：BactestingEngine.clearBacktestingResult
def clearBacktestingResult(self):
    """清空之前回测的结果"""
    # 清空限价单相关
    self.limitOrderCount = 0
    self.limitOrderDict.clear()
    self.workingLimitOrderDict.clear()        
    
    # 清空停止单相关
    self.stopOrderCount = 0
    self.stopOrderDict.clear()
    self.workingStopOrderDict.clear()
    
    # 清空成交相关
    self.tradeCount = 0
    self.tradeDict.clear()
    
    # 清空日线回测结果相关(往往是缺失这里)
    self.dailyResultDict.clear()
'''
#%%策略回测结果可视化问题
#-----1.策略结果可视化有几种形式？
'''
策略结果可视化有两种形式：
1.逐笔统计结果：engine.showBacktestingResult（）
2.按日统计结果：engine.showDailyResult()
'''
#-----2.逐笔统计的回测结果有那些字段和图？
'''
第一笔交易：第一笔交易的平仓时间

最后一笔交易：最后一笔交易的平仓时间

总交易次数：整个回测的总交易次数

总盈亏：整个回测的总盈亏，由于回测时的初始资金为0，总盈亏其实就是当前资金。

最大回撤：每次交易后的回撤=每笔交易后的资金-回测中最大资金。由于回撤为非正值，
所以最大回撤为所有交易后的回撤绝对值最大的。

平均每笔盈利：总盈亏/总交易次数

平均每笔滑点：总滑点成本/总交易次数

平均每笔佣金:总佣金成本/总交易次数

胜率：盈利交易次数/总交易次数*100%

盈利交易平均值：总盈利交易的盈利/总盈利交易次数

亏损交易平均值：总亏损交易的亏损/总亏损交易次数

盈亏比：盈利交易平均值/亏损交易平均值

capital:每笔交易后的资金序列图

dropdown（DD）:每笔交易后的回撤序列图

profit&loss(pnl)：每笔交易的盈亏直方图（概率分布图）
'''
#-----3.按日统计的回测结果有那些字段和图？
'''
首个交易日:策略的开始日期=数据开始日期+数据初始化天数

最后交易日：策略的结束日期，默认为mongo数据库的合约的最后日期

总交易日：策略开始日期到策略结束日期的总交易天数

盈利交易日：盈利的交易天数

亏损交易日：亏损的交易天数

起始资金：回测引擎的起始资金

结束资金：最后交易日的结束资金

总收益：（结束资金/起始资金-1）*100%

年化收益：总收益/总交易日*240

总盈亏：每日盈亏的累加

最大回撤：回撤序列的最大值，回撤=当期的资金-回测历史的最大资金

百分比最大回撤：最大回撤/历史最大的资金*100%

总手续费：每笔交易手续费的累加，每笔手续费=合约大小*价格*手续费率*2（双边）

总滑点：滑点*2*总交易笔数

总成交金额：每笔成交金额额的累加

总成交笔数：总交易的次数

日均盈亏：总盈亏/总交易日

日均手续费：总手续费/总交易日

日均滑点：总滑点/总交易日

日均成交金额：总成交金额/总交易日

日均收益率：总收益率/总交易日

收益标准差：每日收益的标准差（std）

夏普比率：日均收益/收益标准差*根号240
'''

#-----4.为什么每笔统计和每日统计的最大回撤不一样？
'''
每笔统计的是损益的最大回撤，而每日统计的是权益最大回撤。
【损益的最大回撤】
从测试开始到结束，每笔动态损益计算出来的波段从高点到低点回撤的最大值
【权益的最大回撤】
从测试开始到结束，每日的动态权益计算出来的波段从高点到低点回撤的最大值
'''
#%%CTA策略模板
#-----1.vnpy提供那些模板策略类？
'''
1.【DoubleMa】双均线

2.【BollChannel】布林线
计算方法：UP=MB+2*MD  DN=MB+2*MD  MB=(N-1)MA  MD=平方根N日的（C－MA）的两次方之和除以N
作用：研判股价走势的辅助指标，即通过股价所处于布林通道内的位置来评估股票走势的强弱

3.【Atr-Rsi】ATR-RSI指标结合的交易策略
ATR:
ATR又称 Average true range平均真实波动范围，简称ATR指标，是由J.Welles Wilder 发明的，
ATR指标主要是用来衡量市场波动的强烈度，即为了显示市场变化率的指标。
1、当前交易日的最高价与最低价间的波幅
2、前一交易日收盘价与当个交易日最高价间的波幅
3、前一交易日收盘价与当个交易日最低价间的波幅
今日振幅、今日最高与昨收差价，今日最低与昨收差价中的最大值，为真实波幅，
在有了真实波幅后，就可以利用一段时间的平均值计算ATR了。至于用多久计算，
不同的使用者习惯不同，10天、20天乃至65天都有。

RSI:
相对强弱指标
计算方法：N日RSI =N日内收盘涨幅的平均值/(N日内收盘涨幅均值+N日内收盘跌幅均值) ×100%
作用：测量某一个期间内股价上涨总幅度占股价变化总幅度平均值的百分比，来评估多空力量的强弱程度

4.【DualThrust】
Dual Thrust，由Michael Chalek在20世纪80年代开发，曾被FutureTrust杂志评为最赚钱的策略之一。
Dual Thrust系统策略十分简单，思路简明，但正所谓大道至简，该策略适用于股票、期货、外汇等多类型市场，
如果配合上良好的资金管理和策略择时，可以为投资者带来长期稳定的收益。
Dual Thrust是典型的区间突破型策略，以今日开盘价加减一定比例的N周期内的价格振幅（Range），确定上下轨；
Dual Thrust对于多头和空头的触发条件，考虑了非对称的幅度，做多和做空参考的Range可以选择不同的周期数，
也可以通过参数K1和K2来确定。

具体计算过程如下：
(1)N日High的最高价HH, N日Close的最低价LC;
(2)N日Close的最高价HC，N日Low的最低价LL;
(3)Range = Max(HH-LC,HC-LL)
(4)上轨(upperLine )= Open + K1*Range
(5)下轨(lowerLine )= Open + K2*Range

5.【KingKeltner】肯特钠通道
肯特纳通道(KC)是一个移动平均通道，由叁条线组合而成(上通道、中通道及下通道)。
若股价於边界出现不沉常的波动，即表示买卖机会。肯特纳通道是基于平均真实波幅原理而形成的指标，
对价格波动反应灵敏，它可以取代布林线或百分比通道作为判市的新工具。肯特纳通道是由两根围绕
线性加权移动平均线波动的环带组成的，其中线性加权均线的参数通道是20。价格突破带状的上轨和
下轨时，通常会产生做多或做空的交易信号，指标的发明人是Chester Keltner，由Linda Raschke
再度优化改进，她采用10单位的线性加权均线来计算平均真实波幅(ATR)。

基于平均真实波幅的肯特纳通道运算公式如下:

对于顶部环带来讲，在10单位周期基础上计算出平均真实波幅，乘以双倍，然后把这个数值与20单位
周期的线性加权均线数值相加，就会得出新的顶部环带数值。对于底部环带来讲，在10单位周期基础
上计算出平均真实波幅，乘以双倍，把这个数值从20单位周期线性加权均线数值扣除，就会得出新的
底部环带数值。

6.【MultiTimeframe】
一个跨时间周期的策略，基于15分钟K线判断趋势方向，并使用5分钟RSI指标作为入场
'''

#-----2.如何使用交易策略的模板类？
'''
策略模板是具体交易策略的基础，一般把大部分策略都用到的方法和公共变量放到策略模板里
而具体策略继承该策略模板，进而增加个性方法和变量（如：入场价格、止损止盈）。
一般我个人喜欢在最基础模板上，按照交易策略的类型衍生出交易类型模板（如：CTA、套利、对冲等），
具体交易策略继承衍生的交易类型模板进行开发。
'''

#-----3.策略的模板类有哪几个基本部分？
'''
1.定义成员变量
2.加载常量
3.构造函数
4.回调函数
5.主动函数
'''

#-----4.策略模板中的BarGenerator类的应用场景和代码逻辑是什么？
'''
BarGenerator类是K线生成器，基于tick数据生成1分钟数据，或者1分钟数据生成x分钟数据。

【应用场景】
数据库的基础数据和我们回测用到的基础数据可能周期不一样，该类可以使周期同步，但是必须是
数据库的基础数据的周期频率要高于回测用到的基础数据。

【代码逻辑】
一个构造函数（__init__）和两个主动函数(updatetick,updatebar)

构造函数：一分钟目标k线相关成员变量(bar,onBar,lasttick),
        x分钟目标K线相关成员变量（xminBar,onXminBar,xmin）
        
主动函数（updateTick）：
'''