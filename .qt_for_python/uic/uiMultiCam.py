# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiMultiCam.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(766, 466)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lineEdit_filename = QLineEdit(Form)
        self.lineEdit_filename.setObjectName(u"lineEdit_filename")

        self.verticalLayout.addWidget(self.lineEdit_filename)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_canvas1 = QLabel(Form)
        self.label_canvas1.setObjectName(u"label_canvas1")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_canvas1.sizePolicy().hasHeightForWidth())
        self.label_canvas1.setSizePolicy(sizePolicy)
        self.label_canvas1.setStyleSheet(u"")
        self.label_canvas1.setFrameShape(QFrame.Box)

        self.horizontalLayout_2.addWidget(self.label_canvas1)

        self.label_canvas2 = QLabel(Form)
        self.label_canvas2.setObjectName(u"label_canvas2")
        self.label_canvas2.setStyleSheet(u"")
        self.label_canvas2.setFrameShape(QFrame.Box)

        self.horizontalLayout_2.addWidget(self.label_canvas2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.pushButton_reall = QPushButton(Form)
        self.pushButton_reall.setObjectName(u"pushButton_reall")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton_reall.sizePolicy().hasHeightForWidth())
        self.pushButton_reall.setSizePolicy(sizePolicy1)
        self.pushButton_reall.setStyleSheet(u"")
        self.pushButton_reall.setCheckable(True)

        self.gridLayout_4.addWidget(self.pushButton_reall, 3, 0, 1, 4)

        self.pushButton_cam1re = QPushButton(Form)
        self.pushButton_cam1re.setObjectName(u"pushButton_cam1re")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.pushButton_cam1re.sizePolicy().hasHeightForWidth())
        self.pushButton_cam1re.setSizePolicy(sizePolicy2)
        self.pushButton_cam1re.setStyleSheet(u"")
        self.pushButton_cam1re.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam1re, 2, 0, 1, 1)

        self.pushButton_cam2 = QPushButton(Form)
        self.pushButton_cam2.setObjectName(u"pushButton_cam2")
        sizePolicy2.setHeightForWidth(self.pushButton_cam2.sizePolicy().hasHeightForWidth())
        self.pushButton_cam2.setSizePolicy(sizePolicy2)
        self.pushButton_cam2.setStyleSheet(u"")
        self.pushButton_cam2.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam2, 1, 2, 1, 2)

        self.pushButton_cam1 = QPushButton(Form)
        self.pushButton_cam1.setObjectName(u"pushButton_cam1")
        self.pushButton_cam1.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.pushButton_cam1.sizePolicy().hasHeightForWidth())
        self.pushButton_cam1.setSizePolicy(sizePolicy2)
        font = QFont()
        font.setPointSize(12)
        font.setItalic(False)
        self.pushButton_cam1.setFont(font)
        self.pushButton_cam1.setStyleSheet(u"")
        self.pushButton_cam1.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam1, 1, 0, 1, 2)

        self.pushButton_cam1cap = QPushButton(Form)
        self.pushButton_cam1cap.setObjectName(u"pushButton_cam1cap")
        sizePolicy2.setHeightForWidth(self.pushButton_cam1cap.sizePolicy().hasHeightForWidth())
        self.pushButton_cam1cap.setSizePolicy(sizePolicy2)
        self.pushButton_cam1cap.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.pushButton_cam1cap, 2, 1, 1, 1)

        self.pushButton_cam2cap = QPushButton(Form)
        self.pushButton_cam2cap.setObjectName(u"pushButton_cam2cap")
        sizePolicy2.setHeightForWidth(self.pushButton_cam2cap.sizePolicy().hasHeightForWidth())
        self.pushButton_cam2cap.setSizePolicy(sizePolicy2)
        self.pushButton_cam2cap.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.pushButton_cam2cap, 2, 3, 1, 1)

        self.pushButton_cam2re = QPushButton(Form)
        self.pushButton_cam2re.setObjectName(u"pushButton_cam2re")
        sizePolicy2.setHeightForWidth(self.pushButton_cam2re.sizePolicy().hasHeightForWidth())
        self.pushButton_cam2re.setSizePolicy(sizePolicy2)
        self.pushButton_cam2re.setStyleSheet(u"")
        self.pushButton_cam2re.setCheckable(False)

        self.gridLayout_4.addWidget(self.pushButton_cam2re, 2, 2, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout_4)

        self.verticalLayout.setStretch(1, 1)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_canvas1.setText("")
        self.label_canvas2.setText("")
        self.pushButton_reall.setText(QCoreApplication.translate("Form", u"Record All", None))
        self.pushButton_cam1re.setText(QCoreApplication.translate("Form", u"Record", None))
        self.pushButton_cam2.setText(QCoreApplication.translate("Form", u"Camera 2", None))
        self.pushButton_cam1.setText(QCoreApplication.translate("Form", u"Camera 1 ", None))
        self.pushButton_cam1cap.setText(QCoreApplication.translate("Form", u"Capture", None))
        self.pushButton_cam2cap.setText(QCoreApplication.translate("Form", u"Capture", None))
        self.pushButton_cam2re.setText(QCoreApplication.translate("Form", u"Record", None))
    # retranslateUi

