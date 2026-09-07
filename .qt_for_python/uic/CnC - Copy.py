# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CnC - Copy.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1180, 888)
        MainWindow.setStyleSheet(u"QMainWindow {\n"
"background-color: rgb(20, 20, 20)\n"
"}\n"
"\n"
"QMenuBar{\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QMenuBar QMenu{\n"
"background-color: rgb(20, 20, 20);\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QMenuBar::item:selected{\n"
"color:rgb(20, 20, 20);\n"
"background-color: rgb(255, 80, 0);\n"
"}\n"
"\n"
"QMenuBar QMenu::item:selected{\n"
"color:rgb(20, 20, 20);\n"
"background-color: rgb(255, 80, 0);\n"
"}\n"
"\n"
"QMainWindow QLabel{\n"
"font-family:Roboto;\n"
"font-style: normal;\n"
"font-size: 12pt;\n"
"color:rgb(220, 220, 220);\n"
"}\n"
"\n"
"QMainWindow QPushButton{\n"
"font-family:Roboto;\n"
"font-style: normal;\n"
"font-size: 12pt;\n"
"background-color:rgb(40, 40, 40);\n"
"color:rgb(220, 220, 220);\n"
"}\n"
"\n"
"QCheckBox{\n"
"font-family:Roboto;\n"
"font-style: normal;\n"
"font-size: 12pt;\n"
"color:rgb(220, 220, 220);\n"
"}")
        self.actionConnect_F2 = QAction(MainWindow)
        self.actionConnect_F2.setObjectName(u"actionConnect_F2")
        self.actionMapping_Coordination_File_Directory = QAction(MainWindow)
        self.actionMapping_Coordination_File_Directory.setObjectName(u"actionMapping_Coordination_File_Directory")
        self.actionFile_Directory = QAction(MainWindow)
        self.actionFile_Directory.setObjectName(u"actionFile_Directory")
        self.actionUnlock_Buttons = QAction(MainWindow)
        self.actionUnlock_Buttons.setObjectName(u"actionUnlock_Buttons")
        self.actionRefresh_Micropositioner_Reading = QAction(MainWindow)
        self.actionRefresh_Micropositioner_Reading.setObjectName(u"actionRefresh_Micropositioner_Reading")
        self.actionSet_Count_Text_File_Directory = QAction(MainWindow)
        self.actionSet_Count_Text_File_Directory.setObjectName(u"actionSet_Count_Text_File_Directory")
        self.actionSet_Log_File_Firectory = QAction(MainWindow)
        self.actionSet_Log_File_Firectory.setObjectName(u"actionSet_Log_File_Firectory")
        self.actionSet_Initial_Parameter_Directory = QAction(MainWindow)
        self.actionSet_Initial_Parameter_Directory.setObjectName(u"actionSet_Initial_Parameter_Directory")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_canvas1 = QLabel(self.centralwidget)
        self.label_canvas1.setObjectName(u"label_canvas1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_canvas1.sizePolicy().hasHeightForWidth())
        self.label_canvas1.setSizePolicy(sizePolicy)
        self.label_canvas1.setStyleSheet(u"frame-shape:Box;")
        self.label_canvas1.setFrameShape(QFrame.NoFrame)

        self.horizontalLayout_2.addWidget(self.label_canvas1)

        self.label_canvas2 = QLabel(self.centralwidget)
        self.label_canvas2.setObjectName(u"label_canvas2")
        self.label_canvas2.setStyleSheet(u"frame-shape:Box;")
        self.label_canvas2.setFrameShape(QFrame.Box)

        self.horizontalLayout_2.addWidget(self.label_canvas2)


        self.gridLayout_2.addLayout(self.horizontalLayout_2, 1, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_x = QHBoxLayout()
        self.horizontalLayout_x.setObjectName(u"horizontalLayout_x")
        self.checkBox_x_servo = QCheckBox(self.centralwidget)
        self.checkBox_x_servo.setObjectName(u"checkBox_x_servo")
        self.checkBox_x_servo.setStyleSheet(u"")

        self.horizontalLayout_x.addWidget(self.checkBox_x_servo)

        self.label_x = QLabel(self.centralwidget)
        self.label_x.setObjectName(u"label_x")
        sizePolicy.setHeightForWidth(self.label_x.sizePolicy().hasHeightForWidth())
        self.label_x.setSizePolicy(sizePolicy)
        self.label_x.setStyleSheet(u"")

        self.horizontalLayout_x.addWidget(self.label_x)

        self.pushButton_x_neg = QPushButton(self.centralwidget)
        self.pushButton_x_neg.setObjectName(u"pushButton_x_neg")
        sizePolicy1 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_x_neg.sizePolicy().hasHeightForWidth())
        self.pushButton_x_neg.setSizePolicy(sizePolicy1)

        self.horizontalLayout_x.addWidget(self.pushButton_x_neg)

        self.lineEdit_x_loc = QLineEdit(self.centralwidget)
        self.lineEdit_x_loc.setObjectName(u"lineEdit_x_loc")
        sizePolicy2 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.lineEdit_x_loc.sizePolicy().hasHeightForWidth())
        self.lineEdit_x_loc.setSizePolicy(sizePolicy2)
        self.lineEdit_x_loc.setReadOnly(True)

        self.horizontalLayout_x.addWidget(self.lineEdit_x_loc)

        self.pushButton_x_pos = QPushButton(self.centralwidget)
        self.pushButton_x_pos.setObjectName(u"pushButton_x_pos")
        sizePolicy3 = QSizePolicy(QSizePolicy.Ignored, QSizePolicy.Expanding)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.pushButton_x_pos.sizePolicy().hasHeightForWidth())
        self.pushButton_x_pos.setSizePolicy(sizePolicy3)

        self.horizontalLayout_x.addWidget(self.pushButton_x_pos)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_x_tp = QLabel(self.centralwidget)
        self.label_x_tp.setObjectName(u"label_x_tp")

        self.gridLayout.addWidget(self.label_x_tp, 0, 0, 1, 1)

        self.label_x_ss = QLabel(self.centralwidget)
        self.label_x_ss.setObjectName(u"label_x_ss")

        self.gridLayout.addWidget(self.label_x_ss, 1, 0, 1, 1)

        self.label_x_vel = QLabel(self.centralwidget)
        self.label_x_vel.setObjectName(u"label_x_vel")

        self.gridLayout.addWidget(self.label_x_vel, 2, 0, 1, 1)

        self.lineEdit_x_tp = QLineEdit(self.centralwidget)
        self.lineEdit_x_tp.setObjectName(u"lineEdit_x_tp")

        self.gridLayout.addWidget(self.lineEdit_x_tp, 0, 1, 1, 1)

        self.lineEdit_x_ss = QLineEdit(self.centralwidget)
        self.lineEdit_x_ss.setObjectName(u"lineEdit_x_ss")

        self.gridLayout.addWidget(self.lineEdit_x_ss, 1, 1, 1, 1)

        self.lineEdit_x_vel = QLineEdit(self.centralwidget)
        self.lineEdit_x_vel.setObjectName(u"lineEdit_x_vel")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.lineEdit_x_vel.sizePolicy().hasHeightForWidth())
        self.lineEdit_x_vel.setSizePolicy(sizePolicy4)

        self.gridLayout.addWidget(self.lineEdit_x_vel, 2, 1, 1, 1)


        self.horizontalLayout_x.addLayout(self.gridLayout)

        self.pushButton_x_go = QPushButton(self.centralwidget)
        self.pushButton_x_go.setObjectName(u"pushButton_x_go")
        sizePolicy1.setHeightForWidth(self.pushButton_x_go.sizePolicy().hasHeightForWidth())
        self.pushButton_x_go.setSizePolicy(sizePolicy1)

        self.horizontalLayout_x.addWidget(self.pushButton_x_go)

        self.pushButton_x_halt = QPushButton(self.centralwidget)
        self.pushButton_x_halt.setObjectName(u"pushButton_x_halt")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.pushButton_x_halt.sizePolicy().hasHeightForWidth())
        self.pushButton_x_halt.setSizePolicy(sizePolicy5)

        self.horizontalLayout_x.addWidget(self.pushButton_x_halt)

        self.horizontalLayout_x.setStretch(1, 1)
        self.horizontalLayout_x.setStretch(2, 1)
        self.horizontalLayout_x.setStretch(3, 10)
        self.horizontalLayout_x.setStretch(4, 1)
        self.horizontalLayout_x.setStretch(5, 8)
        self.horizontalLayout_x.setStretch(6, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_x)

        self.horizontalLayout_y = QHBoxLayout()
        self.horizontalLayout_y.setObjectName(u"horizontalLayout_y")
        self.checkBox_y_servo = QCheckBox(self.centralwidget)
        self.checkBox_y_servo.setObjectName(u"checkBox_y_servo")
        self.checkBox_y_servo.setStyleSheet(u"")

        self.horizontalLayout_y.addWidget(self.checkBox_y_servo)

        self.label_y = QLabel(self.centralwidget)
        self.label_y.setObjectName(u"label_y")
        sizePolicy.setHeightForWidth(self.label_y.sizePolicy().hasHeightForWidth())
        self.label_y.setSizePolicy(sizePolicy)
        self.label_y.setStyleSheet(u"")

        self.horizontalLayout_y.addWidget(self.label_y)

        self.pushButton_y_neg = QPushButton(self.centralwidget)
        self.pushButton_y_neg.setObjectName(u"pushButton_y_neg")
        sizePolicy1.setHeightForWidth(self.pushButton_y_neg.sizePolicy().hasHeightForWidth())
        self.pushButton_y_neg.setSizePolicy(sizePolicy1)

        self.horizontalLayout_y.addWidget(self.pushButton_y_neg)

        self.lineEdit_y_loc = QLineEdit(self.centralwidget)
        self.lineEdit_y_loc.setObjectName(u"lineEdit_y_loc")
        sizePolicy2.setHeightForWidth(self.lineEdit_y_loc.sizePolicy().hasHeightForWidth())
        self.lineEdit_y_loc.setSizePolicy(sizePolicy2)
        self.lineEdit_y_loc.setReadOnly(True)

        self.horizontalLayout_y.addWidget(self.lineEdit_y_loc)

        self.pushButton_y_pos = QPushButton(self.centralwidget)
        self.pushButton_y_pos.setObjectName(u"pushButton_y_pos")
        sizePolicy3.setHeightForWidth(self.pushButton_y_pos.sizePolicy().hasHeightForWidth())
        self.pushButton_y_pos.setSizePolicy(sizePolicy3)

        self.horizontalLayout_y.addWidget(self.pushButton_y_pos)

        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.label_y_tp = QLabel(self.centralwidget)
        self.label_y_tp.setObjectName(u"label_y_tp")

        self.gridLayout_3.addWidget(self.label_y_tp, 0, 0, 1, 1)

        self.label_y_ss = QLabel(self.centralwidget)
        self.label_y_ss.setObjectName(u"label_y_ss")

        self.gridLayout_3.addWidget(self.label_y_ss, 1, 0, 1, 1)

        self.label_y_vel = QLabel(self.centralwidget)
        self.label_y_vel.setObjectName(u"label_y_vel")

        self.gridLayout_3.addWidget(self.label_y_vel, 2, 0, 1, 1)

        self.lineEdit_y_tp = QLineEdit(self.centralwidget)
        self.lineEdit_y_tp.setObjectName(u"lineEdit_y_tp")

        self.gridLayout_3.addWidget(self.lineEdit_y_tp, 0, 1, 1, 1)

        self.lineEdit_y_ss = QLineEdit(self.centralwidget)
        self.lineEdit_y_ss.setObjectName(u"lineEdit_y_ss")

        self.gridLayout_3.addWidget(self.lineEdit_y_ss, 1, 1, 1, 1)

        self.lineEdit_y_vel = QLineEdit(self.centralwidget)
        self.lineEdit_y_vel.setObjectName(u"lineEdit_y_vel")
        sizePolicy4.setHeightForWidth(self.lineEdit_y_vel.sizePolicy().hasHeightForWidth())
        self.lineEdit_y_vel.setSizePolicy(sizePolicy4)

        self.gridLayout_3.addWidget(self.lineEdit_y_vel, 2, 1, 1, 1)


        self.horizontalLayout_y.addLayout(self.gridLayout_3)

        self.pushButton_y_go = QPushButton(self.centralwidget)
        self.pushButton_y_go.setObjectName(u"pushButton_y_go")
        sizePolicy1.setHeightForWidth(self.pushButton_y_go.sizePolicy().hasHeightForWidth())
        self.pushButton_y_go.setSizePolicy(sizePolicy1)

        self.horizontalLayout_y.addWidget(self.pushButton_y_go)

        self.pushButton_y_halt = QPushButton(self.centralwidget)
        self.pushButton_y_halt.setObjectName(u"pushButton_y_halt")
        sizePolicy5.setHeightForWidth(self.pushButton_y_halt.sizePolicy().hasHeightForWidth())
        self.pushButton_y_halt.setSizePolicy(sizePolicy5)

        self.horizontalLayout_y.addWidget(self.pushButton_y_halt)

        self.horizontalLayout_y.setStretch(1, 1)
        self.horizontalLayout_y.setStretch(2, 1)
        self.horizontalLayout_y.setStretch(3, 10)
        self.horizontalLayout_y.setStretch(4, 1)
        self.horizontalLayout_y.setStretch(5, 8)
        self.horizontalLayout_y.setStretch(6, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_y)

        self.horizontalLayout_z = QHBoxLayout()
        self.horizontalLayout_z.setObjectName(u"horizontalLayout_z")
        self.checkBox_z_servo = QCheckBox(self.centralwidget)
        self.checkBox_z_servo.setObjectName(u"checkBox_z_servo")
        self.checkBox_z_servo.setStyleSheet(u"")

        self.horizontalLayout_z.addWidget(self.checkBox_z_servo)

        self.label_z = QLabel(self.centralwidget)
        self.label_z.setObjectName(u"label_z")
        sizePolicy.setHeightForWidth(self.label_z.sizePolicy().hasHeightForWidth())
        self.label_z.setSizePolicy(sizePolicy)
        self.label_z.setStyleSheet(u"")

        self.horizontalLayout_z.addWidget(self.label_z)

        self.pushButton_z_neg = QPushButton(self.centralwidget)
        self.pushButton_z_neg.setObjectName(u"pushButton_z_neg")
        sizePolicy1.setHeightForWidth(self.pushButton_z_neg.sizePolicy().hasHeightForWidth())
        self.pushButton_z_neg.setSizePolicy(sizePolicy1)

        self.horizontalLayout_z.addWidget(self.pushButton_z_neg)

        self.lineEdit_z_loc = QLineEdit(self.centralwidget)
        self.lineEdit_z_loc.setObjectName(u"lineEdit_z_loc")
        sizePolicy2.setHeightForWidth(self.lineEdit_z_loc.sizePolicy().hasHeightForWidth())
        self.lineEdit_z_loc.setSizePolicy(sizePolicy2)
        self.lineEdit_z_loc.setReadOnly(True)

        self.horizontalLayout_z.addWidget(self.lineEdit_z_loc)

        self.pushButton_z_pos = QPushButton(self.centralwidget)
        self.pushButton_z_pos.setObjectName(u"pushButton_z_pos")
        sizePolicy3.setHeightForWidth(self.pushButton_z_pos.sizePolicy().hasHeightForWidth())
        self.pushButton_z_pos.setSizePolicy(sizePolicy3)

        self.horizontalLayout_z.addWidget(self.pushButton_z_pos)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.label_z_tp = QLabel(self.centralwidget)
        self.label_z_tp.setObjectName(u"label_z_tp")

        self.gridLayout_5.addWidget(self.label_z_tp, 0, 0, 1, 1)

        self.label_z_ss = QLabel(self.centralwidget)
        self.label_z_ss.setObjectName(u"label_z_ss")

        self.gridLayout_5.addWidget(self.label_z_ss, 1, 0, 1, 1)

        self.label_z_vel = QLabel(self.centralwidget)
        self.label_z_vel.setObjectName(u"label_z_vel")

        self.gridLayout_5.addWidget(self.label_z_vel, 2, 0, 1, 1)

        self.lineEdit_z_tp = QLineEdit(self.centralwidget)
        self.lineEdit_z_tp.setObjectName(u"lineEdit_z_tp")

        self.gridLayout_5.addWidget(self.lineEdit_z_tp, 0, 1, 1, 1)

        self.lineEdit_z_ss = QLineEdit(self.centralwidget)
        self.lineEdit_z_ss.setObjectName(u"lineEdit_z_ss")

        self.gridLayout_5.addWidget(self.lineEdit_z_ss, 1, 1, 1, 1)

        self.lineEdit_z_vel = QLineEdit(self.centralwidget)
        self.lineEdit_z_vel.setObjectName(u"lineEdit_z_vel")
        sizePolicy4.setHeightForWidth(self.lineEdit_z_vel.sizePolicy().hasHeightForWidth())
        self.lineEdit_z_vel.setSizePolicy(sizePolicy4)

        self.gridLayout_5.addWidget(self.lineEdit_z_vel, 2, 1, 1, 1)


        self.horizontalLayout_z.addLayout(self.gridLayout_5)

        self.pushButton_z_go = QPushButton(self.centralwidget)
        self.pushButton_z_go.setObjectName(u"pushButton_z_go")
        sizePolicy1.setHeightForWidth(self.pushButton_z_go.sizePolicy().hasHeightForWidth())
        self.pushButton_z_go.setSizePolicy(sizePolicy1)

        self.horizontalLayout_z.addWidget(self.pushButton_z_go)

        self.pushButton_z_halt = QPushButton(self.centralwidget)
        self.pushButton_z_halt.setObjectName(u"pushButton_z_halt")
        sizePolicy5.setHeightForWidth(self.pushButton_z_halt.sizePolicy().hasHeightForWidth())
        self.pushButton_z_halt.setSizePolicy(sizePolicy5)

        self.horizontalLayout_z.addWidget(self.pushButton_z_halt)

        self.horizontalLayout_z.setStretch(1, 1)
        self.horizontalLayout_z.setStretch(2, 1)
        self.horizontalLayout_z.setStretch(3, 10)
        self.horizontalLayout_z.setStretch(4, 1)
        self.horizontalLayout_z.setStretch(5, 8)
        self.horizontalLayout_z.setStretch(6, 2)

        self.verticalLayout_3.addLayout(self.horizontalLayout_z)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout.setStretch(0, 2)

        self.gridLayout_2.addLayout(self.verticalLayout, 4, 0, 1, 1)

        self.lineEdit_filename = QLineEdit(self.centralwidget)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")

        self.gridLayout_2.addWidget(self.lineEdit_filename, 0, 0, 1, 2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_appmap = QPushButton(self.centralwidget)
        self.pushButton_appmap.setObjectName(u"pushButton_appmap")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.pushButton_appmap.sizePolicy().hasHeightForWidth())
        self.pushButton_appmap.setSizePolicy(sizePolicy6)

        self.verticalLayout_4.addWidget(self.pushButton_appmap)


        self.gridLayout_2.addLayout(self.verticalLayout_4, 5, 0, 1, 2)

        self.textBrowser_log = QTextBrowser(self.centralwidget)
        self.textBrowser_log.setObjectName(u"textBrowser_log")
        sizePolicy7 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.textBrowser_log.sizePolicy().hasHeightForWidth())
        self.textBrowser_log.setSizePolicy(sizePolicy7)

        self.gridLayout_2.addWidget(self.textBrowser_log, 4, 1, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_cam2re = QPushButton(self.centralwidget)
        self.pushButton_cam2re.setObjectName(u"pushButton_cam2re")
        sizePolicy8 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(1)
        sizePolicy8.setHeightForWidth(self.pushButton_cam2re.sizePolicy().hasHeightForWidth())
        self.pushButton_cam2re.setSizePolicy(sizePolicy8)
        self.pushButton_cam2re.setStyleSheet(u"")
        self.pushButton_cam2re.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam2re, 1, 2, 1, 1)

        self.pushButton_cam1 = QPushButton(self.centralwidget)
        self.pushButton_cam1.setObjectName(u"pushButton_cam1")
        self.pushButton_cam1.setEnabled(True)
        sizePolicy8.setHeightForWidth(self.pushButton_cam1.sizePolicy().hasHeightForWidth())
        self.pushButton_cam1.setSizePolicy(sizePolicy8)
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        self.pushButton_cam1.setFont(font)
        self.pushButton_cam1.setStyleSheet(u"")
        self.pushButton_cam1.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam1, 0, 0, 1, 2)

        self.pushButton_cam2cap = QPushButton(self.centralwidget)
        self.pushButton_cam2cap.setObjectName(u"pushButton_cam2cap")
        sizePolicy8.setHeightForWidth(self.pushButton_cam2cap.sizePolicy().hasHeightForWidth())
        self.pushButton_cam2cap.setSizePolicy(sizePolicy8)
        self.pushButton_cam2cap.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.pushButton_cam2cap, 1, 3, 1, 1)

        self.pushButton_cam1cap = QPushButton(self.centralwidget)
        self.pushButton_cam1cap.setObjectName(u"pushButton_cam1cap")
        sizePolicy8.setHeightForWidth(self.pushButton_cam1cap.sizePolicy().hasHeightForWidth())
        self.pushButton_cam1cap.setSizePolicy(sizePolicy8)
        self.pushButton_cam1cap.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.pushButton_cam1cap, 1, 1, 1, 1)

        self.pushButton_cam2 = QPushButton(self.centralwidget)
        self.pushButton_cam2.setObjectName(u"pushButton_cam2")
        sizePolicy8.setHeightForWidth(self.pushButton_cam2.sizePolicy().hasHeightForWidth())
        self.pushButton_cam2.setSizePolicy(sizePolicy8)
        self.pushButton_cam2.setStyleSheet(u"")
        self.pushButton_cam2.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam2, 0, 2, 1, 2)

        self.pushButton_reall = QPushButton(self.centralwidget)
        self.pushButton_reall.setObjectName(u"pushButton_reall")
        sizePolicy9 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.pushButton_reall.sizePolicy().hasHeightForWidth())
        self.pushButton_reall.setSizePolicy(sizePolicy9)
        self.pushButton_reall.setStyleSheet(u"")
        self.pushButton_reall.setCheckable(True)

        self.gridLayout_4.addWidget(self.pushButton_reall, 2, 0, 1, 4)

        self.pushButton_cam1re = QPushButton(self.centralwidget)
        self.pushButton_cam1re.setObjectName(u"pushButton_cam1re")
        sizePolicy8.setHeightForWidth(self.pushButton_cam1re.sizePolicy().hasHeightForWidth())
        self.pushButton_cam1re.setSizePolicy(sizePolicy8)
        self.pushButton_cam1re.setStyleSheet(u"")
        self.pushButton_cam1re.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam1re, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 2)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShadow(QFrame.Raised)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.gridLayout_2.addWidget(self.line, 3, 0, 1, 2)

        self.gridLayout_2.setRowStretch(1, 5)
        self.gridLayout_2.setColumnStretch(0, 5)
        self.gridLayout_2.setColumnStretch(1, 3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1180, 22))
        self.menubar.setStyleSheet(u"")
        self.menuMicropositioner = QMenu(self.menubar)
        self.menuMicropositioner.setObjectName(u"menuMicropositioner")
        self.menuMicropositioner.setStyleSheet(u"")
        self.menuCamera = QMenu(self.menubar)
        self.menuCamera.setObjectName(u"menuCamera")
        self.menuGUI = QMenu(self.menubar)
        self.menuGUI.setObjectName(u"menuGUI")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuMicropositioner.menuAction())
        self.menubar.addAction(self.menuCamera.menuAction())
        self.menubar.addAction(self.menuGUI.menuAction())
        self.menuMicropositioner.addAction(self.actionConnect_F2)
        self.menuMicropositioner.addSeparator()
        self.menuMicropositioner.addAction(self.actionMapping_Coordination_File_Directory)
        self.menuMicropositioner.addAction(self.actionSet_Count_Text_File_Directory)
        self.menuMicropositioner.addAction(self.actionSet_Log_File_Firectory)
        self.menuMicropositioner.addAction(self.actionSet_Initial_Parameter_Directory)
        self.menuCamera.addAction(self.actionFile_Directory)
        self.menuGUI.addAction(self.actionUnlock_Buttons)
        self.menuGUI.addAction(self.actionRefresh_Micropositioner_Reading)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionConnect_F2.setText(QCoreApplication.translate("MainWindow", u"Connect", None))
