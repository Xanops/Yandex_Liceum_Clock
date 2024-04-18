import datetime                                                     # добавление необходимых библиотек
import sqlite3
import os
import sys
from PySide6 import QtWidgets, QtMultimedia, QtCore
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QTableWidgetItem, QDialog, QHeaderView
from PySide6.QtCore import Qt, QTimer
from Interfaces.Clock_interface import Ui_MainWindow
from Interfaces.About import Ui_Form
from Interfaces.Budilnik_signal_interface import Ui_Dialog as B_UI_Dialog
from Interfaces.Alerts import Ui_Dialog

melody = 'Music/Maid with the Flaxen Hair.mp3'                # создание глобальных переменных для использования
alert = ''                                              # во всех классах при необходимости


class Info(QWidget, Ui_Form):                           # класс для представления окно об информации приложения нажав
    def __init__(self):                                 # на кнопку "О приложении"
        super().__init__()
        self.setupUi(self)


class Alerts(QDialog, Ui_Dialog):                       # класс вывода ошибок при неверном вводе данных
    def __init__(self):                                 # в необходимом формате
        global alert
        super().__init__()
        self.setupUi(self)
        if alert == 'date':
            self.label_3.hide()
        else:
            self.label.hide()
            self.label_2.hide()
            if alert == 'name':
                self.label_3.setText("Введите название будильника")
            elif alert == 'povt':
                self.label_3.setText('Введите количество повторений будильника')
            else:
                self.label_3.setText('Введите время между повторениями будильника')

        self.pushButton.clicked.connect(self.close)


class BudilnikSignal(QDialog, B_UI_Dialog):
    def __init__(self):
        global melody
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('bd/clock_bd.db3')
        self.kur = self.con.cursor()

        melody = self.con.execute("SELECT [Мелодия] FROM clocks ORDER BY [Время срабатывания] ASC").fetchone()
        self.music = QtCore.QUrl.fromLocalFile(melody)

        self.pushButton.clicked(self.close())


