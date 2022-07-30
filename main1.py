import sys
import math

import sympy as sy
import numpy as np
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import socket

class Window(QMainWindow):
      
    def __init__(self):
        super().__init__()
        global result
        
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
        
        self.MainWindow()
  
        # showing all the widgets
        self.show()
        
    def MainWindow(self):
        
    
        
        
        
        
        # Creating a left frame 
        self.main_frame = QFrame(self) 
        self.main_frame.resize(1445, 970)
        self.main_frame.move(30, 15)
        self.main_frame.setFrameShape(QFrame.WinPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.main_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
            
        )
        
        # Creating a frame for title
        self.title_frame = QFrame(self.main_frame)
        self.title_frame.resize(1425, 90)
        self.title_frame.move(10, 15)
        self.title_frame.setFrameShape(QFrame.WinPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.title_frame.setStyleSheet(
            "background-color: white;"  +
            "border-radius: 25px;"
        )
        
        # Creating a right frame 
        self.right_vert_frame = QFrame(self.main_frame)
        self.right_vert_frame.resize(650, 830)
        self.right_vert_frame.move(770, 120)
        self.right_vert_frame.setFrameShape(QFrame.WinPanel)
        self.right_vert_frame.setFrameShadow(QFrame.Raised)
        self.right_vert_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
        )
        
        self.top_horiz_frame = QFrame(self.main_frame)
        self.top_horiz_frame.resize(750, 400)
        self.top_horiz_frame.move(10, 120)
        self.top_horiz_frame.setFrameShape(QFrame.WinPanel)
        self.top_horiz_frame.setFrameShadow(QFrame.Raised)
        self.top_horiz_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
        )
        
        self.bottom_horiz_frame = QFrame(self.main_frame)
        self.bottom_horiz_frame.resize(750, 400)
        self.bottom_horiz_frame.move(10, 550)
        self.bottom_horiz_frame.setFrameShape(QFrame.WinPanel)
        self.bottom_horiz_frame.setFrameShadow(QFrame.Raised)
        self.bottom_horiz_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
        )
        
        # creating a button to show the IP address
        self.myIP_button = QPushButton("My IP address", self.right_vert_frame)
        self.myIP_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        self.myIP_button.setStyleSheet(
                                    "*{border: 5px solid '#BC006C';" +
                                    "border-radius: 45px;" +
                                    "color: 'white';" +
                                    "font-size: 20px;}" +
                                    "*:hover{background: '#BC006C';}"           
        ) # setting border style
    
        # setting geometry to the push button
        self.myIP_button.setGeometry(50, 300, 200, 40)
        # adding action to the button
        
        
        
        
    
    
        # creating a button to show the IP address
        self.exit_button = QPushButton("Exit", self.right_vert_frame)
        self.exit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        self.exit_button.setStyleSheet(
                                    "*{border: 5px solid '#BC006C';" +
                                    "border-radius: 45px;" +
                                    "color: 'black';" +
                                    "font-size: 20px;}" +
                                    "*:hover{background: '#BC006C';}"           
        ) # setting border style
    
        # setting geometry to the exit button
        self.exit_button.setGeometry(50, 350, 200, 40)
        
        
        # Creating a label to show the result
        
        self.result = QLabel(self.top_horiz_frame)
        self.result.setAlignment(Qt.AlignCenter)
        self.result.setGeometry(90, 210, 800, 60)
        self.result.setStyleSheet("QLabel"
                                    "{"
                                    "border : 3px solid black;"
                                    "background : white;"
                                    "}")
        self.result.setFont(QFont('Arial', 11))
        
        def myIPAddress():
            
            
            host_name = socket.gethostname()
            IP_address = socket.gethostbyname(host_name)

            print(IP_address)
            self.result.setText(IP_address)
            
    
        
    
    
    
        # creating function to close the window
        def close_window(self):
            self.close()
        
        self.myIP_button.clicked.connect(myIPAddress)
        self.exit_button.clicked.connect(close_window)
            
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
self = Window()
  
# start the app
sys.exit(App.exec())
 