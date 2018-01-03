# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 11:59:58 2018

@author: doktor
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1,2,1)

"Live plotting the Temp in the subplot"
def animate(i) :
    graph_data = open('HStemperature.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax1.clear()
    ax1.plot(xs,ys)

ani = animation.FuncAnimation(fig, animate, interval=2000)
plt.show()

"Live plotting something else"
ax2 = fig.add_subplot(1,2,2)
def animate2(i) :
    graph_data = open('HSvolt.txt','r').read()
    lines = graph_data.split('\n')
    xs = []
    ys = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs.append(x)
            ys.append(y)
    ax2.clear()
    ax2.plot(xs,ys)

ani2 = animation.FuncAnimation(fig, animate2, interval=1000)
plt.show()