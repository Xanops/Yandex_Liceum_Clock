# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Clock_interface.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QDateTimeEdit,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QTabWidget, QTableWidget, QTableWidgetItem,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1380, 451)
        MainWindow.setMinimumSize(QSize(1380, 451))
        MainWindow.setMaximumSize(QSize(1380, 451))
        MainWindow.setCursor(QCursor(Qt.ArrowCursor))
        self.About = QAction(MainWindow)
        self.About.setObjectName(u"About")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.WidgetGlavnixVkladok = QTabWidget(self.centralwidget)
        self.WidgetGlavnixVkladok.setObjectName(u"WidgetGlavnixVkladok")
        self.WidgetGlavnixVkladok.setGeometry(QRect(0, 0, 1381, 405))
        self.WidgetGlavnixVkladok.setMinimumSize(QSize(0, 405))
        self.WidgetGlavnixVkladok.setMaximumSize(QSize(16777215, 405))
        palette = QPalette()
        brush = QBrush(QColor(0, 170, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush)
        brush1 = QBrush(QColor(0, 0, 0, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.NoRole, brush1)
        brush2 = QBrush(QColor(0, 0, 255, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.NoRole, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush2)
        brush3 = QBrush(QColor(255, 255, 255, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.NoRole, brush3)
        self.WidgetGlavnixVkladok.setPalette(palette)
        font = QFont()
        font.setPointSize(12)
        self.WidgetGlavnixVkladok.setFont(font)
        self.WidgetGlavnixVkladok.setTabShape(QTabWidget.Triangular)
        self.Vkladka_budilnik = QWidget()
        self.Vkladka_budilnik.setObjectName(u"Vkladka_budilnik")
        self.Vkladka_budilnik.setMinimumSize(QSize(0, 0))
        self.Vkladka_budilnik.setMaximumSize(QSize(16777215, 16777215))
        self.Vkladka_budilnik.setStyleSheet(u"background-color: rgb(170, 170, 0);")
        self.pushButton_3 = QPushButton(self.Vkladka_budilnik)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1200, 220, 161, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(170, 170, 255);")
        self.label = QLabel(self.Vkladka_budilnik)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(1060, 10, 201, 21))
        font1 = QFont()
        font1.setFamilies([u"MS Shell Dlg 2"])
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setItalic(False)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"font: 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(22, 25, 194);\n"
"background-color: qlineargradient(spread:reflect, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(153, 61, 0, 255), stop:1 rgba(183, 255, 255, 255));")
        self.lineEdit_2 = QLineEdit(self.Vkladka_budilnik)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(1160, 120, 201, 31))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(174, 255, 190);")
        self.dateTimeEdit = QDateTimeEdit(self.Vkladka_budilnik)
        self.dateTimeEdit.setObjectName(u"dateTimeEdit")
        self.dateTimeEdit.setGeometry(QRect(1160, 81, 201, 31))
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setCursor(QCursor(Qt.IBeamCursor))
        self.dateTimeEdit.setStyleSheet(u"background-color: rgb(174, 255, 190);")
        self.label_3 = QLabel(self.Vkladka_budilnik)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(960, 130, 191, 21))
        self.label_3.setFont(font)
        self.label_2 = QLabel(self.Vkladka_budilnik)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(970, 80, 161, 31))
        self.label_2.setFont(font)
        self.pushButton_2 = QPushButton(self.Vkladka_budilnik)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(950, 270, 91, 31))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(255, 0, 0);")
        self.pushButton = QPushButton(self.Vkladka_budilnik)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1060, 270, 111, 31))
        self.pushButton.setFont(font)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(9, 41, 4, 255), stop:0.085 rgba(2, 79, 0, 255), stop:0.19 rgba(50, 147, 22, 255), stop:0.275 rgba(236, 191, 49, 255), stop:0.39 rgba(243, 61, 34, 255), stop:0.555 rgba(135, 81, 60, 255), stop:0.667 rgba(121, 75, 255, 255), stop:0.825 rgba(164, 255, 244, 255), stop:0.885 rgba(104, 222, 71, 255), stop:1 rgba(93, 128, 0, 255));")
        self.checkBox = QCheckBox(self.Vkladka_budilnik)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setGeometry(QRect(1190, 270, 181, 31))
        self.checkBox.setFont(font)
        self.checkBox.setCursor(QCursor(Qt.PointingHandCursor))
        self.checkBox.setStyleSheet(u"background-color: rgb(170, 170, 127);")
        self.lineEdit_4 = QLineEdit(self.Vkladka_budilnik)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(950, 220, 251, 31))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setCursor(QCursor(Qt.ArrowCursor))
        self.lineEdit_4.setStyleSheet(u"background-color: rgb(85, 170, 255);")
        self.lineEdit_4.setReadOnly(True)
        self.label_5 = QLabel(self.Vkladka_budilnik)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(970, 45, 171, 21))
        self.label_5.setFont(font)
        self.lineEdit_1 = QLineEdit(self.Vkladka_budilnik)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(1160, 39, 201, 31))
        self.lineEdit_1.setFont(font)
        self.lineEdit_1.setStyleSheet(u"background-color: rgb(174, 255, 190);")
        self.label_7 = QLabel(self.Vkladka_budilnik)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(1020, 190, 91, 20))
        self.label_7.setFont(font)
        self.lineEdit_3 = QLineEdit(self.Vkladka_budilnik)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(1160, 170, 201, 41))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setCursor(QCursor(Qt.IBeamCursor))
        self.lineEdit_3.setStyleSheet(u"background-color: rgb(174, 255, 190);")
        self.label_4 = QLabel(self.Vkladka_budilnik)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(940, 160, 221, 31))
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"")
        self.tableWidget = QTableWidget(self.Vkladka_budilnik)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(0, 0, 931, 321))
        self.tableWidget.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setSortingEnabled(True)
        self.label_6 = QLabel(self.Vkladka_budilnik)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(160, 110, 601, 101))
        font2 = QFont()
        font2.setPointSize(30)
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"background-color: rgb(170, 170, 0);")
        self.pushButton_7 = QPushButton(self.Vkladka_budilnik)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(10, 330, 1361, 41))
        self.pushButton_7.setStyleSheet(u"background-color: rgb(85, 85, 255);\n"
"font: 75 19pt \"Arial\";\n"
"selection-color: rgb(85, 170, 0);")
        icon = QIcon()
        icon.addFile(u"Clock/Clock_images/off.png", QSize(), QIcon.Active, QIcon.Off)
        icon.addFile(u"Clock/Clock_images/on.png", QSize(), QIcon.Active, QIcon.On)
        self.WidgetGlavnixVkladok.addTab(self.Vkladka_budilnik, icon, "")
        self.Vkladka_pleer = QWidget()
        self.Vkladka_pleer.setObjectName(u"Vkladka_pleer")
        self.Vkladka_pleer.setStyleSheet(u"")
        self.widget = QWidget(self.Vkladka_pleer)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 531, 151))
        self.widget.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:1, x2:0, y2:0, stop:0 rgba(0, 0, 0, 255), stop:0.05 rgba(14, 8, 73, 255), stop:0.36 rgba(28, 17, 145, 255), stop:0.6 rgba(126, 14, 81, 255), stop:0.75 rgba(234, 11, 11, 255), stop:0.79 rgba(244, 70, 5, 255), stop:0.86 rgba(255, 136, 0, 255), stop:0.935 rgba(239, 236, 55, 255));")
        self.pushButton_4 = QPushButton(self.widget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(60, 20, 161, 51))
        self.pushButton_4.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 0, 0, 255), stop:0.166 rgba(255, 255, 0, 255), stop:0.333 rgba(0, 255, 0, 255), stop:0.5 rgba(0, 255, 255, 255), stop:0.666 rgba(0, 0, 255, 255), stop:0.833 rgba(255, 0, 255, 255), stop:1 rgba(255, 0, 0, 255));\n"
