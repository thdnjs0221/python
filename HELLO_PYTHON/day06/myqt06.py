import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from _random import Random

form_class = uic.loadUiType("myqt06.ui")[0] 

class MainClass(QMainWindow, form_class):
    
    def __init__(self) :
       
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pbCall.clicked.connect(self.myclick)
        self.pb1.clicked.connect(self.click1)
       
        
    def myclick(self):
    
        self.pb1.setText
    def click1(self):
        number+= self.le.setText("1")
        
      
        
       
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()