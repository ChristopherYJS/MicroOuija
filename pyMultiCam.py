from PyQt5.QtCore import *
from PyQt5.QtGui import *

from PrintException import print_ex

import datetime
import cv2
import re
import os

class MultiCam(QThread):
    sig_uiChange=pyqtSignal(str)
    sig_loginfo=pyqtSignal(str)
    sig_refreshCanvas=pyqtSignal(list)
    def __init__(self,mainwin):
        try:
            super().__init__()
            self.mainwin=mainwin
            self.tech=None
            self.techTimer=QTimer(self,interval=3000)
            self.mcVarDictionary()
            self.TimerBinding()
        except Exception as ex:
            print_ex(ex)

    def StartTimer(self,camnum):
        try:
            if self.camTimerDic[camnum].isActive():
                self.sig_uiChange.emit(f'self.camDisplayDic[{camnum}].setStyleSheet("color:rgb(220,220,220)")')
                self.camTimerDic[camnum].stop()
            else:
                self.sig_uiChange.emit(f'self.camDisplayDic[{camnum}].setStyleSheet("color:rgb(255,0,0)")')
                self.camTimerDic[camnum].start()
        except Exception as ex:
            print_ex(ex)

    def mcVarDictionary(self):
        self.camTimerDic={0:QTimer(self,interval=100),1:QTimer(self,interval=100)}
        self.camDevDic={0:cv2.VideoCapture(0),1:cv2.VideoCapture(1)}
        self.isRecorded={0:False,1:False}
        self.frame={0:None,1:None}
        self.recordPermit={0:False,1:False}
        self.capturePermit={0:False,1:False}
        self.camVideoWriterDic={0:None,1:None}

    def TimerBinding(self):
        self.camTimerDic[0].timeout.connect(lambda: self.SampleFrame(0))
        self.camTimerDic[1].timeout.connect(lambda: self.SampleFrame(1))
        self.techTimer.timeout.connect(self.EraseTech)

    def SampleFrame(self,camnum):
        try:
            self.isRecorded[camnum],self.frame[camnum]=self.camDevDic[camnum].read()
            self.frame[camnum]=cv2.flip(self.frame[camnum],0)
            self.frame[camnum]=cv2.flip(self.frame[camnum],1)
            self.ProcessFrame(camnum)
            self.DisplayFrame(camnum)
            if self.recordPermit[camnum] is True:
                self.RecordCam(camnum)
            if self.capturePermit[camnum] is True:
                self.CaptureCam(camnum)
        except Exception as ex:
            print_ex(ex)
            self.camTimerDic[camnum].stop()

    def ProcessFrame(self,camnum):
        try:
            #Time stamp:
            timestamp= str(datetime.datetime.now().strftime('%y-%m-%d %H:%M:%S.%f')[:-4])
            font = cv2.FONT_HERSHEY_TRIPLEX
            self.frame[camnum] = cv2.putText(self.frame[camnum], timestamp, (5, 470), font, 0.8, (0, 0, 255), 1, cv2.LINE_8)
            if self.tech != None:
                self.frame[camnum] = cv2.putText(self.frame[camnum], self.tech, (400, 470), font, 0.8, (0, 0, 255), 1, cv2.LINE_8)
                if not self.techTimer.isActive():
                    self.techTimer.start()
        except Exception as ex:
            print_ex(ex)


    def DisplayFrame(self, camnum):
        try:
        #Set up canvas:
            qformat = QImage.Format_Indexed8
            if len(self.frame[camnum].shape)==3 :
                if self.frame[camnum].shape[2]==4:
                    qformat = QImage.Format_RGBA8888
                else:
                    qformat = QImage.Format_RGB888
            #Display frame
            outImage = QImage(self.frame[camnum], self.frame[camnum].shape[1], self.frame[camnum].shape[0], self.frame[camnum].strides[0], qformat)
            outImage = outImage.rgbSwapped()
            self.sig_refreshCanvas.emit([camnum,outImage])
        except Exception as ex:
            self.camTimerDic[camnum].stop()
            self.camDevDic[camnum]=None
            print_ex(ex)

    def RecordCam(self,camnum):
        try:
            if self.camTimerDic[camnum].isActive():
                self.camVideoWriterDic[camnum].write(self.frame[camnum])
            else:
                self.sig_loginfo.emit(f'Camera{camnum+1} not on')
        except Exception as ex:
            self.camTimerDic[camnum].stop()
            print_ex(ex)

    def record_slots(self):
        self.record_slot(0)
        self.record_slot(1)
        
    def CaptureCam(self,camnum):
        try:
            self.GetFileName()
            pictureName=self.CheckFileExist(camnum,'png')
            cv2.imwrite(f'{pictureName}', self.frame[camnum])
            print(f'>>>Picture saved at {pictureName}')
        except Exception as ex:
            self.camTimerDic[camnum].stop()
            print_ex(ex)
        finally:
            self.capturePermit[camnum]=False

    def record_slot(self,camnum):
        if self.recordPermit[camnum] is False:
            width= int(self.camDevDic[camnum].get(cv2.CAP_PROP_FRAME_WIDTH))
            height= int(self.camDevDic[camnum].get(cv2.CAP_PROP_FRAME_HEIGHT))
            self.GetFileName()
            self.filepath=self.CheckFileExist(camnum,'avi')
            self.camVideoWriterDic[camnum]= cv2.VideoWriter(self.filepath, cv2.VideoWriter_fourcc(*'DIVX'), 20, (width,height))
            self.recordPermit[camnum]=not self.recordPermit[camnum]
            self.sig_uiChange.emit(f'self.camRecordDic[{camnum}].setStyleSheet("color:rgb(255,0,0)")')
        else:
            self.recordPermit[camnum]=not self.recordPermit[camnum]
            self.camVideoWriterDic[camnum].release()
            self.sig_uiChange.emit(f'self.camRecordDic[{camnum}].setStyleSheet("color:rgb(255,255,255)")')

    def capture_slot(self,camnum):
        self.capturePermit[camnum]=not self.capturePermit[camnum]
        
    def EraseTech(self):
        self.tech=None
        self.techTimer.stop()

#MultiCam Auxilary Functions:
##Check and modify filename to be saved as
    def CheckFileExist(self,camnum,suffix):
        try:
            outputname=f'{self.filepath}_Cam{camnum+1}.{suffix}'
            while os.path.exists(outputname):
                print(f'>>>Rename')
                pattern='-\d+\.'
                if re.search(pattern,outputname) is None:
                    outputname=f'{self.filepath}_Cam{camnum+1}-1.{suffix}'
                else:
                    print(f'>>>pattern detected')
                    currentSign=re.findall(pattern,outputname)[-1]
                    currentNumber=int(currentSign.replace('-','').replace('.',''))
                    newSign=f'-{currentNumber+1}.'
                    outputname=outputname.replace(f'{currentSign}',f'{newSign}')
                print(outputname)
            return outputname
        except Exception as ex:
            print_ex(ex)


##Set filedir before recording and capturing 
    def GetFileName(self):
        try:
            self.filename=self.mainwin.lineEdit_filename.text()
            self.filepath=f'{self.mainwin.mediaToday}\{self.filename}'
        except Exception as ex:
            print_ex(ex)