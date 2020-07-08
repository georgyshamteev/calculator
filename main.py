import sys
import math
from decimal import Decimal
from PySide2 import QtWidgets
from test import Ui_Calculator

app = QtWidgets.QApplication(sys.argv)


class Calculator(QtWidgets.QMainWindow, Ui_Calculator):
    # Конструктор класса
    list_of_operations = [0]
    list_of_numbers = [0]

    def __init__(self):
        super().__init__()

        # Создание формы и Ui
        self.setupUi(self)
        # Показать окно
        self.show()
        self.setWindowTitle("Калькулятор")
        self.lineEdit_2.clear()
        self.pushButton_1.clicked.connect(self.one_divide_by_x)  # 1/x
        self.pushButton_2.clicked.connect(self.x_pow_y)  # x^y
        self.pushButton_3.clicked.connect(self.clear_all)  # clear
        self.pushButton_4.clicked.connect(self.delete_last_symbol)  # delete_last_symbol
        self.pushButton_5.clicked.connect(self.factorial)  # !
        self.pushButton_6.clicked.connect(self.square)  # в квадрате
        self.pushButton_7.clicked.connect(self.sqrt)  # корень квадратный
        self.pushButton_8.clicked.connect(self.divide)  # /
        self.pushButton_9.clicked.connect(self.digit_pressed)  # 1
        self.pushButton_10.clicked.connect(self.digit_pressed)  # 2
        self.pushButton_11.clicked.connect(self.digit_pressed)  # 3
        self.pushButton_12.clicked.connect(self.multiply)  # *
        self.pushButton_13.clicked.connect(self.digit_pressed)  # 4
        self.pushButton_14.clicked.connect(self.digit_pressed)  # 5
        self.pushButton_15.clicked.connect(self.digit_pressed)  # 6
        self.pushButton_16.clicked.connect(self.subtract)  # --
        self.pushButton_17.clicked.connect(self.digit_pressed)  # 7
        self.pushButton_18.clicked.connect(self.digit_pressed)  # 8
        self.pushButton_19.clicked.connect(self.digit_pressed)  # 9
        self.pushButton_20.clicked.connect(self.add)  # +
        self.pushButton_21.clicked.connect(self.print_pi)  # П
        self.pushButton_22.clicked.connect(self.digit_pressed)  # 0
        self.pushButton_23.clicked.connect(self.put_comma)  # ,
        self.pushButton_24.clicked.connect(self.equals)  # ==

        self.lineEdit.setText("0")

    def digit_pressed(self):
        button = self.sender()
        if self.lineEdit.text() == '0':
            self.lineEdit.setText(button.text())
        elif self.lineEdit.text() == "Cannot divide by zero":
            self.lineEdit.clear()
            self.lineEdit.setText(button.text())
        else:
            self.lineEdit.setText(self.lineEdit.text() + button.text())

    def clear_all(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.list_of_numbers.clear()
        self.list_of_numbers = [0]
        self.list_of_operations.clear()
        self.list_of_operations = [0]
        self.lineEdit.setText("0")

    def square(self):
        a = self.lineEdit.text()
        b = Decimal(a) ** 2
        self.lineEdit_2.setText("sqr(" + a + ")")
        self.lineEdit.setText(str(b))

    def sqrt(self):
        a = self.lineEdit.text()
        b = math.sqrt(Decimal(a))
        self.lineEdit_2.setText("√(" + a + ")")
        self.lineEdit.setText(str(b))

    def factorial(self):
        a = self.lineEdit.text()
        b = math.factorial(int(a))
        self.lineEdit_2.setText("!" + a)
        self.lineEdit.setText(str(b))

    def one_divide_by_x(self):
        a = self.lineEdit.text()
        if Decimal(a) == 0:
            self.lineEdit_2.setText("1/(" + a + ")")
            self.lineEdit.setText("Cannot divide by zero")
        else:
            self.lineEdit_2.setText("1/(" + a + ")")
            self.lineEdit.setText(str(1 / Decimal(a)))

    def print_pi(self):
        self.lineEdit.setText("3.14")

    def delete_last_symbol(self):
        a = self.lineEdit.text()
        self.lineEdit.setText(a[:-1])

    def put_comma(self):
        a = self.lineEdit.text()
        for letter in a:
            if letter == ".":
                return
        b = a + "."
        self.lineEdit.setText(b)

    def add(self):
        if self.list_of_operations[-1] == 0:
            a = Decimal(self.lineEdit.text())
            b = "plus"
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " + ")
        elif self.list_of_operations[-1] == "plus":
            a = Decimal(self.lineEdit.text())
            b = "plus"
            a += self.list_of_numbers[-1]
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " + ")
        elif self.list_of_operations[-1] == "minus":
            a = Decimal(self.lineEdit.text())
            b = "plus"
            a = self.list_of_numbers[-1] - a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " + ")
        elif self.list_of_operations[-1] == "division":
            a = Decimal(self.lineEdit.text())
            b = "plus"
            a = self.list_of_numbers[-1] / a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " + ")
        elif self.list_of_operations[-1] == "multiplication":
            a = Decimal(self.lineEdit.text())
            b = "plus"
            a = self.list_of_numbers[-1] * a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " + ")

    def subtract(self):
        if self.list_of_operations[-1] == 0:
            a = Decimal(self.lineEdit.text())
            b = "minus"
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " - ")
        elif self.list_of_operations[-1] == "plus":
            a = Decimal(self.lineEdit.text())
            b = "minus"
            a += self.list_of_numbers[-1]
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " - ")
        elif self.list_of_operations[-1] == "minus":
            a = Decimal(self.lineEdit.text())
            b = "minus"
            a = self.list_of_numbers[-1] - a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " - ")
        elif self.list_of_operations[-1] == "division":
            a = Decimal(self.lineEdit.text())
            b = "minus"
            a = self.list_of_numbers[-1] / a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " - ")
        elif self.list_of_operations[-1] == "multiplication":
            a = Decimal(self.lineEdit.text())
            b = "minus"
            a = self.list_of_numbers[-1] * a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " - ")

    def divide(self):
        if self.list_of_operations[-1] == 0:
            a = Decimal(self.lineEdit.text())
            if a == 0:
                self.lineEdit_2.setText(str(a) + " / ")
                self.lineEdit.setText("Cannot divide by zero")
            else:
                b = "division"
                self.lineEdit.clear()
                self.list_of_numbers.append(a)
                self.list_of_operations.append(b)
                self.lineEdit_2.setText(str(a) + " / ")
        elif self.list_of_operations[-1] == "plus":
            a = Decimal(self.lineEdit.text())
            if a == 0:
                self.lineEdit_2.setText(str(a) + " / ")
                self.lineEdit.setText("Cannot divide by zero")
            else:
                b = "division"
                a += self.list_of_numbers[-1]
                self.lineEdit.clear()
                self.list_of_numbers.append(a)
                self.list_of_operations.append(b)
                self.lineEdit_2.setText(str(a) + " / ")
        elif self.list_of_operations[-1] == "minus":
            a = Decimal(self.lineEdit.text())
            if a == 0:
                self.lineEdit_2.setText(str(a) + " / ")
                self.lineEdit.setText("Cannot divide by zero")
            else:
                b = "division"
                a = self.list_of_numbers[-1] - a
                self.lineEdit.clear()
                self.list_of_numbers.append(a)
                self.list_of_operations.append(b)
                self.lineEdit_2.setText(str(a) + " / ")
        elif self.list_of_operations[-1] == "division":
            a = Decimal(self.lineEdit.text())
            if a == 0:
                self.lineEdit_2.setText(str(a) + " / ")
                self.lineEdit.setText("Cannot divide by zero")
            else:
                b = "division"
                a = self.list_of_numbers[-1] / a
                self.lineEdit.clear()
                self.list_of_numbers.append(a)
                self.list_of_operations.append(b)
                self.lineEdit_2.setText(str(a) + " / ")
        elif self.list_of_operations[-1] == "multiplication":
            a = Decimal(self.lineEdit.text())
            if a == 0:
                self.lineEdit_2.setText(str(a) + " / ")
                self.lineEdit.setText("Cannot divide by zero")
            else:
                b = "division"
                a = self.list_of_numbers[-1] * a
                self.lineEdit.clear()
                self.list_of_numbers.append(a)
                self.list_of_operations.append(b)
                self.lineEdit_2.setText(str(a) + " / ")

    def multiply(self):
        if self.list_of_operations[-1] == 0:
            a = Decimal(self.lineEdit.text())
            b = "multiplication"
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " * ")
        elif self.list_of_operations[-1] == "plus":
            a = Decimal(self.lineEdit.text())
            b = "multiplication"
            a += self.list_of_numbers[-1]
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " * ")
        elif self.list_of_operations[-1] == "minus":
            a = Decimal(self.lineEdit.text())
            b = "multiplication"
            a = self.list_of_numbers[-1] - a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " * ")
        elif self.list_of_operations[-1] == "division":
            a = Decimal(self.lineEdit.text())
            b = "multiplication"
            a = self.list_of_numbers[-1] / a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " * ")
        elif self.list_of_operations[-1] == "multiplication":
            a = Decimal(self.lineEdit.text())
            b = "multiplication"
            a = self.list_of_numbers[-1] * a
            self.lineEdit.clear()
            self.list_of_numbers.append(a)
            self.list_of_operations.append(b)
            self.lineEdit_2.setText(str(a) + " * ")

    def x_pow_y(self):
        a = Decimal(self.lineEdit.text())
        b = "pow"
        self.lineEdit.clear()
        self.list_of_numbers.append(a)
        self.list_of_operations.append(b)
        self.lineEdit_2.setText(str(a) + "^")

    def equals(self):
        a = Decimal(self.lineEdit.text())
        if self.list_of_operations[-1] == "plus":
            self.lineEdit.setText(str(self.list_of_numbers[-1] + a))
            self.list_of_operations.append("equals")
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(str(self.list_of_numbers[-1]) + " + " + str(a))
            self.list_of_numbers.append(a)
        elif self.list_of_operations[-1] == "minus":
            self.lineEdit.setText(str(self.list_of_numbers[-1] - a))
            self.list_of_operations.append("equals")
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(str(self.list_of_numbers[-1]) + " - " + str(a))
            self.list_of_numbers.append(a)
        elif self.list_of_operations[-1] == "division":
            if a == 0:
                self.lineEdit.setText("Cannot divide by zero")
            else:
                self.lineEdit.setText(str(self.list_of_numbers[-1] / a))
                self.list_of_operations.append("equals")
                self.lineEdit_2.clear()
                self.lineEdit_2.setText(str(self.list_of_numbers[-1]) + " / " + str(a))
                self.list_of_numbers.append(a)
        elif self.list_of_operations[-1] == "multiplication":
            self.lineEdit.setText(str(self.list_of_numbers[-1] * a))
            self.list_of_operations.append("equals")
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(str(self.list_of_numbers[-1]) + " * " + str(a))
            self.list_of_numbers.append(a)
        elif self.list_of_operations[-1] == "pow":
            self.lineEdit.setText(str(self.list_of_numbers[-1] ** a))
            self.list_of_operations.append("equals")
            self.lineEdit_2.clear()
            self.lineEdit_2.setText(str(self.list_of_numbers[-1]) + " ** " + str(a))
            self.list_of_numbers.append(a)
        elif self.list_of_operations[-1] == "equals":
            a = Decimal(self.lineEdit.text())
            if self.list_of_operations[-2] == "plus":
                self.lineEdit.setText(str(self.list_of_numbers[-1] + a))
                self.lineEdit_2.clear()
                self.lineEdit_2.setText(str(a) + " + " + str(self.list_of_numbers[-1]))
            elif self.list_of_operations[-2] == "minus":
                self.lineEdit.setText(str(a - self.list_of_numbers[-1]))
                self.lineEdit_2.clear()
                self.lineEdit_2.setText(str(a) + " - " + str(self.list_of_numbers[-1]))
            elif self.list_of_operations[-2] == "division":
                if a == 0:
                    self.lineEdit.setText("Cannot divide by zero")
                else:
                    self.lineEdit.setText(str(a / self.list_of_numbers[-1]))
                    self.lineEdit_2.clear()
                    self.lineEdit_2.setText(str(a) + " / " + str(self.list_of_numbers[-1]))
            elif self.list_of_operations[-2] == "multiplication":
                self.lineEdit.setText(str(a * self.list_of_numbers[-1]))
                self.lineEdit_2.clear()
                self.lineEdit_2.setText(str(a) + " * " + str(self.list_of_numbers[-1]))
            elif self.list_of_operations[-2] == "pow":
                self.lineEdit.setText(str(a ** self.list_of_numbers[-1]))
                self.lineEdit_2.clear()
                self.lineEdit_2.setText(str(a) + " ** " + str(self.list_of_numbers[-1]))
            else:
                self.lineEdit.setText("err")
        else:
            self.lineEdit.setText("err")


# Сздание инстанса класса Калькулятор, который мы создадим далее
calc = Calculator()
# Запуск
sys.exit(app.exec_())