#if QT_CONFIG(shortcut)
        self.actionConnect_F2.setShortcut(QCoreApplication.translate("MainWindow", u"F2", None))
#endif // QT_CONFIG(shortcut)
        self.actionMapping_Coordination_File_Directory.setText(QCoreApplication.translate("MainWindow", u"Set Mapping Coordination File Directory", None))
        self.actionFile_Directory.setText(QCoreApplication.translate("MainWindow", u"Set Image/Video File Directory", None))
        self.actionUnlock_Buttons.setText(QCoreApplication.translate("MainWindow", u"Unlock Buttons", None))
        self.actionRefresh_Micropositioner_Reading.setText(QCoreApplication.translate("MainWindow", u"Refresh Micropositioner Reading", None))
#if QT_CONFIG(shortcut)
        self.actionRefresh_Micropositioner_Reading.setShortcut(QCoreApplication.translate("MainWindow", u"F5", None))
#endif // QT_CONFIG(shortcut)
        self.actionSet_Count_Text_File_Directory.setText(QCoreApplication.translate("MainWindow", u"Set Count Text File Directory", None))
        self.actionSet_Log_File_Firectory.setText(QCoreApplication.translate("MainWindow", u"Set Log File Firectory", None))
        self.actionSet_Initial_Parameter_Directory.setText(QCoreApplication.translate("MainWindow", u"Set Initial Parameter Directory", None))
        self.label_canvas1.setText("")
        self.label_canvas2.setText("")
        self.checkBox_x_servo.setText(QCoreApplication.translate("MainWindow", u"Servo", None))
        self.label_x.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">X</span></p></body></html>", None))
        self.pushButton_x_neg.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.lineEdit_x_loc.setText(QCoreApplication.translate("MainWindow", u"0.0000", None))
        self.pushButton_x_pos.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_x_tp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Target Position</p></body></html>", None))
        self.label_x_ss.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Step Size</p></body></html>", None))
        self.label_x_vel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Velocity</p></body></html>", None))
        self.pushButton_x_go.setText(QCoreApplication.translate("MainWindow", u"Go to", None))
        self.pushButton_x_halt.setText(QCoreApplication.translate("MainWindow", u"Halt", None))
        self.checkBox_y_servo.setText(QCoreApplication.translate("MainWindow", u"Servo", None))
        self.label_y.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Y</span></p></body></html>", None))
        self.pushButton_y_neg.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_y_pos.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_y_tp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Target Position</p></body></html>", None))
        self.label_y_ss.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Step Size</p></body></html>", None))
        self.label_y_vel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Velocity</p></body></html>", None))
        self.pushButton_y_go.setText(QCoreApplication.translate("MainWindow", u"Go to", None))
        self.pushButton_y_halt.setText(QCoreApplication.translate("MainWindow", u"Halt", None))
        self.checkBox_z_servo.setText(QCoreApplication.translate("MainWindow", u"Servo", None))
        self.label_z.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-weight:600;\">Z</span></p></body></html>", None))
        self.pushButton_z_neg.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.pushButton_z_pos.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.label_z_tp.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Target Position</p></body></html>", None))
        self.label_z_ss.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Step Size</p></body></html>", None))
        self.label_z_vel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">Velocity</p></body></html>", None))
        self.pushButton_z_go.setText(QCoreApplication.translate("MainWindow", u"Go to", None))
        self.pushButton_z_halt.setText(QCoreApplication.translate("MainWindow", u"Halt", None))
        self.pushButton_appmap.setText(QCoreApplication.translate("MainWindow", u"ApproachCurve-Map", None))
        self.pushButton_cam2re.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.pushButton_cam1.setText(QCoreApplication.translate("MainWindow", u"Camera 1 ", None))
        self.pushButton_cam2cap.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushButton_cam1cap.setText(QCoreApplication.translate("MainWindow", u"Capture", None))
        self.pushButton_cam2.setText(QCoreApplication.translate("MainWindow", u"Camera 2", None))
        self.pushButton_reall.setText(QCoreApplication.translate("MainWindow", u"Record All", None))
        self.pushButton_cam1re.setText(QCoreApplication.translate("MainWindow", u"Record", None))
        self.menuMicropositioner.setTitle(QCoreApplication.translate("MainWindow", u"Micropositioner", None))
        self.menuCamera.setTitle(QCoreApplication.translate("MainWindow", u"Camera", None))
        self.menuGUI.setTitle(QCoreApplication.translate("MainWindow", u"GUI", None))
    # retranslateUi

