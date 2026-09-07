import numpy as np
import cv2
import pytesseract as pt
pt.pytesseract.tesseract_cmd = r'C:\Users\jy1u18\AppData\Local\Programs\Tesseract-OCR\tesseract.exe'

imBGR=cv2.imread('origin.png')


def checkBlank(imArray:np.ndarray):
    if imArray.flatten().any()==1:
        return False
    else:
        return True



#Create gray image and HLS colour mask and apply to the gray image
imHLS = cv2.cvtColor(imBGR,cv2.COLOR_BGR2HLS)
imGray=cv2.cvtColor(imBGR,cv2.COLOR_RGB2GRAY)
lower = np.uint8([0, 150, 0])
upper = np.uint8([50, 200, 10])
imFrame = cv2.inRange(imHLS, lower, upper)
cv2.imwrite("imFrame.png",imFrame )
imText=cv2.inRange(-imGray,0,0.3)
cv2.imwrite("imText.png",imText)


#Extrace horizontal lines from the gray img and dilate
horizontal=np.copy(imFrame)
cols = horizontal.shape[1]
horizontal_size = cols // 15
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
horizontal = cv2.erode(horizontal, horizontalStructure)
horizontal_size = cols // 10
horizontalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (horizontal_size, 1))
horizontal = cv2.dilate(horizontal, horizontalStructure)
cv2.imwrite("imHorizontal.png",horizontal )

#Extrace vertical lines and dilate
vertical=np.copy(imFrame)  
rows = vertical.shape[1]
vertical_size = rows // 10
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
vertical = cv2.erode(vertical, verticalStructure)
vertical_size = rows // 5
verticalStructure = cv2.getStructuringElement(cv2.MORPH_RECT, (1, vertical_size))
vertical = cv2.dilate(vertical, verticalStructure)
cv2.imwrite("imVertical.png",vertical )

#combine horizontal and vertical feature to get anchor points
anchor = cv2.bitwise_and(horizontal, vertical)
cv2.imwrite("imAnchor.png",anchor )

# print(type(anchor[0,10]))
pointList=[]
for y in range(len(anchor)):
    for x in range(len(anchor[y])):
        if anchor[y,x]!=0:
            pointList.append((x,y))
print(pointList)
xPoints=list(dict.fromkeys(np.sort([tlp[0] for tlp in pointList])))
yPoints=list(dict.fromkeys(np.sort([tlp[1] for tlp in pointList])))
print(xPoints,yPoints)
leftPoint=xPoints[0]
rightPoint=xPoints[-1]
bottomPoint=yPoints[-2]
topPoint=yPoints[-3]
# print(leftPoint,topPoint,rightPoint,bottomPoint)
imTech=imText[topPoint+1:bottomPoint,leftPoint+1:rightPoint]
cv2.imwrite("imTech.png",imTech)
stripList=[]
for i in np.arange(0,len(imTech),16):
    stripList.append(imTech[i:i+16,:])
    cv2.imwrite(f'imStrip-{int(i/16)}.png',imTech[i:i+16,:])

for strip in stripList:
    head=strip[:,0:int(2/9*len(strip[0]))]
    if not checkBlank(head):
        targetStrip=strip[:,int(1.8/9*len(strip[0])):]
        cv2.imshow("Found",targetStrip)
        cv2.waitKey(0)
        text=pt.image_to_string(targetStrip)
        text=text.replace('\n','')
        print(text)
        break

