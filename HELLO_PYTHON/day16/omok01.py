import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QPushButton, QSize, QIcon
from prompt_toolkit.contrib.telnet.protocol import SE
from future.backports.xmlrpc.client import boolean
from conda.common._logic import TRUE

form_class = uic.loadUiType("./omok01.ui")[0]

class MainClass(QMainWindow, form_class):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.arr =[]
        self.flag_wb = True

        
        for i in range(10):
            for j in range(10):
                lego = QPushButton('', self)
                lego.setIcon(QtGui.QIcon('0.png'))
                lego.setGeometry(i*40 , j*40, 40, 40)
                lego.setIconSize(QSize(40, 40)) 
                lego.clicked.connect(self.myClick)  
                self.arr.append(lego)     

        self.show()
        self.pb.clicked.connect(self.myClick)

        
    def myClick(self):
        print("myClick")
        
        if self.flag_wb:
            self.sender().setIcon(QtGui.QIcon('1.png'))
        else:
            self.sender().setIcon(QtGui.QIcon('2.png'))
        self.flag_wb = not self.flag_wb
        
          
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = MainClass()
    app.exec_()
    

