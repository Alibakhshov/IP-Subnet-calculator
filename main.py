# importing from packages fromPyQt5

from PyQt5.QtWidgets import (
QApplication, 
QWidget,
QFrame, 
QLabel, 
QPushButton,
QLineEdit,)
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import socket
import ipaddress

from numpy import number

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
    global binToDec_input
    global decToBin_input 
    global global_input
    global top_horiz_frame
    global global_label
    global link_local_label
    global result1
    global result2
    global result3
    global result4
    global result5
    global reserved_label
    global multicast_label
    global loopback_label
    
    
    
    
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
        
    def BinToDec():         
        binary_number = int(binToDec_input.text())
        count_bin_num = 0
        while(binary_number > 0):
            count_bin_num = count_bin_num + 1
            binary_number = binary_number // 10
        print("The number of digits in the number are:", count_bin_num)
                    
        if int(binToDec_input.text()) == "" or int(binToDec_input.text()) == '':
            result.setText("Please fill in all \n required entry fields")
            result.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" +
                "color: red;"
            )
        elif count_bin_num > 8:
            result.setText("Binary numbers should \nnot be greater than 8 digits")
            result.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" +
                "color: red;"
            )
        else:
            binary_number = int(binToDec_input.text())
            decimal_value=0
            a = 1
            length = len(str(binary_number))
            for i in range(length):
                reminder = binary_number % 10
                decimal_value = decimal_value + (reminder * a)
                a = a * 2
                binary_number = int(binary_number/10)
            #display the decimal value
            print("Decimal number is  ", decimal_value)
            result.setText(str(decimal_value))
            result.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" 
            )
    def DecToBin():
        
        if int(decToBin_input.text()) == '':
            result.setText("Please fill in all \n required entry fields")
        else:
            dec_number = int(decToBin_input.text())
            dec_result = (bin(dec_number)[2:])
            result.setText(str(dec_result))
            
    def globalFind():
        
        
        
        # global_label.setStyleSheet(
        #     "background-color: white;" +
        #     "border-color: white;" + 
        #     "font: 35px;"
        # )
        ip = ipaddress.IPv4Address(global_input.text())
        result.setText(str(ip.is_global))
        result1.setText(str(ip.is_link_local))
        result2.setText(str(ip.is_reserved))
        result3.setText(str(ip.is_multicast))
        result4.setText(str(ip.is_loopback))
        global_label.setText("Is global: ")
        link_local_label.setText("Is link local: ")
        reserved_label.setText("Is reserved: ")
        multicast_label.setText("Is multicast: ")
        loopback_label.setText("Is loopback")
        # result.setText("Is global: \n")
        
        # result.setText(str(ip.is_link_local))
        # print("Is global:", ip.is_global)
        # print("Is link-local:", ip.is_link_local)
            
    def Clear():
        decToBin_input.setText('')
        binToDec_input.setText('')
        global_input.setText('')
        result.setText('')
    
    # creating function to close the window
    def close_window():
        app.close()
        
