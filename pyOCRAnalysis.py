import numpy as np
import cv2
import pytesseract as pt
from PrintException import print_ex
# pt.pytesseract.tesseract_cmd = r'C:\Users\jy1u18\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'
pt.pytesseract.tesseract_cmd =r'C:\Program Files\Tesseract-OCR\tesseract.exe'



def checkArrow(imArray:np.ndarray):
    try:
        if imArray.flatten().any()==1:
            return True
        else:
            return False
    except Exception as ex:
            print_ex(ex)

def OCRAnalysis(imBGR):
    try:
        # imBGR=cv2.imread('origin.png')
        #Create gray image and HLS colour mask and apply to the gray image
        imHLS = cv2.cvtColor(imBGR,cv2.COLOR_BGR2HLS)
        imGray=cv2.cvtColor(imBGR,cv2.COLOR_RGB2GRAY)
        lower = np.uint8([0, 150, 0])
        upper = np.uint8([50, 200, 10])
        imFrame = cv2.inRange(imHLS, lower, upper)
        # cv2.imwrite(r"default\OCR\imFrame.png",imFrame )
        imText=cv2.inRange(-imGray,0,0.3)
        # cv2.imwrite("imText.png",imText)


        #Extrace horizontal lines from the gray img and dilate
        horizontal=np.copy(imFrame)
        cols = horizontal.shape[1]
        horizontal_size = cols // 15
        horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
        horizontal = cv2.erode(horizontal, horizontalStructure)
        horizontal_size = cols // 10
        horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
        horizontal = cv2.dilate(horizontal, horizontalStructure)
        # cv2.imwrite(r"default\OCR\imHorizontal.png",horizontal )

        #Extrace vertical lines and dilate
        vertical=np.copy(imFrame)  
        rows = vertical.shape[1]
        vertical_size = rows // 5
        verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
        vertical = cv2.erode(vertical, verticalStructure)
        vertical_size = rows // 5
        verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
        vertical = cv2.dilate(vertical, verticalStructure)
        # cv2.imwrite(r"default\OCR\imVertical.png",vertical )

        #combine horizontal and vertical feature to get anchor points
        anchor = cv2.bitwise_and(horizontal, vertical)
        # cv2.imwrite(r"default\OCR\imAnchor.png",anchor )

        # print(type(anchor[0,10]))
        pointList=[]
        for y in range(len(anchor)):
            for x in range(len(anchor[y])):
                if anchor[y,x]!=0:
                    pointList.append((x,y))
        # print(pointList)
        xPoints=list(dict.fromkeys(np.sort([tlp[0] for tlp in pointList])))
        yPoints=list(dict.fromkeys(np.sort([tlp[1] for tlp in pointList])))
        # print(xPoints,yPoints)
        leftPoint=xPoints[0]
        rightPoint=xPoints[-1]
        bottomPoint=yPoints[-2]
        topPoint=yPoints[-3]
        # print(leftPoint,topPoint,rightPoint,bottomPoint)
        imTech=imText[topPoint+1:bottomPoint,leftPoint+1:rightPoint]
        # cv2.imwrite("imTech.png",imTech)
        stripList=[]
        for i in np.arange(0,len(imTech),16):
            stripList.append(imTech[i:i+16,:])
            # cv2.imwrite(f'imStrip-{int(i/16)}.png',imTech[i:i+16,:])
        techList=[]
        numList=[]
        headList=[]
        for i in range(len(stripList)):
            strip=stripList[i]
            # cv2.imwrite(fr"default\OCR\strip{i}.png",strip)
            if checkArrow(strip):
                head=strip[:,0:int(1/5*len(strip[0]))]
                num=strip[:,int(1/5*len(strip[0])):int(1/5*len(strip[0]))+20]
                tech=strip[:,int(1/3*len(strip[0]))-2:int(2/3*len(strip[0]))]
                # cv2.imshow(f'head{i}',head)
                # cv2.imshow(f'num{i}',num)
                # cv2.imshow(f'tech{i}',tech)
                headbool=checkArrow(head)
                numstr=pt.image_to_string(num,lang='eng', config='--psm 7 --oem 3 -c tessedit_char_whitelist=0123456789')
                # techstr=pt.image_to_string(tech,lang='eng', config='--psm 6 --oem 3')
                numstr=numstr.replace('\n','')
                # techstr=techstr.replace('\n','')
                headList.append(headbool)
                # techList.append(techstr)
                numList.append(numstr)
            else:
                break
        return headList,numList
    except Exception as ex:
            print_ex(ex)


