from traceback import print_tb
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QComboBox
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QProgressBar
from PyQt5.QtWidgets import QLabel
from  PyQt5.QtWidgets import QSizePolicy
from  PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pyOCRMask import OCRMask
from pyOCRThread import OCRThread
from pyOCRCrop import *
from pyOCRAnalysis import *
from PrintException import print_ex

import sys
import pandas as pd
import re

class MappingWin(QWidget):
    sig_trigger1=pyqtSignal(object)
    sig_trigger2=pyqtSignal(object)
    sig_info=pyqtSignal(str)
    def __init__(self,mainwin):
        try:
            super().__init__()
            self.mainwin=mainwin
            self.ocrmask=None
            self.ocrThread=None
            self.progressbar=None
            self.LoadUi()
            self.Restyle()
            self.SignalSlotBinding()
            self.show()
        except Exception as ex:
            print_ex(ex)

    def LoadUi(self):
        self.ui=uic.loadUi('uiMappingWin.ui',self)

    def SignalSlotBinding(self):
        self.pushButton_OCR_tab1.clicked.connect(self.OCRMaskSlot)
        self.pushButton_proceed_tab1.clicked.connect(self.ExpProceed)
        self.lineEdit_xp_tab1.editingFinished.connect(self.ExpNum)
        self.lineEdit_yp_tab1.editingFinished.connect(self.ExpNum)
        self.combo_zp_tab1.lineEdit().editingFinished.connect(self.ExpNum)
        self.toolButton_cf_tab2_2.clicked.connect(self.select_folder)
    
    def Restyle(self):
        self.resize(600,300)
        self.combo_zp_tab1.addItem('0,500,1000,1200,1500,1600,1700,1800,1900,1920,1940,1950,1955,1960,1965,1970,1975,1980,1982,1984,1986,1988,1990,1992,1994,1996,1998,2000,2002,2004,2006,2008,2010')
        self.combo_zp_tab1.addItem('0, -500, -1000, -1200, -1500, -1600, -1700, -1800, -1900, -1920, -1940, -1950, -1955, -1960, -1965, -1970, -1975, -1980, -1982, -1984, -1986, -1988, -1990, -1992, -1994, -1996, -1998, -2000, -2002, -2004, -2006, -2008, -2010')
        self.combo_zp_tab3.addItem('0, -500, -1000, -1200, -1500, -1600, -1700, -1800, -1900, -1920, -1940, -1950, -1955, -1960, -1965, -1970, -1975, -1980, -1982, -1984, -1986, -1988, -1990, -1992, -1994, -1996, -1998, -2000, -2002, -2004, -2006, -2008, -2010')

    def OCRMaskSlot(self):
        try:
            if self.ocrmask is None:
                self.ocrmask=OCRMask(self.mainwin)
                self.ocrmask.GetECLab()
                self.ocrmask.ShowMask()
            else:
                self.ocrmask=None
                self.ocrmask=OCRMask(self.mainwin)
                self.ocrmask.GetECLab()
                self.ocrmask.ShowMask()
        except Exception as ex:
            print_ex(ex)

    def OCRThreadSlot(self):
        try:
            self.ocrThread=OCRThread(self,self.xList,self.yList,self.zList,self.triggerList,self.num3d)
            self.ocrThread.sig_move.connect(self.mainwin.mpThread.AutoMove)
            self.ocrThread.sig_loginfo.connect(self.mainwin.LogInfo)
            self.ocrThread.sig_changeTech.connect(self.ChangeTech)
            self.ocrThread.sig_relaxmove.connect(self.RelaxMove)
            self.ocrThread.sig_complete.connect(self.ExpComplete)
            self.ocrThread.sig_loopComplete.connect(self.LoopComplete)
            self.ocrThread.sig_uiChange.connect(self.change_ui)
            self.ocrThread.start()
        except Exception as ex:
            print_ex(ex)


    def ExpProceed(self):
        try:
            if self.ocrmask is not None:
                if self.ocrThread is None:
                    self.xList=self.list_read(self.lineEdit_xp_tab1)
                    self.yList=self.list_read(self.lineEdit_yp_tab1)
                    self.zList=self.list_read(self.combo_zp_tab1)
                    self.triggerList=self.list_read(self.lineEdit_tt_tab1)
                    self.mainwin.LogInfo([self.xList,self.yList,self.zList,self.triggerList])
                    self.SetProgressBar()
                    self.OCRThreadSlot()
                else:
                    self.ocrThread.terminate()
                    self.ocrThread.wait()
                    self.ocrThread=None
                    self.progressbar.hide()
                    self.progresslabel.hide()

                    QApplication.processEvents()
            else:
                self.mainwin.LogInfo('OCR region not selected.')
        except Exception as ex:
            print_ex(ex)


    def ExpComplete(self):
        try:
            self.mainwin.LogInfo('Experiment finished')
            self.ocrThread=None
            self.progressbar.hide()
            self.progresslabel.hide()
        except Exception as ex:
            print_ex(ex)

    def ChangeTech(self,tech):
        try:
            self.mainwin.mcThread.tech=tech
        except Exception as ex:
            print_ex(ex)


    def RelaxMove(self):
        try:
            self.mainwin.mpThread.Movement1(2)
        except Exception as ex:
            print_ex(ex)


    def ExpNum(self):
        try:
            self.xList=self.list_read(self.lineEdit_xp_tab1)
            self.yList=self.list_read(self.lineEdit_yp_tab1)
            self.zList=self.list_read(self.combo_zp_tab1)
            self.num3d=len(self.xList)*len(self.yList)*len(self.zList)
            self.num2d=len(self.xList)*len(self.yList)
            self.lineEdit_3d_tab1.setText(f'{self.num3d}')
            self.lineEdit_2d_tab1.setText(f'{self.num2d}')
        except Exception as ex:
            print_ex(ex)

    def SetProgressBar(self):
        try:
            if self.progressbar is None:
                self.progressbar=QProgressBar()
                self.progressbar.setValue(0)
                self.progressbar.setAlignment(Qt.AlignCenter)
                self.progresslabel=QLabel()
                self.progresslabel.setText(
                    'Approach Curve experiments running. Do not close this window while running! '
                    )
                self.progresslabel.setStyleSheet('color: rgb(255, 80, 0)')
                self.progresslabel.setAlignment(Qt.AlignCenter)
                sizePolicy=QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
                self.progresslabel.setSizePolicy(sizePolicy)
                self.verticalLayout.addWidget(self.progressbar)
                self.verticalLayout.addWidget(self.progresslabel)
            else:
                self.progressbar.show()
                self.progresslabel.show()
        except Exception as ex:
            print_ex(ex)

    def LoopComplete(self,percent):
        try:
            self.progressbar.setValue(percent)
        except Exception as ex:
            print_ex(ex)

    def change_ui(self,text):
        eval(text)

    def list_read(self,widget,tlist=[],ty=int):
        try:
            if type(widget)==QLineEdit:
                string=widget.text()
            elif type(widget)==QComboBox:
                string=widget.currentText()
            res=[]
            element=string.split(",")
            sets=[]
            num=[]
            for ele in element:
                if '(' in ele:
                    sets.append(ele)           
                else:
                    num.append(ty(ele))
            res+=num
            for i in sets:
                numset=re.findall(r'[(](.*?)[)]', i)
                rangepara=numset[0].split(' ')
                rangepara=list(map(ty, rangepara))
                res+=np.arange(rangepara[0],rangepara[1]+1,rangepara[2]).tolist()
            tlist[:]=res
            return res
        except Exception as ex:
            print_ex(ex)

    def select_folder(self):
        self.dir=QFileDialog.getExistingDirectory(None, 'Select a folder:', r'D:\OneDrive - University of Southampton\PhD\Second Project\Electrochemistry', QFileDialog.ShowDirsOnly)
        self.lineEdit_ef_tab3.setText(self.dir)


if __name__ =='__main__':
    Qapp=QApplication(sys.argv)
    mainwin=QMainWindow()
    app=MappingWin(mainwin)
    sys.exit(Qapp.exec_())
