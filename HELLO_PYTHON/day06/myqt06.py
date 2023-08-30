import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QMessageBox

form_class = uic.loadUiType("myqt06.ui")[0] 

class MainClass(QMainWindow, form_class):
    
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()
        self.pbCall.clicked.connect(self.myclick)
        self.pb1.clicked.connect(self.click1)
        self.pb2.clicked.connect(self.click2)
        self.pb3.clicked.connect(self.click3)
        self.pb4.clicked.connect(self.click4)
        self.pb5.clicked.connect(self.click5)
        self.pb6.clicked.connect(self.click6)
        self.pb7.clicked.connect(self.click7)
        self.pb8.clicked.connect(self.click8)
        self.pb9.clicked.connect(self.click9)
        self.pb0.clicked.connect(self.click10)
        self.number = ""  # 전역 변수 대신 인스턴스 변수로 사용
        
    def myclick(self):
        a=self.le.text()
        QMessageBox.about(self,'전화번호 ',a+"\n calling")

    def click1(self):
        self.number += "1"
        self.le.setText(self.number)
        
    def click2(self):
        self.number += "2"
        self.le.setText(self.number)
        
    def click3(self):
        self.number += "3"
        self.le.setText(self.number)
        
    def click4(self):
        self.number += "4"
        self.le.setText(self.number)
             
    def click5(self):
        self.number += "5"
        self.le.setText(self.number)
               
    def click6(self):
        self.number += "6"
        self.le.setText(self.number)
    def click7(self):
        self.number += "7"
        self.le.setText(self.number)
    def click8(self):
        self.number += "8"
        self.le.setText(self.number)
    def click9(self):
        self.number += "9"
        self.le.setText(self.number)
        
    def click10(self):
        self.number += "0"
        self.le.setText(self.number)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainClass()
    myWindow.show()
    app.exec_()
