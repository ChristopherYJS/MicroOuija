from cv2 import cvtColor
import win32gui
import win32ui
from ctypes import windll

import cv2
import numpy as np
from PIL import Image

from GDI_func import enumHandler
from GDI_func import RectObj
from SelectArea import SelectArea

global param
winHwnd=0
winKeyword='Global View'
param=[winKeyword,winHwnd]
win32gui.EnumWindows(enumHandler,param)
winHwnd=param[1]
winRect=RectObj(*win32gui.GetWindowRect(winHwnd))
winDCHwnd = win32gui.GetWindowDC(winHwnd)
newDC  = win32ui.CreateDCFromHandle(winDCHwnd)
memoDC = newDC.CreateCompatibleDC()
winBitMap = win32ui.CreateBitmap()
winBitMap.CreateCompatibleBitmap(newDC, winRect.width, winRect.height)
memoDC.SelectObject(winBitMap)
result = windll.user32.PrintWindow(winHwnd, memoDC.GetSafeHdc(),2)
bmpinfo = winBitMap.GetInfo()
bmparray = np.asarray(winBitMap.GetBitmapBits(), dtype=np.uint8)
imRGB = Image.frombuffer('RGB', (winRect.width,winRect.height), bmparray, 'raw', 'BGRX', 0, 1)
imRGB=np.array(imRGB)
imBGR=cv2.cvtColor(imRGB,cv2.COLOR_RGB2BGR)
cv2.imwrite("GlobalView.png",imBGR)