#------------------------------------------------------FRAMES--------------------------------    
    # Creating a left frame 
    main_frame = QFrame(window) 
    main_frame.resize(1445, 970)
    main_frame.move(30, 15)
    main_frame.setFrameShape(QFrame.WinPanel)
    main_frame.setFrameShadow(QFrame.Raised)
    main_frame.setStyleSheet(
        "border: 5px solid #2F4F4F;" +
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
        "border: 5px solid #2F4F4F;" +
        "background-color: white;" +
        "border-radius: 25px;" 
    )
    
    # Creating a right frame 
    right_vert_frame = QFrame(main_frame)
    right_vert_frame.resize(650, 830)
    right_vert_frame.move(770, 120)
    right_vert_frame.setFrameShape(QFrame.WinPanel)
    right_vert_frame.setFrameShadow(QFrame.Raised)
    right_vert_frame.setStyleSheet(
        "border: 5px solid #2F4F4F;" +
        "background-color: white;" +
        "border-radius: 25px;" 
    )
    
    top_horiz_frame = QFrame(main_frame)
    top_horiz_frame.resize(750, 400)
    top_horiz_frame.move(10, 120)
    top_horiz_frame.setFrameShape(QFrame.WinPanel)
    top_horiz_frame.setFrameShadow(QFrame.Raised)
    top_horiz_frame.setStyleSheet(
        "border: 5px solid #2F4F4F;" +
        "background-color: white;" +
        "border-radius: 25px;"  
    )
    
    bottom_horiz_frame = QFrame(main_frame)
    bottom_horiz_frame.resize(750, 400)
    bottom_horiz_frame.move(10, 550)
    bottom_horiz_frame.setFrameShape(QFrame.WinPanel)
    bottom_horiz_frame.setFrameShadow(QFrame.Raised)
    bottom_horiz_frame.setStyleSheet(
        "border: 5px solid #2F4F4F;" +
        "background-color: white;" +
        "border-radius: 25px;" 
    )
    
    #----------------------------------------------------BUTTONS--------------------------------------
    
    # creating a button to show the IP address
    myIP_button = QPushButton("My IP address", right_vert_frame)
    myIP_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    myIP_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"           
    ) # setting border style
    myIP_button.setGeometry(50, 300, 200, 40)
    myIP_button.clicked.connect(myIPAddress)
    
    # creating a button to show the hostname
    myHostName_button = QPushButton("My hostname", right_vert_frame)
    myHostName_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    myHostName_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"            
    ) # setting border style
    myHostName_button.setGeometry(50, 350, 200, 40)
    myHostName_button.clicked.connect(myHostName)
    
    # creating a button to convert binary to decimal
    binToDec_button = QPushButton("To Decimal", right_vert_frame)
    binToDec_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    binToDec_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"            
    ) # setting border style
    binToDec_button.setGeometry(50, 450, 200, 40)
    binToDec_button.clicked.connect(BinToDec)
    
    # creating a button to convert decimal to binary
    DecToBin_button = QPushButton("To Binary", right_vert_frame)
    DecToBin_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    DecToBin_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"            
    ) # setting border style
    DecToBin_button.setGeometry(50, 500, 200, 40)
    DecToBin_button.clicked.connect(DecToBin)
    
    # creating a button to clear all the inputs
    clear_button = QPushButton("Clear", right_vert_frame)
    clear_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    clear_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"            
    ) # setting border style
    clear_button.setGeometry(50, 550, 200, 40)
    clear_button.clicked.connect(Clear)
    
    # creating a button to find whether the IP is global or not. If it is global it prints True
    global_button = QPushButton("Global", right_vert_frame)
    global_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    global_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"            
    ) # setting border style
    global_button.setGeometry(50, 600, 200, 40)
    global_button.clicked.connect(globalFind)
    
    # creating a button to exit the program
    exit_button = QPushButton("Exit", right_vert_frame)
    exit_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    exit_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"                                 
    ) # setting border style
    exit_button.setGeometry(50, 400, 200, 40)
    exit_button.clicked.connect(close_window)
     
    #----------------------------------------------LABELS-------------------------------------- 
     
    
     
    # Creating a label to show the result
    result = QLabel(top_horiz_frame)
    # result.setAlignment(Qt.AlignCenter)
    result.setGeometry(150, 10, 300, 50)
    result.setStyleSheet(
        "background-color: white;" +
        "border-color: black;" + 
        "font: 30px;"
    )
    result.setFont(QFont('Arial', 11))
    
    # Creating a label to show the result of link local
    result1 = QLabel(top_horiz_frame)
    result1.setGeometry(185, 65, 300, 50)
    result1.setStyleSheet(
        "background-color: white;" +
        "border-color: black;" + 
        "font: 30px;"
    )
    result1.setFont(QFont('Arial', 11))
    
    
    # Creating a label to show whether the given IP address is reserved or not
    result2 = QLabel(top_horiz_frame)
    result2.setGeometry(185, 110, 300, 50)
    result2.setStyleSheet(
        "background-color: white;" +
        "border-color: black;" + 
        "font: 30px;"
    )
    result2.setFont(QFont('Arial', 11))
    
    # Creating a label to show whether the given IP address is multicast or not
    result3 = QLabel(top_horiz_frame)
    result3.setGeometry(185, 165, 300, 50)
    result3.setStyleSheet(
        "background-color: white;" +
        "border-color: black;" + 
        "font: 30px;"
    )
    result3.setFont(QFont('Arial', 11))
    
    # Creating a label to for converting binary to decimal
    binToDec_label = QLabel("Enter binary number", bottom_horiz_frame)
    binToDec_label.setGeometry(5, 5, 500, 100)
    binToDec_label.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 35px;"
    )
    # decToBin_label.setFont(QFont('Arial', 11))
    
     # Creating a label to for converting decimal to binary
    decToBin_label = QLabel("Enter decimal number", bottom_horiz_frame)
    decToBin_label.setGeometry(5, 80, 500, 100)
    decToBin_label.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 35px;"
    )
    
    # prints Is global on the top horizontal frame
    global_label = QLabel(top_horiz_frame)
    global_label.setGeometry(10, 10, 140, 50) 
    global_label.setStyleSheet(
            "background-color: white;" +
            "border-color: black;" + 
            "font: 30px;"
    )
    
    # prints Is link local on the top horizontal frame
    link_local_label = QLabel(top_horiz_frame)
    link_local_label.setGeometry(10, 65, 175, 50) 
    link_local_label.setStyleSheet(
            "background-color: white;" +
            "border-color: black;" + 
            "font: 30px;"
    )
    
    # prints Is reserved on the top horizontal frame
    reserved_label = QLabel(top_horiz_frame)
    reserved_label.setGeometry(10, 110, 175, 50) 
    reserved_label.setStyleSheet(
            "background-color: white;" +
            "border-color: black;" + 
            "font: 30px;"
    )
    
    # prints Is multicast on the top horizontal frame
    multicast_label = QLabel(top_horiz_frame)
    multicast_label.setGeometry(10, 165, 175, 50) 
    multicast_label.setStyleSheet(
            "background-color: white;" +
            "border-color: black;" + 
            "font: 30px;"
    )
    
    #-----------------------------------------------INPUTS-------------------------------------------
    
    # creating an input space for converting binary to decimal
    binToDec_input = QLineEdit(bottom_horiz_frame)
    binToDec_input.setStyleSheet(
        "font: 25px;" +
        "border-radius: 0px;"
    )
    binToDec_input.setGeometry(400, 30, 300, 60)
    
    # creating an input space for converting decimal to binary
    decToBin_input = QLineEdit(bottom_horiz_frame)
    decToBin_input.setStyleSheet(
        "font: 25px;" + 
        "border-radius: 0px;"
    )
    decToBin_input.setGeometry(400, 100, 300, 60)
    
    
    # creating an input space to check whether the IP address global or not
    global_input = QLineEdit(bottom_horiz_frame)
    global_input.setStyleSheet(
        "font: 25px;" + 
        "border-radius: 0px;"
    )
    global_input.setGeometry(400, 170, 300, 60)
    
    
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
