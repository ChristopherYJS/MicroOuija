from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import win32gui
import win32con
from ctypes import windll

import sys
import numpy as np

from GDI_func import enumHandler
from GDI_func import RectObj
from pyOCRAnalysis import *
from pyOCRCrop import *

class OCRMask(QMainWindow):
    sig_complete=pyqtSignal(object)
    def __init__(self,mainwin):
        try:
            super().__init__()
            self.mainwin=mainwin
            self.InitialParam()
        except Exception as ex:
            print_ex(ex)

    def InitialParam(self):
        self.is_snipping=True
        self.begin = QPoint()
        self.end = QPoint()

    def GetECLab(self):
        try:
            #Enumerate and get window handle related to the keyword given
            global param
            self.winHwnd=0
            winKeyword='experiment'
            param=[winKeyword,self.winHwnd]
            win32gui.EnumWindows(enumHandler,param)
            self.winHwnd=param[1]
            #Show and bring the target window to front
            win32gui.ShowWindow(self.winHwnd,win32con.SW_MAXIMIZE)
            # win32gui.SetForegroundWindow(self.winHwnd)
            #Get window rectangel params and calculate margin 
            self.winRect=RectObj(*win32gui.GetWindowRect(self.winHwnd))
            self.cliRect=RectObj(*win32gui.GetClientRect(self.winHwnd))
            relaPos=win32gui.ClientToScreen(self.winHwnd,(self.cliRect.left,self.cliRect.top))
            self.xErr=self.winRect.left-relaPos[0]
            self.yErr=self.winRect.top-relaPos[1]
        except Exception as ex:
            print_ex(ex)

    # Show semi-transparent mask
    def ShowMask(self):
        try:
            self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
            self.setWindowOpacity(0.5)
            self.setWindowTitle('MaskWindow')
            self.setStyleSheet("background-color: Gray;")
            self.show()
            pyhwnd=0
            winKeyword='MaskWindow'
            param=[winKeyword,pyhwnd]
            win32gui.EnumWindows(enumHandler,param)
            pyhwnd=param[1]
            print(pyhwnd)
            winLong=win32gui.GetWindowText(pyhwnd)
            print(winLong)
            win32gui.SetWindowPos(pyhwnd,win32con.HWND_TOP,self.winRect.left,self.winRect.top,self.winRect.width,self.winRect.height,win32con.SWP_SHOWWINDOW)
        except Exception as ex:
            print_ex(ex)

    # Draw drag rectangle
    def paintEvent(self, event):
        try:
            if self.is_snipping is True:
                brush_color = (255, 255, 255, 255)
                lw = 3
            else:
                self.begin = QPoint()
                self.end = QPoint()
                brush_color = (0, 0, 0, 0)
                lw = 0

            qp = QPainter(self)
            qcolor=QColor()
            qcolor.setRgb(255,100,0)
            qp.setPen(QPen(qcolor, lw))
            qp.setBrush(QColor(*brush_color))
            rect = QRectF(self.begin, self.end)
            qp.drawRect(rect)
        except Exception as ex:
            print_ex(ex)

    def mousePressEvent(self, event):
        try:
            self.begin = event.pos()
            self.end = self.begin
            self.update()
        except Exception as ex:
            print_ex(ex)

    def mouseMoveEvent(self, event):
        try:
            self.end = event.pos()
            self.update()
        except Exception as ex:
            print_ex(ex)

    def mouseReleaseEvent(self, event):
        try:
            self.is_snipping = False
            QApplication.restoreOverrideCursor()
            x1 = min(self.begin.x(), self.end.x())
            y1 = min(self.begin.y(), self.end.y())
            x2 = max(self.begin.x(), self.end.x())
            y2 = max(self.begin.y(), self.end.y())
            self.screenshotCliRect=RectObj(x1,y1,x2,y2)
            self.repaint()
            self.close()
            self.imBGR=WholeWindowSnap(self.screenshotCliRect,self.xErr,self.yErr)
            cv2.imwrite(r"default\OCR\Origin.png",self.imBGR)
            self.resList=OCRAnalysis(self.imBGR)
            self.mainwin.LogInfo(self.resList)
        except Exception as ex:
            print_ex(ex)


    def keyPressEvent(self, event):
        try:
            if event.key() == Qt.Key_Escape:
                self.close()
            event.accept()
        except Exception as ex:
            print_ex(ex)


if __name__=='__main__':
    Qapp=QApplication(sys.argv)
    app=OCRMask()
    sys.exit(Qapp.exec_())