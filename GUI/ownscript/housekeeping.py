# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 15:27:14 2018

@author: doktor
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 15:34:02 2018

@author: doktor
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:01:32 2018

@author: doktor
"""

import sys

import datetime

from PyQt4 import QtGui


import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar



"Live plotter stuff"
import matplotlib.animation as animation
#from matplotlib import style
#style.use('fivethirtyeight')
"end live plotter stuff"

global errorinterval
errorinterval = 4
        
f1 = plt.figure(figsize=(1,2))
ax1 = f1.add_subplot(111)

def animate1(i):
    graph_data = open('HStemperature.txt','r').read()
    global xs1
    global ys1
    lines = graph_data.split('\n')
    xs1 = []
    ys1 = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs1.append(x)
            ys1.append(y)
    ax1.clear()
    ax1.plot(xs1,ys1)

f2 = plt.figure(figsize=(1,2))
ax2 = f2.add_subplot(111)

def animate2(i):
    graph_data = open('HSvolt.txt','r').read()
    lines = graph_data.split('\n')
    global xs2
    global ys2
    xs2 = []
    ys2 = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs2.append(x)
            ys2.append(y)
    ax2.clear()
    ax2.plot(xs2,ys2)
    
f3 = plt.figure(figsize=(1,2))
ax3 = f3.add_subplot(111)

def animate3(i):
    graph_data = open('HSrandom.txt','r').read()
    lines = graph_data.split('\n')
    global xs3
    global ys3
    xs3 = []
    ys3 = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs3.append(x)
            ys3.append(y)
    ax3.clear()
    ax3.plot(xs3,ys3)
    

f4 = plt.figure(figsize=(1,2))
f4.patch.set_alpha(0.25)
f4.set_facecolor('g')
ax4 = f4.add_subplot(111)

def animate4(i):
    graph_data = open('testfile.txt','r').read()
    lines = graph_data.split('\n')
    global xs4
    global ys4
    xs4 = []
    ys4 = []
    for line in lines:
        if len(line)>1:
            x, y = line.split(',')
            xs4.append(x)
            ys4.append(y)
    ax4.clear()
    ax4.plot(xs4[-20:],ys4[-20:])
    global Last_value4
    Last_value4=float(ys4[-1])
    if float(Last_value4) > 16.00:
        f4.set_facecolor('r')
        Errordata = open('Error-Testfile.txt','a')
        Errordata.write("%s,%s\n" % (datetime.datetime.now().strftime("%I:%M%p on %B %d"),datetime.datetime.now().strftime("%Y")))
        Errordata.close()
        for j in range(errorinterval):
            Errordata = open('Error-Testfile.txt','a')
            xerror4=float(xs4[-errorinterval+(j)])
            yerror4=float(ys4[-errorinterval+(j)])
            Errordata.write("%5.2f,%5.2f\n" % (xerror4,yerror4))
            Errordata.close()
    
    
class PrettyWidget(QtGui.QTabWidget):
    
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        #self.setGeometry(0,0, 1500, 600)
        self.showMaximized()        
        self.center()
        self.setWindowTitle('HK data')     
       

       
#Test - adding tabs
        tab1 = QtGui.QWidget()
        
        self.addTab(tab1,'hk')
        grid = QtGui.QGridLayout()
        tab1.setLayout(grid)
#End tab test 1 All below inserted into tab?
       
        btn1 = QtGui.QPushButton('Plot 1', self)
        btn1.resize(btn1.sizeHint()) 
        btn1.clicked.connect(self.plot1)
        grid.addWidget(btn1, 3,0,1,1)

        btn2 = QtGui.QPushButton('Plot 2', self)
        btn2.resize(btn2.sizeHint())    
        btn2.clicked.connect(self.plot2)
        grid.addWidget(btn2, 3,1,1,1)
        
        btn3 = QtGui.QPushButton('Plot 3', self)
        btn3.resize(btn3.sizeHint())    
        btn3.clicked.connect(self.plot3)
        grid.addWidget(btn3, 3,2,1,1)
        
        btn4 = QtGui.QPushButton('Plot 4', self)
        btn4.resize(btn4.sizeHint())    
        btn4.clicked.connect(self.plot4)
        grid.addWidget(btn4, 3,3,1,1)
        
     
        self.figure1 = f1# plt.figure(figsize=(1,2))
        self.canvas1 = FigureCanvas(self.figure1)
        grid.addWidget(self.canvas1, 2,0)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
        
        self.figure2 = f2#plt.figure(figsize=(2,2))
        self.canvas2 = FigureCanvas(self.figure2)
        grid.addWidget(self.canvas2, 2,1)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
        
        self.figure3 = f3#plt.figure(figsize=(2,2))
        self.canvas3 = FigureCanvas(self.figure3)
        grid.addWidget(self.canvas3, 2,2)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
        
        self.figure4 = f4#plt.figure(figsize=(1,2))
        self.canvas4 = FigureCanvas(self.figure4)
        grid.addWidget(self.canvas4, 2,3)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)

        
        self.figure = plt.figure(figsize=(30,8))    
        self.canvas = FigureCanvas(self.figure)     
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 1,0,1,4)
#        grid.addWidget(self.toolbar, 0,0,1,4)
        self.show()
           
#Tab 2
        tab2 = QtGui.QWidget()
        self.addTab(tab2,'ErrorHandling')
        grid = QtGui.QGridLayout()
        tab2.setLayout(grid)
        
        
    
    def plot1(self):
        plt.cla()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs1,ys1)
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('Temperature of... plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Temperature Celcius?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()
    
    def plot2(self):
        plt.cla()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs2,ys2)
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('Voltage of... plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Voltage?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()


    def plot3(self):
        plt.cla()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs3,ys3)
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('More?... plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Random?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()
        
    def plot4(self):
        plt.cla()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs4[-200:],ys4[-200:])
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('More?... plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Random?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    
        
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    animate1(1); animate2(1); animate3(3)
    ani1 = animation.FuncAnimation(f1, animate1, interval=5000)
    ani2 = animation.FuncAnimation(f2, animate2, interval=5000)
    ani3 = animation.FuncAnimation(f3, animate3, interval=5000)
    ani4 = animation.FuncAnimation(f4, animate4, interval=1200)
    app.exec_()


if __name__ == '__main__':
    main()