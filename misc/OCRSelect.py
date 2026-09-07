from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import Qt, QPoint, QRect, QRectF, QThread
from PyQt5.QtGui import QPixmap, QImage, QPainter, QPen, QColor


import sys
import time
import numpy as np

import win32gui
import win32ui
import win32con
from ctypes import windll
from pynput.mouse import Listener

import cv2
from PIL import Image

from GDI_func import enumHandler
from GDI_func import RectObj
from SelectArea import SelectArea


class SelectionMask(QThread, QMainWindow):
    def __init__(self):
        super().__init__()
        self.InitialParam()
        self.WholeWindowSnap()
        self.ShowMask()

    def InitialParam(self):
        self.is_snipping=True
        self.begin = QPoint()
        self.end = QPoint()

    # Find EC-Lab hwnd, get rect.
    def WholeWindowSnap(self):
        #Enumerate and get window handle related to the keyword given
        global param
        self.winHwnd=0
        winKeyword='experiment'
        param=[winKeyword,self.winHwnd]
        win32gui.EnumWindows(enumHandler,param)
        self.winHwnd=param[1]
        #Show and bring the target window to front
        win32gui.ShowWindow(self.winHwnd,win32con.SW_SHOWNA)
        win32gui.SetForegroundWindow(self.winHwnd)
        #Get window rectangel params and create memory DC to copy bitmap image and save it as np.array
        self.winRect=RectObj(*win32gui.GetWindowRect(self.winHwnd))
        self.cliRect=RectObj(*win32gui.GetClientRect(self.winHwnd))
        winDCHwnd = win32gui.GetWindowDC(self.winHwnd)
        newDC  = win32ui.CreateDCFromHandle(winDCHwnd)
        memoDC = newDC.CreateCompatibleDC()
        winBitMap = win32ui.CreateBitmap()
        winBitMap.CreateCompatibleBitmap(newDC, self.winRect.width, self.winRect.height)
        memoDC.SelectObject(winBitMap)
        result = windll.user32.PrintWindow(self.winHwnd, memoDC.GetSafeHdc(),2)
        bmpinfo = winBitMap.GetInfo()
        self.bmparray = np.asarray(winBitMap.GetBitmapBits(), dtype=np.uint8)
        #winRect and cliRect error calculation:
        relaPos=win32gui.ClientToScreen(self.winHwnd,(self.cliRect.left,self.cliRect.top))
        self.xErr=self.winRect.left-relaPos[0]
        self.yErr=self.winRect.top-relaPos[1]

    # Show semi-transparent mask
    def ShowMask(self):
        self.setWindowFlags(Qt.WindowStaysOnTopHint | Qt.FramelessWindowHint)
        self.setWindowOpacity(0.5)
        self.setWindowTitle('Mask')
        self.setStyleSheet("background-color: Gray;")
        self.show()
        pyhwnd=0
        winKeyword='Mask'
        param=[winKeyword,pyhwnd]
        win32gui.EnumWindows(enumHandler,param)
        pyhwnd=param[1]
        print(pyhwnd)
        winLong=win32gui.GetWindowText(pyhwnd)
        print(winLong)
        win32gui.MoveWindow(pyhwnd,self.winRect.left,self.winRect.top,self.winRect.width,self.winRect.height,True)
    
    def ScreenshotCrop(self):
        
        #Get absolute coordinates (relative to display device cordinates) of the selected area
        #Error calculated because the whole screentshot has a black border of usually 8 pixels
        x1,y1=win32gui.ClientToScreen(self.winHwnd,(self.screenshotCliRect.left,self.screenshotCliRect.top))
        x2,y2=win32gui.ClientToScreen(self.winHwnd,(self.screenshotCliRect.right,self.screenshotCliRect.bottom))
        x1+=self.xErr
        x2+=self.xErr
        y1+=self.yErr
        y2+=self.yErr
        self.screenshotWinRect=RectObj(x1,y1,x2,y2)
        
        #The whole screenshot array from 1D array to 2D
        bmp2DArray=np.reshape(self.bmparray,(-1,self.winRect.width*4))
        initRow=self.screenshotWinRect.top-self.winRect.top
        finaRow=initRow+self.screenshotWinRect.height
        initCol=(self.screenshotWinRect.left-self.winRect.left)*4
        finaCol=(self.screenshotWinRect.left-self.winRect.left+self.screenshotWinRect.width)*4
        #Screenshot area 2D array
        output2DArray=bmp2DArray[initRow:finaRow,initCol:finaCol]
        outputArray=output2DArray.flatten()
        #Save selected screenshot
        imRGB = Image.frombuffer('RGB', (self.screenshotWinRect.width,self.screenshotWinRect.height), outputArray, 'raw', 'BGRX', 0, 1)
        arrayRGB = np.array(imRGB)
        imBGR = cv2.cvtColor(arrayRGB, cv2.COLOR_RGB2BGR)
        cv2.imwrite('origin.png',imBGR)

    # Draw drag rectangle
    def paintEvent(self, event):
        if self.is_snipping is True:
            brush_color = (255, 255, 255, 255)
            lw = 3
            opacity = 1
        else:
            # reset points, so the rectangle won't show up again.
            self.begin = QPoint()
            self.end = QPoint()
            brush_color = (0, 0, 0, 0)
            lw = 0
            opacity = 0
        # self.setWindowOpacity(opacity)
        qp = QPainter(self)
        qcolor=QColor()
        qcolor.setRgb(255,100,0)
        qp.setPen(QPen(qcolor, lw))
        qp.setBrush(QColor(*brush_color))
        rect = QRectF(self.begin, self.end)
        qp.drawRect(rect)

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.is_snipping = False
        QApplication.restoreOverrideCursor()
        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())
        self.screenshotCliRect=RectObj(x1,y1,x2,y2) #used in self.ScreenshotCrop()
        self.repaint()
        self.close()
        self.ScreenshotCrop()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            print('keypressed')
        if event.key() == Qt.Key_Escape:
            self.close()
        event.accept()


if __name__=='__main__':
    Qapp=QApplication(sys.argv)
    app=SelectionMask()
    sys.exit(Qapp.exec_())