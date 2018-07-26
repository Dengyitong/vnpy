# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:48:13 2018
#pyqt绘图：TL8K线图
@author: Administrator
"""

import pyqtgraph as pg
import tushare as ts
import numpy as np

data = ts.get_hist_data('sh',start='2017-10-01',end='2017-12-01').sort_index()

xdict = dict(enumerate(data.index))

axis_1 = [(i,list(data.index)[i]) for i in range(0,len(data.index),5)]
app = pg.QtGui.QApplication([])
win = pg.GraphicsWindow(title=u'州的先生zmister.com pyqtgraph数据可视化 - 绘制精美折线图')
stringaxis = pg.AxisItem(orientation='bottom')
stringaxis.setTicks([axis_1,xdict.items()])	
plot = win.addPlot(axisItems={'bottom': stringaxis},title=u'上证指数 - zmister.com绘制')

label = pg.TextItem()
plot.addItem(label)
plot.addLegend(size=(150,80))
plot.showGrid(x=True, y=True, alpha=0.5)

plot.plot(x=list(xdict.keys()), y=data['open'].values, pen='r', name=u'开盘指数',symbolBrush=(255,0,0),)
plot.plot(x=list(xdict.keys()), y=data['close'].values, pen='g', name=u'收盘指数',symbolBrush=(0,255,0))
 
plot.setLabel(axis='left',text=u'指数')
plot.setLabel(axis='bottom',text=u'日期')
vLine = pg.InfiniteLine(angle=90, movable=False,)
hLine = pg.InfiniteLine(angle=0, movable=False,)
plot.addItem(vLine, ignoreBounds=True)
plot.addItem(hLine, ignoreBounds=True)
vb = plot.vb
def mouseMoved(evt):
    pos = evt[0]  ## using signal proxy turns original arguments into a tuple
    if plot.sceneBoundingRect().contains(pos):
        mousePoint = vb.mapSceneToView(pos)
        index = int(mousePoint.x())
        pos_y = int(mousePoint.y())
        print(index)
        if 0 < index < len(data.index):
            print(xdict[index],data['open'][index],data['close'][index])
            label.setHtml(u"<p style='color:white'>日期：{0}</p><p style='color:white'>开盘：{1}</p><p style='color:white'>收盘：{2}</p>".format(xdict[index],data['open'][index],data['close'][index]))
            label.setPos(mousePoint.x(),mousePoint.y())
        vLine.setPos(mousePoint.x())
        hLine.setPos(mousePoint.y())
proxy = pg.SignalProxy(plot.scene().sigMouseMoved, rateLimit=60, slot=mouseMoved)

app.exec_()

