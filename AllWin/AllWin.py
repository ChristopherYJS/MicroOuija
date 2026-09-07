import win32gui
def enumHandler(hwnd,param):
    if win32gui.IsWindowVisible(hwnd) :
        className=win32gui.GetClassName(hwnd)
        winName=win32gui.GetWindowText(hwnd)
        print(f'>>>className:{className},\t hwnd:{hwnd},\t window title:{winName}')

param=0
win32gui.EnumWindows(enumHandler,param)