from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pyOCRCrop import *
from pyOCRAnalysis import *

import pandas as pd
import time

class OCRThread(QThread):
    sig_move=pyqtSignal(list)
    sig_loginfo=pyqtSignal(str)
    sig_logerror=pyqtSignal(object)
    sig_changeTech=pyqtSignal(str)
    sig_relaxmove=pyqtSignal()
    sig_complete=pyqtSignal()
    sig_loopComplete=pyqtSignal(float)
    sig_uiChange=pyqtSignal(str)
    def __init__(self,mapwin,xList,yList,zList,triggerList,num3d):
        try:
            super().__init__()
            self.mapwin=mapwin
            self.xList=xList
            self.yList=yList
            self.zList=zList
            self.triggerList=triggerList
            self.num3d=num3d
            self.count=0
            self.flag=False
            self.df=pd.DataFrame()
            self.currentTechnum=''
        except Exception as ex:
            print_ex(ex)

    def run(self):
        try:
            #X-axis
            for i in range(len(self.xList)):
                if i==0:
                    xdif=self.xList[i]-0
                else:
                    xdif=self.xList[i]-self.xList[i-1]
                if xdif!=0:
                    self.sig_move.emit([0,xdif/1000])
                #Y-axis
                for j in range(len(self.yList)):
                    if j==0 and i==0:
                        ydif=self.yList[j]-0
                    elif j==0 and i!=0:
                        ydif=self.yList[0]-self.yList[-1]
                    else:
                        ydif=self.yList[j]-self.yList[j-1]
                    if ydif!=0:
                        self.sig_move.emit([1,ydif/1000])
                    #Z-axis
                    for k in range(len(self.zList)):
                        if k==0 and j==0 and i==0   :
                            zdif=self.zList[k]-0
                        elif k==0 and ((j or i)!=0):
                            zdif=self.zList[0]-self.zList[-1]
                        else:
                            zdif=self.zList[k]-self.zList[k-1]
                        if zdif!=0:
                            self.sig_move.emit([2,zdif/1000])
                        #start OCR moniter
                        if (i==len(self.xList)-1) and (j==len(self.yList)-1) and (k==len(self.zList)-1):
                            self.flag=True
                            self.sig_complete.emit()
                        else:
                            self.count+=1
                            self.sig_loopComplete.emit(float(format(self.count/self.num3d,'.2f'))*100)
                            # print(float(format(self.count/self.num3d,'.1f')))
                            self.sig_loginfo.emit(f'({self.xList[i]}, {self.yList[j]}, {self.zList[k]}) done.')
                            self.flag=False
                            while self.flag is False:
                                self.OCRMoniter()
                                time.sleep(0.1)
        except Exception as ex:
            print_ex(ex)
            self.sig_loginfo.emit('MoveThread Error.')

    def OCRMoniter(self):
        try:
            self.imBGR=WholeWindowSnap(self.mapwin.ocrmask.screenshotCliRect,self.mapwin.ocrmask.xErr,self.mapwin.ocrmask.yErr)
            self.resList=list(OCRAnalysis(self.imBGR))
            for i in range(len(self.resList)):
                self.df[i]=self.resList[i]
            index=self.df.index[self.df[0]].tolist()
            if index != []:
                index=index[0]
                #if Tech number changed:
                if self.currentTechnum!=f'{self.df.loc[index,1]}':
                    self.currentTechnum=f'{self.df.loc[index,1]}'
                    # if self.mapwin.mainwin.mcThread!=None:
                        # self.sig_changeTech.emit(f'{self.currentTechnum}.{self.df.loc[index,1]}')
                    if self.currentTechnum==f'{self.triggerList[0]}':
                        self.sig_relaxmove.emit()
                    elif self.currentTechnum==f'{self.triggerList[1]}':
                        self.flag=True
        except Exception as ex:
            print_ex(ex)
