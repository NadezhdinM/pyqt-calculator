from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 600)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.display = QtWidgets.QLineEdit(self.centralwidget)
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 0, 0, 1, 4)

        self.button_1 = QtWidgets.QPushButton(self.centralwidget, text="1")
        self.gridLayout.addWidget(self.button_1, 1, 0)

        self.button_2 = QtWidgets.QPushButton(self.centralwidget, text="2")
        self.gridLayout.addWidget(self.button_2, 1, 1)

        self.button_3 = QtWidgets.QPushButton(self.centralwidget, text="3")
        self.gridLayout.addWidget(self.button_3, 1, 2)

        self.button_add = QtWidgets.QPushButton(self.centralwidget, text="+")
        self.gridLayout.addWidget(self.button_add, 1, 3)

        self.button_4 = QtWidgets.QPushButton(self.centralwidget, text="4")
        self.gridLayout.addWidget(self.button_4, 2, 0)

        self.button_5 = QtWidgets.QPushButton(self.centralwidget, text="5")
        self.gridLayout.addWidget(self.button_5, 2, 1)

        self.button_6 = QtWidgets.QPushButton(self.centralwidget, text="6")
        self.gridLayout.addWidget(self.button_6, 2, 2)

        self.button_subtract = QtWidgets.QPushButton(self.centralwidget, text="-")
        self.gridLayout.addWidget(self.button_subtract, 2, 3)

        self.button_7 = QtWidgets.QPushButton(self.centralwidget, text="7")
        self.gridLayout.addWidget(self.button_7, 3, 0)

        self.button_8 = QtWidgets.QPushButton(self.centralwidget, text="8")
        self.gridLayout.addWidget(self.button_8, 3, 1)

        self.button_9 = QtWidgets.QPushButton(self.centralwidget, text="9")
        self.gridLayout.addWidget(self.button_9, 3, 2)

        self.button_multiply = QtWidgets.QPushButton(self.centralwidget, text="*")
        self.gridLayout.addWidget(self.button_multiply, 3, 3)

        self.button_0 = QtWidgets.QPushButton(self.centralwidget, text="0")
        self.gridLayout.addWidget(self.button_0, 4, 0)

        self.button_clear = QtWidgets.QPushButton(self.centralwidget, text="C")
        self.gridLayout.addWidget(self.button_clear, 4, 1)

        self.button_equals = QtWidgets.QPushButton(self.centralwidget, text="=")
        self.gridLayout.addWidget(self.button_equals, 4, 2)

        self.button_divide = QtWidgets.QPushButton(self.centralwidget, text="/")
        self.gridLayout.addWidget(self.button_divide, 4, 3)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Калькулятор"))
