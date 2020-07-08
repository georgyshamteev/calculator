# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Calculator(object):
    def setupUi(self, Calculator):
        if not Calculator.objectName():
            Calculator.setObjectName(u"Calculator")
        Calculator.resize(351, 473)
        Calculator.setAutoFillBackground(False)
        Calculator.setStyleSheet(u"QPushButton{\n"
"  background-color: white;\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"\n"
"QLineEdit {\n"
"  background-color: rgb(197, 197, 197);\n"
"}\n"
"QDialog{\n"
"background-color: black;\n"
"}\n"
"")
        self.gridLayoutWidget = QWidget(Calculator)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(0, 170, 348, 301))
        self.gridLayout = QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setSpacing(2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(1, 1, 1, 1)
        self.pushButton_15 = QPushButton(self.gridLayoutWidget)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.gridLayout.addWidget(self.pushButton_15, 3, 2, 1, 1)

        self.pushButton_14 = QPushButton(self.gridLayoutWidget)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.gridLayout.addWidget(self.pushButton_14, 3, 1, 1, 1)

        self.pushButton_23 = QPushButton(self.gridLayoutWidget)
        self.pushButton_23.setObjectName(u"pushButton_23")

        self.gridLayout.addWidget(self.pushButton_23, 5, 2, 1, 1)

        self.pushButton_22 = QPushButton(self.gridLayoutWidget)
        self.pushButton_22.setObjectName(u"pushButton_22")

        self.gridLayout.addWidget(self.pushButton_22, 5, 1, 1, 1)

        self.pushButton_19 = QPushButton(self.gridLayoutWidget)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setStyleSheet(u"")

        self.gridLayout.addWidget(self.pushButton_19, 4, 2, 1, 1)

        self.pushButton_9 = QPushButton(self.gridLayoutWidget)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.gridLayout.addWidget(self.pushButton_9, 2, 0, 1, 1)

        self.pushButton_17 = QPushButton(self.gridLayoutWidget)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.gridLayout.addWidget(self.pushButton_17, 4, 0, 1, 1)

        self.pushButton_13 = QPushButton(self.gridLayoutWidget)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.gridLayout.addWidget(self.pushButton_13, 3, 0, 1, 1)

        self.pushButton_21 = QPushButton(self.gridLayoutWidget)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.gridLayout.addWidget(self.pushButton_21, 5, 0, 1, 1)

        self.pushButton_11 = QPushButton(self.gridLayoutWidget)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout.addWidget(self.pushButton_11, 2, 2, 1, 1)

        self.pushButton_10 = QPushButton(self.gridLayoutWidget)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.gridLayout.addWidget(self.pushButton_10, 2, 1, 1, 1)

        self.pushButton_18 = QPushButton(self.gridLayoutWidget)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.gridLayout.addWidget(self.pushButton_18, 4, 1, 1, 1)

        self.pushButton_1 = QPushButton(self.gridLayoutWidget)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_1, 0, 0, 1, 1)

        self.pushButton_2 = QPushButton(self.gridLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_2, 0, 1, 1, 1)

        self.pushButton_3 = QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_3, 0, 2, 1, 1)

        self.pushButton_4 = QPushButton(self.gridLayoutWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}\n"
