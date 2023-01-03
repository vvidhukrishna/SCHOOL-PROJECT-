import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtGui import QIcon
from PyQt5 import QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtCore, QtGui, QtWidgets
from algoritham import values_and_target


class Ui_MainWindow_(object):
    def __init__(self):
        self.Difficulty = 3
        self.moving_value = 1
        self.values, self.target = values_and_target(8, self.Difficulty)
        self.target = str(int(float(self.target)))
        print(self.target)

    def win_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Victory Box!")
        msg.setText("YOU WON!!!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Close)
        msg.setInformativeText("Do you want to play again?")
        msg.setDefaultButton(QMessageBox.Close)
        msg.buttonClicked.connect(self.reply)
        msg.exec_()

    def reply(self, i):
        if i.text() == 'Close':
            exit()

    def animation(self):
        self.animation = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation.setDuration(1000)
        self.animation.setEndValue(QRect(self.pushButton4.x(), self.pushButton4.y(), 90, 90))
        self.animation.start()

    def animation1(self):
        self.animation1 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation1.setDuration(1000)
        self.animation1.setEndValue(QRect(self.pushButton1.x(), self.pushButton1.y(), 90, 90))
        self.animation1.start()
        self.moving_value = round(eval(str(self.moving_value) +self.values[0]))
        print(self.moving_value)
        print(self.target)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton1.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation2(self):
        self.animation2 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation2.setDuration(1000)
        self.animation2.setEndValue(QRect(self.pushButton2.x(), self.pushButton2.y(), 90, 90))
        self.animation2.start()
        self.moving_value = round(eval(str(self.moving_value) +self.values[1]))
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton2.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation3(self):
        self.animation3 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation3.setDuration(1000)
        self.animation3.setEndValue(QRect(self.pushButton3.x(), self.pushButton3.y(), 90, 90))
        self.animation3.start()
        self.moving_value = round(eval(str(self.moving_value) +self.values[2]))
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton3.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation4(self):
        self.animation4 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation4.setDuration(1000)
        self.animation4.setEndValue(QRect(self.pushButton4.x(), self.pushButton4.y(), 90, 90))
        self.animation4.start()
        self.moving_value = round(eval(str(self.moving_value) + self.values[3]))
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton4.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation5(self):
        self.animation5 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation5.setDuration(1000)
        self.animation5.setEndValue(QRect(self.pushButton5.x(), self.pushButton5.y(), 90, 90))
        self.animation5.start()
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation6(self):
        self.animation6 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation6.setDuration(1000)
        self.animation6.setEndValue(QRect(self.pushButton6.x(), self.pushButton6.y(), 90, 90))
        self.animation6.start()
        self.moving_value = round(eval(str(self.moving_value) + self.values[4]))
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton6.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation7(self):
        self.animation7 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation7.setDuration(1000)
        self.animation7.setEndValue(QRect(self.pushButton7.x(), self.pushButton7.y(), 90, 90))
        self.animation7.start()
        self.moving_value = round(eval(str(self.moving_value) + self.values[5]))
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton7.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation8(self):
        self.animation8 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation8.setDuration(1000)
        self.animation8.setEndValue(QRect(self.pushButton8.x(), self.pushButton8.y(), 90, 90))
        self.animation8.start()
        self.moving_value = round(eval(str(self.moving_value) + self.values[6]))
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton8.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def animation9(self):
        self.animation9 = QPropertyAnimation(self.movingbutton, b'geometry')
        self.animation9.setDuration(1000)
        self.animation9.setEndValue(QRect(self.pushButton9.x(), self.pushButton9.y(), 90, 90))
        self.animation9.start()
        self.moving_value = round(eval(str(self.moving_value) + self.values[7]))
        print(self.moving_value)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton9.setEnabled(False)
        if int(self.moving_value) == int(self.target):
            self.win_message()

    def StartOver(self):
        self.pushButton1.setEnabled(True)
        self.pushButton2.setEnabled(True)
        self.pushButton3.setEnabled(True)
        self.pushButton4.setEnabled(True)
        self.pushButton6.setEnabled(True)
        self.pushButton7.setEnabled(True)
        self.pushButton8.setEnabled(True)
        self.pushButton9.setEnabled(True)
        self.moving_value = 1
        self.movingbutton.setText(str(self.moving_value))

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("TASK 1")
        MainWindow.resize(1280, 720)
        MainWindow.setWindowIcon(QtGui.QIcon('Pc_builder_logo.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(0, 0, 1280, 720)
        self.label.setPixmap(QPixmap("task_back.jpeg"))
        self.label.setText("")
        self.label.setObjectName("label")

        self.req_output_display = QtWidgets.QLabel(self.centralwidget)
        self.req_output_display.setGeometry(1080, 360, 90, 90)
        self.req_output_display.setStyleSheet("background:white;")
        self.req_output_display.setText(self.target)
        self.req_output_display.setAlignment(Qt.AlignCenter)
        self.req_output_display.setObjectName("req_output_display")
        self.req_output_display.setStyleSheet("background-color:pink;border-radius:10%;font-size:20px")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setText("Solve the mystery of the ancient temple")
        self.label_20.setGeometry(630, 40, 361, 91)
        self.label_20.setStyleSheet("font-size:30px;")
        self.label_20.adjustSize()
        self.label_20.font().setBold(True)
        self.label_20.setObjectName("label_20")

        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
        self.startbutton.clicked.connect(self.StartOver)
        self.startbutton.setGeometry(810, 530, 151, 31)
        self.startbutton.setObjectName("startbutton")
        self.startbutton.setText('START OVER')
        self.startbutton.setStyleSheet("background-color:#21b079;border-radius:10%;font-size:20px;")

        self.exitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.exitbutton.clicked.connect(MainWindow.close)
        self.exitbutton.setText("EXIT")
        self.exitbutton.setGeometry(810, 580, 151, 31)
        self.exitbutton.setObjectName("exitbutton")
        self.exitbutton.setStyleSheet("background-color:#21b079;border-radius:10%;font-size:20px;")

        self.pushButton1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton1.clicked.connect(self.animation1)
        self.pushButton1.setGeometry(150, 250, 90, 90)
        self.pushButton1.setText(self.values[0])
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.clicked.connect(self.animation2)
        self.pushButton2.setGeometry(260, 250, 90, 90)
        self.pushButton2.setText(self.values[1])
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.clicked.connect(self.animation3)
        self.pushButton3.setGeometry(370, 250, 90, 90)
        self.pushButton3.setText(self.values[2])
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.clicked.connect(self.animation4)
        self.pushButton4.setGeometry(150, 360, 90, 90)
        self.pushButton4.setText(self.values[3])
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.clicked.connect(self.animation5)
        self.pushButton5.setGeometry(260, 360, 90, 90)
        self.pushButton5.setText("")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.clicked.connect(self.animation6)
        self.pushButton6.setGeometry(370, 360, 90, 90)
        self.pushButton6.setText(self.values[4])
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton6.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.clicked.connect(self.animation7)
        self.pushButton7.setGeometry(150, 470, 90, 90)
        self.pushButton7.setText(self.values[5])
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton7.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.clicked.connect(self.animation8)
        self.pushButton8.setGeometry(260, 470, 90, 90)
        self.pushButton8.setText(self.values[6])
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton8.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton9.clicked.connect(self.animation9)
        self.pushButton9.setGeometry(370, 470, 90, 90)
        self.pushButton9.setText(self.values[7])
        self.pushButton9.setObjectName("pushButton9")
        self.pushButton9.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.movingbutton = QtWidgets.QPushButton(self.centralwidget)
        self.movingbutton.setGeometry(260, 360, 90, 90)
        self.movingbutton.setText("1")
        self.movingbutton.setObjectName("movingbutton")
        self.movingbutton.setStyleSheet("background-color:pink;border-radius:10%;font-size:20px;")

        self.end_block_1 = QtWidgets.QPushButton(self.centralwidget)
        self.end_block_1.setGeometry(480, 360, 90, 90)
        self.end_block_1.setText("")
        self.end_block_1.setObjectName("end_block_1")
        self.end_block_1.setStyleSheet("background-color:white;border-radius:10%;")

        self.end_block_2 = QtWidgets.QPushButton(self.centralwidget)
        self.end_block_2.setGeometry(610, 360, 90, 90)
        self.end_block_2.setText("")
        self.end_block_2.setObjectName("end_block_2")
        self.end_block_2.setStyleSheet("background-color:white;border-radius:10%;")

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow_()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
