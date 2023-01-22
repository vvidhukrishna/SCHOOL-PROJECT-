from PyQt5.QtGui import *
from PyQt5 import QtGui, QtWidgets
from task_1 import Ui_MainWindow_
from task_2 import Ui_MainWindow__


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

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 720)
        MainWindow.setWindowTitle("MAIN WINDOW")
        MainWindow.setWindowIcon(QtGui.QIcon('Pc_builder_logo.ico'))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(270, 560, 101, 41)
        self.pushButton.setObjectName("Task 1 ")
        self.pushButton.clicked.connect(self.task__1)
        self.pushButton.clicked.connect(MainWindow.close)

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(910, 560, 101, 41)
        self.pushButton_2.setStyleSheet("background-color:#42f5e0;border-radius:10%")
        self.pushButton.setStyleSheet("background-color:#42f5e0;border-radius:10%")
        self.pushButton_2.setObjectName("Task 2")
        self.pushButton_2.clicked.connect(self.task__2)
        self.pushButton_2.clicked.connect(MainWindow.close)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(0, 0, 1280, 720)
        self.label.setText("")
        self.label.setPixmap(QPixmap("main_background.jpeg"))
        self.label.setObjectName("label")

        self.pushButton.raise_()
        self.pushButton_2.raise_()
        self.pushButton.setText("TASK 1 ")
        self.pushButton_2.setText("TASK 2")

        MainWindow.setCentralWidget(self.centralwidget)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
