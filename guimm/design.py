# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'design.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableView, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(870, 607)
        MainWindow.setStyleSheet(u"background-color: #191919;\n"
"font-family: Montserrat")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.taskscount = QFrame(self.centralwidget)
        self.taskscount.setObjectName(u"taskscount")
        self.taskscount.setStyleSheet(u"background-color: rgba(255, 255, 255, 30);\n"
"border: 1px solid rgba(255, 255, 255, 40);\n"
"border-radius: 7px;")
        self.verticalLayout = QVBoxLayout(self.taskscount)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.activetask = QLabel(self.taskscount)
        self.activetask.setObjectName(u"activetask")
        self.activetask.setStyleSheet(u"color: #F6F6F6;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: None;")

        self.horizontalLayout.addWidget(self.activetask)

        self.donetask = QLabel(self.taskscount)
        self.donetask.setObjectName(u"donetask")
        self.donetask.setStyleSheet(u"color: #F6F6F6;\n"
"font-weight: bold;\n"
"font-size: 20pt;\n"
"background-color: None;")

        self.horizontalLayout.addWidget(self.donetask)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.count = QFrame(self.taskscount)
        self.count.setObjectName(u"count")
        self.count.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.count)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.activecount = QLabel(self.count)
        self.activecount.setObjectName(u"activecount")
        self.activecount.setStyleSheet(u"color: #F6F6F6;\n"
"font-size: 18pt;\n"
"background-color: None;")

        self.horizontalLayout_2.addWidget(self.activecount)

        self.donecount = QLabel(self.count)
        self.donecount.setObjectName(u"donecount")
        self.donecount.setStyleSheet(u"color: #F6F6F6;\n"
"font-size: 18pt;\n"
"background-color: None;")

        self.horizontalLayout_2.addWidget(self.donecount)


        self.verticalLayout.addWidget(self.count)


        self.horizontalLayout_3.addWidget(self.taskscount)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.btn_delete = QPushButton(self.centralwidget)
        self.btn_delete.setObjectName(u"btn_delete")
        self.btn_delete.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_delete)

        self.btn_add = QPushButton(self.centralwidget)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_2.addWidget(self.btn_add)


        self.horizontalLayout_3.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_3)

        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 90);\n"
"border: 1px solid rgba(255, 255, 255, 30);\n"
"border-bottom-left-radius: 10px;\n"
"border-bottom-right-radius: 10px;\n"
"}\n"
"QTableView::section {\n"
"background-color: rgba(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 14pt;;\n"
"}\n"
"QTableView::item {\n"
"border-style: none;\n"
"border-bottom: rgba(255, 255, 255, 50);\n"
"}\n"
"QTableView::item:selected {\n"
"border: none;\n"
"color: rgba(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 50);\n"
"}")

        self.verticalLayout_3.addWidget(self.tableView)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"TasksOnDay", None))
        self.activetask.setText(QCoreApplication.translate("MainWindow", u"\u0410\u043a\u0442\u0438\u0432\u043d\u044b\u0435 \u0437\u0430\u0434\u0430\u0447\u0438:", None))
        self.donetask.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043d\u044b\u0435 \u0437\u0430\u0434\u0430\u0447\u0438:", None))
        self.activecount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.donecount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.btn_delete.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u0434\u0430\u0447\u0443", None))
    # retranslateUi

