from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtWidgets import QSplashScreen
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import *
from PyQt5.QtGui import *


from pyMultiCam import MultiCam
from pyPI import MicroPositioner
from pyMappingWin import MappingWin
from pyAutoMove_Nova import AutoMoveWin
from PrintException import print_ex, print_log
from SubThread_AppcurveGenerator import Subwin_AppCurveGenerator

import sys
import datetime
import cv2
import os
import re     

LOGDIR=fr'.\Log'
DEFAULTDIR=fr'.\default'
class CnC_Main_GUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.LoadUI()
        self.Splash()
        self.VarInitialise()
        self.ProgramInitialise()
        self.WidgetDictionary() 
        self.Restyle()
        self.SignalSlotBinding()
        self.splash.close()
        self.showMaximized()
        
    def LoadUI(self):
        self.ui=uic.loadUi('uiMain.ui',self)

    def Splash(self):
        self.splash = QSplashScreen(QPixmap(r'.\splash.jpg'))
        self.splash.show()

    def VarInitialise(self):
        self.subwinlist=[]
        self.mpThread=None
        self.mcThread=None
        self.mapping=None

    def ProgramInitialise(self):
        self.datetoday=datetime.date.today().strftime("%Y%m%d")
        #Create Log folder and file under current folder
        if not os.path.exists(LOGDIR):
            self.LogInfo('LogFolder not found, might have other issues')
            self.LogInfo('Use script within the original folder!')
            os.makedirs(self.LOGDIR)
            with open(fr'{self.LOGDIR}\LogFile.txt', 'w') as file:
                file.write(f'>>>{datetime.date.today()} LogFile created'+'\n')
        #Create default folders under current folder
        if not os.path.exists(DEFAULTDIR):
                    os.makedirs(DEFAULTDIR)
        #Check logfile date
        with open(fr'{LOGDIR}\LogFile.txt','r') as file:
            Date=file.readline()
        if Date != str(datetime.date.today())+'\n':
            with open(fr'{LOGDIR}\LogFile.txt','a') as file:
                file.write(str(datetime.date.today())+'\n')
        with open(fr'{LOGDIR}\LogFile.txt','a') as file:
            time=datetime.datetime.now()
            file.write(f'>>>{time.hour:02}:{time.minute:02}:{time.second:02}>NEW SESSION!!!'+'\n')
        #Set source folders from defaultDir.txt or default setting
        try:
            with open(fr'.\default\defaultDir.txt','r') as file:
                lines=file.read().splitlines()
            self.ocrDir=lines[0]
            self.triggerDir=lines[1]
            self.disfileDir=lines[2]
            self.mediaDir=lines[3]
            self.dirDict={'OCR':self.ocrDir,'trigger':self.triggerDir,'disfile':self.disfileDir,'media':self.mediaDir}
            for dir in self.dirDict.values():
                dir=dir.strip('\\n')
                if not os.path.exists(dir):
                    os.makedirs(dir)
            #Create daily subfolders:
            self.mediaToday=fr'{self.mediaDir}\{self.datetoday}'
            self.disTodat=fr'{self.disfileDir}\{self.datetoday}'
            if not os.path.exists(self.mediaToday):
                os.makedirs(self.mediaToday)
            if not os.path.exists(self.disTodat):
                os.makedirs(self.disTodat)
        except Exception as ex:
            if type(ex) == IndexError:
                self.ocrDir=fr'.\default\OCR'
                self.triggerDir=fr'.\default\Trigger'
                self.disfileDir=fr'.\default\DisFile'
                self.mediaDir=fr'.\default\MultiMedia'
                self.dirDict={'OCR':self.ocrDir,'trigger':self.triggerDir,'disfile':self.disfileDir,'media':self.mediaDir}
                for dir in self.dirDict.values():
                    if not os.path.exists(dir):
                        os.makedirs(dir)
                with open(fr'.\default\defaultDir.txt','w') as file:
                    file.writelines([dir+'\n' for dir in self.dirDict.values()])
            else:
                raise ex

    def WidgetDictionary(self):
        #Camera widgets:
        self.camCanvasDic={0:self.label_canvas1,1:self.label_canvas2}
        self.camDisplayDic={0:self.pushButton_cam1,1:self.pushButton_cam2}
        self.camRecordDic={0:self.pushButton_cam1re,1:self.pushButton_cam2re}
        self.camCaptureDic={0:self.pushButton_cam1cap,2:self.pushButton_cam1cap}
        #Micropositioner (mp) widgets:
        self.mpServoDic={0:self.checkBox_x_servo,1:self.checkBox_y_servo,2:self.checkBox_z_servo}
        self.mpAxisDic={0:self.label_x,1:self.label_y,2:self.label_z}
        self.mpMoveNegDic={0:self.pushButton_x_neg,1:self.pushButton_y_neg,2:self.pushButton_z_neg}
        self.mpMovePosDic={0:self.pushButton_x_pos,1:self.pushButton_y_pos,2:self.pushButton_z_pos}
        self.mpGoToDic={0:self.pushButton_x_go,1:self.pushButton_y_go,2:self.pushButton_z_go}
        self.mpHaltDic={0:self.pushButton_x_halt,1:self.pushButton_y_halt,2:self.pushButton_z_halt}
        self.mpDisplayDic={0:self.lineEdit_x_loc,1:self.lineEdit_y_loc,2:self.lineEdit_z_loc}
        self.mpTargetPosDic={0:self.lineEdit_x_tp,1:self.lineEdit_y_tp,2:self.lineEdit_z_tp}
        self.mpStepSizeDic={0:self.lineEdit_x_ss,1:self.lineEdit_y_ss,2:self.lineEdit_z_ss}
        self.mpVelDic={0:self.lineEdit_x_vel,1:self.lineEdit_y_vel,2:self.lineEdit_z_vel}

    def Restyle(self):
        self.setWindowTitle('SECM Master')
        self.setWindowIcon(QIcon(r'C:\Users\jy1u18\OneDrive - University of Southampton\PhD\python\MicroOuija2\icon.png'))
        self.resize(1500,300)
        #Micropositioner widgets restyle:
        for widget in self.mpDisplayDic.values():
            widget.setText("0.0000")
            widget.setAlignment(Qt.AlignCenter)
            widget.setStyleSheet("background-color: rgb(40,40,40); color: rgb(255,255,255); font-family:Roboto; font-size:28pt")
        for widget in self.mpTargetPosDic.values():
            widget.setStyleSheet("background-color: rgb(40,40,40);color: rgb(220,220,220); font-family:Roboto; font-size:10pt")
        for widget in self.mpStepSizeDic.values():
            widget.setStyleSheet("background-color: rgb(40,40,40);color: rgb(220,220,220); font-family:Roboto; font-size:10pt")
        for widget in self.mpVelDic.values():
            widget.setStyleSheet("background-color: rgb(40,40,40);color: rgb(220,220,220); font-family:Roboto; font-size:10pt")
        for widget in self.mpHaltDic.values():
            widget.setStyleSheet("color: rgb(250,10,0); font-family:Roboto; font-size:18pt; font-style: black")
        #Camera widgets restyle:
        self.label_canvas1.setAlignment(Qt.AlignCenter)
        self.label_canvas2.setAlignment(Qt.AlignCenter)
        self.lineEdit_filename.setText(self.datetoday)
        self.lineEdit_filename.setStyleSheet("background-color: rgb(20,20,20);color: rgb(220,220,220); font-family:Roboto; font-size:10pt")

    def SignalSlotBinding(self):
        #Micropositioner Signals:
        self.actionConnect.triggered.connect(self.mpThreadSlot)
        self.lineEdit_cmd.returnPressed.connect(self.LogCommand)
        #PushButton Mapping
        self.pushButton_appmap.clicked.connect(self.MappingWinSlot)
        self.pushButton_cam1.clicked.connect(lambda: self.mcThreadSlot(0))
        self.pushButton_cam2.clicked.connect(lambda: self.mcThreadSlot(1))
        self.pushButton_AM.clicked.connect(self.AutoMoveWinShow)
        self.pushButton_AG.clicked.connect(self.AppCurveGenerate)

    def UnlockButtons(self):
        for widget in self.findChildren(QPushButton):
            widget.setEnabled(True)

    def RefreshDisplay(self,param):
        axis,cpos=param
        self.mpDisplayDic[axis].setText(f'{cpos}')

    def UIChange(self,command):
        eval(command)

    def AutoMoveWinShow(self):
        self.winAM=AutoMoveWin(self)
        self.subwinlist.append(self.winAM)
        
    def AppCurveGenerate(self):
        self.thrdappcurve=Subwin_AppCurveGenerator(self)
        self.subwinlist.append(self.thrdappcurve)

    def mpThreadSlot(self):
        def mpSignalSlotBinding():
            self.actionRefresh_Micropositioner_Reading.triggered.connect(
            lambda: self.mpThread.ShowPos(0,1,2))
            self.actionUnlock_Buttons.triggered.connect(self.UnlockButtons)
            #CheckBox Servo
            self.checkBox_x_servo.clicked.connect(lambda: self.mpThread.Servo(0))
            self.checkBox_y_servo.clicked.connect(lambda: self.mpThread.Servo(1))
            self.checkBox_z_servo.clicked.connect(lambda: self.mpThread.Servo(2))
            #PushButton Move
            self.pushButton_x_neg.clicked.connect(
                lambda: self.mpThread.MoveTo(0,'-'+self.lineEdit_x_ss.text(),self.lineEdit_x_vel.text())
                )
            self.pushButton_y_neg.clicked.connect(
                lambda: self.mpThread.MoveTo(1,'-'+self.lineEdit_y_ss.text(),self.lineEdit_y_vel.text())
                )
            self.pushButton_z_neg.clicked.connect(
                lambda: self.mpThread.MoveTo(2,'-'+self.lineEdit_z_ss.text(),self.lineEdit_z_vel.text())
                )
            self.pushButton_x_pos.clicked.connect(
                lambda: self.mpThread.MoveTo(0,self.lineEdit_x_ss.text(),self.lineEdit_x_vel.text())
                )
            self.pushButton_y_pos.clicked.connect(
                lambda: self.mpThread.MoveTo(1,self.lineEdit_y_ss.text(),self.lineEdit_y_vel.text())
                )
            self.pushButton_z_pos.clicked.connect(
                lambda: self.mpThread.MoveTo(2,self.lineEdit_z_ss.text(),self.lineEdit_z_vel.text())
                )
            #PushButton Goto
            self.pushButton_x_go.clicked.connect(
                lambda: self.mpThread.GoTo(0,self.lineEdit_x_tp.text(),self.lineEdit_x_vel.text())
                )
            self.pushButton_y_go.clicked.connect(
                lambda: self.mpThread.GoTo(1,self.lineEdit_y_tp.text(),self.lineEdit_y_vel.text())
                )
            self.pushButton_z_go.clicked.connect(
                lambda: self.mpThread.GoTo(2,self.lineEdit_z_tp.text(),self.lineEdit_z_vel.text())
                )
            #PushButton Halt
            self.pushButton_x_halt.clicked.connect(lambda: self.mpThread.Halt(0))
            self.pushButton_y_halt.clicked.connect(lambda: self.mpThread.Halt(1))
            self.pushButton_z_halt.clicked.connect(lambda: self.mpThread.Halt(2))

        if self.mpThread is None:
            self.mpThread=MicroPositioner(self)
            self.mpThread.sig_loginfo.connect(self.LogInfo)
            self.mpThread.sig_showpos.connect(self.RefreshDisplay)
            self.mpThread.sig_uiChange.connect(self.UIChange)
            self.mpThread.start()
            mpSignalSlotBinding()
        else:
            self.LogInfo('\"self.mpThread is not None\". MicroPositioner might have been connected.')

    def mcThreadSlot(self,camnum):
        def mcSignalSlotBinding():
            #Camera Widgets Signals:
            self.pushButton_cam1re.clicked.connect(lambda: self.mcThread.record_slot(0))
            self.pushButton_cam2re.clicked.connect(lambda: self.mcThread.record_slot(1))
            self.pushButton_cam1cap.clicked.connect(lambda: self.mcThread.capture_slot(0))
            self.pushButton_cam2cap.clicked.connect(lambda: self.mcThread.capture_slot(1))
            self.pushButton_reall.clicked.connect(self.mcThread.record_slots)

        def RefreshCanvas(params):
            camnum,image=params
            self.camCanvasDic[camnum].setPixmap(QPixmap.fromImage(image))

        if self.mcThread is None:
            self.mcThread=MultiCam(self)
            self.mcThread.sig_loginfo.connect(self.LogInfo)
            self.mcThread.sig_uiChange.connect(self.UIChange)
            self.mcThread.sig_refreshCanvas.connect(RefreshCanvas)
            mcSignalSlotBinding()
            self.mcThread.StartTimer(camnum)
        else:
            self.mcThread.camDevDic[camnum]=cv2.VideoCapture(camnum)
            self.mcThread.StartTimer(camnum)

    def MappingWinSlot(self):
        if self.mapping is None:
            self.mapping=MappingWin(self)
        else:                                                                                                                                                                                                                                                                                                                                                                                           
            self.mapping.show()
            self.mapping.setWindowState(self.mapping.windowState() & ~Qt.WindowMinimized | Qt.WindowActive)
            self.mapping.activateWindow()

    def LogCommand(self):
        try:
            cmd=self.lineEdit_cmd.text()
            self.lineEdit_cmd.setText('')
            res=eval(cmd)
            self.LogInfo(cmd)
            self.LogInfo(f'{res}')
        except Exception as ex:
            print_ex(ex)

    def LogInfo(self,info):
        try:
            self.textBrowser_log.append(f'>{info}')
            self.textBrowser_log.verticalScrollBar().setValue(self.textBrowser_log.verticalScrollBar().maximum())
            print_log(info)
        except Exception as ex:
            print_ex(ex)

    def keyPressEvent(self, event: QKeyEvent):
        self.LogInfo('')
        if event.key()==Qt.Key_F3:
            self.mpThread.ServoCheck(0,1,2)




    def closeEvent(self, event):
        super().closeEvent(event)
        for subwin in self.subwinlist:
            subwin.close()
        event.accept()
        print('Session Terminated')

if __name__ =='__main__':
    try:
        Qapp=QApplication(sys.argv)
        app=CnC_Main_GUI()
        sys.exit(Qapp.exec_())
    except Exception as ex:
        print_ex(ex)
