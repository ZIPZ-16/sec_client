import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel,QLineEdit, QPushButton,QGridLayout


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        title = QLabel('Login')
        author = QLabel('Password')

        titleEdit = QLineEdit()
        authorEdit = QLineEdit()
        grid = QGridLayout()
        grid.setSpacing(10)
        grid.addWidget(title, 1, 0)
        grid.addWidget(titleEdit, 1, 1)
        grid.addWidget(author, 2, 0)
        grid.addWidget(authorEdit, 2, 1)
        self.setLayout(grid)
        self.btnq = QPushButton("Login", self)
        self.setGeometry(300, 300, 450, 400)
        self.setWindowTitle('Seif')
        self.show()

        self.btnq.clicked.connect(self.ButtonClicked)

    def ButtonClicked(self):
        print("hi")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())