# -*- coding: utf-8 -*-
"""
Created on Wed Jan  3 15:01:32 2018

@author: doktor
"""




import sys

from PyQt4 import QtGui
import matplotlib.pyplot as plt

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar




class PrettyWidget(QtGui.QWidget):
    
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.setGeometry(600,300, 1000, 600)
        self.center()
        self.setWindowTitle('HK data')     
       
        grid = QtGui.QGridLayout()
        self.setLayout(grid)
       
        btn1 = QtGui.QPushButton('Plot 1', self)
        btn1.resize(btn1.sizeHint()) 
        btn1.clicked.connect(self.plot1)
        grid.addWidget(btn1, 3,0)

        btn2 = QtGui.QPushButton('Plot 2', self)
        btn2.resize(btn2.sizeHint())    
        btn2.clicked.connect(self.plot2)
        grid.addWidget(btn2, 3,1)
        
        "more buttons for more plots"
        
        
        btn3 = QtGui.QPushButton('Plot 3', self)
        btn3.resize(btn3.sizeHint())    
        btn3.clicked.connect(self.plot3)
        grid.addWidget(btn3, 4,0)
        
        btn4 = QtGui.QPushButton('Plot 4', self)
        btn4.resize(btn4.sizeHint())    
        btn4.clicked.connect(self.plot4)
        grid.addWidget(btn4, 4,1)
        
        "figure and toolbar"
               
        self.figure = plt.figure(figsize=(15,5))    
        self.canvas = FigureCanvas(self.figure)     
        self.toolbar = NavigationToolbar(self.canvas, self)
        grid.addWidget(self.canvas, 1,0,1,2)
        grid.addWidget(self.toolbar, 0,0,1,2)
               
        self.show()
    
    "Will try to plot HK data over each button"
        
    
    
    def plot1(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**2 for i in x]
        ax.plot(x,y, 'b.-')
        ax.set_title('Quadratic Plot')
        self.canvas.draw()
    
    
    def plot2(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**0.5 for i in x]
        ax.plot(x,y, 'r.-')
        ax.set_title('Square Root Plot')
        self.canvas.draw()
    
    def plot3(self):
        plt.cla()
        ax = self.figure.add_subplot(111)
        x = [i for i in range(100)]
        y = [i**4 for i in x]
        ax.plot(x,y, 'r.-')
        ax.set_title('Square Root Plot')
        self.canvas.draw()
        
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