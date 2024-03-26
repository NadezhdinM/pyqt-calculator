class CalculatorLogic:
    def __init__(self, ui):
        self.ui = ui
        self.reset()

    def reset(self):
        self.current_expression = ""
        self.ui.display.setText(self.current_expression)

    def append_number(self, number):
        self.current_expression += number
        self.ui.display.setText(self.current_expression)

    def append_operator(self, operator):
        self.current_expression += operator
        self.ui.display.setText(self.current_expression)

    def clear(self):
        self.reset()

    def calculate(self):
        try:
            result = str(eval(self.current_expression))
            self.ui.display.setText(result)
            self.current_expression = result
        except Exception as e:
            self.ui.display.setText("Ошибка")
            self.current_expression = ""
