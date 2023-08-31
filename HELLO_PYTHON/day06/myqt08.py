import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("./myqt08.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
    def getstar(self,cnt):
        ret=""
        
        for i in range(cnt):
            ret+= "*"
        ret+="\n"
        return ret
        
                
    def btnClick(self):
        
        a=self.le_first.text()
        aa=int(a)
        
        b=self.le_last.text()
        bb=int(b)
        
        txt=""
        
        for i in range(aa,bb+1):
            txt+=self.getstar(i)  
        

        self.te.setText(txt)
        

       
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()