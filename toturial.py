import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import QMessageBox
from PyQt5 import QtGui, QtWidgets
from task_1 import Ui_MainWindow_


class Ui_MainWindow___(object):
    def __init__(self):
        self.moving_value = 1

    def task__1(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow_()
        self.ui2.setupUi(self.window3)
        self.window3.show()

    def win_message(self):
        msg = QMessageBox()
        msg.setWindowTitle("Victory Box!")
        msg.setText("YOU WON!!!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.buttonClicked.connect(self.reply)
        msg.exec_()

    def reply(self, i):
        if i.text() == 'OK':
            self.task__1()


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
        self.moving_value = round(eval(str(self.moving_value) + '+ 3'))
        print(self.moving_value)
        print(4)
        self.movingbutton.setText(str(self.moving_value))
        self.pushButton1.setEnabled(False)
        if int(self.moving_value) == int('4'):
            self.win_message()

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
        self.req_output_display.setText('4')
        self.req_output_display.setAlignment(Qt.AlignCenter)
        self.req_output_display.setObjectName("req_output_display")
        self.req_output_display.setStyleSheet("background-color:pink;border-radius:10%;font-size:20px")

        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setText("Click + 3 to reach the target")
        self.label_20.setGeometry(630, 40, 361, 91)
        self.label_20.setStyleSheet("font-size:30px;")
        self.label_20.adjustSize()
        self.label_20.font().setBold(True)
        self.label_20.setObjectName("label_20")

        self.startbutton = QtWidgets.QPushButton(self.centralwidget)
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
        self.pushButton1.setText('+ 3')
        self.pushButton1.setObjectName("pushButton1")
        self.pushButton1.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton2.setGeometry(260, 250, 90, 90)
        self.pushButton2.setText('')
        self.pushButton2.setObjectName("pushButton2")
        self.pushButton2.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton3.setGeometry(370, 250, 90, 90)
        self.pushButton3.setText('')
        self.pushButton3.setObjectName("pushButton3")
        self.pushButton3.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton4.setGeometry(150, 360, 90, 90)
        self.pushButton4.setText('')
        self.pushButton4.setObjectName("pushButton4")
        self.pushButton4.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton5.setGeometry(260, 360, 90, 90)
        self.pushButton5.setText("")
        self.pushButton5.setObjectName("pushButton5")
        self.pushButton5.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton6.setGeometry(370, 360, 90, 90)
        self.pushButton6.setText('')
        self.pushButton6.setObjectName("pushButton6")
        self.pushButton6.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton7.setGeometry(150, 470, 90, 90)
        self.pushButton7.setText('')
        self.pushButton7.setObjectName("pushButton7")
        self.pushButton7.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton8.setGeometry(260, 470, 90, 90)
        self.pushButton8.setText('')
        self.pushButton8.setObjectName("pushButton8")
        self.pushButton8.setStyleSheet("background-color:white;border-radius:10%;font-size:20px;")

        self.pushButton9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton9.setGeometry(370, 470, 90, 90)
        self.pushButton9.setText('')
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
    ui = Ui_MainWindow___()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
