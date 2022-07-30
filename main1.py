import sys
import math
import sympy as sy
import numpy as np
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class Window(QMainWindow):
      
    def __init__(self):
        super().__init__()
    
        self.setWindowTitle("IP Subnet Calculator")
        win_width = 1500
        win_height = 1000
        self.setGeometry(100, 50, win_width, win_height)
        self.setStyleSheet(
            "background-color: #696969;" +
            "border-radius: 50px"

        )
        
        
        grid = QGridLayout() # initializing grid layout
        self.setLayout(grid) # applying grid in window object
        # calling method
        
        self.UiComponents()
  
        # showing all the widgets
        self.show()
        
    def UiComponents(self):
      
        # creating head label
        head = QLabel("Taylor and Maclaurin Series Calculator", self)
        head.setStyleSheet(
                            "color: white;" +
                            "font-size: 45px;" 
                
            
        )
    
        head.setWordWrap(True)
    
        # setting geometry to the head
        head.setGeometry(190, 25, 550, 100)
            
        # setting alignment of the head
        head.setAlignment(Qt.AlignCenter)
            
        
        
        
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
self = Window()
  
# start the app
sys.exit(App.exec())
 