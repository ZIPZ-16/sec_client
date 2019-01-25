import sys
from PyQt5.QtCore import  pyqtSlot
from PyQt5.QtWidgets import QMainWindow,QApplication,QLineEdit,QLabel,QTextEdit,QGridLayout,QPushButton,QHBoxLayout,QVBoxLayout,QFormLayout


class NewWindow(QMainWindow):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(NewWindow, self).__init__()
        self.initUI()

    def initUI(self):
        b1 = QPushButton("Button1")
        b2 = QPushButton("Button2")

        self.lab = QLabel("Введите код подтверждения который был отправлен вам на почту",self)
        self.subm = QPushButton('Submit',self)
        self.textbox = QLineEdit(self)
        self.textbox.move(10, 10)
        self.textbox.resize(480, 280)
        self.lab.move(50,300)
        self.lab.resize(400,50)
        self.subm.move(200,360)
        mainLayout = QVBoxLayout()
        mainLayout.addWidget(b1)
        mainLayout.addWidget(b2)
        self.setLayout(mainLayout)
        self.setGeometry(500, 500, 500, 500)
        self.setWindowTitle('Absolute')
        self.show()

class Example(QMainWindow):
    ##################################
    def getx(self): return self.__addwin
    def setx(self, value): self.__addwin = value
    def delx(self): del self.__addwin
    addwin = property(getx, setx, delx, "Свойство 'addwin'.")

    def getx(self): return self.__addwin2
    def setx(self, value): self.__addwin2 = value
    def delx(self): del self.__addwin2
    addwin2 = property(getx, setx, delx, "Свойство 'addwin2'.")
    ################################################
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        self.bqt = QPushButton('Login',self)
        self.login = QLabel('Login',self)
        self.password = QLabel('Password',self)
        self.loginIn = QLineEdit(self)
        self.passIn = QLineEdit(self)
        self.login.move(250,10)
        self.password.move(240,100)
        self.loginIn.move(220,50)
        self.passIn.move(220,140)
        self.bqt.move(220,200)
        self.setGeometry(300, 300, 550, 300)
        self.setWindowTitle('Review')
        self.show()
        self.bqt.clicked.connect(self.addwindow)
    @pyqtSlot()
    def addwindow(self):
        self.addwin = NewWindow()

def main():
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()