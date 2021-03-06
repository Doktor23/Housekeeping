
#   Importing all necessary libs.

import time
import sys
import subprocess
import datetime
import os
from PyQt4 import QtGui
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.animation as animation


#####Setting up need to know values before the GUI is initiated.

#   The amount of datapoints we would like to include before an error (to see trends in the data)
global errorinterval
errorinterval = 70

#   Defining sizes of the read HK data files to make sure it doesn't double save same datapoint if the... 
#   file already contains HK data points
global size_of_1
global size_of_2
global size_of_3
global size_of_4
size_of_1=len(open('HStemperature.txt','r').read().split('\n'))-1
size_of_2=len(open('HSvolt.txt','r').read().split('\n'))-1
size_of_3=len(open('HSrandom.txt','r').read().split('\n'))-1
size_of_4=len(open('testfile.txt','r').read().split('\n'))-1

#   Read the total amount of recorded errors from the error file
last_line = subprocess.check_output(['tail', '-1', 'Error-Testfile.txt'])[0:-1].decode()
if os.stat("Error-Testfile.txt").st_size == 0:
    recorded_errors = 0
else:
    c1,c2,c3=last_line.split(',')
    recorded_errors = int(c3)

##### Defining animation functions

#   Figure properties
f1 = plt.figure(figsize=(1,2))
f1.patch.set_alpha(0.50)
f1.set_facecolor('lime')
ax1 = f1.add_subplot(111)
plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)

##### liveplotting animations

def animate1(i):
#   This part read the HK data file and plots the data to a figure which will be drawn on canvas
    start_time = time.time()
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
    ax1.plot(xs1[-500:],ys1[-500:],'bo-')
    ax1.set_title('Temperature P31U',fontweight="bold", size=20) # Title
    ax1.set_ylabel('Temperature(celcius)', fontsize = 20.0) # Y label
    ax1.set_xlabel('real time', fontsize = 20) # X label

#   This part examines each new datapoint from the HK datafile and will record an error if it occurs
    global size_of_1
    if len(xs1) > size_of_1:
        newpoints=len(xs1)-size_of_1
        for k in range(newpoints):
            global Last_value1
            Last_value1=float(ys1[len(ys1)-newpoints+k])
            if float(Last_value1) > 12.00:
                size_of_1=len(xs1)
                global recorded_errors
                recorded_errors += 1
                f1.patch.set_alpha(1)
                f1.set_facecolor('r')
                Errordata = open('Error-Testfile.txt','a')
                Errordata.write("%s,%s,%s\n" % ("Test-File1","Y-unit!",str(recorded_errors)))
                Errordata.write("%s,%s,%s\n" % (datetime.datetime.now().strftime("%I:%M%p on %B %d"),datetime.datetime.now().strftime("%Y"),str(recorded_errors)))
                Errordata.close()
                global xerror1; global yerror1
                #xerror1=float(xs1[-1]); yerror1=float(ys1[-1])
                for j in range(errorinterval):
                    Errordata = open('Error-Testfile.txt','a')
                    try:
                        xerror1=float(xs1[-errorinterval+(j)])
                        yerror1=float(ys1[-errorinterval+(j)])
                        Errordata.write("%5.2f,%5.2f,%s\n" % (xerror1,yerror1,str(recorded_errors)))
                        Errordata.close()
                    except:
                        ""
    print("--- %s seconds ---" % (time.time() - start_time))

f2 = plt.figure(figsize=(1,2))
plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
f2.patch.set_alpha(0.50)
f2.set_facecolor('lime')
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
    ax2.plot(xs2[-500:],ys2[-500:],'mo-')
    ax2.set_title('Voltage out P31U',fontweight="bold", size=20) # Title
    ax2.set_ylabel('Volt (V)', fontsize = 20.0) # Y label
    ax2.set_xlabel('real time', fontsize = 20) # X label
    
    global size_of_2
    if len(xs2) > size_of_2:
        newpoints=len(xs2)-size_of_2
        for k in range(newpoints):
            global Last_value2
            Last_value2=float(ys2[len(ys2)-newpoints+k])
            if float(Last_value2) > 12.00:
                size_of_2=len(xs2)
                global recorded_errors
                recorded_errors += 1
                f2.patch.set_alpha(1)
                f2.set_facecolor('r')
                Errordata = open('Error-Testfile.txt','a')
                Errordata.write("%s,%s,%s\n" % ("Test-File2","Y-unit!",str(recorded_errors)))
                Errordata.write("%s,%s,%s\n" % (datetime.datetime.now().strftime("%I:%M%p on %B %d"),datetime.datetime.now().strftime("%Y"),str(recorded_errors)))
                Errordata.close()
                global xerror2; global yerror2
                #xerror2=float(xs2[-1]); yerror2=float(ys2[-1])
                for j in range(errorinterval):
                    Errordata = open('Error-Testfile.txt','a')
                    try:
                        xerror2=float(xs2[-errorinterval+(j)])
                        yerror2=float(ys2[-errorinterval+(j)])
                        Errordata.write("%5.2f,%5.2f,%s\n" % (xerror2,yerror2,str(recorded_errors)))
                        Errordata.close()
                    except:
                        ""

    
