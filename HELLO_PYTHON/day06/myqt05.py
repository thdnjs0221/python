import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from random import random
from _random import Random

form_class = uic.loadUiType("myqt05.ui")[0] 

class MainClass(QMainWindow, form_class):
    def __init__(self) :
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.show()
        self.pb.clicked.connect(self.myclick)
       
        
    def myclick(self):
        a = self.le.text()
        aa = int(a)
        result=""
        
        for i in range(1,9+1):
            result+= "{}*{}={} \n".format(aa,i,aa*i)
        
        self.td.setText(result)
        
       
        
if __name__ == "__main__" :
    app = QApplication(sys.argv) 
    myWindow = MainClass() 
    myWindow.show()
    app.exec_()
