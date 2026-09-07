# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiAutoMove_Nova.ui'
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QToolButton, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(326, 127)
        Form.setLayoutDirection(Qt.LeftToRight)
        Form.setStyleSheet(u"")
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_MF = QLabel(Form)
        self.label_MF.setObjectName(u"label_MF")

        self.horizontalLayout_2.addWidget(self.label_MF)

        self.lineEdit_MF = QLineEdit(Form)
        self.lineEdit_MF.setObjectName(u"lineEdit_MF")

        self.horizontalLayout_2.addWidget(self.lineEdit_MF)

        self.toolButton_MF = QToolButton(Form)
        self.toolButton_MF.setObjectName(u"toolButton_MF")

        self.horizontalLayout_2.addWidget(self.toolButton_MF)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_SS = QLabel(Form)
        self.label_SS.setObjectName(u"label_SS")

        self.horizontalLayout_3.addWidget(self.label_SS)

        self.lineEdit_CC1 = QLineEdit(Form)
        self.lineEdit_CC1.setObjectName(u"lineEdit_CC1")

        self.horizontalLayout_3.addWidget(self.lineEdit_CC1)

        self.label_CC1 = QLabel(Form)
        self.label_CC1.setObjectName(u"label_CC1")

        self.horizontalLayout_3.addWidget(self.label_CC1)

        self.lineEdit_CC2 = QLineEdit(Form)
        self.lineEdit_CC2.setObjectName(u"lineEdit_CC2")

        self.horizontalLayout_3.addWidget(self.lineEdit_CC2)

        self.label_CC2 = QLabel(Form)
        self.label_CC2.setObjectName(u"label_CC2")

        self.horizontalLayout_3.addWidget(self.label_CC2)

        self.lineEdit_CC3 = QLineEdit(Form)
        self.lineEdit_CC3.setObjectName(u"lineEdit_CC3")

        self.horizontalLayout_3.addWidget(self.lineEdit_CC3)

        self.horizontalLayout_3.setStretch(0, 1)
        self.horizontalLayout_3.setStretch(1, 1)
        self.horizontalLayout_3.setStretch(2, 1)
        self.horizontalLayout_3.setStretch(3, 1)
        self.horizontalLayout_3.setStretch(4, 1)
        self.horizontalLayout_3.setStretch(5, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit_AB = QLineEdit(Form)
        self.lineEdit_AB.setObjectName(u"lineEdit_AB")

        self.horizontalLayout_4.addWidget(self.lineEdit_AB)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_4.addWidget(self.label_2)

        self.lineEdit_BCI = QLineEdit(Form)
        self.lineEdit_BCI.setObjectName(u"lineEdit_BCI")

        self.horizontalLayout_4.addWidget(self.lineEdit_BCI)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")

        self.horizontalLayout.addWidget(self.pushButton_start)

        self.pushButton_stop = QPushButton(Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")

        self.horizontalLayout.addWidget(self.pushButton_stop)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_MF.setText(QCoreApplication.translate("Form", u"Monitered File:", None))
        self.lineEdit_MF.setText("")
        self.toolButton_MF.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_SS.setText(QCoreApplication.translate("Form", u"Current Control", None))
        self.lineEdit_CC1.setText(QCoreApplication.translate("Form", u"1.02", None))
        self.label_CC1.setText(QCoreApplication.translate("Form", u"->", None))
        self.lineEdit_CC2.setText(QCoreApplication.translate("Form", u"1.05", None))
        self.label_CC2.setText(QCoreApplication.translate("Form", u"->", None))
        self.lineEdit_CC3.setText(QCoreApplication.translate("Form", u"1.1", None))
        self.label.setText(QCoreApplication.translate("Form", u"Average Boundary", None))
        self.lineEdit_AB.setText(QCoreApplication.translate("Form", u"0.38", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Bulk Current Index", None))
        self.lineEdit_BCI.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"Start", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"Stop", None))
    # retranslateUi

