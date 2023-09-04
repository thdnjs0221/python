import sys
from PyQt5 import uic, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.Qt import QIcon



form_class = uic.loadUiType("./my_tetris01.ui")[0]


class WindowClass(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pb.clicked.connect(self.btnClick)
        #self.lbl.clicked.connect(self.btnClick)
        self.lbl.mousePressEvent = self.btnClick  #라벨 클릭

    def btnClick(self,event):
        self.lbl.setPixmap(QtGui.QPixmap("1.png")) 
        self.pb.setIcon(QIcon('1.png'))
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = WindowClass()
    myWindow.show()
    app.exec_()