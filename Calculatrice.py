from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, \
    QHBoxLayout, QVBoxLayout, QGridLayout, QTextEdit, QLineEdit
import sys

# QApplication is the application handler
app = QApplication(sys.argv)

# Create an instance of a QWidget in the variable window
window = QWidget()
window.setWindowTitle("Calculatrice")
window.setGeometry(1300, 300, 200, 300)


# Grid for the calculator key
grid = QGridLayout()
window.setLayout(grid)

screen = QTextEdit()
grid.addWidget(screen, 0, 0, 1, 4)
# screen.setFixedWidth(200)


def zero():
    screen.setPlainText("0")

button0 = QPushButton("0")
grid.addWidget(button0, 4, 0)
button0.clicked.connect(zero)


def one():
    screen.setPlainText("1")

button1 = QPushButton("1")
grid.addWidget(button1, 3, 0)
button1.clicked.connect(one)


def two():
    screen.setPlainText("2")

button2 = QPushButton("2")
grid.addWidget(button2, 3, 1)
button2.clicked.connect(two)


def three():
    screen.setPlainText("3")

button3 = QPushButton("3")
grid.addWidget(button3, 3, 2)
button3.clicked.connect(three)


def four():
    screen.setPlainText("4")

button4 = QPushButton("4")
grid.addWidget(button4, 2, 0)
button4.clicked.connect(four)


def five():
    screen.setPlainText("5")

button5 = QPushButton("5")
grid.addWidget(button5, 2, 1)
button5.clicked.connect(five)


def six():
    screen.setPlainText("6")

button6 = QPushButton("6")
grid.addWidget(button6, 2, 2)
button6.clicked.connect(six)


def seven():
    screen.setPlainText("7")

button7 = QPushButton("7")
grid.addWidget(button7, 1, 0)
button7.clicked.connect(seven)


def eight():
    screen.setPlainText("8")

button8 = QPushButton("8")
grid.addWidget(button8, 1, 1)
button8.clicked.connect(eight)


def nine():
    screen.setPlainText("9")

button9 = QPushButton("9")
grid.addWidget(button9, 1, 2)
button9.clicked.connect(nine)


def point():
    screen.setPlainText(".")

button_point = QPushButton(".")
grid.addWidget(button_point, 4, 1)
button_point.clicked.connect(point)



# grid.addWidget(QPushButton("1"), 3, 0)
# grid.addWidget(QPushButton("2"), 3, 1)
# grid.addWidget(QPushButton("3"), 3, 2)
# grid.addWidget(QPushButton("4"), 2, 0)
# grid.addWidget(QPushButton("5"), 2, 1)
# grid.addWidget(QPushButton("6"), 2, 2)
# grid.addWidget(QPushButton("7"), 1, 0)
# grid.addWidget(QPushButton("8"), 1, 1)
# grid.addWidget(QPushButton("9"), 1, 2)
# grid.addWidget(QPushButton("."), 4, 1)
grid.addWidget(QPushButton("="), 4, 2)
grid.addWidget(QPushButton("+"), 4, 3)
grid.addWidget(QPushButton("-"), 3, 3)
grid.addWidget(QPushButton("*"), 2, 3)
grid.addWidget(QPushButton("/"), 1, 3)


# Create the textBox and set plain text

# .clicked.connect(btnPress1_Clicked)

window.show()

# Execute la runloop
app.exec_()

# Stop the runloop
# sys.exit(app.exec_())

# print([(i, j) for i in range(5) for j in range(4)])