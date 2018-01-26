# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:01:32 2018

@author: doktor
"""




import sys
import time
import tkinter
from tkinter import *
root=Tk()
import threading
from threading import Timer

from time import sleep
from PyQt4 import QtGui
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar

"Live plotter stuff"
import matplotlib.animation as animation
from matplotlib import style

#style.use('fivethirtyeight')
"end live plotter stuff"

class PrettyWidget(QtGui.QWidget):
    
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        #self.setGeometry(0,0, 1500, 600)
        self.showMaximized()        
        self.center()
        self.setWindowTitle('HK data')     
       
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
       
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
        #btn3.clicked.connect(self.liveplotting3)
        grid.addWidget(btn3, 3,2,1,1)
        
        btn4 = QtGui.QPushButton('Plot 4', self)
        btn4.resize(btn4.sizeHint())    
        btn4.clicked.connect(self.plot4)
        grid.addWidget(btn4, 3,3,1,1)
        
     
        self.figure1 = plt.figure(figsize=(1,2))
        self.canvas1 = FigureCanvas(self.figure1)
        grid.addWidget(self.canvas1, 2,0)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
        self.figure2 = plt.figure(figsize=(2,2))
        self.canvas2 = FigureCanvas(self.figure2)
        grid.addWidget(self.canvas2, 2,1)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
        self.figure3 = plt.figure(figsize=(2,2))
        self.canvas3 = FigureCanvas(self.figure3)
        grid.addWidget(self.canvas3, 2,2)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
        self.figure4 = plt.figure(figsize=(1,2))
        self.canvas4 = FigureCanvas(self.figure4)
        grid.addWidget(self.canvas4, 2,3)
        plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
#        self.figure = plt.figure(figsize=(30,10))    
#        self.canvas = FigureCanvas(self.figure)     
#        self.toolbar = NavigationToolbar(self.canvas, self)
#        grid.addWidget(self.canvas, 1,0,1,4)
#        grid.addWidget(self.toolbar, 0,0,1,4)
#        self.show()
        
        self.figure = plt.figure(figsize=(30,8))    
        self.canvas = FigureCanvas(self.figure)     
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 1,0,1,4)
        grid.addWidget(self.toolbar, 0,0,1,4)
        self.show()
        
        hk4=self.figure4.add_subplot(111)
        x4 = [i for i in range(100)]
        y4 = [i**10 for i in x4]
        hk4.plot(x4,y4)
        self.canvas4.draw()
        hk4.set_xlabel('hej')
        hk4.set_ylabel('Noget')
        
        global pl2
      
        
#        def animate2(i) :
#            graph_data = open('HSvolt.txt','r').read()
#            lines = graph_data.split('\n')
#            x3 = []
#            y3 = []
#            for line in lines:
#                if len(line)>1:
#                    x, y = line.split(',')
#                    x3.append(x)
#                    y3.append(y)
#                hk3.clear()
#                hk3.plot(x3,y3)
#                hk3.set_xlabel('hej')
#                hk3.set_ylabel('Voltage')
#        hk3=self.figure3.add_subplot(111)
#        ani2 = animation.FuncAnimation(self.figure3, animate2, interval=1000)        
#        self.canvas3.draw()
        
        
        
 

        
      
        #a2 = QtGui.QPushButton('fig2', self)
        #a2.resize(a2.sizeHint())    
       # a2.clicked.connect(self.plot2)
        #grid.addWidget(a2, 2,1)        
     
               
       
    
#    def liveplotting3(self):
#        def animate3(i) :
#            graph_data = open('HSvolt.txt','r').read()
#            lines = graph_data.split('\n')
#            x3 = []
#            y3 = []
#            for line in lines:
#                if len(line)>1:
#                    x, y = line.split(',')
#                    x3.append(x)
#                    y3.append(y)
#                hk3.clear()
#                hk3.plot(x3,y3)
#                hk3.set_xlabel('hej')
#                hk3.set_ylabel('Voltage')
#        hk3=self.figure3.add_subplot(111)
#        ani3 = animation.FuncAnimation(self.figure3, animate3, interval=1000)        
#        self.canvas3.draw()
        
        
    
    
    
    def plot1(self):
#        plt.cla()
#        ax = self.figure.add_subplot(111)
#        x = [i for i in range(100)]
#        y = [i**2 for i in x]
#        ax.plot(x,y, 'b.-')
#        ax.set_title('Quadratic Plot')
#        ax.set_xlabel('time')
#        ax.set_ylabel('maybe temp')
#        self.canvas.draw()
        plt.cla()
        ax = self.figure.add_subplot(111)
        
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
            ax.clear()
            ax.plot(xs,ys)

        ani = animation.FuncAnimation(self.figure, animate, interval=11170)
        
        #self.canvas.draw()
        
        ax1 = self.figure1.add_subplot(111)
        
        def animate1(i) :
            graph_data = open('HSvolt.txt','r').read()
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

        ani2 = animation.FuncAnimation(self.figure1, animate1, interval=31173)
        
        self.canvas.draw()
        self.canvas1.draw()

    
    
    def plot2(self):
        
        plt.cla()
        hk2 = self.figure.add_subplot(111)
        def plotterfunc():
            graph_data = open('HSvolt.txt','r').read()
            lines = graph_data.split('\n')
            x2 = []
            y2 = []
            for line in lines:
                if len(line)>1:
                    x, y = line.split(',')
                    x2.append(x)
                    y2.append(y)
            hk2.plot(x2,y2)
            hk2.set_xlabel('hej')
            hk2.set_ylabel('Voltage') 
            self.canvas.draw()
            plotterfunc()
        plotterfunc()
            
        
        
       # root.after(2000,plotterfunc)
       
            #root.after(2000,plotterfunc())
            #time.sleep(2)
            #plt.cla()
            #time.sleep(2)
    
    def plot3(self):
        plt.cla()
        hk31=self.figure.add_subplot(111)
        hk3=self.figure3.add_subplot(111)
        hk31.set_xlabel('hej')
        hk31.set_ylabel('Voltage')
        hk3.set_xlabel('hej')
        hk3.set_ylabel('Voltage')
        def animate2() :
            graph_data1 = open('HSvolt.txt','r').read()
            lines = graph_data1.split('\n')
            x31 = []
            y31 = []
            for line in lines:
                if len(line)>1:
                    x1, y1 = line.split(',')
                    x31.append(x1)
                    y31.append(y1)
                hk31.clear()
                hk31.plot(x31,y31)
            self.canvas.draw()
            b3=Timer(5,animate3())
            b3.start()
                #hk3.clear()
                #hk3.plot(x3,y3)
        #ani2 = animation.FuncAnimation(self.figure, animate2, interval=5.000)  
        #self.canvas.draw()
        # ani2 = animation.FuncAnimation(self.figure, animate2, interval=500)  
        #self.canvas.draw()
        #hk3=self.figure3.add_subplot(111)
        def animate3() :
            graph_data = open('HSrandom.txt','r').read()
            lines = graph_data.split('\n')
            x3 = []
            y3 = []
            for line in lines:
                if len(line)>1:
                    x, y = line.split(',')
                    x3.append(x)
                    y3.append(y)
                hk3.clear()
                hk3.plot(x3,y3)
                #hk3.set_xlabel('hej')
                #hk3.set_ylabel('Voltage')
            self.canvas3.draw()
          
            b2=Timer(5,animate2())
            b2.start()
        animate2()
        #ani3 = animation.FuncAnimation(self.figure3, animate3, interval=3.1330)        
        #self.canvas3.draw()
        
    def plot4(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**10 for i in x]
        ax.plot(x,y, 'r.-')
        ax.set_title('Square Root Plot')
        self.canvas.draw()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QtGui.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    
    
        
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    app.exec_()



if __name__ == '__main__':
    main()