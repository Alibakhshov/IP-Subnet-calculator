# importing from packages fromPyQt5

from audioop import mul
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
    global result0
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
    global result6
    global reserved_label
    global multicast_label
    global loopback_label
    global max_prefixlen_label
    global reverse_label
    global info_about_ip_input
    global error_msg_label
    
    
    def myIPAddress():
        
        host_name = socket.gethostname()
        IP_address = socket.gethostbyname(host_name)

        print(IP_address)
        print(host_name)
        error_msg_label.setText(IP_address)
        error_msg_label.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;"    
        )
        
    def myHostName():
        
        host_name = socket.gethostname()
        print(host_name)
        error_msg_label.setText(host_name)
        
        error_msg_label.setText(host_name)
        error_msg_label.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;"    
        )
        
        
        
    def BinToDec():         
        
        
        if binToDec_input.text() == '':
            
            error_msg_label.setText("Please enter \n your binary number. \n Ex: 10101111")
            error_msg_label.setStyleSheet(
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
            error_msg_label.setText(str(decimal_value))
            error_msg_label.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" 
            )
            
            
    def DecToBin():
        
        if decToBin_input.text() == '':
            error_msg_label.setText("Please enter your \n decimal value. \n Ex: 175")
            error_msg_label.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" +
                "color: red;"
            )
            
        else:
            dec_number = int(decToBin_input.text())
            dec_result = (bin(dec_number)[2:])
            error_msg_label.setText(str(dec_result))
            error_msg_label.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" 
            )
            
    def ipInfo():
        
        
        if info_about_ip_input.text() == '':
            error_msg_label.setText("Please enter \n an IP address. \n Ex: 192.168.0.0 ")
            error_msg_label.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" +
                "color: red;"
            )
            
        else:
        
            ip = ipaddress.IPv4Address(info_about_ip_input.text())
            result.setText(str(ip.is_global))
            result1.setText(str(ip.is_link_local))
            result2.setText(str(ip.is_reserved))
            result3.setText(str(ip.is_multicast))
            result4.setText(str(ip.is_loopback))
            result5.setText(str(ip.max_prefixlen))
            result6.setText(str(ip.reverse_pointer))
            global_label.setText("Is global: ")
            link_local_label.setText("Is link local: ")
            reserved_label.setText("Is reserved: ")
            multicast_label.setText("Is multicast: ")
            loopback_label.setText("Is loopback: ")
            max_prefixlen_label.setText("Max prefixlength:")
            reverse_label.setText("Reversed: ")
            
            
            
    def Netmask():
        
        if info_about_ip_input.text() == '':
            error_msg_label.setText("Please enter \n an IP address. \n Ex: 192.168.0.0/16 ")
            error_msg_label.setStyleSheet(
                "background-color: white;" +
                "border-color: white;" + 
                "font: 55px;" +
                "color: red;"
            )
            
        else:
            # initialize an IPv4 Network
            network = ipaddress.IPv4Network(info_about_ip_input.text())
            result.setText(str(network.netmask))
            result.setGeometry(220, 10, 300, 50)
            result1.setText(str(network.broadcast_address))
            result1.setGeometry(270, 65, 300, 50)
            result2.setText(str(network.num_addresses))
            result2.setGeometry(260, 120, 300, 50)
            global_label.setText("Network mask: ")
            global_label.setGeometry(10, 10, 220, 50) 
            link_local_label.setText("Broadcast address: ")
            link_local_label.setGeometry(10, 65, 270, 50) 
            reserved_label.setText("Number of hosts: ")
            reserved_label.setGeometry(10, 120, 260, 50) 
            
            

        # # get the network mask
        # print("Network mask:", network.netmask)

        # # get the broadcast address
        # print("Broadcast address:", network.broadcast_address)

        # # print the number of IP addresses under this network
        # print("Number of hosts under", str(network), ":", network.num_addresses)
        
        
    
    def Clear():
        decToBin_input.setText('')
        binToDec_input.setText('')
        info_about_ip_input.setText('')
        result.setText('')
        result1.setText('')
        result2.setText('')
        result3.setText('')
        result4.setText('')
        result5.setText('')
        result6.setText('')
        global_label.setText('')
        reverse_label.setText('')
        link_local_label.setText('')
        reserved_label.setText('')
        multicast_label.setText('')
        loopback_label.setText('')
        max_prefixlen_label.setText('')
        error_msg_label.setText('')
    
    
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
        "border-radius: 15px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"           
    ) # setting border style
    myIP_button.setGeometry(100, 350, 220, 50)
    myIP_button.clicked.connect(myIPAddress)
    
    # creating a button to show the hostname
    myHostName_button = QPushButton("My hostname", right_vert_frame)
    myHostName_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    myHostName_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 15px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"            
    ) # setting border style
    myHostName_button.setGeometry(325, 350, 220, 50)
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
    binToDec_button.setGeometry(50, 450, 220, 60)
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
    DecToBin_button.setGeometry(50, 550, 220, 60)
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
    clear_button.setGeometry(180, 650, 280, 100)
    clear_button.clicked.connect(Clear)
    
    # creating a button to find whether the IP is global or not. If it is global it prints True
    IP_info_button = QPushButton("Get info", right_vert_frame)
    IP_info_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    IP_info_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"            
    ) # setting border style
    IP_info_button.setGeometry(375, 550, 220, 60)
    IP_info_button.clicked.connect(ipInfo)
    
    # creating a button to find the netmask
    netmask_button = QPushButton("Netmask", right_vert_frame)
    netmask_button.setCursor(QCursor(QtCore.Qt.PointingHandCursor)) # setting cursor to pointer
    netmask_button.setStyleSheet(
        "*{border: 5px solid '#2F4F4F';" +
        "border-radius: 25px;" +
        "color: 'black';" +
        "font-size: 20px;}" +
        "*:hover{background: '#2F4F4F';}"                                 
    ) # setting border style
    netmask_button.setGeometry(375, 450, 220, 60)
    netmask_button.clicked.connect(Netmask)
     
    
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
    exit_button.setGeometry(500, 750, 120, 40)
    exit_button.clicked.connect(close_window)
     
    
     
    #----------------------------------------------LABELS-------------------------------------- 
     
     
    # Creating a label to show the result
    result = QLabel(top_horiz_frame)
    # result.setAlignment(Qt.AlignCenter)
    result.setGeometry(140, 10, 300, 50)
    result.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 30px;"
    )
    result.setFont(QFont('Arial', 11))
    
    # Creating a label to show the result of link local
    result1 = QLabel(top_horiz_frame)
    result1.setGeometry(175, 65, 300, 50)
    result1.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 30px;"
    )
    result1.setFont(QFont('Arial', 11))
    
    
    # Creating a label to show whether the given IP address is reserved or not
    result2 = QLabel(top_horiz_frame)
    result2.setGeometry(175, 110, 300, 50)
    result2.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 30px;"
    )
    result2.setFont(QFont('Arial', 11))
    
    # Creating a label to show whether the given IP address is multicast or not
    result3 = QLabel(top_horiz_frame)
    result3.setGeometry(175, 165, 300, 50)
    result3.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 30px;"
    )
    result3.setFont(QFont('Arial', 11))
    
    # Creating a label to show whether the given IP address is loopback or not
    result4 = QLabel(top_horiz_frame)
    result4.setGeometry(185, 210, 300, 50)
    result4.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 30px;"
    )
    result4.setFont(QFont('Arial', 11))
    
    # Creating a label to show the max prefixlength
    result5 = QLabel(top_horiz_frame)
    result5.setGeometry(250, 265, 300, 50)
    result5.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 30px;"
    )
    result5.setFont(QFont('Arial', 11))
    
    # Creating a label to show whether the IP address is packed or not
    result6 = QLabel(top_horiz_frame)
    result6.setGeometry(145, 310, 300, 50)
    result6.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 30px;"
    )
    result6.setFont(QFont('Arial', 11))
    
    # Creating a label to for converting binary to decimal
    binToDec_label = QLabel("Enter binary number", bottom_horiz_frame)
    binToDec_label.setGeometry(5, 5, 500, 100)
    binToDec_label.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 35px;"
    )
    
    
     # Creating a label to for converting decimal to binary
    decToBin_label = QLabel("Enter decimal number", bottom_horiz_frame)
    decToBin_label.setGeometry(5, 80, 500, 100)
    decToBin_label.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 35px;"
    )
    
     # Creating a label to for converting decimal to binary
    IP_info_label = QLabel("Enter an IP address", bottom_horiz_frame)
    IP_info_label.setGeometry(5, 155, 500, 100)
    IP_info_label.setStyleSheet(
        "background-color: white;" +
        "border-color: white;" + 
        "font: 35px;"
    )
    
    
    # prints Is global on the top horizontal frame
    global_label = QLabel(top_horiz_frame)
    global_label.setGeometry(10, 10, 140, 50) 
    global_label.setStyleSheet(
            "background-color: white;" +
            "border-color: white;" + 
            "font: 30px;"
    )
    
    # prints Is link local on the top horizontal frame
    link_local_label = QLabel(top_horiz_frame)
    link_local_label.setGeometry(10, 65, 175, 50) 
    link_local_label.setStyleSheet(
            "background-color: white;" +
            "border-color: white;" + 
            "font: 30px;"
    )
    
    # prints Is reserved on the top horizontal frame
    reserved_label = QLabel(top_horiz_frame)
    reserved_label.setGeometry(10, 110, 175, 50) 
    reserved_label.setStyleSheet(
            "background-color: white;" +
            "border-color: white;" + 
            "font: 30px;"
    )
    
    # prints Is multicast on the top horizontal frame
    multicast_label = QLabel(top_horiz_frame)
    multicast_label.setGeometry(10, 165, 175, 50) 
    multicast_label.setStyleSheet(
            "background-color: white;" +
            "border-color: white;" + 
            "font: 30px;"
    )
    
    # prints Is loopback on the top horizontal frame
    loopback_label = QLabel(top_horiz_frame)
    loopback_label.setGeometry(10, 210, 185, 50) 
    loopback_label.setStyleSheet(
            "background-color: white;" +
            "border-color: white;" + 
            "font: 30px;"
    )
    
     # prints mac prefixlength on the top horizontal frame
    max_prefixlen_label = QLabel(top_horiz_frame)
    max_prefixlen_label.setGeometry(10, 265, 250, 50) 
    max_prefixlen_label.setStyleSheet(
            "background-color: white;" +
            "border-color: white;" + 
            "font: 30px;"
    )
    
     # prints is packed on the top horizontal frame
    reverse_label = QLabel(top_horiz_frame)
    reverse_label.setGeometry(10, 310, 150, 50) 
    reverse_label.setStyleSheet(
            "background-color: white;" +
            "border-color: white;" + 
            "font: 30px;"
    )
    
    # prints errors in the left frame
    error_msg_label = QLabel(right_vert_frame)
    error_msg_label.setGeometry(10, 10, 630, 290) 
    error_msg_label.setAlignment(Qt.AlignCenter)
    
    
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
    info_about_ip_input = QLineEdit(bottom_horiz_frame)
    info_about_ip_input.setStyleSheet(
        "font: 25px;" + 
        "border-radius: 0px;"
    )
    info_about_ip_input.setGeometry(400, 170, 300, 60)
    
    
    # Creating a title for the calculator
    title = QLabel("IP subnet Calculator", title_frame)
    title.setStyleSheet(
        "color: black;" +
        "border-color: white;" +
        "font-size: 45px;" 
    )
    title.setWordWrap(True)
    title.setGeometry(500, 5, 550, 80)
    
    # # Adding an image
    # image = QLabel(title_frame)
    # # image.setGeometry(30, 120, 50, 40)
    # image.setAlignment(Qt.AlignCenter)
    # pixmap = QPixmap('1.png')
    # image.setPixmap(pixmap)
    
    
    # Window is hidden by default that is why we are showing it
    window.show()
    
   
   
    

# starting up the event loop
app.exec()