"")

        self.gridLayout.addWidget(self.pushButton_4, 0, 3, 1, 1)

        self.pushButton_5 = QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_5, 1, 0, 1, 1)

        self.pushButton_6 = QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_6, 1, 1, 1, 1)

        self.pushButton_7 = QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_7, 1, 2, 1, 1)

        self.pushButton_8 = QPushButton(self.gridLayoutWidget)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_8, 1, 3, 1, 1)

        self.pushButton_12 = QPushButton(self.gridLayoutWidget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_12, 2, 3, 1, 1)

        self.pushButton_16 = QPushButton(self.gridLayoutWidget)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_16, 3, 3, 1, 1)

        self.pushButton_20 = QPushButton(self.gridLayoutWidget)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setStyleSheet(u"QPushButton{\n"
"  background-color: rgb(229, 229, 229);\n"
"  width: 85px;\n"
"  height: 45px;\n"
"  font-size: 14px;\n"
"  font-weight: bold;\n"
"  border: none;\n"
"  text-align: center;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"  background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_20, 4, 3, 1, 1)

        self.pushButton_24 = QPushButton(self.gridLayoutWidget)
        self.pushButton_24.setObjectName(u"pushButton_24")
        self.pushButton_24.setStyleSheet(u"QPushButton{\n"
"background-color: rgb(148, 186, 255);\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color: silver;\n"
"}")

        self.gridLayout.addWidget(self.pushButton_24, 5, 3, 1, 1)

        self.lineEdit = QLineEdit(Calculator)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 90, 351, 41))
        self.lineEdit.setStyleSheet(u"font-size: 22px;\n"
"font-weight: bold;\n"
"text-align: left;\n"
"border: none;\n"
"")
        self.lineEdit_2 = QLineEdit(Calculator)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(10, 60, 351, 31))
        self.lineEdit_2.setStyleSheet(u"font-size: 12px;\n"
"text-align: left;\n"
"border: none;\n"
"")

        self.retranslateUi(Calculator)

        QMetaObject.connectSlotsByName(Calculator)
    # setupUi

    def retranslateUi(self, Calculator):
        Calculator.setWindowTitle(QCoreApplication.translate("Calculator", u"Dialog", None))
        self.pushButton_15.setText(QCoreApplication.translate("Calculator", u"6", None))
        self.pushButton_14.setText(QCoreApplication.translate("Calculator", u"5", None))
        self.pushButton_23.setText(QCoreApplication.translate("Calculator", u",", None))
        self.pushButton_22.setText(QCoreApplication.translate("Calculator", u"0", None))
        self.pushButton_19.setText(QCoreApplication.translate("Calculator", u"3", None))
        self.pushButton_9.setText(QCoreApplication.translate("Calculator", u"7", None))
        self.pushButton_17.setText(QCoreApplication.translate("Calculator", u"1", None))
        self.pushButton_13.setText(QCoreApplication.translate("Calculator", u"4", None))
        self.pushButton_21.setText(QCoreApplication.translate("Calculator", u"\u03c0", None))
        self.pushButton_11.setText(QCoreApplication.translate("Calculator", u"9", None))
        self.pushButton_10.setText(QCoreApplication.translate("Calculator", u"8", None))
        self.pushButton_18.setText(QCoreApplication.translate("Calculator", u"2", None))
        self.pushButton_1.setText(QCoreApplication.translate("Calculator", u"1/x", None))
        self.pushButton_2.setText(QCoreApplication.translate("Calculator", u"x^y", None))
        self.pushButton_3.setText(QCoreApplication.translate("Calculator", u"C", None))
        self.pushButton_4.setText(QCoreApplication.translate("Calculator", u"\u0421\u0442\u0435\u0440\u0435\u0442\u044c", None))
        self.pushButton_5.setText(QCoreApplication.translate("Calculator", u"!", None))
        self.pushButton_6.setText(QCoreApplication.translate("Calculator", u"\u0445^2", None))
        self.pushButton_7.setText(QCoreApplication.translate("Calculator", u"\u221a(x)", None))
        self.pushButton_8.setText(QCoreApplication.translate("Calculator", u"/", None))
        self.pushButton_12.setText(QCoreApplication.translate("Calculator", u"*", None))
        self.pushButton_16.setText(QCoreApplication.translate("Calculator", u"-", None))
        self.pushButton_20.setText(QCoreApplication.translate("Calculator", u"+", None))
        self.pushButton_24.setText(QCoreApplication.translate("Calculator", u"=", None))
        self.lineEdit.setText(QCoreApplication.translate("Calculator", u"dfghj", None))
        self.lineEdit_2.setText(QCoreApplication.translate("Calculator", u"dsfsdf", None))
    # retranslateUi