f3 = plt.figure(figsize=(1,2))
plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
f3.patch.set_alpha(0.50)
f3.set_facecolor('lime')
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
    ax3.plot(xs3[-500:],ys3[-500:],'ko-')
    ax3.set_title('Housekeeping DATA 3',fontweight="bold", size=20) # Title
    ax3.set_ylabel('Temperature(celcius)', fontsize = 20.0) # Y label
    ax3.set_xlabel('real time', fontsize = 20) # X label
    
    global size_of_3
    if len(xs3) > size_of_3:
        newpoints=len(xs3)-size_of_3
        for k in range(newpoints):
            global Last_value3
            Last_value3=float(ys3[len(ys3)-newpoints+k])
            if float(Last_value3) > 12.00:
                size_of_3=len(xs3)
                global recorded_errors
                recorded_errors += 1
                f3.patch.set_alpha(1)
                f3.set_facecolor('r')
                Errordata = open('Error-Testfile.txt','a')
                Errordata.write("%s,%s,%s\n" % ("Test-File3","Y-unit!",str(recorded_errors)))
                Errordata.write("%s,%s,%s\n" % (datetime.datetime.now().strftime("%I:%M%p on %B %d"),datetime.datetime.now().strftime("%Y"),str(recorded_errors)))
                Errordata.close()
                global xerror3; global yerror3
                #xerror3=float(xs3[-1]); yerror3=float(ys3[-1])
                for j in range(errorinterval):
                    Errordata = open('Error-Testfile.txt','a')
                    try:
                        xerror3=float(xs3[-errorinterval+(j)])
                        yerror3=float(ys3[-errorinterval+(j)])
                        Errordata.write("%5.2f,%5.2f,%s\n" % (xerror3,yerror3,str(recorded_errors)))
                        Errordata.close()
                    except:
                        ""


f4 = plt.figure(figsize=(1,2))
plt.subplots_adjust(left=0.15, bottom=0.17, right=0.9, top=0.92)
f4.patch.set_alpha(0.50)
f4.set_facecolor('lime')
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
    ax4.plot(xs4[-500:],ys4[-500:],'yo-')
    ax4.set_title('Housekeeping DATA 4',fontweight="bold", size=20) # Title
    ax4.set_ylabel('Temperature(celcius)', fontsize = 20.0) # Y label
    ax4.set_xlabel('real time', fontsize = 20) # X label
    
    global size_of_4
    if len(xs4) > size_of_4:
        newpoints=len(xs4)-size_of_4
        for k in range(newpoints):
            global Last_value4
            Last_value4=float(ys4[len(ys4)-newpoints+k])
            if float(Last_value4) > 12.00:
                size_of_4=len(xs4)
                global recorded_errors
                recorded_errors += 1
                f4.patch.set_alpha(1)
                f4.set_facecolor('r')
                Errordata = open('Error-Testfile.txt','a')
                Errordata.write("%s,%s,%s\n" % ("Test-File4","Y-unit!",str(recorded_errors)))
                Errordata.write("%s,%s,%s\n" % (datetime.datetime.now().strftime("%I:%M%p on %B %d"),datetime.datetime.now().strftime("%Y"),str(recorded_errors)))
                Errordata.close()
                global xerror4; global yerror4
                #xerror4=float(xs4[-1]); yerror4=float(ys4[-1])
                for j in range(errorinterval):
                    Errordata = open('Error-Testfile.txt','a')
                    try:
                        xerror4=float(xs4[-errorinterval+(j)])
                        yerror4=float(ys4[-errorinterval+(j)])
                        Errordata.write("%5.2f,%5.2f,%s\n" % (xerror4,yerror4,str(recorded_errors)))
                        Errordata.close()
                    except:
                        ""

    
    
class PrettyWidget(QtGui.QTabWidget):
    
    
    def __init__(self):
        super(PrettyWidget, self).__init__()
        self.initUI()
        
        
    def initUI(self):
        self.showMaximized()        
        self.setWindowTitle('HK data')     
       
        stylesheet = """QTabWidget::tab-bar {alignment: center;}"""
        self.setStyleSheet(stylesheet)
       
