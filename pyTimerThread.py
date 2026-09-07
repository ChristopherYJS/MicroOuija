from PyQt5.QtGui import *
from PyQt5.QtCore import QThread, pyqtSignal 

from PrintException import print_ex

import os
import time
import datetime

class OnTargetTimer(QThread):
    sig_refresh=pyqtSignal()
    flag=True
    def __init__(self):
        super().__init__()
        
    def run(self):
        while True:
            if self.flag==True:
                self.sig_refresh.emit()
                time.sleep(0.5)
            else:
                continue