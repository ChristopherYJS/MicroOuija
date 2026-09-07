# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'PI_GUI_App_Map.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QToolButton, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(621, 297)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_1 = QHBoxLayout()
        self.horizontalLayout_1.setObjectName(u"horizontalLayout_1")
        self.label_xp = QLabel(Form)
        self.label_xp.setObjectName(u"label_xp")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_xp.sizePolicy().hasHeightForWidth())
        self.label_xp.setSizePolicy(sizePolicy)

        self.horizontalLayout_1.addWidget(self.label_xp)

        self.lineEdit_xp = QLineEdit(Form)
        self.lineEdit_xp.setObjectName(u"lineEdit_xp")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Maximum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.lineEdit_xp.sizePolicy().hasHeightForWidth())
        self.lineEdit_xp.setSizePolicy(sizePolicy1)

        self.horizontalLayout_1.addWidget(self.lineEdit_xp)

        self.horizontalLayout_1.setStretch(0, 1)
        self.horizontalLayout_1.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_yp = QLabel(Form)
        self.label_yp.setObjectName(u"label_yp")
        sizePolicy.setHeightForWidth(self.label_yp.sizePolicy().hasHeightForWidth())
        self.label_yp.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.label_yp)

        self.lineEdit_yp = QLineEdit(Form)
        self.lineEdit_yp.setObjectName(u"lineEdit_yp")
        sizePolicy1.setHeightForWidth(self.lineEdit_yp.sizePolicy().hasHeightForWidth())
        self.lineEdit_yp.setSizePolicy(sizePolicy1)

        self.horizontalLayout_2.addWidget(self.lineEdit_yp)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_zp = QLabel(Form)
        self.label_zp.setObjectName(u"label_zp")
        sizePolicy.setHeightForWidth(self.label_zp.sizePolicy().hasHeightForWidth())
        self.label_zp.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.label_zp)

        self.combo_zp = QComboBox(Form)
        self.combo_zp.setObjectName(u"combo_zp")
        self.combo_zp.setEditable(True)

        self.horizontalLayout_3.addWidget(self.combo_zp)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_zp_3 = QLabel(Form)
        self.label_zp_3.setObjectName(u"label_zp_3")
        sizePolicy.setHeightForWidth(self.label_zp_3.sizePolicy().hasHeightForWidth())
        self.label_zp_3.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_zp_3)

        self.lineEdit_total_exp = QLineEdit(Form)
        self.lineEdit_total_exp.setObjectName(u"lineEdit_total_exp")
        sizePolicy.setHeightForWidth(self.lineEdit_total_exp.sizePolicy().hasHeightForWidth())
        self.lineEdit_total_exp.setSizePolicy(sizePolicy)
        self.lineEdit_total_exp.setReadOnly(False)

        self.horizontalLayout_4.addWidget(self.lineEdit_total_exp)

        self.label_zp_2 = QLabel(Form)
        self.label_zp_2.setObjectName(u"label_zp_2")
        sizePolicy.setHeightForWidth(self.label_zp_2.sizePolicy().hasHeightForWidth())
        self.label_zp_2.setSizePolicy(sizePolicy)

        self.horizontalLayout_4.addWidget(self.label_zp_2)

        self.lineEdit_total_2d = QLineEdit(Form)
        self.lineEdit_total_2d.setObjectName(u"lineEdit_total_2d")
        sizePolicy1.setHeightForWidth(self.lineEdit_total_2d.sizePolicy().hasHeightForWidth())
        self.lineEdit_total_2d.setSizePolicy(sizePolicy1)
        self.lineEdit_total_2d.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.lineEdit_total_2d)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.lineEdit_monitee = QLineEdit(Form)
        self.lineEdit_monitee.setObjectName(u"lineEdit_monitee")

        self.horizontalLayout_5.addWidget(self.lineEdit_monitee)

        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout_5.addWidget(self.toolButton)

        self.horizontalLayout_5.setStretch(0, 1)
        self.horizontalLayout_5.setStretch(1, 3)
        self.horizontalLayout_5.setStretch(2, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.line = QFrame(Form)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setChecked(True)

        self.horizontalLayout_6.addWidget(self.checkBox)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_7.addWidget(self.label_3)

        self.lineEdit_stbr = QLineEdit(Form)
        self.lineEdit_stbr.setObjectName(u"lineEdit_stbr")

        self.horizontalLayout_7.addWidget(self.lineEdit_stbr)

        self.horizontalLayout_7.setStretch(0, 1)
        self.horizontalLayout_7.setStretch(1, 3)

        self.verticalLayout.addLayout(self.horizontalLayout_7)

        self.line_2 = QFrame(Form)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.proceed = QPushButton(Form)
        self.proceed.setObjectName(u"proceed")
        self.proceed.setEnabled(True)
        sizePolicy.setHeightForWidth(self.proceed.sizePolicy().hasHeightForWidth())
        self.proceed.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.proceed)

        self.clear = QPushButton(Form)
        self.clear.setObjectName(u"clear")
        sizePolicy.setHeightForWidth(self.clear.sizePolicy().hasHeightForWidth())
        self.clear.setSizePolicy(sizePolicy)

        self.horizontalLayout_8.addWidget(self.clear)


        self.verticalLayout.addLayout(self.horizontalLayout_8)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_xp.setText(QCoreApplication.translate("Form", u"X points", None))
        self.lineEdit_xp.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_xp.setPlaceholderText(QCoreApplication.translate("Form", u"(<start> <end> <interval>) or use ',' as seperator", None))
        self.label_yp.setText(QCoreApplication.translate("Form", u"Y points", None))
        self.lineEdit_yp.setText(QCoreApplication.translate("Form", u"0", None))
        self.lineEdit_yp.setPlaceholderText(QCoreApplication.translate("Form", u"(<start> <end> <interval>) or use ',' as seperator", None))
        self.label_zp.setText(QCoreApplication.translate("Form", u"Z points", None))
        self.label_zp_3.setText(QCoreApplication.translate("Form", u"Total exps", None))
        self.lineEdit_total_exp.setPlaceholderText("")
        self.label_zp_2.setText(QCoreApplication.translate("Form", u"Total 2D points", None))
        self.lineEdit_total_2d.setPlaceholderText("")
        self.label.setText(QCoreApplication.translate("Form", u"Monitee Folder", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\">Rename Session</p></body></html>", None))
        self.checkBox.setText("")
        self.label_3.setText(QCoreApplication.translate("Form", u"String to be replaced", None))
        self.proceed.setText(QCoreApplication.translate("Form", u"Proceed", None))
        self.clear.setText(QCoreApplication.translate("Form", u"Clear", None))
    # retranslateUi

