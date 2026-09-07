from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtCore import *
from PyQt5.QtGui import *

from pipython import GCSDevice
from PrintException import print_ex

import numpy as np
import time

from pyTimerThread import OnTargetTimer as OTT

class MicroPositioner(QThread):
    sig_logerror=pyqtSignal(object) 
    sig_loginfo=pyqtSignal(str) 
    sig_showpos=pyqtSignal(list)
    sig_uiChange=pyqtSignal(str)
    def __init__(self,mainwin):
        super().__init__()
        self.mainwin=mainwin
        self.mpVarDictionary()
        self.TimerBinding()
        self.timerTimer=QTimer(self,interval=1000)

    def run(self):
        try:
            self.sig_loginfo.emit('Connecting...')
            self.devz=GCSDevice('C-863')
            self.devz.OpenRS232DaisyChain(comport=10, baudrate=9600)
            chainid=self.devz.dcid
            self.devz.ConnectDaisyChainDevice(3, chainid)
            self.devy=GCSDevice('C-863')
            self.devy.ConnectDaisyChainDevice(2, chainid)
            self.devx=GCSDevice('C-863')
            self.devx.ConnectDaisyChainDevice(1, chainid)
            self.mpDeviceDic={0:self.devx,1:self.devy,2:self.devz}
            # self.sig_loginfo.emit('Connected, resetting error')
            # for dev in self.mpDeviceDic.values():
            #     dev.SPA(1,8,0.2)
            self.sig_loginfo.emit('Retriving location')
            self.ServoCheck(0,1,2)
            self.sig_loginfo.emit('Connection finished.')
        except Exception as ex:
            print_ex(ex)
            pass


    def mpVarDictionary(self):
        self.devStrDic={0:'X',1:'Y',2:'Z'}
        self.mpOTTimerDic={0:QTimer(self,interval=100),1:QTimer(self,interval=100),2:QTimer(self,interval=100)}
        self.otCount={0:0,1:0,2:0}
        self.hpos={0:-1,1:-1,2:-1}
    def TimerBinding(self):
        self.mpOTTimerDic[0].timeout.connect(lambda: self.OnTarget(0))
        self.mpOTTimerDic[1].timeout.connect(lambda: self.OnTarget(1))
        self.mpOTTimerDic[2].timeout.connect(lambda: self.OnTarget(2))

    def ShowPos(self,*axis):
        for axes in axis:
            cpos=f'{self.mpDeviceDic[axes].qPOS("1")["1"]:.4f}'
            self.sig_showpos.emit([axes,cpos])


    
    def Servo(self,*axis):
        for axes in axis:
            if self.mainwin.mpServoDic[axes].isChecked()==True:
                try:
                    servoOn=False
                    self.mpDeviceDic[axes].SVO(1,True)
                    servoOn=self.mpDeviceDic[axes].qSVO()['1']
                    self.ShowPos(axes)
                except Exception as ex:
                    print_ex(ex)
                finally:
                    if servoOn==True:
                        self.sig_uiChange.emit(f'self.mpAxisDic[{axes}].setStyleSheet("color: lime")')
                        self.sig_uiChange.emit(f'self.mpServoDic[{axes}].setChecked(True)')
                    else: 
                        self.sig_uiChange.emit(f"self.mpAxisDic[{axes}].setStyleSheet('color: red')")
                        self.sig_uiChange.emit(f"self.mpServoDic[{axes}].setChecked(False)")
            else:
                try:
                    servoOn=True
                    self.mpDeviceDic[axes].SVO(1,False)
                    servoOn=self.mpDeviceDic[axes].qSVO()['1']
                except Exception as ex:
                    print_ex(ex)
                finally:
                    if servoOn==True:
                        self.sig_uiChange.emit(f"self.mpAxisDic[{axes}].setStyleSheet('color: lime')")
                        self.sig_uiChange.emit(f"self.mpServoDic[{axes}].setChecked(True)")
                    else: 
                        self.sig_uiChange.emit(f"self.mpAxisDic[{axes}].setStyleSheet('color: red')")
                        self.sig_uiChange.emit(f"self.mpServoDic[{axes}].setChecked(False)")

    def MoveTo(self,axis,step='0',vel='2'):
        try:
            self.sig_uiChange.emit(f"self.mpMoveNegDic[{axis}].setEnabled(False)")
            self.sig_uiChange.emit(f"self.mpMovePosDic[{axis}].setEnabled(False)")
            self.sig_uiChange.emit(f"self.mpGoToDic[{axis}].setEnabled(False)")
            self.sig_uiChange.emit(f"self.mpAxisDic[{axis}].setStyleSheet('color:yellow')")
            device=self.mpDeviceDic[axis]
            step=float(f'{float(step):.4f}')
            vel=np.abs(float(f'{float(vel):.4f}'))
            QApplication.processEvents()
            cpos=float(format(device.qPOS('1')['1'],'.4f'))
            tpos=float(format(cpos+step,'.4f'))
            tdis=float(format(tpos-cpos,'.4f'))
            self.sig_loginfo.emit(f'axis {self.devStrDic[axis]}: {str(cpos)} to {str(tpos)} ({tdis}) at {vel}\n')
            device.VEL('1',vel)
            device.MVR('1',step)
            self.otCount[axis]=0
            self.hpos[axis]=-1
            self.mpOTTimerDic[axis].start()
        except Exception as ex:
            self.sig_loginfo.emit('Move-relavent Error')
            print_ex(ex)
            self.sig_uiChange.emit(f"self.mpMoveNegDic[{axis}].setEnabled(True)")
            self.sig_uiChange.emit(f"self.mpMovePosDic[{axis}].setEnabled(True)")
            self.sig_uiChange.emit(f"self.mpGoToDic[{axis}].setEnabled(True)")
            self.sig_uiChange.emit(f"self.mpAxisDic[{axis}].setStyleSheet('color:red')")

    def GoTo(self,axis,tpos,vel='2'):
        try:
            self.sig_uiChange.emit(f"self.mpMoveNegDic[{axis}].setEnabled(False)")
            self.sig_uiChange.emit(f"self.mpMovePosDic[{axis}].setEnabled(False)")
            self.sig_uiChange.emit(f"self.mpGoToDic[{axis}].setEnabled(False)")
            self.sig_uiChange.emit(f"self.mpAxisDic[{axis}].setStyleSheet('color:yellow')")
            device=self.mpDeviceDic[axis]
            tpos=float(tpos)
            vel=float(f'{float(vel):.4f}')
            QApplication.processEvents()
            cpos=float(format(device.qPOS('1')['1'],'.4f'))
            tdis=float(format(tpos-cpos,'.4f'))
            self.sig_loginfo.emit(f'axis {self.devStrDic[axis]}: {str(cpos)} to {str(tpos)} ({tdis}) at {vel}\n')
            device.VEL('1',vel)
            device.MOV('1',tpos)
            self.otCount[axis]=0
            self.hpos[axis]=-1
            self.mpOTTimerDic[axis].start()
        except Exception as ex:
            self.sig_loginfo.emit('Move-Absolute Error')
            print_ex(ex)
            self.sig_uiChange.emit(f"self.mpMoveNegDic[{axis}].setEnabled(True)")
            self.sig_uiChange.emit(f"self.mpMovePosDic[{axis}].setEnabled(True)")
            self.sig_uiChange.emit(f"self.mpGoToDic[{axis}].setEnabled(True)")
            self.sig_uiChange.emit(f"self.mpAxisDic[{axis}].setStyleSheet('color:red')")

    def Halt(self,*axis):
        for axes in axis:
            try:
                self.mpOTTimerDic[axes].stop()
                dev=self.mpDeviceDic[axes]
                dev.HLT('1',noraise=True)
                self.sig_uiChange.emit(f"self.mpMoveNegDic[{axes}].setEnabled(False)")
                self.sig_uiChange.emit(f"self.mpMovePosDic[{axes}].setEnabled(False)")
                self.sig_uiChange.emit(f"self.mpGoToDic[{axes}].setEnabled(False)")
                self.sig_uiChange.emit(f"self.mpAxisDic[{axes}].setStyleSheet('color:red')")
                QApplication.processEvents()
                self.sig_loginfo.emit(
                    "<span style=\" font-size:10pt; font-weight:600; color:#ff0000;\" >"
                    'HALTING!'
                    "</span>")
                self.otCount[axes]=0
                self.hpos[axes]=-1
                self.mpOTTimerDic[axes].start()
                QApplication.processEvents()
                self.sig_loginfo.emit('Halt finished')
            except Exception as ex:
                self.sig_loginfo.emit('Halt Error')
                print_ex(ex)
                self.sig_uiChange.emit(f"self.mpMoveNegDic[{axes}].setEnabled(True)")
                self.sig_uiChange.emit(f"self.mpMovePosDic[{axes}].setEnabled(True)")
                self.sig_uiChange.emit(f"self.mpGoToDic[{axes}].setEnabled(True)")
                self.sig_uiChange.emit(f"self.mpAxisDic[{axes}].setStyleSheet('color:red')")

    def OnTarget(self,axis):
        device=self.mpDeviceDic[axis]
        cpos=float(f'{device.qPOS("1")["1"]:.4f}')
        diff=np.abs(cpos-self.hpos[axis])
        self.hpos[axis]=cpos
        if diff<0.0001:
            self.otCount[axis]+=1
            if self.otCount[axis]>=15:
                self.mpOTTimerDic[axis].stop()
                self.sig_uiChange.emit(f"self.mpAxisDic[{axis}].setStyleSheet('color:lime')")
                self.sig_uiChange.emit(f"self.mpMoveNegDic[{axis}].setEnabled(True)")
                self.sig_uiChange.emit(f"self.mpMovePosDic[{axis}].setEnabled(True)")
                self.sig_uiChange.emit(f"self.mpGoToDic[{axis}].setEnabled(True)")
        else:
            self.otCount[axis]=0
        self.ShowPos(axis)

    def ServoCheck(self,*axis):
        for axes in axis:
            if self.mpDeviceDic[axes].qSVO()['1']==False:
                self.sig_uiChange.emit(f'self.mpAxisDic[{axes}].setStyleSheet("color:red")')
                self.sig_uiChange.emit(f'self.mpServoDic[{axes}].setChecked(False)')
            else:
                self.sig_uiChange.emit(f'self.mpAxisDic[{axes}].setStyleSheet("color:lime")')
                self.ShowPos(axes)
                self.sig_uiChange.emit(f'self.mpServoDic[{axes}].setChecked(True)')


    def RefreshMove(self,axis,dis):
        self.MoveTo(axis,step=0.2,vel=0.2)
        while self.mpOTTimerDic[axis].isActive():
            QCoreApplication.processEvents()
        self.MoveTo(axis,step=-0.18,vel=0.2)
        while self.mpOTTimerDic[axis].isActive():
            QCoreApplication.processEvents()
        self.MoveTo(axis,step=-0.01,vel=0.005)
        while self.mpOTTimerDic[axis].isActive():
            QCoreApplication.processEvents()
        self.MoveTo(axis,step=-0.005,vel=0.002)
        while self.mpOTTimerDic[axis].isActive():
            QCoreApplication.processEvents()
        self.MoveTo(axis,step=-0.005+dis,vel=0.001)

    def TimerTimerSlot(self,axis):
        if not self.mpOTTimerDic[axis].isActive():
            self.MoveTo(axis,step=-0.1,vel=0.005)
            self.timerTimer.stop()

    def AutoMove(self,params):
        axis,step=params
        if step>=0.1:
            vel=f'{(step/2)}'
            step=f'{step}'
        else:
            vel=f'{(step/4)}'
            step=f'{step}'
        self.MoveTo(axis,step,vel)




    