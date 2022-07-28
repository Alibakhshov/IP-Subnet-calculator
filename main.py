# importing from packages fromPyQt5
from PyQt5.QtWidgets import QApplication, QWidget, QFrame
import sys

app = QApplication(sys.argv)

class MainWindow():
    window = QWidget()
    window.setWindowTitle("IP Subnet Calculator")
    win_width = 1500
    win_height = 900
    window.setGeometry(100, 100, win_width, win_height)
    # window.setStyleSheet(
    #     "background-color: #696969;" 

    # )
    
    
    frame = QFrame(window)
    frame.setFrameShape(QFrame.WinPanel)
    frame.resize(500, 100)
    frame.setFrameShadow(QFrame.Raised)
    # Window is hidden by default that is why we are showing it
    window.show()
    


# starting up the event loop
app.exec()