#   adding tab1
        tab1 = QtGui.QWidget()
        self.addTab(tab1,'House Keeping')
        grid = QtGui.QGridLayout()
        tab1.setLayout(grid)
        
#   All below inserted into tab (Until new tab is inserted)
        #Inserting buttons       
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
        
#       Inserting canvasses on which the animated figures will be plottet     
        self.figure1 = f1
        self.canvas1 = FigureCanvas(self.figure1)
        grid.addWidget(self.canvas1, 2,0)
        
        self.figure2 = f2
        self.canvas2 = FigureCanvas(self.figure2)
        grid.addWidget(self.canvas2, 2,1)
        
        self.figure3 = f3
        self.canvas3 = FigureCanvas(self.figure3)
        grid.addWidget(self.canvas3, 2,2)
        
        self.figure4 = f4
        self.canvas4 = FigureCanvas(self.figure4)
        grid.addWidget(self.canvas4, 2,3)

#       Inserting main canvas
        self.figure = plt.figure(figsize=(50,8))    
        self.figure.patch.set_alpha(0)
        self.canvas = FigureCanvas(self.figure)     
        grid.addWidget(self.canvas, 1,0,1,4)
        self.show()
           
#   Tab 2 - ErrorHandling
#       Here tab2 is initiated
        tab2 = QtGui.QWidget()
        self.addTab(tab2,'Error Handling')
        grid = QtGui.QGridLayout()
        tab2.setLayout(grid)
        grid.setSpacing(15)

#       Labels for the two text editors were one can see and write regarding recorded errors.
        label_ed = QtGui.QLabel(self)
        label_ed.setText('Here you see the amount of errors recorded in the Error-Testfile.txt')
        grid.addWidget(label_ed,2,0,1,1)        
        label_ev = QtGui.QLabel(self)
        label_ev.setText('Insert the integer of the error you want to display')
        grid.addWidget(label_ev,1,0,1,1)
        
        
#       Here i design a textbox that can only be read (not accesed by user), it shows the # of errors
        global errordisplay
        errordisplay = QtGui.QLineEdit(self)
        errordisplay.setReadOnly(True)
        errordisplay.setText("recorded errors  =  " + str(recorded_errors))
        grid.addWidget(errordisplay,2,1,1,1)
        
#       Here i design a textbox that will read the user input (An integer of #error)     
        global errorvalue
        errorvalue = QtGui.QLineEdit(self)
        errorvalue.resize(1,1)
        grid.addWidget(errorvalue,1,1,1,1)
        errorvalue.resize(1,1)
    
#       Here i design a button which will plot the error, assigned by the user input above    
        ploterror = QtGui.QPushButton('Plot chosen error in the window above', self)
        ploterror.resize(ploterror.sizeHint()) 
        ploterror.clicked.connect(self.Perror)
        grid.addWidget(ploterror, 1,2,1,1)     
        
#       Here i design a button that will display current number of recorded errors        
        UpdateError = QtGui.QPushButton('Update the display of recorded errors', self)
        UpdateError.resize(UpdateError.sizeHint()) 
        UpdateError.clicked.connect(self.Uerror)
        grid.addWidget(UpdateError, 2,2,1,1)        

#       Here i design the canvas on which the recorded error will be drawn
        self.errorplot = plt.figure()
        self.errorplot.patch.set_alpha(0)
        self.errorcanvas = FigureCanvas(self.errorplot)
        grid.addWidget(self.errorcanvas, 0,0,1,3)
        self.errorplot.add_subplot(111)
        self.errorcanvas.draw()
    
#       A simple spacer to beautify the GUI    
        my_spacer = QtGui.QSpacerItem(100, 1, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)        
        grid.addItem(my_spacer,0,3,1,1)
                
        
        
        global errorinfo
        errorinfo = QtGui.QPlainTextEdit(self)
        grid.addWidget(errorinfo,0,4,1,2)
        errorinfo.insertPlainText("The recorded error will be displayed below\n")
        
#   Reset HK data on tab1 - All buttons that will reset the green color on the face of plot 1,2,3,4
        Reset1 = QtGui.QPushButton('Reset error in window 1', self)
        Reset1.resize(Reset1.sizeHint()) 
        Reset1.clicked.connect(self.R1)
        grid.addWidget(Reset1, 1,4,1,1)
        
        Reset2 = QtGui.QPushButton('Reset error in window 2', self)
        Reset2.resize(Reset2.sizeHint()) 
        Reset2.clicked.connect(self.R2)
        grid.addWidget(Reset2, 1,5,1,1)
        
        Reset3 = QtGui.QPushButton('Reset error in window 3', self)
        Reset3.resize(Reset3.sizeHint()) 
        Reset3.clicked.connect(self.R3)
        grid.addWidget(Reset3, 2,4,1,1)
        
        Reset4 = QtGui.QPushButton('Reset error in window 4', self)
        Reset4.resize(Reset4.sizeHint()) 
        Reset4.clicked.connect(self.R4)
        grid.addWidget(Reset4, 2,5,1,1)

