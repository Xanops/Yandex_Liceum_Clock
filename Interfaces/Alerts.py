# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Alerts.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(401, 131)
        Dialog.setMinimumSize(QSize(401, 131))
        Dialog.setMaximumSize(QSize(401, 131))
        Dialog.setStyleSheet(u"background-color: rgb(200, 200, 0);")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 70, 361, 51))
        font = QFont()
        font.setPointSize(17)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 170, 0);")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 381, 21))
        font1 = QFont()
        font1.setPointSize(13)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.label.setTextFormat(Qt.PlainText)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 30, 381, 31))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"background-color: rgb(170, 0, 0);")
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 10, 321, 41))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color: rgb(170, 0, 0);")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"\u041e\u0448\u0438\u0431\u043a\u0430", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"OK", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"  \u0412\u0440\u0435\u043c\u044f \u0431\u0443\u0434\u0438\u043b\u044c\u043d\u0438\u043a\u0430 \u043e\u043f\u0430\u0437\u0434\u044b\u0432\u0430\u0435\u0442 \u043e\u0442 \u043d\u0430\u0441\u0442\u043e\u044f\u0449\u0435\u0433\u043e.", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u0414\u043b\u044f \u0443\u0434\u0430\u043b\u0435\u043d\u0438\u044f \u0432\u044b\u0431\u0435\u0440\u0435\u0442\u0435 \u0440\u044f\u0434", None))
    # retranslateUi

