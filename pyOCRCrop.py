from PyQt5.QtCore import *
from PyQt5.QtGui import *

import win32gui
import win32ui
import win32con
from ctypes import windll

import numpy as np
import cv2
from PIL import Image

from GDI_func import RectObj
from GDI_func import enumHandler
from PrintException import print_ex

def WholeWindowSnap(screenshotCliRect,xErr,yErr):
    try:
        #Enumerate and get window handle related to the keyword given
        global param
        winHwnd=0
        winKeyword='experiment'
        param=[winKeyword,winHwnd]
        win32gui.EnumWindows(enumHandler,param)
        winHwnd=param[1]
        #Show and bring the target window to front
        # win32gui.ShowWindow(winHwnd,win32con.SW_SHOWNA)
        # win32gui.SetForegroundWindow(winHwnd)
        #Get window rectangel params and create memory DC to copy bitmap image and save it as np.array
        winRect=RectObj(*win32gui.GetWindowRect(winHwnd))
        cliRect=RectObj(*win32gui.GetClientRect(winHwnd))
        winDCHwnd = win32gui.GetWindowDC(winHwnd)
        newDC  = win32ui.CreateDCFromHandle(winDCHwnd)
        memoDC = newDC.CreateCompatibleDC()
        winBitMap = win32ui.CreateBitmap()
        winBitMap.CreateCompatibleBitmap(newDC, winRect.width, winRect.height)
        memoDC.SelectObject(winBitMap)
        result = windll.user32.PrintWindow(winHwnd, memoDC.GetSafeHdc(),2)
        bmpinfo = winBitMap.GetInfo()
        bmparray = np.asarray(winBitMap.GetBitmapBits(), dtype=np.uint8)
        #Get absolute coordinates (relative to display device cordinates) of the selected area
        #Error calculated because the whole screentshot has a black border of usually 8 pixels
        x1,y1=win32gui.ClientToScreen(winHwnd,(screenshotCliRect.left,screenshotCliRect.top))
        x2,y2=win32gui.ClientToScreen(winHwnd,(screenshotCliRect.right,screenshotCliRect.bottom))
        x1+=xErr
        x2+=xErr
        y1+=yErr
        y2+=yErr
        screenshotWinRect=RectObj(x1,y1,x2,y2)
        #The whole screenshot array from 1D array to 2D
        bmp2DArray=np.reshape(bmparray,(-1,winRect.width*4))
        initRow=screenshotWinRect.top-winRect.top
        finaRow=initRow+screenshotWinRect.height
        initCol=(screenshotWinRect.left-winRect.left)*4
        finaCol=(screenshotWinRect.left-winRect.left+screenshotWinRect.width)*4
        #Screenshot area 2D array
        output2DArray=bmp2DArray[initRow:finaRow,initCol:finaCol]
        outputArray=output2DArray.flatten()
        #Save selected screenshot
        imRGB = Image.frombuffer('RGB', (screenshotWinRect.width,screenshotWinRect.height), outputArray, 'raw', 'BGRX', 0, 1)
        arrayRGB = np.array(imRGB)
        imBGR = cv2.cvtColor(arrayRGB, cv2.COLOR_RGB2BGR)
        win32gui.DeleteObject(winBitMap.GetHandle())
        memoDC.DeleteDC()
        newDC.DeleteDC()
        win32gui.ReleaseDC(winHwnd, winDCHwnd)
        return imBGR
    except Exception as ex:
        print_ex(ex)

