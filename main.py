import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from calculator_ui import Ui_MainWindow
from calculator_logic import CalculatorLogic

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.logic = CalculatorLogic(self)
        self.setStyleSheet(open("styles.qss", "r").read())
        self.statusBar().showMessage("Готово")

        # Подключаем кнопки
        self.connect_buttons()

    def connect_buttons(self):
        self.button_0.clicked.connect(lambda: self.logic.append_number('0'))
        self.button_1.clicked.connect(lambda: self.logic.append_number('1'))
        self.button_2.clicked.connect(lambda: self.logic.append_number('2'))
        self.button_3.clicked.connect(lambda: self.logic.append_number('3'))
        self.button_4.clicked.connect(lambda: self.logic.append_number('4'))
        self.button_5.clicked.connect(lambda: self.logic.append_number('5'))
        self.button_6.clicked.connect(lambda: self.logic.append_number('6'))
        self.button_7.clicked.connect(lambda: self.logic.append_number('7'))
        self.button_8.clicked.connect(lambda: self.logic.append_number('8'))
        self.button_9.clicked.connect(lambda: self.logic.append_number('9'))

        self.button_add.clicked.connect(lambda: self.logic.append_operator('+'))
        self.button_subtract.clicked.connect(lambda: self.logic.append_operator('-'))
        self.button_multiply.clicked.connect(lambda: self.logic.append_operator('*'))
        self.button_divide.clicked.connect(lambda: self.logic.append_operator('/'))

        self.button_clear.clicked.connect(self.logic.clear)
        self.button_equals.clicked.connect(self.logic.calculate)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
