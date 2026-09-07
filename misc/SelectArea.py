#src:https://www.reddit.com/r/Python/comments/plyi20/draw_transparent_rectangle_on_screen_like/

import win32gui 
import win32ui 
import win32api 
from pynput.mouse import Listener
import ctypes
import sys

from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from GDI_func import enumHandler
from GDI_func import RectObj

class SelectArea:
    def __init__(self,hwnd):
        self.hwnd=hwnd
        self.InitialiseParam()
        self.Selector()
        
        
    def InitialiseParam(self):
        self.pos = []
        dc = win32gui.GetWindowDC(self.hwnd)
        self.dcObj = win32ui.CreateDCFromHandle(dc)
        self.brush = win32ui.CreateBrush()
        self.brush.CreateSolidBrush(0x000000FF)
        self.winRect=RectObj(*win32gui.GetWindowRect(self.hwnd))
        self.winCvtRect=self.RectConvert(self.winRect)
        self.cliRect=RectObj(*win32gui.GetClientRect(self.hwnd))
        # print(self.winCvtRect)
        # print(self.cliRect)
        self.xErr=self.cliRect.left-self.winCvtRect.left
        self.yErr=self.cliRect.top-self.winCvtRect.top
    
    def Selector(self):
        def OnClick(x,y,button,press):
            self.pos.append(x)
            self.pos.append(y)
            if not press:
                return False
        def OnMove(x,y):
            try:
                # win32gui.RedrawWindow(self.hwnd,None,None,1)
                selectScrRect=self.Output(self.pos[0:2]+[x,y])
                selectCliRect=self.RectConvert(selectScrRect)
                selectCliRect.left+=self.xErr
                selectCliRect.top+=self.yErr     
                selectCliRect.right+=self.xErr
                selectCliRect.bottom+=self.yErr           
                # win32gui.InvalidateRect(self.hwnd,win32gui.GetWindowRect(self.hwnd), True)
                self.dcObj.FrameRect(selectCliRect.Rect(),self.brush)
                # print(f'Current Rect:{selectCliRect}')
            except Exception as exc:
                # print(f'{exc}:{x},{y}')
                pass
        listener=Listener(on_move=OnMove,on_click=OnClick) 
        listener.start()
        listener.join()

    def RectConvert(self,rect:RectObj):
        pos=win32gui.ScreenToClient(self.hwnd,(rect.left,rect.top))
        outputrect=RectObj(*pos,pos[0]+rect.width,pos[1]+rect.height)
        return outputrect

    def Output(self,rectlist):
        top=[rectlist[1],rectlist[3]][rectlist[1]>rectlist[3]]
        bottom=[rectlist[3],rectlist[1]][rectlist[1]>rectlist[3]]
        left=[rectlist[0],rectlist[2]][rectlist[0]>rectlist[2]]
        right=[rectlist[2],rectlist[0]][rectlist[0]>rectlist[2]]
        outputRect=RectObj(left,top,right,bottom)
        return outputRect
if __name__ == '__main__':
    global param
    winHwnd=0
    winKeyword='experiment'
    param=[winKeyword,winHwnd]

    #enumerate visiable windows with keyword in and retrieve the handle.
    win32gui.EnumWindows(enumHandler,param)
    winHwnd=param[1]
    print(winHwnd)
    # Qapp=QApplication(sys.argv)
    app = SelectArea(winHwnd)
    # sys.exit(Qapp.exec_())