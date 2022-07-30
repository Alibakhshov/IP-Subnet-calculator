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
        
        global result
        
        
        def myIPAddress():
            
            global IP_address
            host_name = socket.gethostname()
            IP_address = socket.gethostbyname(host_name)

            print(IP_address)
            
        ip = str(myIPAddress())
        result.setText(str(ip))
        print(ip)
        
    
    
    
        # creating function to close the window
        def close_window():
            self.close()
        
        # Creating a left frame 
        main_frame = QFrame(self) 
        main_frame.resize(1445, 970)
        main_frame.move(30, 15)
        main_frame.setFrameShape(QFrame.WinPanel)
        main_frame.setFrameShadow(QFrame.Raised)
        main_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
            
        )
        
        # Creating a frame for title
        title_frame = QFrame(main_frame)
        title_frame.resize(1425, 90)
        title_frame.move(10, 15)
        title_frame.setFrameShape(QFrame.WinPanel)
        title_frame.setFrameShadow(QFrame.Raised)
        title_frame.setStyleSheet(
            "background-color: white;"  +
            "border-radius: 25px;"
        )
        
        # Creating a right frame 
        right_vert_frame = QFrame(main_frame)
        right_vert_frame.resize(650, 830)
        right_vert_frame.move(770, 120)
        right_vert_frame.setFrameShape(QFrame.WinPanel)
        right_vert_frame.setFrameShadow(QFrame.Raised)
        right_vert_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
        )
        
        top_horiz_frame = QFrame(main_frame)
        top_horiz_frame.resize(750, 400)
        top_horiz_frame.move(10, 120)
        top_horiz_frame.setFrameShape(QFrame.WinPanel)
        top_horiz_frame.setFrameShadow(QFrame.Raised)
        top_horiz_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
        )
        
        bottom_horiz_frame = QFrame(main_frame)
        bottom_horiz_frame.resize(750, 400)
        bottom_horiz_frame.move(10, 550)
        bottom_horiz_frame.setFrameShape(QFrame.WinPanel)
        bottom_horiz_frame.setFrameShadow(QFrame.Raised)
        bottom_horiz_frame.setStyleSheet(
            "border: 5px solid yellow;" +
            "background-color: white;" +
            "border-radius: 25px;" 
        )
        
        # creating a button to show the IP address
        myIP_button = QPushButton("My IP address", right_vert_frame)
        myIP_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        myIP_button.setStyleSheet(
                                    "*{border: 5px solid '#BC006C';" +
                                    "border-radius: 45px;" +
                                    "color: 'white';" +
                                    "font-size: 20px;}" +
                                    "*:hover{background: '#BC006C';}"           
        ) # setting border style
    
        # setting geometry to the push button
        myIP_button.setGeometry(50, 300, 200, 40)
        # adding action to the button
        myIP_button.clicked.connect(myIPAddress)
        
        
        
    
    
        # creating a button to show the IP address
        exit_button = QPushButton("Exit", right_vert_frame)
        exit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
        exit_button.setStyleSheet(
                                    "*{border: 5px solid '#BC006C';" +
                                    "border-radius: 45px;" +
                                    "color: 'black';" +
                                    "font-size: 20px;}" +
                                    "*:hover{background: '#BC006C';}"           
        ) # setting border style
    
        # setting geometry to the exit button
        exit_button.setGeometry(50, 350, 200, 40)
        exit_button.clicked.connect(close_window)
        
        # Creating a label to show the result
        
        result = QLabel(top_horiz_frame)
        result.setAlignment(Qt.AlignCenter)
        result.setGeometry(90, 210, 800, 60)
        result.setStyleSheet("QLabel"
                                    "{"
                                    "border : 3px solid black;"
                                    "background : white;"
                                    "}")
        result.setFont(QFont('Arial', 11))
        
        
            
            
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
self = Window()
  
# start the app
sys.exit(App.exec())
 