# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiMappingWin.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(639, 361)
        Form.setStyleSheet(u"QWidget {\n"
"background-color: rgb(20, 20, 20)\n"
"}\n"
"\n"
"QWidget QTabWidget Line{\n"
"color: rgb(220,220,220);\n"
"}\n"
"\n"
"QTabWidget{\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(220, 220, 220);\n"
"}\n"
"\n"
"QTabBar::tab{\n"
"background-color: rgb(40, 40, 40);\n"
"color: rgb(220, 220, 220);\n"
"height: 20px;\n"
"width: 130px\n"
"}\n"
"\n"
"QTabBar::tab:selected{\n"
"color:rgb(20, 20, 20);\n"
"background-color: rgb(255, 80, 0);\n"
"font-weight: bold;\n"
"\n"
"}\n"
"\n"
"QWidget QLabel{\n"
"font-family:Roboto;\n"
"font-style: normal;\n"
"font-size: 12pt;\n"
"color:rgb(220, 220, 220);\n"
"}\n"
"\n"
"QWidget QPushButton{\n"
"font-family:Roboto;\n"
"font-style: normal;\n"
"font-size: 12pt;\n"
"background-color:rgb(40, 40, 40);\n"
"color:rgb(220, 220, 220);\n"
"}\n"
"\n"
"QWidget QPushButton:hover{\n"
"background-color:rgb(255, 80, 0);\n"
"color:rgb(20, 20, 20);\n"
"}\n"
"\n"
"QWidget QToolButton{\n"
"font-family:Roboto;\n"
"font-style: normal;\n"
"font-size: 12pt;\n"
"background-color:rgb(40, 4"
                        "0, 40);\n"
"color:rgb(220, 220, 220);\n"
"}\n"
"\n"
"QWidget QToolButton:hover{\n"
"background-color:rgb(255, 80, 0);\n"
"color:rgb(20, 20, 20);\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(150,150,150);\n"
"color: rgb(220,220,220);\n"
"font-family:Roboto; \n"
"font-size:10pt;\n"
"}\n"
"\n"
"QComboBox{\n"
"background-color: rgb(150,150,150);\n"
"color: rgb(220,220,220);\n"
"font-family:Roboto; \n"
"font-size:10pt;\n"
"}")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setFocusPolicy(Qt.NoFocus)
        self.tabWidget.setStyleSheet(u"Line{\n"
"color: rgb(220,220,220);\n"
"}")
        self.tabWidget.setTabShape(QTabWidget.Rounded)
        self.tabWidget.setElideMode(Qt.ElideNone)
        self.tab1 = QWidget()
        self.tab1.setObjectName(u"tab1")
        self.verticalLayout_2 = QVBoxLayout(self.tab1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label_xp_tab1 = QLabel(self.tab1)
        self.label_xp_tab1.setObjectName(u"label_xp_tab1")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_xp_tab1.sizePolicy().hasHeightForWidth())
        self.label_xp_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_1.addWidget(self.label_xp_tab1)

        self.lineEdit_xp_tab1 = QLineEdit(self.tab1)
        self.lineEdit_xp_tab1.setObjectName(u"lineEdit_xp_tab1")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_xp_tab1.sizePolicy().hasHeightForWidth())
        self.lineEdit_xp_tab1.setSizePolicy(sizePolicy1)
        self.lineEdit_xp_tab1.setFrame(False)

        self.horizontalLayout_1.addWidget(self.lineEdit_xp_tab1)

        self.horizontalLayout_1.setStretch(0, 1)
        self.horizontalLayout_1.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_yp_tab1 = QLabel(self.tab1)
        self.label_yp_tab1.setObjectName(u"label_yp_tab1")
        sizePolicy.setHeightForWidth(self.label_yp_tab1.sizePolicy().hasHeightForWidth())
        self.label_yp_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_yp_tab1)

        self.lineEdit_yp_tab1 = QLineEdit(self.tab1)
        self.lineEdit_yp_tab1.setObjectName(u"lineEdit_yp_tab1")
        sizePolicy1.setHeightForWidth(self.lineEdit_yp_tab1.sizePolicy().hasHeightForWidth())
        self.lineEdit_yp_tab1.setSizePolicy(sizePolicy1)
        self.lineEdit_yp_tab1.setFrame(False)

        self.horizontalLayout_2.addWidget(self.lineEdit_yp_tab1)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_zp_tab1 = QLabel(self.tab1)
        self.label_zp_tab1.setObjectName(u"label_zp_tab1")
        sizePolicy.setHeightForWidth(self.label_zp_tab1.sizePolicy().hasHeightForWidth())
        self.label_zp_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_zp_tab1)

        self.combo_zp_tab1 = QComboBox(self.tab1)
        self.combo_zp_tab1.addItem("")
        self.combo_zp_tab1.setObjectName(u"combo_zp_tab1")
        self.combo_zp_tab1.setEditable(True)
        self.combo_zp_tab1.setFrame(True)
        self.combo_zp_tab1.setModelColumn(0)

        self.horizontalLayout_3.addWidget(self.combo_zp_tab1)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_3d_tab1 = QLabel(self.tab1)
        self.label_3d_tab1.setObjectName(u"label_3d_tab1")
        sizePolicy.setHeightForWidth(self.label_3d_tab1.sizePolicy().hasHeightForWidth())
        self.label_3d_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_3d_tab1)

        self.lineEdit_3d_tab1 = QLineEdit(self.tab1)
        self.lineEdit_3d_tab1.setObjectName(u"lineEdit_3d_tab1")
        sizePolicy.setHeightForWidth(self.lineEdit_3d_tab1.sizePolicy().hasHeightForWidth())
        self.lineEdit_3d_tab1.setSizePolicy(sizePolicy)
        self.lineEdit_3d_tab1.setFrame(False)
        self.lineEdit_3d_tab1.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_3d_tab1)

        self.label_2d_tab1 = QLabel(self.tab1)
        self.label_2d_tab1.setObjectName(u"label_2d_tab1")
        sizePolicy.setHeightForWidth(self.label_2d_tab1.sizePolicy().hasHeightForWidth())
        self.label_2d_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_2d_tab1)

        self.lineEdit_2d_tab1 = QLineEdit(self.tab1)
        self.lineEdit_2d_tab1.setObjectName(u"lineEdit_2d_tab1")
        sizePolicy1.setHeightForWidth(self.lineEdit_2d_tab1.sizePolicy().hasHeightForWidth())
        self.lineEdit_2d_tab1.setSizePolicy(sizePolicy1)
        self.lineEdit_2d_tab1.setFrame(False)
        self.lineEdit_2d_tab1.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_2d_tab1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.line = QFrame(self.tab1)
        self.line.setObjectName(u"line")
        self.line.setAutoFillBackground(False)
        self.line.setStyleSheet(u"color: rgb(220,220,220)")
        self.line.setFrameShadow(QFrame.Plain)
        self.line.setLineWidth(1)
        self.line.setMidLineWidth(0)
        self.line.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_OCR_tab1 = QPushButton(self.tab1)
        self.pushButton_OCR_tab1.setObjectName(u"pushButton_OCR_tab1")
        self.pushButton_OCR_tab1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_OCR_tab1.sizePolicy().hasHeightForWidth())
        self.pushButton_OCR_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.pushButton_OCR_tab1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_tt_tab1 = QLabel(self.tab1)
        self.label_tt_tab1.setObjectName(u"label_tt_tab1")
        sizePolicy.setHeightForWidth(self.label_tt_tab1.sizePolicy().hasHeightForWidth())
        self.label_tt_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_tt_tab1)

        self.lineEdit_tt_tab1 = QLineEdit(self.tab1)
        self.lineEdit_tt_tab1.setObjectName(u"lineEdit_tt_tab1")
        sizePolicy1.setHeightForWidth(self.lineEdit_tt_tab1.sizePolicy().hasHeightForWidth())
        self.lineEdit_tt_tab1.setSizePolicy(sizePolicy1)
        self.lineEdit_tt_tab1.setFrame(False)

        self.horizontalLayout_6.addWidget(self.lineEdit_tt_tab1)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.line_3 = QFrame(self.tab1)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setStyleSheet(u"color: rgb(220,220,220)")
        self.line_3.setFrameShadow(QFrame.Plain)
        self.line_3.setFrameShape(QFrame.HLine)

        self.verticalLayout_2.addWidget(self.line_3)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton_proceed_tab1 = QPushButton(self.tab1)
        self.pushButton_proceed_tab1.setObjectName(u"pushButton_proceed_tab1")
        self.pushButton_proceed_tab1.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_proceed_tab1.sizePolicy().hasHeightForWidth())
        self.pushButton_proceed_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.pushButton_proceed_tab1)

        self.pushButton_clear_tab1 = QPushButton(self.tab1)
        self.pushButton_clear_tab1.setObjectName(u"pushButton_clear_tab1")
        sizePolicy.setHeightForWidth(self.pushButton_clear_tab1.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_tab1.setSizePolicy(sizePolicy)

        self.horizontalLayout_7.addWidget(self.pushButton_clear_tab1)


        self.verticalLayout_2.addLayout(self.horizontalLayout_7)

        self.tabWidget.addTab(self.tab1, "")
        self.tab2 = QWidget()
        self.tab2.setObjectName(u"tab2")
        self.verticalLayout_4 = QVBoxLayout(self.tab2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_xp_tab2 = QLabel(self.tab2)
        self.label_xp_tab2.setObjectName(u"label_xp_tab2")
        sizePolicy.setHeightForWidth(self.label_xp_tab2.sizePolicy().hasHeightForWidth())
        self.label_xp_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.label_xp_tab2)

        self.lineEdit_xp_tab2 = QLineEdit(self.tab2)
        self.lineEdit_xp_tab2.setObjectName(u"lineEdit_xp_tab2")
        sizePolicy1.setHeightForWidth(self.lineEdit_xp_tab2.sizePolicy().hasHeightForWidth())
        self.lineEdit_xp_tab2.setSizePolicy(sizePolicy1)
        self.lineEdit_xp_tab2.setFrame(False)

        self.horizontalLayout_8.addWidget(self.lineEdit_xp_tab2)

        self.horizontalLayout_8.setStretch(0, 1)
        self.horizontalLayout_8.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_yp_tab2 = QLabel(self.tab2)
        self.label_yp_tab2.setObjectName(u"label_yp_tab2")
        sizePolicy.setHeightForWidth(self.label_yp_tab2.sizePolicy().hasHeightForWidth())
        self.label_yp_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_9.addWidget(self.label_yp_tab2)

        self.lineEdit_yp_tab2 = QLineEdit(self.tab2)
        self.lineEdit_yp_tab2.setObjectName(u"lineEdit_yp_tab2")
        sizePolicy1.setHeightForWidth(self.lineEdit_yp_tab2.sizePolicy().hasHeightForWidth())
        self.lineEdit_yp_tab2.setSizePolicy(sizePolicy1)
        self.lineEdit_yp_tab2.setFrame(False)

        self.horizontalLayout_9.addWidget(self.lineEdit_yp_tab2)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_zp_tab2 = QLabel(self.tab2)
        self.label_zp_tab2.setObjectName(u"label_zp_tab2")
        sizePolicy.setHeightForWidth(self.label_zp_tab2.sizePolicy().hasHeightForWidth())
        self.label_zp_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.label_zp_tab2)

        self.combo_zp_tab2 = QComboBox(self.tab2)
        self.combo_zp_tab2.setObjectName(u"combo_zp_tab2")
        self.combo_zp_tab2.setEditable(True)

        self.horizontalLayout_10.addWidget(self.combo_zp_tab2)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_3d_tab2 = QLabel(self.tab2)
        self.label_3d_tab2.setObjectName(u"label_3d_tab2")
        sizePolicy.setHeightForWidth(self.label_3d_tab2.sizePolicy().hasHeightForWidth())
        self.label_3d_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_3d_tab2)

        self.lineEdit_3d_tab2 = QLineEdit(self.tab2)
        self.lineEdit_3d_tab2.setObjectName(u"lineEdit_3d_tab2")
        sizePolicy.setHeightForWidth(self.lineEdit_3d_tab2.sizePolicy().hasHeightForWidth())
        self.lineEdit_3d_tab2.setSizePolicy(sizePolicy)
        self.lineEdit_3d_tab2.setFrame(False)
        self.lineEdit_3d_tab2.setReadOnly(False)

        self.horizontalLayout_11.addWidget(self.lineEdit_3d_tab2)

        self.label_2d_tab2 = QLabel(self.tab2)
        self.label_2d_tab2.setObjectName(u"label_2d_tab2")
        sizePolicy.setHeightForWidth(self.label_2d_tab2.sizePolicy().hasHeightForWidth())
        self.label_2d_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_2d_tab2)

        self.lineEdit_2d_tab2 = QLineEdit(self.tab2)
        self.lineEdit_2d_tab2.setObjectName(u"lineEdit_2d_tab2")
        sizePolicy1.setHeightForWidth(self.lineEdit_2d_tab2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2d_tab2.setSizePolicy(sizePolicy1)
        self.lineEdit_2d_tab2.setFrame(False)
        self.lineEdit_2d_tab2.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_2d_tab2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.line_4 = QFrame(self.tab2)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setStyleSheet(u"color: rgb(220,220,220)")
        self.line_4.setFrameShadow(QFrame.Plain)
        self.line_4.setFrameShape(QFrame.HLine)

        self.verticalLayout_4.addWidget(self.line_4)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_cf_tab2 = QLabel(self.tab2)
        self.label_cf_tab2.setObjectName(u"label_cf_tab2")
        sizePolicy.setHeightForWidth(self.label_cf_tab2.sizePolicy().hasHeightForWidth())
        self.label_cf_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_12.addWidget(self.label_cf_tab2)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lineEdit_cf_tab2 = QLineEdit(self.tab2)
        self.lineEdit_cf_tab2.setObjectName(u"lineEdit_cf_tab2")
        sizePolicy1.setHeightForWidth(self.lineEdit_cf_tab2.sizePolicy().hasHeightForWidth())
        self.lineEdit_cf_tab2.setSizePolicy(sizePolicy1)
        self.lineEdit_cf_tab2.setFrame(False)

        self.horizontalLayout_13.addWidget(self.lineEdit_cf_tab2)

        self.toolButton_cf_tab2 = QToolButton(self.tab2)
        self.toolButton_cf_tab2.setObjectName(u"toolButton_cf_tab2")

        self.horizontalLayout_13.addWidget(self.toolButton_cf_tab2)


        self.horizontalLayout_12.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.line_5 = QFrame(self.tab2)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setStyleSheet(u"color: rgb(220,220,220)")
        self.line_5.setFrameShadow(QFrame.Plain)
        self.line_5.setFrameShape(QFrame.HLine)

        self.verticalLayout_4.addWidget(self.line_5)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.pushButton_proceed_tab2 = QPushButton(self.tab2)
        self.pushButton_proceed_tab2.setObjectName(u"pushButton_proceed_tab2")
        self.pushButton_proceed_tab2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_proceed_tab2.sizePolicy().hasHeightForWidth())
        self.pushButton_proceed_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.pushButton_proceed_tab2)

        self.pushButton_clear_tab2 = QPushButton(self.tab2)
        self.pushButton_clear_tab2.setObjectName(u"pushButton_clear_tab2")
        sizePolicy.setHeightForWidth(self.pushButton_clear_tab2.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_tab2.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.pushButton_clear_tab2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_14)

        self.tabWidget.addTab(self.tab2, "")
        self.tab3 = QWidget()
        self.tab3.setObjectName(u"tab3")
        self.verticalLayout_3 = QVBoxLayout(self.tab3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_xp_tab3 = QLabel(self.tab3)
        self.label_xp_tab3.setObjectName(u"label_xp_tab3")
        sizePolicy.setHeightForWidth(self.label_xp_tab3.sizePolicy().hasHeightForWidth())
        self.label_xp_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.label_xp_tab3)

        self.lineEdit_xp_tab3 = QLineEdit(self.tab3)
        self.lineEdit_xp_tab3.setObjectName(u"lineEdit_xp_tab3")
        sizePolicy1.setHeightForWidth(self.lineEdit_xp_tab3.sizePolicy().hasHeightForWidth())
        self.lineEdit_xp_tab3.setSizePolicy(sizePolicy1)
        self.lineEdit_xp_tab3.setFrame(False)

        self.horizontalLayout_15.addWidget(self.lineEdit_xp_tab3)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_yp_tab3 = QLabel(self.tab3)
        self.label_yp_tab3.setObjectName(u"label_yp_tab3")
        sizePolicy.setHeightForWidth(self.label_yp_tab3.sizePolicy().hasHeightForWidth())
        self.label_yp_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.label_yp_tab3)

        self.lineEdit_yp_tab3 = QLineEdit(self.tab3)
        self.lineEdit_yp_tab3.setObjectName(u"lineEdit_yp_tab3")
        sizePolicy1.setHeightForWidth(self.lineEdit_yp_tab3.sizePolicy().hasHeightForWidth())
        self.lineEdit_yp_tab3.setSizePolicy(sizePolicy1)
        self.lineEdit_yp_tab3.setFrame(False)

        self.horizontalLayout_16.addWidget(self.lineEdit_yp_tab3)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.label_zp_tab3 = QLabel(self.tab3)
        self.label_zp_tab3.setObjectName(u"label_zp_tab3")
        sizePolicy.setHeightForWidth(self.label_zp_tab3.sizePolicy().hasHeightForWidth())
        self.label_zp_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_17.addWidget(self.label_zp_tab3)

        self.combo_zp_tab3 = QComboBox(self.tab3)
        self.combo_zp_tab3.setObjectName(u"combo_zp_tab3")
        self.combo_zp_tab3.setEditable(True)

        self.horizontalLayout_17.addWidget(self.combo_zp_tab3)

        self.horizontalLayout_17.setStretch(0, 1)
        self.horizontalLayout_17.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_3d_tab3 = QLabel(self.tab3)
        self.label_3d_tab3.setObjectName(u"label_3d_tab3")
        sizePolicy.setHeightForWidth(self.label_3d_tab3.sizePolicy().hasHeightForWidth())
        self.label_3d_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.label_3d_tab3)

        self.lineEdit_3d_tab3 = QLineEdit(self.tab3)
        self.lineEdit_3d_tab3.setObjectName(u"lineEdit_3d_tab3")
        sizePolicy.setHeightForWidth(self.lineEdit_3d_tab3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3d_tab3.setSizePolicy(sizePolicy)
        self.lineEdit_3d_tab3.setFrame(False)
        self.lineEdit_3d_tab3.setReadOnly(False)

        self.horizontalLayout_18.addWidget(self.lineEdit_3d_tab3)

        self.label_2d_tab3 = QLabel(self.tab3)
        self.label_2d_tab3.setObjectName(u"label_2d_tab3")
        sizePolicy.setHeightForWidth(self.label_2d_tab3.sizePolicy().hasHeightForWidth())
        self.label_2d_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_18.addWidget(self.label_2d_tab3)

        self.lineEdit_2d_tab3 = QLineEdit(self.tab3)
        self.lineEdit_2d_tab3.setObjectName(u"lineEdit_2d_tab3")
        sizePolicy1.setHeightForWidth(self.lineEdit_2d_tab3.sizePolicy().hasHeightForWidth())
        self.lineEdit_2d_tab3.setSizePolicy(sizePolicy1)
        self.lineEdit_2d_tab3.setFrame(False)
        self.lineEdit_2d_tab3.setReadOnly(True)

        self.horizontalLayout_18.addWidget(self.lineEdit_2d_tab3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_18)

        self.line_6 = QFrame(self.tab3)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setStyleSheet(u"color: rgb(220,220,220)")
        self.line_6.setFrameShadow(QFrame.Plain)
        self.line_6.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_6)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.label_ef_tab3 = QLabel(self.tab3)
        self.label_ef_tab3.setObjectName(u"label_ef_tab3")
        sizePolicy.setHeightForWidth(self.label_ef_tab3.sizePolicy().hasHeightForWidth())
        self.label_ef_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_19.addWidget(self.label_ef_tab3)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.lineEdit_ef_tab3 = QLineEdit(self.tab3)
        self.lineEdit_ef_tab3.setObjectName(u"lineEdit_ef_tab3")
        sizePolicy1.setHeightForWidth(self.lineEdit_ef_tab3.sizePolicy().hasHeightForWidth())
        self.lineEdit_ef_tab3.setSizePolicy(sizePolicy1)
        self.lineEdit_ef_tab3.setFrame(False)

        self.horizontalLayout_20.addWidget(self.lineEdit_ef_tab3)

        self.toolButton_cf_tab2_2 = QToolButton(self.tab3)
        self.toolButton_cf_tab2_2.setObjectName(u"toolButton_cf_tab2_2")

        self.horizontalLayout_20.addWidget(self.toolButton_cf_tab2_2)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)

        self.horizontalLayout_19.setStretch(0, 1)
        self.horizontalLayout_19.setStretch(1, 3)

        self.verticalLayout_3.addLayout(self.horizontalLayout_19)

        self.line_7 = QFrame(self.tab3)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setStyleSheet(u"color: rgb(220,220,220)")
        self.line_7.setFrameShadow(QFrame.Plain)
        self.line_7.setFrameShape(QFrame.HLine)

        self.verticalLayout_3.addWidget(self.line_7)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_proceed_tab3 = QPushButton(self.tab3)
        self.pushButton_proceed_tab3.setObjectName(u"pushButton_proceed_tab3")
        self.pushButton_proceed_tab3.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_proceed_tab3.sizePolicy().hasHeightForWidth())
        self.pushButton_proceed_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_21.addWidget(self.pushButton_proceed_tab3)

        self.pushButton_clear_tab3 = QPushButton(self.tab3)
        self.pushButton_clear_tab3.setObjectName(u"pushButton_clear_tab3")
        sizePolicy.setHeightForWidth(self.pushButton_clear_tab3.sizePolicy().hasHeightForWidth())
        self.pushButton_clear_tab3.setSizePolicy(sizePolicy)

        self.horizontalLayout_21.addWidget(self.pushButton_clear_tab3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_21)

        self.tabWidget.addTab(self.tab3, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_xp_tab1.setText(QCoreApplication.translate("Form", u"X Points", None))
        self.lineEdit_xp_tab1.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_xp_tab1.setPlaceholderText(QCoreApplication.translate("Form", u"Example: (<start> <end> <interval>) use ',' as seperator", None))
        self.label_yp_tab1.setText(QCoreApplication.translate("Form", u"Y Points", None))
        self.lineEdit_yp_tab1.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_yp_tab1.setPlaceholderText(QCoreApplication.translate("Form", u"Example: (<start> <end> <interval>) use ',' as seperator", None))
        self.label_zp_tab1.setText(QCoreApplication.translate("Form", u"Z Points", None))
        self.combo_zp_tab1.setItemText(0, QCoreApplication.translate("Form", u"2000,0", None))

        self.label_3d_tab1.setText(QCoreApplication.translate("Form", u"Total Exps", None))
        self.lineEdit_3d_tab1.setPlaceholderText("")
        self.label_2d_tab1.setText(QCoreApplication.translate("Form", u"Total 2D points", None))
        self.lineEdit_2d_tab1.setPlaceholderText("")
        self.pushButton_OCR_tab1.setText(QCoreApplication.translate("Form", u"Select OCR Region", None))
        self.label_tt_tab1.setText(QCoreApplication.translate("Form", u"Trigger Tech(s)", None))
        self.lineEdit_tt_tab1.setText(QCoreApplication.translate("Form", u"2,4", None))
        self.lineEdit_tt_tab1.setPlaceholderText(QCoreApplication.translate("Form", u"Example: 1.CV,4.WAIT", None))
        self.pushButton_proceed_tab1.setText(QCoreApplication.translate("Form", u"Proceed", None))
        self.pushButton_clear_tab1.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab1), QCoreApplication.translate("Form", u"EC-Lab-OCR", None))
        self.label_xp_tab2.setText(QCoreApplication.translate("Form", u"X Points", None))
        self.lineEdit_xp_tab2.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_xp_tab2.setPlaceholderText(QCoreApplication.translate("Form", u"Example: (<start> <end> <interval>) use ',' as seperator", None))
        self.label_yp_tab2.setText(QCoreApplication.translate("Form", u"Y Points", None))
        self.lineEdit_yp_tab2.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_yp_tab2.setPlaceholderText(QCoreApplication.translate("Form", u"Example: (<start> <end> <interval>) use ',' as seperator", None))
        self.label_zp_tab2.setText(QCoreApplication.translate("Form", u"Z Points", None))
        self.label_3d_tab2.setText(QCoreApplication.translate("Form", u"Total Exps", None))
        self.lineEdit_3d_tab2.setPlaceholderText("")
        self.label_2d_tab2.setText(QCoreApplication.translate("Form", u"Total 2D points", None))
        self.lineEdit_2d_tab2.setPlaceholderText("")
        self.label_cf_tab2.setText(QCoreApplication.translate("Form", u"Count.txt Folder", None))
        self.lineEdit_cf_tab2.setText("")
        self.lineEdit_cf_tab2.setPlaceholderText("")
        self.toolButton_cf_tab2.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButton_proceed_tab2.setText(QCoreApplication.translate("Form", u"Proceed", None))
        self.pushButton_clear_tab2.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab2), QCoreApplication.translate("Form", u"EC-Lab-EXTAPP", None))
        self.label_xp_tab3.setText(QCoreApplication.translate("Form", u"X Points", None))
        self.lineEdit_xp_tab3.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_xp_tab3.setPlaceholderText(QCoreApplication.translate("Form", u"Example: (<start> <end> <interval>) use ',' as seperator", None))
        self.label_yp_tab3.setText(QCoreApplication.translate("Form", u"Y Points", None))
        self.lineEdit_yp_tab3.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_yp_tab3.setPlaceholderText(QCoreApplication.translate("Form", u"Example: (<start> <end> <interval>) use ',' as seperator", None))
        self.label_zp_tab3.setText(QCoreApplication.translate("Form", u"Z Points", None))
        self.label_3d_tab3.setText(QCoreApplication.translate("Form", u"Total Exps", None))
        self.lineEdit_3d_tab3.setPlaceholderText("")
        self.label_2d_tab3.setText(QCoreApplication.translate("Form", u"Total 2D points", None))
        self.lineEdit_2d_tab3.setPlaceholderText("")
        self.label_ef_tab3.setText(QCoreApplication.translate("Form", u"Experiment Folder", None))
        self.lineEdit_ef_tab3.setText("")
        self.lineEdit_ef_tab3.setPlaceholderText("")
        self.toolButton_cf_tab2_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.pushButton_proceed_tab3.setText(QCoreApplication.translate("Form", u"Proceed", None))
        self.pushButton_clear_tab3.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab3), QCoreApplication.translate("Form", u"NOVA2", None))
    # retranslateUi

