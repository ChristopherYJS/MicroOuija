from dataclasses import dataclass
import win32gui

@dataclass
class RectObj():
    left:int
    top:int
    right:int
    bottom:int
    width:int
    height:int
    def __init__(self,left, top, right, bottom):
        self.left=left
        self.top=top
        self.right=right
        self.bottom=bottom
        self.width=self.right - self.left
        self.height=self.bottom - self.top
    def Rect(self):
        return (self.left,self.top,self.right,self.bottom)

def enumHandler(hwnd,param):
    if param[0] in win32gui.GetWindowText(hwnd):
        param[1]=hwnd