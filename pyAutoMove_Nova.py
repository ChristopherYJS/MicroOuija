import typing
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QToolButton
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from FileMonitor import FileMonitor
from PrintException import print_ex

import sys

class AutoMoveWin(QWidget):
    def __init__(self,mainwin) -> None:
        super().__init__()
        self.mainwin=mainwin
        self.ui=uic.loadUi('uiAutoMove_Nova.ui',self)
        self.SignalSlotBind()
        self.Restyle()
        self.setWindowTitle('AutoMove')
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
        self.toolButton_MF.clicked.connect(self.MonitorFileSelect)
        self.pushButton_start.clicked.connect(self.FileMonitorActivate)
        self.pushButton_stop.clicked.connect(self.FileMonitorDeactivate)

    def MonitorFileSelect(self):
        self.filepath=QFileDialog.getOpenFileName(self,'Select File To Monitor', r'D:\OneDrive - University of Southampton\PhD\Second Project\Electrochemistry')[0]
        self.lineEdit_MF.setText(f'{self.filepath}')

    def FileMonitorActivate(self):
        def RefreshMove(dis):
            dis=dis/1000
            self.mainwin.mpThread.RefreshMove(2,dis)
        def ParamRead():
            self.monitorThread.boundary1=self.lineEdit_CC1.text()
            self.monitorThread.boundary2=self.lineEdit_CC2.text()
            self.monitorThread.boundary3=self.lineEdit_CC3.text()
            self.monitorThread.average_boundary=self.lineEdit_AB.text()
            self.monitorThread.bulk_current_index=self.lineEdit_BCI.text()
        def MainReact(string):
            self.mainwin.LogInfo(string)

        self.monitorThread=FileMonitor(self.filepath)
        self.monitorThread.sig_refresh.connect(RefreshMove)
        self.monitorThread.sig_read.connect(ParamRead)
        self.monitorThread.sig_main.connect(MainReact)
        self.monitorThread.run()

    def FileMonitorDeactivate(self):
        if hasattr(self,'monitorThread'):
            self.monitorThread.terminate()
            del self.monitorThread
        else:
            print('File Monitor Thread not Activated!')

if __name__=='__main__':
    try:
        Qapp=QApplication(sys.argv)
        app=AutoMoveWin(1)
        sys.exit(Qapp.exec_())
    except Exception as ex:
        print_ex(ex)