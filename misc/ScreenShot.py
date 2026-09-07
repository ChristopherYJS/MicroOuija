import win32con
import win32gui
import win32ui
from ctypes import windll
from PIL import Image

class AutoWinRect():
    def __init__(self,left, top, right, bot):
        self.left=left
        self.top=top
        self.right=right
        self.bot=bot
        self.width=self.right - self.left
        self.height=self.bot - self.top

AWR=AutoWinRect

#Enumerate visible windows find the handle of window according to given keyword 
def enumHandler(hwnd,param):
    global winHndl
    if win32gui.IsWindowVisible(hwnd) and param in win32gui.GetWindowText(hwnd):
        winHndl=hwnd

winKeyword='experiment'

#Get window handle with the keyword and retrieve full window name
win32gui.EnumWindows(enumHandler,winKeyword)
print(f'>>>Window Handle: {winHndl}')
winText=win32gui.GetWindowText(winHndl)

print(f'>>>Window Name: {winText}')

#get window size
winRect=AWR(*win32gui.GetWindowRect(winHndl))

#get window device context and create a related memory device context
winDCHndl = win32gui.GetWindowDC(winHndl)
print(f'>>>Window Device Context Handle: {winDCHndl}')
newDC  = win32ui.CreateDCFromHandle(winDCHndl)
print(f'>>>Device Context: {newDC}')
memoDC = newDC.CreateCompatibleDC()
print(f'>>>Memory Device Context: {memoDC}')

#create bitmap according to the window size
winBitMap = win32ui.CreateBitmap()
winBitMap.CreateCompatibleBitmap(newDC, winRect.width, winRect.height)
print(f'>>>Bitmap: {winBitMap}')

#memory DC get bitmap
memoDC.SelectObject(winBitMap)

#draw EC-Lab window content to the memory DC. However I have tried different drawing options, it always raises "ValueError: not enough image data" but the same code works with other windows.
result = windll.user32.PrintWindow(winHndl, memoDC.GetSafeHdc(),           2      )
####################################################^^^HERE^^^

# memoDC.BitBlt((0, 0), ( winRect.width,  winRect.height), newDC, (winRect.left,winRect. top), win32con.SRCERASE)
# result=1


#get drawn bitmap info
bmpinfo = winBitMap.GetInfo()
bmpstr = winBitMap.GetBitmapBits(True)

#save picture

#winImg=Image.frombuffer('RGB',(bmpinfo['bmWidth'],bmpinfo['bmHeight']),bmpstr,'raw','BGRX',0,1)
#^^^This^^^ will raise the error if I try to convert bitmap to png. So I just directly save the bitmap:
if result==1:
    winBitMap.SaveBitmapFile(memoDC, 'screenshot.bmp')
    
win32gui.DeleteObject(winBitMap.GetHandle())
newDC.DeleteDC()
memoDC.DeleteDC()
win32gui.ReleaseDC(winHndl, winDCHndl)