from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
from PyQt5 import QtGui, QtWidgets
from task_1 import Ui_MainWindow_
from task_2 import Ui_MainWindow__
from toturial import Ui_MainWindow___


class Ui_MainWindow(object):
    def task__1(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow_()
        self.ui.setupUi(self.window2)
        self.window2.show()

    def task__2(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow__()
        self.ui2.setupUi(self.window3)
        self.window3.show()

    def task__3(self):
        self.window4 = QtWidgets.QMainWindow()
        self.ui2 = Ui_MainWindow___()
        self.ui2.setupUi(self.window4)
        self.window4.show()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setWindowTitle("MAIN WINDOW")
        MainWindow.setWindowIcon(QtGui.QIcon('Pc_builder_logo.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(270, 400, 101, 41)
        self.pushButton.setStyleSheet(
            "background-color:#42f5e0;border-radius:10%;font-size: 14px;font-weight: bold;color: #003d69")
        self.pushButton.setObjectName("Easy")
        self.pushButton.clicked.connect(self.task__1)
        self.pushButton.clicked.connect(MainWindow.close)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(905, 400, 101, 41)
        self.pushButton_2.setStyleSheet(
            "background-color:#42f5e0;border-radius:10%;font-size: 14px;font-weight: bold;color: #003d69")
        self.pushButton_2.setObjectName("Hard")
        self.pushButton_2.clicked.connect(self.task__2)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(0, 0, 1280, 720)
        self.label.setText("")
        self.label.setPixmap(QPixmap("main_background.jpeg"))
        self.label.setObjectName("label")

        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton.setText("EASY")
        self.pushButton_2.setText("HARD")

        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(517, 390, 250, 100)
        self.label_1.setText("""
In this quest you will have to match the number in your movable pink tile to that of the white tile on the pillar of answers. You may obtain your target by using the tiles beside you.
        """)
        self.label_1.setStyleSheet("background-color:#037ba7;border-radius:10%;color: white;font-size: 13px;")
        self.label_1.setAlignment(Qt.AlignCenter)
        self.label_1.setWordWrap(True)
        self.label_1.setObjectName("label1")

        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(483, 120, 320, 40)
        self.label_2.setText('WELCOME TO THE TEMPLE OF OPERATIONS')
        self.label_2.setStyleSheet("background-color:#004167;border-radius:10%; font-weight: bold;color: white;font-size: 14px;")
        self.label_2.setAlignment(Qt.AlignCenter)
        self.label_2.setWordWrap(True)
        self.label_2.setObjectName("label1")

        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(523, 510, 101, 41)
        self.pushButton_3.setStyleSheet(
            "background-color:#42f5e0;border-radius:10%; font-weight: bold;color: #003d69;font-size: 14px;")
        self.pushButton_3.setObjectName("Tutorial")
        self.pushButton_3.clicked.connect(self.task__3)
        self.pushButton_3.clicked.connect(MainWindow.close)
        self.pushButton_3.raise_()
        self.pushButton_3.setText("Tutorial")

        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(663, 510, 101, 41)
        self.label_3.setText('GOOD LUCK')
        self.label_3.setStyleSheet(
            "background-color:#42f5e0;border-radius:10%; font-weight: bold;color: #003d69;font-size: 14px;")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)
        self.label_3.setObjectName("label1")

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
