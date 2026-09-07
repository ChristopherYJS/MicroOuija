# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'uiPathInput.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
        Form.resize(400, 187)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_FM = QLabel(Form)
        self.label_FM.setObjectName(u"label_FM")

        self.horizontalLayout.addWidget(self.label_FM)

        self.lineEdit_FM = QLineEdit(Form)
        self.lineEdit_FM.setObjectName(u"lineEdit_FM")

        self.horizontalLayout.addWidget(self.lineEdit_FM)

        self.toolButton = QToolButton(Form)
        self.toolButton.setObjectName(u"toolButton")

        self.horizontalLayout.addWidget(self.toolButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_BA = QLabel(Form)
        self.label_BA.setObjectName(u"label_BA")

        self.horizontalLayout_3.addWidget(self.label_BA)

        self.lineEdit_BA = QLineEdit(Form)
        self.lineEdit_BA.setObjectName(u"lineEdit_BA")

        self.horizontalLayout_3.addWidget(self.lineEdit_BA)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_DS = QLabel(Form)
        self.label_DS.setObjectName(u"label_DS")

        self.horizontalLayout_2.addWidget(self.label_DS)

        self.lineEdit_DS = QLineEdit(Form)
        self.lineEdit_DS.setObjectName(u"lineEdit_DS")

        self.horizontalLayout_2.addWidget(self.lineEdit_DS)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_M1 = QPushButton(Form)
        self.pushButton_M1.setObjectName(u"pushButton_M1")

        self.horizontalLayout_4.addWidget(self.pushButton_M1)

        self.pushButton_M2 = QPushButton(Form)
        self.pushButton_M2.setObjectName(u"pushButton_M2")

        self.horizontalLayout_4.addWidget(self.pushButton_M2)

        self.pushButton_M3 = QPushButton(Form)
        self.pushButton_M3.setObjectName(u"pushButton_M3")

        self.horizontalLayout_4.addWidget(self.pushButton_M3)

        self.pushButton_M4 = QPushButton(Form)
        self.pushButton_M4.setObjectName(u"pushButton_M4")

        self.horizontalLayout_4.addWidget(self.pushButton_M4)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.pushButton_M5 = QPushButton(Form)
        self.pushButton_M5.setObjectName(u"pushButton_M5")

        self.horizontalLayout_5.addWidget(self.pushButton_M5)

        self.pushButton_M6 = QPushButton(Form)
        self.pushButton_M6.setObjectName(u"pushButton_M6")

        self.horizontalLayout_5.addWidget(self.pushButton_M6)

        self.pushButton_M7 = QPushButton(Form)
        self.pushButton_M7.setObjectName(u"pushButton_M7")

        self.horizontalLayout_5.addWidget(self.pushButton_M7)

        self.pushButton_M8 = QPushButton(Form)
        self.pushButton_M8.setObjectName(u"pushButton_M8")

        self.horizontalLayout_5.addWidget(self.pushButton_M8)


        self.verticalLayout.addLayout(self.horizontalLayout_5)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_FM.setText(QCoreApplication.translate("Form", u"Folder to monitor", None))
        self.lineEdit_FM.setText(QCoreApplication.translate("Form", u"C:\\Users\\jy1u18\\OneDrive - University of Southampton\\PhD\\Second Project\\Electrochemistry\\20230610", None))
        self.toolButton.setText(QCoreApplication.translate("Form", u"...", None))
        self.label_BA.setText(QCoreApplication.translate("Form", u"Boundary to average", None))
        self.lineEdit_BA.setText(QCoreApplication.translate("Form", u"0.35", None))
        self.label_DS.setText(QCoreApplication.translate("Form", u"Data to simplify", None))
        self.lineEdit_DS.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"ok", None))
        self.pushButton_M1.setText(QCoreApplication.translate("Form", u"Move down 5", None))
        self.pushButton_M2.setText(QCoreApplication.translate("Form", u"Move down 2", None))
        self.pushButton_M3.setText(QCoreApplication.translate("Form", u"Move down 1", None))
        self.pushButton_M4.setText(QCoreApplication.translate("Form", u"Move down 0.5", None))
        self.pushButton_M5.setText(QCoreApplication.translate("Form", u"Move up 5", None))
        self.pushButton_M6.setText(QCoreApplication.translate("Form", u"Move up 2", None))
        self.pushButton_M7.setText(QCoreApplication.translate("Form", u"Move up 1", None))
        self.pushButton_M8.setText(QCoreApplication.translate("Form", u"Move up 0.5", None))
    # retranslateUi

