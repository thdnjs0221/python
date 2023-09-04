import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic, QtGui
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.Qt import QMainWindow, QLabel


class Block:
    def __init__(self):
        self.i = 2
        self.j = 5
        self.type = 7
        self.status = 0
    
    def __str__(self):
        return "{}:{}:{}:{}".format(self.i,self.j,self.type,self.status)
        






form_class = uic.loadUiType("./My_Tetris02.ui")[0]

class MyWindow(QMainWindow, form_class):

    def __init__(self):
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.b2D=[
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0]
        ]
        
        
        self.s2D=[
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [4,4,4,4,4,  4,4,4,4,4]
        ]
        
        self.d2D=[
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0],
            [0,0,0,0,0,  0,0,0,0,0]
        ]
        self.l2D= []
        
        self.b = Block()
        
        print("self.b",self.b)
        for i in range(25):
            line = []
            for j in range(10):
                lbl = QLabel(self)
                lbl.setPixmap(QtGui.QPixmap("0.png"))
                lbl.setGeometry(j*31, i*31, 40, 40)
                line.append(lbl)
            self.l2D.append(line)
        
        self.show()        
        self.setB2D()
        self.setD2D()
        self.show2D(self.d2D)
        self.myrender()
        


        
    def myrender(self):  
        for i in range(25):
            for j in range(10):
                if self.d2D[i][j]==0:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("0.png"))
                if self.d2D[i][j]==1:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("1.png"))
                if self.d2D[i][j]==2:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("2.png"))
                if self.d2D[i][j]==3:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("3.png"))
                if self.d2D[i][j]==4:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("4.png"))
                if self.d2D[i][j]==5:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("5.png"))
                if self.d2D[i][j]==6:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("6.png"))
                if self.d2D[i][j]==7:
                    self.l2D[i][j].setPixmap(QtGui.QPixmap("7.png"))

    
    def setB2D(self):
        b = self.b
        if b.type == 7:
            if b.status == 0:
                self.b2D[b.i    ][b.j   ]= b.type
                self.b2D[b.i    ][b.j-1 ]= b.type
                self.b2D[b.i-1  ][b.j   ]= b.type
                self.b2D[b.i    ][b.j+1 ]= b.type
    
    def setD2D(self):   #s2d, b2d , d2d
        for i in range(25):
            for j in range(10):
                if self.b2D[i][j]>0:
                    self.d2D[i][j]=self.b2D[i][j]  
                
                if self.s2D[i][j]>0:
                    self.d2D[i][j]=self.s2D[i][j] 
                    
    
        
    
    def show2D(self,arr2d):
        for i in range(25):
            print(arr2d[i])
            
if __name__ == "__main__":
    app= QApplication(sys.argv)
    window = MyWindow()
    app.exec_()