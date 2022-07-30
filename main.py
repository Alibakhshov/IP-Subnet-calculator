# importing from packages fromPyQt5

from PyQt5.QtWidgets import QApplication, QWidget, QFrame, QLabel, QPushButton
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import socket

from numpy import int16, str0



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
    
    global result
    
    def myIPAddress():
        
        host_name = socket.gethostname()
        IP_address = socket.gethostbyname(host_name)

        print(IP_address)
        print(host_name)
        result.setText(IP_address)
        
    def myHostName():
        
        host_name = socket.gethostname()
        print(host_name)
        result.setText(host_name)
    
    
    # creating function to close the window
    def close_window():
        app.close()
        
    
    # Creating a left frame 
    main_frame = QFrame(window) 
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
    
    # ip = str(myIPAddress())
    # result.setText(str(myIPAddress()))
    # print(ip)
    
    
    
   
    
    
    # Creating a title for the calculator
    # title = QLabel("IP subnet Calculator", left_frame)
    # title.setStyleSheet(
    #     "color: black;" +
    #     "font-size: 45px;" 
    # )
    # # title.setWordWrap(True)
    # title.setGeometry(500, 25, 550, 40)
    
    # Adding an image
    # image = QLabel(title_frame)
    # # image.setGeometry(30, 120, 50, 40)
    # image.setAlignment(Qt.AlignCenter)
    # pixmap = QPixmap('1.png')
    # image.setPixmap(pixmap)
    
    
    # Window is hidden by default that is why we are showing it
    window.show()
    
   
   
    

# starting up the event loop
app.exec()
