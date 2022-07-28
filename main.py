# importing from packages fromPyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
import sys

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
    
    title_frame = QFrame(window)
    title_frame.resize(700, 90)
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
    
    # Window is hidden by default that is why we are showing it
    window.show()
    


# starting up the event loop
app.exec()
