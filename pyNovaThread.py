from PyQt5.QtGui import *
from PyQt5.QtCore import QThread, pyqtSignal 

from PrintException import print_ex

import os
import time
import datetime

#####Monkey Patch


class ExpMonitor(QThread):
    sig_ascent=pyqtSignal(list)
    sig_goto=pyqtSignal(list)
    sig_complete=pyqtSignal()
    sig_progressbar=pyqtSignal(int)
    sig_info=pyqtSignal(str)

    def __init__(self,mainthread,xlist,ylist,zlist,maxval,monitee):
        super().__init__()
        self.mainthread=mainthread
        self.xlist=xlist
        self.ylist=ylist
        self.zlist=zlist
        self.maxval=maxval-1
        self.ddif=[]
        self.monitee=monitee
        # for i in range(1,len(self.zlist)):
        #     self.ddif.append(self.zlist[i]-self.zlist[i-1])
        
    def run(self):
        ready=self.CheckReady()
        if ready==True:
            self.RunExp()
            self.sig_complete.emit()

    def CheckReady(self):
        ready=False
        try:
            self.file = open(self.monitee, "w")
            self.file.write('0')
            self.file.close()
            ready=True
        except Exception as ex:
            print_ex(ex)
            self.sig_info.emit('ExpMonitor Error')
    
        finally:
            self.file.close()
            return ready

    def RunExp(self):
        try:
            self.n=0
            #X-axis
            for i in range(len(self.xlist)):
                if i==0:
                    xdif=self.xlist[i]-0
                else:
                    xdif=self.xlist[i]-self.xlist[i-1]
                if xdif!=0:
                    self.sig_ascent.emit([0,xdif/1000])
                #Y-axis
                for j in range(len(self.ylist)):
                    if j==0 and i==0:
                        ydif=self.ylist[j]-0
                    elif j==0 and i!=0:
                        ydif=self.ylist[0]-self.ylist[-1]
                    else:
                        ydif=self.ylist[j]-self.ylist[j-1]
                    if ydif!=0:
                        self.sig_ascent.emit([1,ydif/1000])
                    #Z-axis
                    for k in range(len(self.zlist)):
                        if k==0 and j==0 and i==0   :
                            zdif=self.zlist[k]-0
                        elif k==0 and ((j or i)!=0):
                            zdif=self.zlist[0]-self.zlist[-1]
                        else:
                            zdif=self.zlist[k]-self.zlist[k-1]
                        if zdif!=0:
                            self.sig_ascent.emit([2,zdif/1000])
                        # start to monitor:
                        self.file = open(self.monitee, "r")
                        self.before=self.file.read()
                        self.file.close()
                        arg_err=None
                        while True:
                            self.file = open(self.monitee, "r")
                            time.sleep(0.2)
                            self.after = self.file.read()
                            self.file.close()
                            # loop-terminate trigger
                            if self.before!=self.after:
                                self.n+=1
                                self.sig_progressbar.emit(int(self.n/self.maxval*100))
                                self.mainthread.LogWriter(f'>>>Number {self.n} ({self.xlist[i]}.{self.ylist[j]}.{self.zlist[k]})  Loop Done')
                                break         
        except Exception as ex:
            print_ex(ex)

    def ReturnDistanceFile(self):
        datetoday=datetime.date.today().strftime("%Y%m%d")
        disDone=[f'{dis-min(self.zlist[0:self.n])}' for dis in self.zlist[0:self.n]]
        disAll=[f'{z}' for z in self.zlist]
        disDoneOutput=','.join(disDone)
        disAllOutput=','.join(disAll)
        dir=fr'C:\Users\jy1u18\OneDrive - University of Southampton\PhD\Second Project\Electrochemistry\{datetoday}'
        if not os.path.exists(dir):
            os.makedirs(dir)
        with open(fr'{dir}\disFile.txt','a') as disFile:
            disFile.writelines(f'Planned Steps: [{disAllOutput}]')
            disFile.writelines(f'Steps Done: [{disDoneOutput}]\n')


class RenameMonitor(QThread):

    def __init__(self,mainthread,path,format_list,value_list):
        super().__init__()
        self.mainthread=mainthread
        self.path=path
        self.format_list=format_list
        self.value_list=value_list
    def run(self):
        for value in self.value_list:
            for symbol in self.format_list:
                flag=True
                while flag==True:
                    time.sleep(1)
                    flag=self.Rename(symbol,value)
    def Rename(self,symbol,value):
        flag=True
        filelist=os.listdir(self.path)
        for file in filelist:
            if symbol in file:
                try:
                    flag=False
                    newname=file.replace(symbol, str(value))
                    os.rename(self.path+os.sep+file,self.path+os.sep+newname)
                except Exception as arg_err:
                    if arg_err==FileExistsError:
                        newname=file.replace('.txt', ' new.txt')
                        os.rename(self.path+os.sep+file,self.path+os.sep+newname)
                    elif arg_err==PermissionError or FileNotFoundError:
                        flag=True
                        print(f'PermissionError or FileNotFoundError')
                    else:
                        print(arg_err)
                        self.mainthread.LogWriter('Unexpected rename thread Error: ')
                        self.mainthread.LogWriter(arg_err)
        return flag 


