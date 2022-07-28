# importing from packages fromPyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

from matplotlib.pyplot import title
from sympy import true

app = QApplication(sys.argv)

class MainWindow():
    window = QWidget()
    window.setWindowTitle("IP Subnet Calculator")
    win_width = 1500
    win_height = 1000
    window.setGeometry(100, 50, win_width, win_height)
    window.setStyleSheet(
        "background-color: #696969;" +
        "border-radius: 50px"

    )
    
    
    # Creating a frame for title
    title_frame = QFrame(window)
    title_frame.resize(1450, 90)
    title_frame.move(30, 15)
    title_frame.setFrameShape(QFrame.WinPanel)
    title_frame.setFrameShadow(QFrame.Raised)
    title_frame.setStyleSheet(
        "background-color: white;"  +
        "border-radius: 25px"
    )
    
    # Creating a left frame 
    left_frame = QFrame(window) 
    left_frame.resize(700, 860)
    left_frame.move(30, 120)
    left_frame.setFrameShape(QFrame.WinPanel)
    left_frame.setFrameShadow(QFrame.Raised)
    left_frame.setStyleSheet(
        "background-color: white;"  +
        "border-radius: 25px"
    )
    
    # Creating a right frame 
    right_frame = QFrame(window)
    right_frame.resize(700, 860)
    right_frame.move(770, 120)
    right_frame.setFrameShape(QFrame.WinPanel)
    right_frame.setFrameShadow(QFrame.Raised)
    right_frame.setStyleSheet(
        "background-color: white;" +
        "border-radius: 25px"
    )
    
    # Creating a title for the calculator
    title = QLabel("IP subnet Calculator", title_frame)
    title.setStyleSheet(
        "color: black;" +
        "font-size: 45px;" 
    )
    title.setWordWrap(True)
    title.setGeometry(500, 25, 550, 40)
    
    image = QLabel(left_frame)
    image.setGeometry(50, 205, 50, 40)
    image.setAlignment(Qt.AlignCenter)
    pixmap = QPixmap('1.png')
    image.setPixmap(pixmap)
    
    
    # Window is hidden by default that is why we are showing it
    window.show()
    
   
    

# starting up the event loop
app.exec()