"font: 75 25pt \"MS Shell Dlg 2\";")
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(310, 20, 161, 51))
        self.pushButton_5.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"font: 75 25pt \"MS Shell Dlg 2\";")
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 93, 131, 41))
        self.pushButton_6.setStyleSheet(u"background-color: rgb(170, 170, 255);\n"
"font: 75 11pt \"MS Shell Dlg 2\";")
        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(150, 100, 361, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgb(0, 195, 195);")
        self.WidgetGlavnixVkladok.addTab(self.Vkladka_pleer, icon, "")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1380, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.lineEdit_1, self.dateTimeEdit)
        QWidget.setTabOrder(self.dateTimeEdit, self.lineEdit_2)
        QWidget.setTabOrder(self.lineEdit_2, self.lineEdit_3)
        QWidget.setTabOrder(self.lineEdit_3, self.pushButton_3)
        QWidget.setTabOrder(self.pushButton_3, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.pushButton)
        QWidget.setTabOrder(self.pushButton, self.pushButton_2)
        QWidget.setTabOrder(self.pushButton_2, self.lineEdit_4)
        QWidget.setTabOrder(self.lineEdit_4, self.tableWidget)
        QWidget.setTabOrder(self.tableWidget, self.WidgetGlavnixVkladok)
        QWidget.setTabOrder(self.WidgetGlavnixVkladok, self.pushButton_4)
        QWidget.setTabOrder(self.pushButton_4, self.pushButton_5)
        QWidget.setTabOrder(self.pushButton_5, self.pushButton_6)
        QWidget.setTabOrder(self.pushButton_6, self.lineEdit)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.About)

        self.retranslateUi(MainWindow)

        self.WidgetGlavnixVkladok.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Clockopleer", None))
        self.About.setText(QCoreApplication.translate("MainWindow", u"\u041e \u043f\u0440\u0438\u043b\u043e\u0436\u0435\u043d\u0438\u0438", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043c\u0435\u043b\u043e\u0434\u0438\u044e", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"      \u0417\u0430\u0434\u0430\u0439\u0442\u0435 \u0431\u0443\u0434\u0438\u043b\u044c\u043d\u0438\u043a", None))
        self.lineEdit_2.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.dateTimeEdit.setDisplayFormat(QCoreApplication.translate("MainWindow", u"dd.MM.yyyy HH:mm", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u0439:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u0441\u0440\u0430\u0431\u0430\u0442\u044b\u0432\u0430\u043d\u0438\u044f:", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
        self.checkBox.setText(QCoreApplication.translate("MainWindow", u"\u0412\u043a\u043b\u044e\u0447\u0438\u0442\u044c \u0431\u0443\u0434\u0438\u043b\u044c\u043d\u0438\u043a", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0438\u0440\u0438\u0442\u0435 \u043c\u0435\u043b\u043e\u0434\u0438\u044e \u0435\u0441\u043b\u0438 \u0445\u043e\u0442\u0438\u0442\u0435", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0431\u0443\u0434\u0438\u043b\u044c\u043d\u0438\u043a\u0430:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"\u0432 \u0441\u0435\u043a\u0443\u043d\u0434\u0430\u0445:", None))
        self.lineEdit_3.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u0412\u0440\u0435\u043c\u044f \u043c\u0435\u0436\u0434\u0443 \u043f\u043e\u0432\u0442\u043e\u0440\u0435\u043d\u0438\u044f\u043c\u0438", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0435\u0442 \u0434\u0430\u043d\u043d\u044b\u0445, \u0437\u0430\u0434\u0430\u0439\u0442\u0435 \u0431\u0443\u0434\u0438\u043b\u044c\u043d\u0438\u043a", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"\u0421\u043d\u044f\u0442\u044c \u0432\u044b\u0434\u0435\u043b\u0435\u043d\u0438\u0435 \u0441 \u043a\u043e\u043b\u043e\u043d\u043a\u0438", None))
        self.WidgetGlavnixVkladok.setTabText(self.WidgetGlavnixVkladok.indexOf(self.Vkladka_budilnik), QCoreApplication.translate("MainWindow", u"\u0411\u0443\u0434\u0438\u043b\u044c\u043d\u0438\u043a", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Play", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Pause", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"\u0412\u044b\u0431\u0440\u0430\u0442\u044c \u043c\u0443\u0437\u044b\u043a\u0443", None))
        self.WidgetGlavnixVkladok.setTabText(self.WidgetGlavnixVkladok.indexOf(self.Vkladka_pleer), QCoreApplication.translate("MainWindow", u"\u041c\u0443\u0437\u044b\u043a\u0430\u043b\u044c\u043d\u044b\u0439 \u043f\u043b\u0435\u0435\u0440", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438", None))
    # retranslateUi

