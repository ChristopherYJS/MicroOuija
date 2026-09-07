# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiMapping.ui'
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
        Form.resize(688, 372)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_eclab1 = QWidget()
        self.tab_eclab1.setObjectName(u"tab_eclab1")
        self.verticalLayout_2 = QVBoxLayout(self.tab_eclab1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.label_xp_tab1_5 = QLabel(self.tab_eclab1)
        self.label_xp_tab1_5.setObjectName(u"label_xp_tab1_5")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_xp_tab1_5.sizePolicy().hasHeightForWidth())
        self.label_xp_tab1_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_42.addWidget(self.label_xp_tab1_5)

        self.lineEdit_xp_tab1_5 = QLineEdit(self.tab_eclab1)
        self.lineEdit_xp_tab1_5.setObjectName(u"lineEdit_xp_tab1_5")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_xp_tab1_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_xp_tab1_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_42.addWidget(self.lineEdit_xp_tab1_5)

        self.horizontalLayout_42.setStretch(0, 1)
        self.horizontalLayout_42.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_42)

        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_yp_tab1_5 = QLabel(self.tab_eclab1)
        self.label_yp_tab1_5.setObjectName(u"label_yp_tab1_5")
        sizePolicy.setHeightForWidth(self.label_yp_tab1_5.sizePolicy().hasHeightForWidth())
        self.label_yp_tab1_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_46.addWidget(self.label_yp_tab1_5)

        self.lineEdit_yp_tab1_5 = QLineEdit(self.tab_eclab1)
        self.lineEdit_yp_tab1_5.setObjectName(u"lineEdit_yp_tab1_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_yp_tab1_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_yp_tab1_5.setSizePolicy(sizePolicy1)

        self.horizontalLayout_46.addWidget(self.lineEdit_yp_tab1_5)

        self.horizontalLayout_46.setStretch(0, 1)
        self.horizontalLayout_46.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.label_zp_tab1_5 = QLabel(self.tab_eclab1)
        self.label_zp_tab1_5.setObjectName(u"label_zp_tab1_5")
        sizePolicy.setHeightForWidth(self.label_zp_tab1_5.sizePolicy().hasHeightForWidth())
        self.label_zp_tab1_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_44.addWidget(self.label_zp_tab1_5)

        self.combo_zp_tab1_5 = QComboBox(self.tab_eclab1)
        self.combo_zp_tab1_5.setObjectName(u"combo_zp_tab1_5")
        self.combo_zp_tab1_5.setEditable(True)

        self.horizontalLayout_44.addWidget(self.combo_zp_tab1_5)

        self.horizontalLayout_44.setStretch(0, 1)
        self.horizontalLayout_44.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_44)

        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.label_3d_tab1_5 = QLabel(self.tab_eclab1)
        self.label_3d_tab1_5.setObjectName(u"label_3d_tab1_5")
        sizePolicy.setHeightForWidth(self.label_3d_tab1_5.sizePolicy().hasHeightForWidth())
        self.label_3d_tab1_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_43.addWidget(self.label_3d_tab1_5)

        self.lineEdit_3d_tab1_5 = QLineEdit(self.tab_eclab1)
        self.lineEdit_3d_tab1_5.setObjectName(u"lineEdit_3d_tab1_5")
        sizePolicy.setHeightForWidth(self.lineEdit_3d_tab1_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_3d_tab1_5.setSizePolicy(sizePolicy)
        self.lineEdit_3d_tab1_5.setReadOnly(False)

        self.horizontalLayout_43.addWidget(self.lineEdit_3d_tab1_5)

        self.label_2d_tab1_5 = QLabel(self.tab_eclab1)
        self.label_2d_tab1_5.setObjectName(u"label_2d_tab1_5")
        sizePolicy.setHeightForWidth(self.label_2d_tab1_5.sizePolicy().hasHeightForWidth())
        self.label_2d_tab1_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_43.addWidget(self.label_2d_tab1_5)

        self.lineEdit_2d_tab1_5 = QLineEdit(self.tab_eclab1)
        self.lineEdit_2d_tab1_5.setObjectName(u"lineEdit_2d_tab1_5")
        sizePolicy1.setHeightForWidth(self.lineEdit_2d_tab1_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_2d_tab1_5.setSizePolicy(sizePolicy1)
        self.lineEdit_2d_tab1_5.setReadOnly(True)

        self.horizontalLayout_43.addWidget(self.lineEdit_2d_tab1_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_43)

        self.line_1 = QFrame(self.tab_eclab1)
        self.line_1.setObjectName(u"line_1")
        self.line_1.setFrameShape(QFrame.HLine)
        self.line_1.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_1)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_TriggerTech_tab1 = QLabel(self.tab_eclab1)
        self.label_TriggerTech_tab1.setObjectName(u"label_TriggerTech_tab1")

        self.horizontalLayout_47.addWidget(self.label_TriggerTech_tab1)

        self.lineEdit_TriggerTech_tab1 = QLineEdit(self.tab_eclab1)
        self.lineEdit_TriggerTech_tab1.setObjectName(u"lineEdit_TriggerTech_tab1")

        self.horizontalLayout_47.addWidget(self.lineEdit_TriggerTech_tab1)

        self.horizontalLayout_47.setStretch(0, 1)
        self.horizontalLayout_47.setStretch(1, 3)

        self.verticalLayout_2.addLayout(self.horizontalLayout_47)

        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.pushButton_Select_5 = QPushButton(self.tab_eclab1)
        self.pushButton_Select_5.setObjectName(u"pushButton_Select_5")
        self.pushButton_Select_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_Select_5.sizePolicy().hasHeightForWidth())
        self.pushButton_Select_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_48.addWidget(self.pushButton_Select_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_48)

        self.line_2 = QFrame(self.tab_eclab1)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_2.addWidget(self.line_2)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.pushButton_Proceed_tab1_5 = QPushButton(self.tab_eclab1)
        self.pushButton_Proceed_tab1_5.setObjectName(u"pushButton_Proceed_tab1_5")
        self.pushButton_Proceed_tab1_5.setEnabled(True)
        sizePolicy.setHeightForWidth(self.pushButton_Proceed_tab1_5.sizePolicy().hasHeightForWidth())
        self.pushButton_Proceed_tab1_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_45.addWidget(self.pushButton_Proceed_tab1_5)

        self.pushButton_Clear_tab1_5 = QPushButton(self.tab_eclab1)
        self.pushButton_Clear_tab1_5.setObjectName(u"pushButton_Clear_tab1_5")
        sizePolicy.setHeightForWidth(self.pushButton_Clear_tab1_5.sizePolicy().hasHeightForWidth())
        self.pushButton_Clear_tab1_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_45.addWidget(self.pushButton_Clear_tab1_5)


        self.verticalLayout_2.addLayout(self.horizontalLayout_45)

        self.tabWidget.addTab(self.tab_eclab1, "")
        self.tab_eclab1_2 = QWidget()
        self.tab_eclab1_2.setObjectName(u"tab_eclab1_2")
        self.verticalLayout_4 = QVBoxLayout(self.tab_eclab1_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_xp_2 = QLabel(self.tab_eclab1_2)
        self.label_xp_2.setObjectName(u"label_xp_2")
        sizePolicy.setHeightForWidth(self.label_xp_2.sizePolicy().hasHeightForWidth())
        self.label_xp_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_5.addWidget(self.label_xp_2)

        self.lineEdit_xp_2 = QLineEdit(self.tab_eclab1_2)
        self.lineEdit_xp_2.setObjectName(u"lineEdit_xp_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_xp_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_xp_2.setSizePolicy(sizePolicy1)

        self.horizontalLayout_5.addWidget(self.lineEdit_xp_2)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_zp_4 = QLabel(self.tab_eclab1_2)
        self.label_zp_4.setObjectName(u"label_zp_4")
        sizePolicy.setHeightForWidth(self.label_zp_4.sizePolicy().hasHeightForWidth())
        self.label_zp_4.setSizePolicy(sizePolicy)

        self.horizontalLayout_6.addWidget(self.label_zp_4)

        self.lineEdit = QLineEdit(self.tab_eclab1_2)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_6.addWidget(self.lineEdit)

        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_zp_5 = QLabel(self.tab_eclab1_2)
        self.label_zp_5.setObjectName(u"label_zp_5")
        sizePolicy.setHeightForWidth(self.label_zp_5.sizePolicy().hasHeightForWidth())
        self.label_zp_5.setSizePolicy(sizePolicy)

        self.horizontalLayout_10.addWidget(self.label_zp_5)

        self.combo_zp_3 = QComboBox(self.tab_eclab1_2)
        self.combo_zp_3.setObjectName(u"combo_zp_3")
        self.combo_zp_3.setEditable(True)

        self.horizontalLayout_10.addWidget(self.combo_zp_3)

        self.horizontalLayout_10.setStretch(0, 1)
        self.horizontalLayout_10.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_zp_6 = QLabel(self.tab_eclab1_2)
        self.label_zp_6.setObjectName(u"label_zp_6")
        sizePolicy.setHeightForWidth(self.label_zp_6.sizePolicy().hasHeightForWidth())
        self.label_zp_6.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_zp_6)

        self.lineEdit_total_exp_2 = QLineEdit(self.tab_eclab1_2)
        self.lineEdit_total_exp_2.setObjectName(u"lineEdit_total_exp_2")
        sizePolicy.setHeightForWidth(self.lineEdit_total_exp_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_total_exp_2.setSizePolicy(sizePolicy)
        self.lineEdit_total_exp_2.setReadOnly(False)

        self.horizontalLayout_11.addWidget(self.lineEdit_total_exp_2)

        self.label_zp_7 = QLabel(self.tab_eclab1_2)
        self.label_zp_7.setObjectName(u"label_zp_7")
        sizePolicy.setHeightForWidth(self.label_zp_7.sizePolicy().hasHeightForWidth())
        self.label_zp_7.setSizePolicy(sizePolicy)

        self.horizontalLayout_11.addWidget(self.label_zp_7)

        self.lineEdit_total_2d_2 = QLineEdit(self.tab_eclab1_2)
        self.lineEdit_total_2d_2.setObjectName(u"lineEdit_total_2d_2")
        sizePolicy1.setHeightForWidth(self.lineEdit_total_2d_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_total_2d_2.setSizePolicy(sizePolicy1)
        self.lineEdit_total_2d_2.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.lineEdit_total_2d_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.line_3 = QFrame(self.tab_eclab1_2)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_3)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_4 = QLabel(self.tab_eclab1_2)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_12.addWidget(self.label_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit_stbr_2 = QLineEdit(self.tab_eclab1_2)
        self.lineEdit_stbr_2.setObjectName(u"lineEdit_stbr_2")

        self.horizontalLayout.addWidget(self.lineEdit_stbr_2)

        self.toolButton = QToolButton(self.tab_eclab1_2)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.horizontalLayout_12.addLayout(self.horizontalLayout)

        self.horizontalLayout_12.setStretch(0, 1)
        self.horizontalLayout_12.setStretch(1, 3)

        self.verticalLayout_4.addLayout(self.horizontalLayout_12)

        self.line_8 = QFrame(self.tab_eclab1_2)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.HLine)
        self.line_8.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_4.addWidget(self.line_8)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.proceed = QPushButton(self.tab_eclab1_2)
        self.proceed.setObjectName(u"proceed")
        self.proceed.setEnabled(True)
        sizePolicy.setHeightForWidth(self.proceed.sizePolicy().hasHeightForWidth())
        self.proceed.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.proceed)

        self.clear = QPushButton(self.tab_eclab1_2)
        self.clear.setObjectName(u"clear")
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)

        self.horizontalLayout_13.addWidget(self.clear)


        self.verticalLayout_4.addLayout(self.horizontalLayout_13)

        self.tabWidget.addTab(self.tab_eclab1_2, "")
        self.tab_nova = QWidget()
        self.tab_nova.setObjectName(u"tab_nova")
        self.verticalLayout_5 = QVBoxLayout(self.tab_nova)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.label_xp_3 = QLabel(self.tab_nova)
        self.label_xp_3.setObjectName(u"label_xp_3")
        sizePolicy.setHeightForWidth(self.label_xp_3.sizePolicy().hasHeightForWidth())
        self.label_xp_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_16.addWidget(self.label_xp_3)

        self.lineEdit_xp_3 = QLineEdit(self.tab_nova)
        self.lineEdit_xp_3.setObjectName(u"lineEdit_xp_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_xp_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_xp_3.setSizePolicy(sizePolicy1)

        self.horizontalLayout_16.addWidget(self.lineEdit_xp_3)

        self.horizontalLayout_16.setStretch(0, 1)
        self.horizontalLayout_16.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_zp_8 = QLabel(self.tab_nova)
        self.label_zp_8.setObjectName(u"label_zp_8")
        sizePolicy.setHeightForWidth(self.label_zp_8.sizePolicy().hasHeightForWidth())
        self.label_zp_8.setSizePolicy(sizePolicy)

        self.horizontalLayout_14.addWidget(self.label_zp_8)

        self.lineEdit_2 = QLineEdit(self.tab_nova)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.horizontalLayout_14.addWidget(self.lineEdit_2)

        self.horizontalLayout_14.setStretch(0, 1)
        self.horizontalLayout_14.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_zp_9 = QLabel(self.tab_nova)
        self.label_zp_9.setObjectName(u"label_zp_9")
        sizePolicy.setHeightForWidth(self.label_zp_9.sizePolicy().hasHeightForWidth())
        self.label_zp_9.setSizePolicy(sizePolicy)

        self.horizontalLayout_15.addWidget(self.label_zp_9)

        self.combo_zp_4 = QComboBox(self.tab_nova)
        self.combo_zp_4.setObjectName(u"combo_zp_4")
        self.combo_zp_4.setEditable(True)

        self.horizontalLayout_15.addWidget(self.combo_zp_4)

        self.horizontalLayout_15.setStretch(0, 1)
        self.horizontalLayout_15.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_15)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.label_zp_10 = QLabel(self.tab_nova)
        self.label_zp_10.setObjectName(u"label_zp_10")
        sizePolicy.setHeightForWidth(self.label_zp_10.sizePolicy().hasHeightForWidth())
        self.label_zp_10.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.label_zp_10)

        self.lineEdit_total_exp_3 = QLineEdit(self.tab_nova)
        self.lineEdit_total_exp_3.setObjectName(u"lineEdit_total_exp_3")
        sizePolicy.setHeightForWidth(self.lineEdit_total_exp_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_total_exp_3.setSizePolicy(sizePolicy)
        self.lineEdit_total_exp_3.setReadOnly(False)

        self.horizontalLayout_20.addWidget(self.lineEdit_total_exp_3)

        self.label_zp_11 = QLabel(self.tab_nova)
        self.label_zp_11.setObjectName(u"label_zp_11")
        sizePolicy.setHeightForWidth(self.label_zp_11.sizePolicy().hasHeightForWidth())
        self.label_zp_11.setSizePolicy(sizePolicy)

        self.horizontalLayout_20.addWidget(self.label_zp_11)

        self.lineEdit_total_2d_3 = QLineEdit(self.tab_nova)
        self.lineEdit_total_2d_3.setObjectName(u"lineEdit_total_2d_3")
        sizePolicy1.setHeightForWidth(self.lineEdit_total_2d_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_total_2d_3.setSizePolicy(sizePolicy1)
        self.lineEdit_total_2d_3.setReadOnly(True)

        self.horizontalLayout_20.addWidget(self.lineEdit_total_2d_3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_20)

        self.line = QFrame(self.tab_nova)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.label_5 = QLabel(self.tab_nova)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout_18.addWidget(self.label_5)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lineEdit_stbr_3 = QLineEdit(self.tab_nova)
        self.lineEdit_stbr_3.setObjectName(u"lineEdit_stbr_3")

        self.horizontalLayout_19.addWidget(self.lineEdit_stbr_3)

        self.toolButton_2 = QToolButton(self.tab_nova)
        self.toolButton_2.setObjectName(u"toolButton_2")

        self.horizontalLayout_19.addWidget(self.toolButton_2)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)

        self.horizontalLayout_18.setStretch(0, 1)
        self.horizontalLayout_18.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_18)

        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.label_9 = QLabel(self.tab_nova)
        self.label_9.setObjectName(u"label_9")

        self.horizontalLayout_49.addWidget(self.label_9)

        self.lineEdit_3 = QLineEdit(self.tab_nova)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.horizontalLayout_49.addWidget(self.lineEdit_3)

        self.horizontalLayout_49.setStretch(0, 1)
        self.horizontalLayout_49.setStretch(1, 3)

        self.verticalLayout_5.addLayout(self.horizontalLayout_49)

        self.line_14 = QFrame(self.tab_nova)
        self.line_14.setObjectName(u"line_14")
        self.line_14.setFrameShape(QFrame.HLine)
        self.line_14.setFrameShadow(QFrame.Sunken)

        self.verticalLayout_5.addWidget(self.line_14)

        self.horizontalLayout_94 = QHBoxLayout()
        self.horizontalLayout_94.setObjectName(u"horizontalLayout_94")
        self.proceed_2 = QPushButton(self.tab_nova)
        self.proceed_2.setObjectName(u"proceed_2")
        self.proceed_2.setEnabled(True)
        sizePolicy.setHeightForWidth(self.proceed_2.sizePolicy().hasHeightForWidth())
        self.proceed_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_94.addWidget(self.proceed_2)

        self.clear_2 = QPushButton(self.tab_nova)
        self.clear_2.setObjectName(u"clear_2")
        sizePolicy.setHeightForWidth(self.clear_2.sizePolicy().hasHeightForWidth())
        self.clear_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_94.addWidget(self.clear_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_94)

        self.tabWidget.addTab(self.tab_nova, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_xp_tab1_5.setText(QCoreApplication.translate("Form", u"X Points", None))
        self.lineEdit_xp_tab1_5.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_xp_tab1_5.setPlaceholderText(QCoreApplication.translate("Form", u"(<start> <end> <interval>) or use ',' as seperator", None))
        self.label_yp_tab1_5.setText(QCoreApplication.translate("Form", u"Y Points", None))
        self.lineEdit_yp_tab1_5.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_yp_tab1_5.setPlaceholderText(QCoreApplication.translate("Form", u"(<start> <end> <interval>) or use ',' as seperator", None))
        self.label_zp_tab1_5.setText(QCoreApplication.translate("Form", u"Z Points", None))
        self.label_3d_tab1_5.setText(QCoreApplication.translate("Form", u"Total Exps", None))
        self.lineEdit_3d_tab1_5.setPlaceholderText("")
        self.label_2d_tab1_5.setText(QCoreApplication.translate("Form", u"Total 2D Points", None))
        self.lineEdit_2d_tab1_5.setPlaceholderText("")
        self.label_TriggerTech_tab1.setText(QCoreApplication.translate("Form", u"Trigger Tech", None))
        self.lineEdit_TriggerTech_tab1.setPlaceholderText(QCoreApplication.translate("Form", u"Example: 1.CV,4.WAIT", None))
        self.pushButton_Select_5.setText(QCoreApplication.translate("Form", u"Select OCR Region", None))
        self.pushButton_Proceed_tab1_5.setText(QCoreApplication.translate("Form", u"Proceed", None))
        self.pushButton_Clear_tab1_5.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_eclab1), QCoreApplication.translate("Form", u"EC-Lab-OCR", None))
        self.label_xp_2.setText(QCoreApplication.translate("Form", u"X Points", None))
        self.lineEdit_xp_2.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_xp_2.setPlaceholderText(QCoreApplication.translate("Form", u"(<start> <end> <interval>) or use ',' as seperator", None))
        self.label_zp_4.setText(QCoreApplication.translate("Form", u"Y Points", None))
        self.label_zp_5.setText(QCoreApplication.translate("Form", u"Z Points", None))
        self.label_zp_6.setText(QCoreApplication.translate("Form", u"Total Exps", None))
        self.lineEdit_total_exp_2.setPlaceholderText("")
        self.label_zp_7.setText(QCoreApplication.translate("Form", u"Total 2D Points", None))
        self.lineEdit_total_2d_2.setPlaceholderText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"Count.txt Folder", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.proceed.setText(QCoreApplication.translate("Form", u"Proceed", None))
        self.clear.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_eclab1_2), QCoreApplication.translate("Form", u"EC-Lab-EXTAPP", None))
        self.label_xp_3.setText(QCoreApplication.translate("Form", u"X Points", None))
        self.lineEdit_xp_3.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_xp_3.setPlaceholderText(QCoreApplication.translate("Form", u"(<start> <end> <interval>) or use ',' as seperator", None))
        self.label_zp_8.setText(QCoreApplication.translate("Form", u"Y Points", None))
        self.label_zp_9.setText(QCoreApplication.translate("Form", u"Z Points", None))
        self.label_zp_10.setText(QCoreApplication.translate("Form", u"Total Exps", None))
        self.lineEdit_total_exp_3.setPlaceholderText("")
        self.label_zp_11.setText(QCoreApplication.translate("Form", u"Total 2D Points", None))
        self.lineEdit_total_2d_3.setPlaceholderText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"Experiment Folder", None))
        self.toolButton_2.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Rename Pattern", None))
        self.proceed_2.setText(QCoreApplication.translate("Form", u"Proceed", None))
        self.clear_2.setText(QCoreApplication.translate("Form", u"Clear", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_nova), QCoreApplication.translate("Form", u"Nova2", None))
    # retranslateUi

