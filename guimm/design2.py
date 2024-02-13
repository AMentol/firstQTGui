# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design2.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QDateEdit, QDialog,
    QFrame, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(240, 269)
        Dialog.setStyleSheet(u"background-color: #191919;\n"
"font-family: Montserrat")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lbl_newtask = QLabel(self.frame)
        self.lbl_newtask.setObjectName(u"lbl_newtask")
        self.lbl_newtask.setStyleSheet(u"color: #F6F6F6;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: None;\n"
"border: none;")

        self.verticalLayout.addWidget(self.lbl_newtask)

        self.data = QDateEdit(self.frame)
        self.data.setObjectName(u"data")
        self.data.setStyleSheet(u"color: #F6F6F6;\n"
"font-size: 18pt;\n"
"padding-left: 5px;\n"
"padding-top: 10px;\n"
"padding-bottom: 10px;")
        self.data.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.verticalLayout.addWidget(self.data)

        self.taskdesc = QLineEdit(self.frame)
        self.taskdesc.setObjectName(u"taskdesc")
        self.taskdesc.setStyleSheet(u"padding: 10px;\n"
"color: #F6F6F6;\n"
"font-size: 9pt;")

        self.verticalLayout.addWidget(self.taskdesc)

        self.btn_savetask = QPushButton(self.frame)
        self.btn_savetask.setObjectName(u"btn_savetask")
        self.btn_savetask.setStyleSheet(u"QPushButton {\n"
"color: #F6F6F6;\n"
"background-color: #2A2B2B;\n"
"border-radius: 20px;\n"
"font-size: 15pt;\n"
"width: 200px;\n"
"height: 50px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255, 255, 40);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgba(255,255, 255, 70);\n"
"}")

        self.verticalLayout.addWidget(self.btn_savetask)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"NewTask", None))
        self.lbl_newtask.setText(QCoreApplication.translate("Dialog", u"\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u0434\u0430\u0447\u0430", None))
        self.taskdesc.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0437\u0430\u0434\u0430\u0447\u0438...", None))
        self.btn_savetask.setText(QCoreApplication.translate("Dialog", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

