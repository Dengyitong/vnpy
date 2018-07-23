# -*- coding: utf-8 -*-
"""
Created on Mon Jul 23 18:18:29 2018
#绘制可交互的K线
@author: Administrator
"""
#%%导入需要的库
import pandas as pd
import bokeh.plotting as bp
from math import pi
# TODO 可设置的红涨绿跌，还是绿涨红跌
__colorup__ = "red"
__colordown__ = "green"

#%%函数模块
def _do_plot_candle_html(date, p_open, high, low, close, symbol):
    """
    bk绘制可交互的k线图
    :param date: 融时间序列交易日时间，pd.DataFrame.index对象
    :param p_open: 金融时间序列开盘价格序列，np.array对象
    :param high: 金融时间序列最高价格序列，np.array对象
    :param low: 金融时间序列最低价格序列，np.array对象
    :param close: 金融时间序列收盘价格序列，np.array对象
    :param symbol: symbol str对象
    :param save: 是否保存可视化结果在本地
    """
    mids = (p_open + close) / 2
    spans = abs(close - p_open)

    inc = close > p_open
    dec = p_open > close

    w = 24 * 60 * 60 * 800
    bp.output_file(symbol+'.html', title=symbol)
    t_o_o_l_s = "pan,wheel_zoom,box_zoom,reset,save"

    p = bp.figure(x_axis_type="datetime", tools=t_o_o_l_s, plot_width=1280, title=symbol)
    p.xaxis.major_label_orientation = pi / 4
    p.grid.grid_line_alpha = 0.3

    p.segment(date.to_datetime(), high, date.to_datetime(), low, color="black")
    # noinspection PyUnresolvedReferences
    p.rect(date.to_datetime()[inc], mids[inc], w, spans[inc], fill_color=__colorup__, line_color=__colorup__)
    # noinspection PyUnresolvedReferences
    p.rect(date.to_datetime()[dec], mids[dec], w, spans[dec], fill_color=__colordown__, line_color=__colordown__)
    
    bp.show(p)
    
    
def  plot_candle_form_wind(data,symbol):
    data.index=data[u'日期']
    date=data.index
    p_open=data[u'开盘价(元)']
    high=data[u'最高价(元)']
    low=data[u'最低价(元)']
    close=data[u'收盘价(元)']
    _do_plot_candle_html(date, p_open, high, low, close, symbol)
    
#%%业务模块
symbols=['IF0_DAILY','TL8_DAILY','IL9_DAILY']
for symbol in symbols:    
    data=pd.read_excel(symbol+'.xlsx')
    plot_candle_form_wind(data,symbol)
