import win32gui
import win32ui
import win32con
from ctypes import windll

import cv2
import numpy as np
from PIL import Image

from GDI_func import enumHandler
from GDI_func import RectObj
from SelectArea import SelectArea



def ExpListLocator():
    global param
    winHwnd=0
    winKeyword='experiment'
    param=[winKeyword,winHwnd]

    #enumerate visiable windows with keyword in and retrieve the handle.
    win32gui.EnumWindows(enumHandler,param)
    winHwnd=param[1]
    className=win32gui.GetClassName(winHwnd)
    longName=win32gui.GetWindowText(winHwnd)
    winHwnd=win32gui.FindWindow(className,longName)
    win32gui.ShowWindow(winHwnd,win32con.SW_SHOWNA)
    win32gui.SetForegroundWindow(winHwnd)

   
    #Get window information, create compatible memory device context, write bitmap of the window screenshot to memory DC
    winRect=RectObj(*win32gui.GetWindowRect(winHwnd))
    print(f'Window Area Rect: {winRect}')
    # win32gui.RedrawWindow(winHwnd,None,None,1)
    # clientScrPos=win32gui.ClientToScreen(winHwnd,(winRect.left,winRect.top))
    # clientScrRect=RectObj(*clientScrPos,clientScrPos[0]+winRect.width,clientScrPos[1]+winRect.height)
    # print(clientScrRect)
    winDCHwnd = win32gui.GetWindowDC(winHwnd)
    newDC  = win32ui.CreateDCFromHandle(winDCHwnd)
    memoDC = newDC.CreateCompatibleDC()
    winBitMap = win32ui.CreateBitmap()
    winBitMap.CreateCompatibleBitmap(newDC, winRect.width, winRect.height)
    memoDC.SelectObject(winBitMap)
    result = windll.user32.PrintWindow(winHwnd, memoDC.GetSafeHdc(),2)
    
    #Select area to analyse
    # win32gui.EnableWindow(winHwnd,False)
    areaSelected=SelectArea(winHwnd)
    # win32gui.EnableWindow(winHwnd,True)
    # win32gui.RedrawWindow(winHwnd,None,None,1)
    # win32gui.UpdateWindow(winHwnd)
    selectedRect=areaSelected.Output(areaSelected.pos)
    print(f'Selected Area Rect:{selectedRect}')

    #Retrieve bmp from buffer and convert bmp to cv2 bgr file and array, select part of the screenshot.
    bmpinfo = winBitMap.GetInfo()
    bmparray = np.asarray(winBitMap.GetBitmapBits(), dtype=np.uint8)

    bmpWidth=winRect.width
    bmpHeight=winRect.height
    bmpArea=bmpWidth*bmpHeight
    bmpArrayLength=len(bmparray)
    bmpDpP=bmpArrayLength/bmpArea

    #1D array to 2D
    bmp2DArray=np.reshape(bmparray,(-1,bmpWidth*4))
    initRow=selectedRect.top-winRect.top
    finaRow=initRow+selectedRect.height
    initCol=(selectedRect.left-winRect.left)*4
    finaCol=(selectedRect.left-winRect.left+selectedRect.width)*4
    output2DArray=bmp2DArray[initRow:finaRow,initCol:finaCol]
    outputArray=output2DArray.flatten()


    print('>>>')
    print(f'bmpwidth:{bmpWidth}, bmpheight:{bmpHeight}, bmpPixel:{bmpArea}, array length:{bmpArrayLength}, Data per pixel:{bmpDpP}')
    print(f'Array size: {len(bmp2DArray)}x{len(bmp2DArray[0])}')
    print(f'Selected size:{selectedRect.width}x{selectedRect.height}')
    print(f'Output BMP 2D Array size:{len(output2DArray)}x{len(output2DArray[0])}')
    print(f'Output BMP Array size:{len(outputArray)}')
    print('<<<')

    imRGB = Image.frombuffer('RGB', (selectedRect.width,selectedRect.height), outputArray, 'raw', 'BGRX', 0, 1)
    # imRGB = Image.frombuffer('RGB', (winRect.width,winRect.height), bmp2DArray, 'raw', 'BGRX', 0, 1)

    arrayRGB = np.array(imRGB)
    # print(len(arrayRGB[0]))
    imBGR = cv2.cvtColor(arrayRGB, cv2.COLOR_RGB2BGR)
    cv2.imwrite('origin.png',imBGR)

    #Create gray image and HLS colour mask and apply to the gray image
    imHLS = cv2.cvtColor(imBGR,cv2.COLOR_BGR2HLS)
    imGRAY=cv2.cvtColor(imBGR,cv2.COLOR_RGB2GRAY)
    lower = np.uint8([0, 0, 0])
    upper = np.uint8([180, 200, 50])
    HLSmask = cv2.inRange(imHLS, lower, upper)
    imGRAY=cv2.bitwise_or(imGRAY, imGRAY, mask = HLSmask)
    cv2.imwrite("mask.png",HLSmask )
    cv2.imwrite("imGRAY.png",imGRAY )

    #Extrace horizontal lines from the gray img and dilate
    horizontal=np.copy(imGRAY)
    cols = horizontal.shape[1]
    horizontal_size = cols // 15
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    horizontal = cv2.erode(horizontal, horizontalStructure)
    horizontal_size = cols // 10
    horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
    horizontal = cv2.dilate(horizontal, horizontalStructure)
    cv2.imwrite("horizontal.png",horizontal )

    #Extrace vertical lines and dilate
    vertical=np.copy(imGRAY)  
    rows = vertical.shape[1]
    vertical_size = rows // 10
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
    vertical = cv2.erode(vertical, verticalStructure)
    vertical_size = rows // 5
    verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
    vertical = cv2.dilate(vertical, verticalStructure)
    cv2.imwrite("vertical.png",vertical )

    #combine horizontal and vertical feature to get anchor points
    anchor = cv2.bitwise_and(horizontal, vertical)
    cv2.imwrite("anchor.png",anchor )


ExpListLocator()
