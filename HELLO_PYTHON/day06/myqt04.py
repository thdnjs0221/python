import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from _random import Random

form_class = uic.loadUiType("myqt03.ui")[0] 

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
        
    def myclick(self):
        
        a=self.leMine.text()
        com="";
        b = random()
        result="";
        
        if b>0.66:
            com="가위"
        elif b>0.33:
            com="바위"
        else :
            com="보"  
    
        if a=="가위" and com=="가위":
            result="비김"
        elif a=="가위" and com=="바위":
            result="졌음"
        elif a=="가위" and com=="보":
            result="이김"
        elif a=="바위" and com=="가위":
            result="이김"
        elif a=="바위" and com=="바위":
            result="비김"
        elif a=="바위" and com=="보":
            result="졌음"
        elif a=="보" and com=="보":
            result="비김"
        elif a=="보" and com=="가위":
            result="졌음"
        elif a=="보" and com=="바위":
            result="이김"

        self.leCom.setText(com)
        self.leResult.setText(result)
        
        self.lineEdit_search.returnPressed.connect(self.inquire_list_func)
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()