class Main(QMainWindow, Ui_MainWindow):
    def __init__(self):
        global melody
        super().__init__()
        self.setupUi(self)

        self.con = sqlite3.connect('bd/clock_bd.db3')
        self.kur = self.con.cursor()

        self.tableWidget.setColumnCount(6)
        self.tableWidget.setHorizontalHeaderLabels(['Название будильника', 'Время срабатывания',
                                                    'Количество повторений', 'Время между повторениями',
                                                    'Мелодия',
                                                    'Будильник включён'])
        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
        self.tableWidget.setSortingEnabled(True)

        self.raws = self.kur.execute('SELECT COUNT(*) FROM clocks').fetchall()[0][0]
        if self.raws != 0:
            # blig = self.con.execute(
            #     "SELECT [Время срабатывания] FROM clocks ORDER BY [Время срабатывания] ASC").fetchone()
            # timer = QTimer()
            # rand_time = datetime.datetime(int(str(blig)[2:6]), int(str(blig)[7:9]), int(str(blig)[10:13]),
            #                               int(str(blig)[12:15]), int(str(blig)[16:18]), int(str(blig)[19:21]))
            # timer.start((rand_time - datetime.datetime.now()).total_seconds())

            dannie = self.con.execute('SELECT * FROM clocks')
            self.label_6.hide()
            for i, row in enumerate(dannie):
                self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
                for j, elem in enumerate(row):
                    if j == 4:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)[str(elem).rfind('/') + 1:]))
                    else:
                        self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
                    self.tableWidget.item(i, j).setFlags(Qt.ItemIsSelectable)
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()
            self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
        else:
            self.tableWidget.horizontalHeader().hide()
        self.tableWidget.setFixedWidth(927)

        self.dateTimeEdit.setDate(datetime.datetime.now().date())
        self.dateTimeEdit.setTime(datetime.datetime.now().time())

        self.pushButton_3.clicked.connect(self.music)

        self.flag = 'нет'

        self.pushButton_2.hide()

        self.About.triggered.connect(self.info)
        self.alerts = Alerts()
        self.info = Info()
        self.tableWidget.itemSelectionChanged.connect(self.sellected)
        self.pushButton.clicked.connect(self.proverka_na_dobavlenie_izmenenie)
        self.pushButton_2.clicked.connect(self.del_row)
        self.WidgetGlavnixVkladok.tabBarClicked.connect(self.izmenit_razmer_okna)

    def music(self):
        global melody
        fnmusic_vr = QtWidgets.QFileDialog.getOpenFileName(self, 'Выбирете мелодию', '',
                                                           '*.mp3;;*.wav;;All files (*)')[0]
        if fnmusic_vr:
            melody = fnmusic_vr
            self.lineEdit_4.setText(fnmusic_vr[fnmusic_vr.rfind('/') + 1:])
        else:
            melody = 'Music/Maid with the Flaxen Hair.mp3'
            self.lineEdit_4.setText(melody[6:])

    def sellected(self):
        if self.tableWidget.currentRow() != -1:

            self.pushButton_2.show()
            self.lineEdit_1.setText((self.tableWidget.item(self.tableWidget.currentRow(), 0)).text())

            self.dateTimeEdit.setDate(datetime.date(int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[:4]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[5:7]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[8:10])))
            self.dateTimeEdit.setTime(datetime.time(int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[11:13]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[14:16]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[17:19])))

            self.lineEdit_2.setText((self.tableWidget.item(self.tableWidget.currentRow(), 2)).text())
            self.lineEdit_3.setText((self.tableWidget.item(self.tableWidget.currentRow(), 3)).text())
            self.lineEdit_4.setText((self.tableWidget.item(self.tableWidget.currentRow(), 4)).text())
            if self.tableWidget.item(self.tableWidget.currentRow(), 5) == 'да':
                self.checkBox.setTristate(True)
            else:
                self.checkBox.setTristate(False)
            self.pushButton.setText('Изменить')
            self.staroe_znach3 = (self.tableWidget.item(self.tableWidget.currentRow(), 3)).text()

    def proverka_na_dobavlenie_izmenenie(self):
        if self.lineEdit_1.text() and self.lineEdit_2.text() and self.lineEdit_3.text():

            if (self.dateTimeEdit.date() >= datetime.datetime.now().date() and
                self.dateTimeEdit.time() > datetime.datetime.now().time()) or (
                    self.dateTimeEdit.date() > datetime.datetime.now().date()):

                # if self.raws:
                #
                # else:
                    self.dobavlenie_izmenenie_budilnika()

            else:
                alert = 'date'
                self.alerts.show()

        else:
            if not self.lineEdit.text():
                alert = 'name'
            elif not self.lineEdit_2.text():
                alert = 'povt'
            else:
                alert = 'time_m_povt'
            self.alerts.show()



    def dobavlenie_izmenenie_budilnika(self):
        global melody, alert
        if self.lineEdit_4.text() == 'Выбирите мелодию если хотите' or self.lineEdit_4.text() == '':
            self.lineEdit_4.setText(melody[6:])
        if self.checkBox.checkState():
            self.flag = 'да'

        if self.pushButton.text() == 'Добавить':
            self.label_6.hide()
            self.tableWidget.setRowCount(self.raws + 1)

        date = datetime.date(self.dateTimeEdit.date().year(), self.dateTimeEdit.date().month(),
            self.dateTimeEdit.date().day())
        time = datetime.time(self.dateTimeEdit.time().hour(), self.dateTimeEdit.time().minute(),
            self.dateTimeEdit.time().second())
        dt = datetime.datetime.combine(date, time)

        if self.pushButton.text() == 'Добавить':
            self.tableWidget.setItem(self.raws, 0, QTableWidgetItem(self.lineEdit_1.text()))
            self.tableWidget.item(self.raws, 0).setFlags(Qt.ItemIsSelectable)
            self.tableWidget.setItem(self.raws, 1, QTableWidgetItem(self.dateTimeEdit.text()))
            self.tableWidget.item(self.raws, 1).setFlags(Qt.ItemIsSelectable)
            self.tableWidget.setItem(self.raws, 2, QTableWidgetItem(self.lineEdit_2.text()))
            self.tableWidget.item(self.raws, 2).setFlags(Qt.ItemIsSelectable)
            self.tableWidget.setItem(self.raws, 3, QTableWidgetItem(self.lineEdit_3.text()))
            self.tableWidget.item(self.raws, 3).setFlags(Qt.ItemIsSelectable)
            self.tableWidget.setItem(self.raws, 4, QTableWidgetItem(self.lineEdit_4.text()))
            self.tableWidget.item(self.raws, 4).setFlags(Qt.ItemIsSelectable)
            self.tableWidget.setItem(self.raws, 5, QTableWidgetItem(self.flag))
            self.tableWidget.item(self.raws, 5).setFlags(Qt.ItemIsSelectable)

            self.tableWidget.horizontalHeader().show()

            self.kur.execute(f"""INSERT INTO clocks ([Название будильника], [Время срабатывания],
                [Количество повторений срабатывания], [Время между повторениями], [Мелодия],
                [Будильник включён]) VALUES ('{self.lineEdit_1.text()}', '{dt}', {int(self.lineEdit_2.text())},
                {int(self.lineEdit_3.text())}, '{melody}', '{self.flag}')""")
            self.kur.execute(f'''INSERT INTO times ([time], [End_of_signal] VALUES ("{dt}", "{int(self.lineEdit_2.text()) * datetime.time.second(self.lineEdit_3.text()) + os.listdir(path=f'{melody}')}")''')
            self.con.commit()
            self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
            self.raws += 1
            self.flag = 'нет'

        else:
            self.tableWidget.setItem(self.tableWidget.currentRow(), 0, QTableWidgetItem(self.lineEdit_1.text()))
            self.tableWidget.setItem(
                self.tableWidget.currentRow(), 1, QTableWidgetItem(self.dateTimeEdit.text()))
            self.tableWidget.setItem(self.tableWidget.currentRow(), 2, QTableWidgetItem(self.lineEdit_2.text()))
            self.tableWidget.setItem(self.tableWidget.currentRow(), 3, QTableWidgetItem(self.lineEdit_3.text()))
            self.tableWidget.setItem(self.tableWidget.currentRow(), 4, QTableWidgetItem(self.lineEdit_4.text()))
            self.tableWidget.setItem(self.tableWidget.currentRow(), 5, QTableWidgetItem(self.flag))

            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.resizeRowsToContents()

            self.kur.execute(
                f"""UPDATE clocks SET [Название будильника] = '{self.lineEdit_1.text()}' WHERE [Время между повторениями] = {self.staroe_znach3}""")
            self.kur.execute(
                f"""UPDATE clocks SET [Время срабатывания] = '{dt}' WHERE [Время между повторениями] = {self.staroe_znach3}""")
            self.con.commit()
            self.kur.execute(
                f"""UPDATE clocks SET [Количество повторений срабатывания] = '{int(self.lineEdit_2.text())}' WHERE [Название будильника] = '{self.lineEdit_1.text()}'""")
            self.kur.execute(
                f"""UPDATE clocks SET [Время между повторениями] = {int(self.lineEdit_3.text())} WHERE [Название будильника] = '{self.lineEdit_1.text()}'""")
            self.kur.execute(
                f"""UPDATE clocks SET [Мелодия] = '{self.lineEdit_4.text()}' WHERE [Название будильника] = '{self.lineEdit_1.text()}'""")
            self.kur.execute(
                f"""UPDATE clocks SET [Будильник включён] = '{self.flag}' WHERE [Название будильника] = '{self.lineEdit_1.text()}'""")
            self.con.commit()
            self.tableWidget.verticalHeader().setSectionResizeMode(QHeaderView.Fixed)
            self.flag = 'нет'
            self.pushButton.setText('Добавить')
            self.pushButton_2.hide()

    def del_row(self):
        dt = datetime.datetime(int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[:4]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[5:7]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[8:10]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[11:13]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[14:16]), int((self.tableWidget.item(self.tableWidget.currentRow(), 1)).text()[17:19]))
        self.con.execute(f'''DELETE FROM clocks WHERE [Время срабатывания] = "{dt}"''')
        self.con.commit()

        self.tableWidget.removeRow(self.tableWidget.currentRow())
        self.raws -= 1
        if self.raws == 0:
            self.tableWidget.horizontalHeader().hide()
            self.label_6.show()

    def izmenit_razmer_okna(self):
        if self.WidgetGlavnixVkladok.currentIndex() == 0:
            self.setFixedSize(533, 211)
        else:
            self.setFixedSize(1380, 441)

    def info(self):
        self.info.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Main()
    ex.show()
    sys.exit(app.exec())
