from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import *
from PyQt5 import uic

from PrintException import print_ex, print_log

from matplotlib import pyplot as plt
import pandas as pd
import numpy as np
import os
import re
import sys
import pdb

class Subwin_AppCurveGenerator(QWidget):
    def __init__(self,mainwin) -> None:
        super().__init__()
        self.mainwin=mainwin
        self.fig,self.ax=plt.subplots()
        self.ax2 = self.ax.twinx()
        self.ui=uic.loadUi('uiPathInput.ui',self)
        self.Restyle()
        self.SignalSlotBind()
        self.show()
        
    def Restyle(self):
        self.setStyleSheet("background-color: rgb(20, 20, 20)")
        for widget in self.findChildren(QPushButton):
            widget.setStyleSheet("QPushButton{font-family:Roboto;font-style: normal;font-size: 12pt;background-color:rgb(40, 40, 40);color:rgb(220, 220, 220);} QPushButton:hover{background-color:rgb(255, 80, 0);color:rgb(20, 20, 20);}")
        for widget in self.findChildren(QToolButton):
            widget.setStyleSheet("QToolButton{font-family:Roboto;font-style: normal;font-size: 12pt;color:rgb(220, 220, 220);}QToolButton:hover{background-color:rgb(255, 80, 0);color:rgb(20, 20, 20);}")
        for widget in self.findChildren(QLabel):
            widget.setStyleSheet("QLabel{font-family:Roboto;font-style: normal;font-size: 12pt;color:rgb(220, 220, 220);}")
            widget.setAlignment(Qt.AlignCenter)
        for widget in self.findChildren(QLineEdit):
            widget.setStyleSheet("QLineEdit{background-color: rgb(40,40,40);color: rgb(220,220,220); font-family:Roboto; font-size:10pt;}")    
    def SignalSlotBind(self):
        self.pushButton.clicked.connect(self.PlotCalculate)
        self.pushButton_M1.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,-0.005))
        self.pushButton_M2.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,-0.002))
        self.pushButton_M3.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,-0.001))
        self.pushButton_M4.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,-0.0005))
        self.pushButton_M5.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,0.005))
        self.pushButton_M6.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,0.002))
        self.pushButton_M7.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,0.001))
        self.pushButton_M8.clicked.connect(lambda: self.mainwin.mpThread.RefreshMove(2,0.0005))
        self.toolButton.clicked.connect(self.GetPath)
        
    # def TimerStart(self):
    #     self.Read()
    #     self.fig,self.ax=plt.subplots()
    #     self.ax2 = self.ax.twinx()
    #     plt.show()
    #     self.filelist=os.listdir(self.path) 
    #     self.indexilist=[]
    #     self.indexrlist=[]
    #     self.ilist=[]
    #     self.dilist=[]
    #     self.rulist=[]
    #     self.drulist=[]
    #     self.timer=QTimer()
    #     self.timer.timeout.connect(self.PlotCalculate)
    #     self.timer.start(100)
    #     print(self.timer.isActive())

    def GetPath(self):
        path=QFileDialog.getExistingDirectory(self,'Select File To Monitor')
        self.lineEdit_FM.setText(path)

    def Read(self):
        self.path=self.lineEdit_FM.text()
        self.boundary=float(self.lineEdit_BA.text())
        self.bulkcurrentindex=int(self.lineEdit_DS.text())

    def PlotCalculate(self):
        self.ax.clear()
        self.ax2.clear()
        self.indexilist=[]
        self.indexrlist=[]
        self.ilist=[]
        self.dilist=[]
        self.rulist=[]
        self.drulist=[]
        self.Read()
        filelist=os.listdir(self.path)
        for file in filelist:
            file=f'{self.path}\{file}'
            if 'AppCurve-CA' in file:
                try:
                    index=re.findall(r'.*\(Sat\)-\((\d+)\).txt',file)[0]
                    self.indexilist.append(int(index))
                    dfi=pd.read_csv(file,delimiter='\t')
                    dfi.columns=range(len(dfi.columns))
                    iave=np.average(dfi.loc[dfi[0]>self.boundary,1])
                    self.ilist.append(iave*10**9)
                except IndexError:
                    continue
            elif 'AppCurve-EIS' in file:
                try:
                    index=re.findall(r'.*\(Sat\)-\((\d+)\).txt',file)[0]
                    self.indexrlist.append(int(index))
                    dfr=pd.read_csv(file,delimiter='\t')
                    dfr.columns=range(len(dfr.columns))
                    ru=dfr.loc[0,1]
                    self.rulist.append(ru)
                except IndexError:
                    continue
            
        dfires=pd.DataFrame()
        dfires['col0']=self.indexilist
        dfires['col1']=self.ilist
        dfires2=dfires.sort_values(by=['col0'],ignore_index=True)
        dfires2['col2']=dfires2.loc[:,'col1']/dfires2.loc[self.bulkcurrentindex-1,'col1']
        
        dfrures=pd.DataFrame()
        dfrures['col0']=self.indexrlist
        dfrures['col1']=self.rulist
        dfrures2=dfrures.sort_values(by=['col0'],ignore_index=True)
        
        dfrures2['col2']=dfrures2.loc[:,'col1']/dfrures2.loc[self.bulkcurrentindex-1,'col1']
        plt1=self.ax.plot(dfires2['col0'],dfires2['col2'],'.',color='red')
        plt2=self.ax2.plot(dfrures2['col0'],dfrures2['col2'],'.',color='blue')
        
        plt.pause(0.05)
        self.fig.show()

if __name__=='__main__':
    try:
        Qapp=QApplication(sys.argv)
        app=Subwin_AppCurveGenerator(1)
        sys.exit(Qapp.exec_())
    except Exception as ex:
        print_ex(ex)
