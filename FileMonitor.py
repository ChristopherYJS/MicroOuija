from PyQt5.QtGui import *
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer

import os
import re
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import time

class FileMonitor(QThread):
    sig_refresh=pyqtSignal(int)
    sig_read=pyqtSignal()
    sig_main=pyqtSignal(str)
    boundary1=boundary2=boundary3=average_boundary=bulk_current_index=None
    timer=QTimer()
    def __init__(self,filepath) -> None:
        super().__init__()
        
        self.filepath=filepath
        self.path=os.path.dirname(self.filepath)
    def run(self):
        self.flag=True
        self.indexlist=[]
        self.currentlist=[]
        self.dlesscurrentlist=[]
        rulist=[]
        self.modifiedOn=os.path.getmtime(self.filepath)
        self.timer.timeout.connect(self.Loop)
        self.timer.start(100)
        self.sig_main.emit('automove start')
        self.fig,self.ax=plt.subplots()
        plt.show()
    def Loop(self):
        modified = os.path.getmtime(self.filepath)
        if modified !=self.modifiedOn:
            #once find file modified, read lineEdits
            self.sig_read.emit()
            self.sig_main.emit(f'{[self.boundary1,self.boundary2,self.boundary3]}')
            self.modifiedOn=modified
            filelist=os.listdir(self.path)
            for file in filelist:
                if 'AppCurve-CV' in file:
                    # print(file)
                    try:
                        index=re.findall(r'.*\(Sat\)-\((\d+)\).txt',file)[0]
                        # print(index)
                    except IndexError:
                        continue
                    if int(index) not in self.indexlist:
                        self.indexlist.append(int(index))
                        df=pd.read_csv(rf'{self.path}/{file}',delimiter='\t')
                        df.columns=range(len(df.columns))
                        # print(df)
                        iave=np.average(df.loc[df[0]>float(self.average_boundary),1])
                        self.currentlist.append(iave*10**9)

            ndf=pd.DataFrame()
            ndf['col0']=self.indexlist
            ndf['col1']=self.currentlist
            ndf2=ndf.sort_values(by=['col0'],ignore_index=True)
            ndf2['col2']=ndf2.loc[:,'col1']/ndf2.loc[int(self.bulk_current_index),'col1']
            plot=self.ax.plot(ndf2['col0'],ndf2['col2'],'.')

            if self.ax.figure.canvas.manager.window is None:
                plt.show()
            else:
                plt.pause(0.01)
            if ndf2.loc[len(ndf2['col2'])-1,'col2']<=float(self.boundary1):
                self.sig_main.emit(f'Moving down by 0.01')
                self.sig_refresh.emit(10)
            elif  ndf2.loc[len(ndf2['col2'])-1,'col2']<=float(self.boundary2):
                self.sig_main.emit(f'Moving down by 0.005')
                self.sig_refresh.emit(5)
            elif  ndf2.loc[len(ndf2['col2'])-1,'col2']<=float(self.boundary3):
                self.sig_main.emit(f'Moving down by 0.002')
                self.sig_refresh.emit(2)
            else:
                self.sig_main.emit(f'Moving down by 0.001')
                self.sig_refresh.emit(1)


                