#   From here i define all functions that will be called using the buttons on the tabs

#       This function will plot the recorded error, # specified by the user.
    def Perror(self):
        plt.cla()
        xerror=[]
        yerror=[]
        errorinfo.clear()
        errorinfo.insertPlainText("The recorded error will be displayed below in the format\ntime,value,errornumber\n\n")
        global errorwanted;
        errorwanted=errorvalue.text()
        if not errorwanted:
            errorinfo.clear()
            errorinfo.insertPlainText("Please insert an integer of the error you would like to display")
        else:
            try:
                with open('Error-Testfile.txt','r') as ff:
                    for line in ff:
                        line = line.rstrip()
                        if line.endswith(","+errorwanted):
                            errorinfo.insertPlainText(line)
                            errorinfo.insertPlainText("\n")
                            xe,ye,num=line.split(',')
                            xerror.append(xe)
                            yerror.append(ye)
                    errorwindow=self.errorplot.add_subplot(111)
                    errorwindow.set_title(str(xerror[0])+'    recorded: '+str(xerror[1])+', '+str(yerror[1]),fontweight="bold", size=32) # Title
                    errorwindow.set_ylabel(yerror[0], fontsize = 30) # Y label
                    errorwindow.set_xlabel('real time', fontsize = 30) # X label
                    xerror.pop(0)
                    xerror.pop(0)
                    yerror.pop(0)
                    yerror.pop(0)
                    errorwindow.plot(xerror,yerror,'ro-')
                    self.errorcanvas.draw()
            except:
                errorinfo.insertPlainText("\n\n ERROR: You have chosen an error number larger than amount of errors recorded")

#       Updates # of recorded errors                    
    def Uerror(self):
        errordisplay.clear()
        errordisplay.setText("recorded errors  =  " + str(recorded_errors))

#       Resets the face color to green on button click, after potential error (figures tab 1)    
    def R1(self):
        f1.patch.set_alpha(0.50)
        f1.set_facecolor('lime')      
    def R2(self):
        f2.patch.set_alpha(0.50)
        f2.set_facecolor('lime')      
    def R3(self):
        f3.patch.set_alpha(0.50)
        f3.set_facecolor('lime')      
    def R4(self):
        f4.patch.set_alpha(0.50)
        f4.set_facecolor('lime')
    
#       The following plot functions will plot the last 200 HK datapoints from a file
    def plot1(self):
        self.figure.clf()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs1[-200:],ys1[-200:],'bo-')
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('Temperature of... plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Temperature Celcius?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()
    
    def plot2(self):
        self.figure.clf()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs2[-200:],ys2[-200:],'mo-')
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('Voltage of... plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Voltage?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()


    def plot3(self):
        self.figure.clf()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs3[-200:],ys3[-200:],'ko-')
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('More?... plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Random?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()
        
    def plot4(self):
        self.figure.clf()
        mainwindow=self.figure.add_subplot(111)
        mainwindow.plot(xs4[-200:],ys4[-200:],'yo-')
        
        timeofday=datetime.datetime.now().strftime("%I:%M%p on %B %d, %Y")    
        mainwindow.set_title('HK-DATA4. plottet:     '+timeofday,fontweight="bold", size=20) # Title
        mainwindow.set_ylabel('Random?', fontsize = 20.0) # Y label
        mainwindow.set_xlabel('Maybe real time?', fontsize = 20) # X label
        self.canvas.draw()   
    
#   The main function that will initiate the GUI and run the animation functions continuoesly      
def main():
    app = QtGui.QApplication(sys.argv)
    w = PrettyWidget()
    
#   The animation.FuncAnimation runs the function animate1,2,3,4 (Which will plot the live HK data) every interval.    
    animate1(1); animate2(1); animate3(1); animate4(1)
    ani1 = animation.FuncAnimation(f1, animate1, interval=2000)
    ani2 = animation.FuncAnimation(f2, animate2, interval=2000)
    ani3 = animation.FuncAnimation(f3, animate3, interval=2000)
    ani4 = animation.FuncAnimation(f4, animate4, interval=2000)
    
#   Used to initialize the main event loop that waits for usercommands (events) in the GUI.
    app.exec_()

#   makes sure that the main entry point is my defined main function.
if __name__ == '__main__':
    main()